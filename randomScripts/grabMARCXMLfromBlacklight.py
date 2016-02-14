import requests
import sys
import csv
import os

postKaltura_file = sys.argv[1]
csvfile = csv.reader(open(postKaltura_file), delimiter=',')
bibids = []
for row in csvfile:
    if row[4] not in bibids and row[4] and row[4] != 'AccessionNumber':
        bibids.append(row[4])

baseURL = 'https://newcatalog.library.cornell.edu/catalog/'

directory = "data/CUlecturetapes_20160211/marcxml/"
if not os.path.exists(directory):
    os.makedirs(directory)
allmarc = open(directory + 'allmarc.xml', 'w')
allout = ''
for n in range(len(bibids)):
    headers = {'Content-Type': 'application/xml'}
    query = baseURL + bibids[n] + '.marcxml'
    resp = requests.get(query, headers=headers)
    if resp.status_code == 200:
        f = open(directory + bibids[n] + ".xml", "w")
        try:
            f.write(resp.content)
            allout += resp.content
        finally:
            f.close()
    else:
        print(resp.status_code)

allmarc.write("<collection xmlns='http://www.loc.gov/MARC21/slim'>")
allmarc.write(allout)
allmarc.write("</collection>")
