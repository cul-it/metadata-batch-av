from lxml import etree
import csv
import sys
from argparse import ArgumentParser

marcxmlNS = "{http://www.loc.gov/MARC21/slim}"
ns = {'marcxml': 'http://www.loc.gov/MARC21/slim'}


def getHeader(marcxml_file):
    out = []
    for event, record in etree.iterparse(marcxml_file):
        if record.tag == marcxmlNS + "record":
            for field in record.getchildren():
                elem = field.tag.replace(marcxmlNS, '')
                if elem == 'leader':
                    if elem not in out:
                        out.append(elem)
                else:
                    tag = field.get('tag')
                    ind1 = field.get('ind1')
                    ind2 = field.get('ind2')
                    if int(tag) < 10:
                        if tag not in out:
                            out.append(tag)
                    else:
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
                else:
                    tag = field[:3]
                    inds_subf = field.split('_', 1)[1]
                    ind1 = inds_subf.split("$", 1)[0][:1].replace('#', ' ')
                    ind2 = inds_subf.split("$", 1)[0][-1:].replace('#', ' ')
                    subfield = inds_subf.split("$", 1)[1]
                    xpath = ('marcxml:datafield[@tag="' + tag + '"][@ind1="' +
                             ind1 + '"][@ind2="' + ind2 + '"]/' +
                             'marcxml:subfield[@code="' + subfield + '"]')
                    field_value = record.xpath(xpath, namespaces=ns)
                    if len(field_value) > 1:
                        value = ''
                        for n in range(len(field_value)):
                            value = field_value[n].text.encode('utf8')
                        value.strip(';')
                    elif len(field_value) == 1:
                        value = field_value[0].text.encode('utf8')
                    else:
                        value = None
                    nextrow.append(value)
            writer.writerow(nextrow)


def main():
    parser = ArgumentParser(usage='%(prog)s [options] data_filename.xml')
    parser.add_argument("-f", "--full", action="store_true", dest="full",
                        default=False, help="full CSV report")
    parser.add_argument("-t", "--targeted", action="store_true",
                        dest="targeted", default=False, help="targeted CSV \
                        report")
    parser.add_argument("datafile", help="put the datafile you want analyzed \
                        here")

    args = parser.parse_args()

    if not len(sys.argv) > 0:
        parser.print_help()
        parser.exit()

    if args.full and not args.targeted:
        createFullCSV(args.datafile)

    if not args.full and args.targeted:
        createTargetCSV(args.datafile)


if __name__ == "__main__":
    main()
