import csv

with open("project.csv") as f:
    records = csv.DictReader(f)
    for row in records:
         print(row)

import csv
import json

csvfile = open('project.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("Name", "Team", "G", "AB", "PA", "H", "D", "T", "HR", "R", "RBI", "BB", "SO", "HBP", "SB", "CS", "AVG",
              "OBP", "SLG", "OPS", "wOBA", "wRC", "BsR", "Fld",	"Off", "Def", "WAR", "playerid")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')