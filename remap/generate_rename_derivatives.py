#!/usr/bin/env python

import csv
import sys

# This python script will generate a series of bash commands to rename Africana files
# to embed bibids in filenames for derivatives on dcapspub

remap_input = 'Africana_metadata_ingest-ready.csv'

with open(remap_input, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        oldnames = row['Filename Old Ignore'].replace('http://digitalmedia.library.cornell.edu/kaltura/Africana/', '').split(' | ')
        newnames = row['Filename'].split(' | ')

        if len(oldnames) != len(newnames):
            sys.exit("Matching failed.")

        for i in range(0, len(oldnames)):
            print("mv -i -v /Volumes/dcapspub/htdocs/kaltura/Africana/{0} /Volumes/dcapspub/htdocs/kaltura/Africana/{1}".format(oldnames[i], newnames[i]))

 
