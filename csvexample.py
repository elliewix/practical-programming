from collections import Counter
import csv

newcolors = 'colors.txt'
oldcolors = 'oldcolors.txt'

with open(newcolors, 'rt') as newcolors_file:
    newcolorslist = newcolors_file.readlines()

with open(oldcolors, 'rt') as oldcolors_file:
    oldcolorslist = oldcolors_file.readlines()

cleannew = []

for line in newcolorslist:
    cleannew.append(line.strip())

cleanold = []

for line in oldcolorslist:
    cleanold.append(line.strip())

countednew = dict(Counter(cleannew))
countedold = dict(Counter(cleanold))

printlist = []

for color, count in countednew.iteritems():
    rowlist = [color, count]
    printlist.append(rowlist)

headers = ['color', 'count']

outfilename = 'countedcolors.csv'

with open(outfilename, 'wt') as csvout:
    csvout = csv.writer(csvout)
    csvout.writerow(headers)
    csvout.writerows(printlist)

myrows = []

with open(outfilename, 'rt') as csvin:
    csvin = csv.reader(csvin)
    headers = next(csvin)
    for row in csvin:
        myrows.append(row)

print myrows
