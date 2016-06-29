#!/usr/bin/env python

import csv
import sys
import re

# This python script will ... do something ... to rename CU Lecture tapes
# to embed bibids in filenames

# Possible TODO is embedding title information in mp3s.
# woefully python 2.7, but it's just a one-time script

remap_input = 'CU_Lectures_6-27-16_handles.csv'
digpres_input = "i don't know yet"

remap = {}
re_filepattern = re.compile('CUL_Lectures_CU_(\d{4})_AM_(\d{1,2})_\d{1}')
re_filepatternalt = re.compile('CUL_Lectures_CU_(\d{3,4})_(\d{2})_AM_(\d{1})_(\d{1})')

with open(remap_input, 'rb') as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader:
        for filename in row['ID NUMBER'].split('|'):
            filename = filename.strip()
            if filename.endswith('_1'):
                endname = 'A'
            elif filename.endswith('_2'):
                endname = 'B'
            else:
                sys.exit("unexpected end of filename.")
            filepattern = re_filepattern.match(filename)
            if not filepattern:
                filepattern = re_filepatternalt.match(filename)
                if not filepattern:
                    sys.exit("unexpected filename pattern.")

            callno = filepattern.group(1)
            tapeno = filepattern.group(2)

            newname = 'CUL_Lectures_{0}_A{1}_{2}_{3}'.format(row['AccessionNumber'], callno.zfill(4), 
                                                             tapeno.zfill(2), endname)
            print("rename -n -i -s {0} {1} Access_Copies/*".format(filename,newname))
            print("rename -n -i -s {0} {1} Preservation_Masters_96_24/*".format(filename,newname))
#            print("{0} {1}".format(filename, newname))
