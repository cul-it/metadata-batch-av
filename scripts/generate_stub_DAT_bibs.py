import csv
import pymarc

with open('/Users/Christina/Projects/AV2eCommons/data/MusicDATS_20170203/post-metadata-review/Cornell_Recital_Recordings_DAT_updated.csv', 'r') as fh:
    reader = csv.DictReader(fh)
    csv_data = [x for x in reader]

for n in csv_data:
    Year = n['Year']
    Call_Number = n['Call Number']
    Title = n['Title']
    Date2 = n['Date 2']
    Date3 = n['Date 3']
    Date1 = n['Date 1']
    Parts = n['Part(s)']
    three = n['003']
    Notes1 = n['Notes 1']
    Notes2 = n['Notes 2']
    DateRange = n['Date Range']
    Barcode1 = n['Barcode 1']
    Barcode3 = n['Barcode 3']
    Barcode2 = n['Barcode 2']
    seven = n['007']
    eight = n['008'].replace('YYYY', Year)
    ldr = n['Leader']
    record = pymarc.Record()
    record.leader = ldr
    record.add_field(pymarc.Field(tag='003', data=three))
    record.add_field(pymarc.Field(tag='007', data=seven))
    record.add_field(pymarc.Field(tag='008', data=eight))
    record.add_field(pymarc.Field(tag='040', indicators=['\\', '\\'], subfields=['a', 'NIC', 'b', 'eng', 'e', 'rda', 'd', 'NIC']))
    if Parts:
        record.add_field(pymarc.Field(tag='090', indicators=['\\', '\\'], subfields=['a', Call_Number + ' ' + Parts]))
    else:
        record.add_field(pymarc.Field(tag='090', indicators=['\\', '\\'], subfields=['a', Call_Number]))
    record.add_field(pymarc.Field(tag='245', indicators=['0', '0'], subfields=['a', Title]))
    record.add_field(pymarc.Field(tag='264', indicators=['\\', '0'], subfields=['c', Year]))
    if Parts:
        part_num = Parts.split('-')[-1]
        record.add_field(pymarc.Field(tag='300', indicators=['\\', '\\'], subfields=['a', str(part_num) + ' audiocassettes :', 'b', 'digital ;', 'c', '2 7/8 x 2 1/8 in., 3/16 in. tape.']))
    else:
        record.add_field(pymarc.Field(tag='300', indicators=['\\', '\\'], subfields=['a', '1 audiocassette :', 'b', 'digital ;', 'c', '2 7/8 x 2 1/8 in., 3/16 in. tape.']))
    record.add_field(pymarc.Field(tag='500', indicators=['\\', '\\'], subfields=['a', 'Digital audio tape.']))
    if Notes1:
        record.add_field(pymarc.Field(tag='500', indicators=['\\', '\\'], subfields=['a', Notes1]))
    if Notes2:
        record.add_field(pymarc.Field(tag='500', indicators=['\\', '\\'], subfields=['a', Notes2]))
    record.add_field(pymarc.Field(tag='710', indicators=['2', '\\'], subfields=['a', 'Music Library Recital DATs.']))
    record.add_field(pymarc.Field(tag='710', indicators=['2', '\\'], subfields=['a', 'Cornell University. ', 'b', 'Music Library.']))
    record.add_field(pymarc.Field(tag='899', indicators=['\\', '\\'], subfields=['a', 'CULMusicDAT']))
    record.add_field(pymarc.Field(tag='852', indicators=['8', '1'], subfields=['a', 'NIC', 'h', Call_Number]))
    file_name = Call_Number.replace(' ', '_') + '.mrc'
    out = open('/Users/Christina/Projects/AV2eCommons/data/MusicDATS_20170203/bib-stubs/' + file_name, 'wb')
    out.write(record.as_marc())
    out.close()
    out = open('/Users/Christina/Projects/AV2eCommons/data/MusicDATS_20170203/bib-stubs/all.mrc', 'ab')
    out.write(record.as_marc())
    out.close()