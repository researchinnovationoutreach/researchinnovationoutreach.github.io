import csv
import json
import os
import string
import subprocess

convertToJSON = True

base = os.path.split(__file__)[0]
csvPath = os.path.join(base, 'cache.csv')
jsonPath = os.path.join(base, 'cache.json')

remoteURL = "https://docs.google.com/spreadsheets/d/1XVO1smiI3iOoLJt1nPkmnxqWb2Zi4okiDTtghdBfUcQ/export?gid=0&format=csv"

os.chdir(base)

proc = subprocess.Popen(['curl', remoteURL, '-o', 'cache.csv'], stdout=subprocess.PIPE)
out = proc.communicate()[0]

if convertToJSON:
    csvfile = open(csvPath, 'r')
    jsonfile = open(jsonPath, 'w')

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