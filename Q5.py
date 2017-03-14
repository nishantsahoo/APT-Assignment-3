file = open("New file.txt", 'w')
file.write("Nishant" + '\n')
file.write("Samarth" + '\n')
file.write("Paul" + '\n')
file.write("Srishti" + '\n')
file.write("Sharang" + '\n')
file.write("Bobby" + '\n')
file.write("Nandini" + '\n')
file.write("Kanishk" + '\n')
file.write("Adhish" + '\n')

firstDictionary = {}
secondDictionary = {}
fileString = ""

i = 1
file = open("New file.txt", 'r')
filelist = file.readlines()

for each in filelist:
    val = each.strip('\n')
    print(val)
    fileString += val
    firstDictionary.update({i: [val, len(val)]})
    i += 1

fileSet = set(fileString)
for each in fileSet:
    secondDictionary.update({each: fileString.count(each)})

print(firstDictionary)
print(secondDictionary)
