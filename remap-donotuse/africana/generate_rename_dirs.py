#!/usr/bin/env python

import csv
import sys
import os

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

startpath = os.getcwd()

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
                SFSbase = "/Volumes/LIB/digitalpreservation/Africana_CD_Exec_video"
            elif oldbase in digpres2:
                SFSbase = "/Volumes/LIB/digitalpreservation2/Africana_CD_Exec_video"
            else:
                sys.exit("Base not found.")

            # Start at Folder
            print("cd {0}".format(SFSbase))

            # Issue rename
            print("rename -n -i -s {0} {1} *".format(oldbase, newbase))

            # Go back to start
            print("cd {0}".format(startpath))


           
