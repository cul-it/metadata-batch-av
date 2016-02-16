from lxml import etree
import csv
import sys
from argparse import ArgumentParser
import re

marcxmlNS = "{http://www.loc.gov/MARC21/slim}"
ns = {'marcxml': 'http://www.loc.gov/MARC21/slim'}
fieldsNonFile1 = ['240', '245', '830']
fieldsNonFile2 = ['730', '740']
fieldsHeadings = (['100', '110', '111', '130', '600', '610', '611', '630',
                  '648', '650', '651', '700', '710', '711', '730', '751',
                  '800', '810', '811', '830'])
headingsSkip = ['0', '2', 'e']
middleInits_re = re.compile(r" [a-zA-Z]{1}\.$")


def getHeader(marcxml_file):
    out = []
    for event, record in etree.iterparse(marcxml_file):
        if record.tag == marcxmlNS + "record":
            for field in record.getchildren():
                elem = field.tag.replace(marcxmlNS, '')
                tag = field.get('tag')
                if elem == 'leader':
                    if elem not in out:
                        out.append(elem)
                elif int(tag) < 10:
                    if tag not in out:
                        out.append(tag)
                # elif tag in fieldsHeadings:
                #     if tag + '_' not in out:
                #         tag_hdg = tag + '_'
                #         out.append(tag_hdg)

                #     if tag in fieldsNonFile1:
                #         ind1 = field.get('ind1')
                #         ind2 = '*'
                #     elif tag in fieldsNonFile2:
                #         ind1 = '*'
                #         ind2 = field.get('ind2')
                #     else:
                #         ind1 = field.get('ind1')
                #         ind2 = field.get('ind2')
                #         ind1_norm = ind1.replace(' ', '#')
                #         ind2_norm = ind2.replace(' ', '#')
                #         for subfield in field.getchildren():
                #             subf = subfield.get('code')
                #             tag_concat = (tag + '_' + ind1_norm + ind2_norm +
                #                           '$' + subf)
                #             if tag_concat not in out:
                #                 out.append(tag_concat)
                else:
                    if tag in fieldsNonFile1:
                        ind1_norm = field.get('ind1')
                        ind2_norm = '*'
                    elif tag in fieldsNonFile2:
                        ind1_norm = '*'
                        ind2_norm = field.get('ind2')
                    else:
                        ind1 = field.get('ind1')
                        ind2 = field.get('ind2')
                        ind1_norm = ind1.replace(' ', '#')
                        ind2_norm = ind2.replace(' ', '#')
                    for subfield in field.getchildren():
                        subf = subfield.get('code')
                        tag_concat = (tag + '_' + ind1_norm + ind2_norm +
                                      '$' + subf)
                        if tag_concat not in out:
                            out.append(tag_concat)
    out_sorted = sorted(out)
    return(out_sorted)


def createFullCSV(marcxml_file):
    writer = csv.writer(open('data/CUlecturetapes_20160211/marcxml.csv', 'w'))
    header = getHeader(marcxml_file)
    writer.writerow(header)
    for event, record in etree.iterparse(open(marcxml_file, 'rb')):
        if record.tag == marcxmlNS + "record":
            nextrow = []
            for field in header:
                if field == 'leader':
                    field_value = record.xpath('marcxml:leader', namespaces=ns)
                    if len(field_value) == 1:
                        value = field_value[0].text.encode('utf8')
                    else:
                        value = None
                    nextrow.append(value)
                elif len(field) == 3:
                    field_value = record.xpath('marcxml:controlfield[@tag=' +
                                               field + ']', namespaces=ns)
                    if len(field_value) > 1:
                        value = ''
                        for n in range(len(field_value)):
                            value += field_value[n].text.encode('utf8') + ";"
                        value.strip(';')
                    elif len(field_value) == 1:
                        value = field_value[0].text.encode('utf8')
                    else:
                        value = None
                    nextrow.append(value)
                # elif field.strip('_') in fieldsHeadings:
                #     field_value = record.xpath('marcxml:datafield[@tag=' +
                #                                field.strip('_') + ']',
                #                                namespaces=ns)
                #     if len(field_value) > 1:
                #         value = ''
                #         for resp in field_value:
                #             resp_value = ''
                #             for subfield in resp.getchildren():
                #                 if subfield.get('code') not in headingsSkip:
                #                     resp_value += subfield.text.encode('utf8') + ' '
                #                 if middleInits_re.search(resp_value.strip()) is None:
                #                     resp_value = resp_value.strip().strip('.')
                #             value += resp_value + ';'
                #         value = value.strip(';')
                #         print(value)
                #     elif len(field_value) == 1:
                #         value = ''
                #         for resp in field_value:
                #             for subfield in resp.getchildren():
                #                 value += subfield.text.encode('utf8') + ' '
                #             value = value.strip()
                #         if middleInits_re.search(value) is None:
                #             value = value.strip('.')
                #     else:
                #         value = None
                #     nextrow.append(value)
                #     print(value)
                else:
                    tag = field[:3]
                    inds_subf = field.split('_', 1)[1]
                    ind1 = inds_subf.split("$", 1)[0][:1].replace('#', ' ')
                    ind2 = inds_subf.split("$", 1)[0][-1:].replace('#', ' ')
                    subfield = inds_subf.split("$", 1)[1]
                    if tag in fieldsNonFile1:
                        xpath = ('marcxml:datafield[@tag="' + tag +
                                 '"][@ind1="' + ind1 + '"]/' +
                                 'marcxml:subfield[@code="' + subfield + '"]')
                    elif tag in fieldsNonFile2:
                        xpath = ('marcxml:datafield[@tag="' + tag +
                                 '"][@ind2="' + ind2 + '"]/' +
                                 'marcxml:subfield[@code="' + subfield + '"]')
                    else:
                        xpath = ('marcxml:datafield[@tag="' + tag +
                                 '"][@ind1="' + ind1 + '"][@ind2="' + ind2 +
                                 '"]/' + 'marcxml:subfield[@code="' + subfield
                                 + '"]')
                    field_value = record.xpath(xpath, namespaces=ns)
                    if len(field_value) > 1:
                        value = ''
                        for n in range(len(field_value)):
                            value += field_value[n].text.encode('utf8') + ';'
                        print(value)
                        value.strip(';')
                    elif len(field_value) == 1:
                        value = field_value[0].text.encode('utf8')
                    else:
                        value = None
                    nextrow.append(value)
            writer.writerow(nextrow)


def createECCSV(marcxml_file):
    writer = csv.writer(open('data/CUlecturetapes_20160211/marcxml_mapping.csv', 'w'))
    header = getHeader(marcxml_file)
    writer.writerow(header)
    writer.writerow('')


def main():
    parser = ArgumentParser(usage='%(prog)s [options] data_filename.xml')
    parser.add_argument("-f", "--full", action="store_true", dest="full",
                        default=False, help="full CSV report")
    parser.add_argument("-e", "--ecommons", action="store_true",
                        dest="ecommons", default=False, help="eCommons CSV \
                        mapping")
    parser.add_argument("datafile", help="put the datafile you want analyzed \
                        here")

    args = parser.parse_args()

    if not len(sys.argv) > 0:
        parser.print_help()
        parser.exit()

    if args.full and not args.ecommons:
        createFullCSV(args.datafile)

    if not args.full and args.ecommons:
        createECCSV(args.datafile)


if __name__ == "__main__":
    main()
