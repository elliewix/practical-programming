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

newlength =  len(cleannew)
oldlength =  len(cleanold)

if newlength == oldlength:
    print "The lengths are the same"
else:
    print "The lengths are different"
    diff = newlength - oldlength
    if diff > 0:
        print "Old length was bigger by", abs(diff)
    else:
        print "New length was bigger by", abs(diff)

# for item in cleanold:
#     if item not in cleannew:
#         print item

old = set(cleanold)
new = set(cleannew)

print old ^ new

if not old <= new:
    print "The files are diff"
    print "These items are in old but not new"
    for item in cleanold:
        if item not in cleannew:
            print item