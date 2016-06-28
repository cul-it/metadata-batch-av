#!/usr/bin/env python

import csv
import sys

# This python script will ... do something ... to rename CU Lecture tapes
# to embed bibids in filenames

# Possible TODO is embedding title information in mp3s.
# woefully python 2.7, but it's just a one-time script

remap1_input = 'CUlecturetapes_metadata_ingest-ready.csv'
remap2_input = 'CU_Lectures_6-27-16.csv'
digpres_input = "i don't know yet"

remap1 = {}
with open(remap1_input, 'rb') as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader:
        print(row)
