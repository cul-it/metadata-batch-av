#!/usr/bin/env python

import csv
import sys

# This python script will rename hashdeep output to correspond with new filenames

remap_input = 'Africana_metadata_ingest-ready.csv'
digpres1_input = open('digpres1.txt', 'rU').readlines()
digpres2_input = open('digpres2.txt', 'rU').readlines()
hash1 = open('AFR-dig1.csv', 'rU').read()
hash2 = open('AFR-dig2.csv', 'rU').read()


digpres1 = []
for dp1i in digpres1_input:
    digpres1.append(dp1i.strip())

digpres2 = []
for dp2i in digpres2_input:
    digpres2.append(dp2i.strip())



with open(remap_input, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        oldnames = row['Filename Old Ignore'].replace('http://digitalmedia.library.cornell.edu/kaltura/Africana/', '').split(' | ')
        newnames = row['Filename'].split(' | ')

        if len(oldnames) != len(newnames):
            sys.exit("Matching failed.")

        for i in range(0, len(oldnames)):
            oldbase = oldnames[i].replace('.mp4', '')
            newbase = newnames[i].replace('.mp4', '')

            if oldbase in digpres1:
                hash1 = hash1.replace('{0}/{1}'.format(oldbase, oldnames[i]),
                                      '{0}/{1}'.format(newbase, newnames[i]))
                hash1 = hash1.replace('{0}/{0}_7000k.avi'.format(oldbase),
                                      '{0}/{0}_7000k.avi'.format(newbase))
                hash1 = hash1.replace('{0}/{0}_7000k.mov'.format(oldbase),
                                      '{0}/{0}_7000k.mov'.format(newbase))
                hash1 = hash1.replace('{0}/{0}_AM.mov'.format(oldbase),
                                      '{0}/{0}_AM.mov'.format(newbase))
                hash1 = hash1.replace('{0}/{0}_AM_exiftool.txt'.format(oldbase),
                                      '{0}/{0}_AM_exiftool.txt'.format(newbase))
                hash1 = hash1.replace('{0}/{0}_mp4_exiftool.txt'.format(oldbase),
                                      '{0}/{0}_mp4_exiftool.txt'.format(newbase))

            elif oldbase in digpres2:
                hash2 = hash2.replace('{0}/{1}'.format(oldbase, oldnames[i]),
                                      '{0}/{1}'.format(newbase, newnames[i]))
                hash2 = hash2.replace('{0}/{0}_7000k.avi'.format(oldbase),
                                      '{0}/{0}_7000k.avi'.format(newbase))
                hash2 = hash2.replace('{0}/{0}_7000k.mov'.format(oldbase),
                                      '{0}/{0}_7000k.mov'.format(newbase))
                hash2 = hash2.replace('{0}/{0}_AM.mov'.format(oldbase),
                                      '{0}/{0}_AM.mov'.format(newbase))
                hash2 = hash2.replace('{0}/{0}_AM_exiftool.txt'.format(oldbase),
                                      '{0}/{0}_AM_exiftool.txt'.format(newbase))
                hash2 = hash2.replace('{0}/{0}_mp4_exiftool.txt'.format(oldbase),
                                      '{0}/{0}_mp4_exiftool.txt'.format(newbase))

            else:
                sys.exit("Base not found.")


with open('AFR-dig1-renamed.csv', 'w') as hash1_new:
    hash1_new.write(hash1)

with open('AFR-dig2-renamed.csv', 'w') as hash2_new:
    hash2_new.write(hash2)
