import csv
import json
import os
import string

base = os.path.split(__file__)[0]

csvfile = open(os.path.join(base, 'cache.csv'), 'r')
jsonfile = open(os.path.join(base, 'cache.json'), 'w')

fieldnames = tuple(string.strip(csvfile.readlines()[0]).split(','))


csvfile = open(os.path.join(base, 'cache.csv'), 'r')

#fieldnames = ('Name', 'Category', 'Organization', 'Date', 'Application Deadline', 'Location', 'Fee/Free and/or Stipend', 'Description', 'URL', 'Graduate Credit', 'Students too?', 'Emily: \xf0\x9f\x91\x8d')

reader = csv.DictReader(csvfile, fieldnames)
jsonfile.write('var data = [')
i = 0
print reader
for row in reader:
    print row
    if i != 0:
        json.dump(row, jsonfile)
        jsonfile.write(',\n')
    i += 1
jsonfile.write('];')