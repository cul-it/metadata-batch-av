#!/usr/bin/env python

import csv
import sys

# This python script will generate a series of bash commands to rename Africana files
# to embed bibids in filenames

remap_input = 'Africana_metadata_ingest-ready.csv'
digpres1_input = open('digpres1.txt', 'rU').readlines()
digpres2_input = open('digpres2.txt', 'rU').readlines()

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
                SFSbase = "/Volumes/digitalpreservation"
            elif oldbase in digpres2:
                SFSbase = "/Volumes/digitalpreservation2"
            else:
                sys.exit("Base not found.")

           # Individual files
            print("mv -i -v {0}/{1}/{2} {0}/{1}/{3}".format(SFSbase, oldbase, oldnames[i], newnames[i]))
            print("mv -i -v {0}/{1}/{1}_7000k.avi {0}/{1}/{2}_7000k.avi".format(SFSbase, oldbase, newbase))
            print("mv -i -v {0}/{1}/{1}_7000k.mov {0}/{1}/{2}_7000k.mov".format(SFSbase, oldbase, newbase))
            print("mv -i -v {0}/{1}/{1}_AM.mov {0}/{1}/{2}_AM.mov".format(SFSbase, oldbase, newbase))
            print("mv -i -v {0}/{1}/{1}_AM_exiftool.txt {0}/{1}/{2}_AM_exiftool.txt".format(SFSbase, oldbase, newbase))
            print("mv -i -v {0}/{1}/{1}_mp4_exiftool.txt {0}/{1}/{2}_mp4_exiftool.txt".format(SFSbase, oldbase, newbase))

            # Folder Level
            print("mv -i -v {0}/{1} {0}/{2}".format(SFSbase, oldbase, newbase))

 
