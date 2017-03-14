import random
indices = list(range(0, 100))
userDictionary = {}  # empty dictionary
intCount = 0
stringCount = 0
counter = 0
while 1:
    value = str(input('Enter a value: '))
    ans = input('Want to enter another value? y/n: ')
    if value.isdigit():
        intCount += 1
    if not value.isdigit():
        stringCount += 1
    key = random.choice(indices)
    userDictionary.update({key: value})
    indices.remove(key)
    counter += 1
    if ans != "y":
        break

print(userDictionary)
sum = 0
concString = ""

if intCount == counter:
    for key, value in userDictionary.items():
        sum += int(value)
    print("Average: " + str(sum/counter))

if stringCount == counter:
    for key, value in userDictionary.items():
        concString += value
    print("Concatenated string: " + concString)

searchValue = input("Enter the string to be searched: ")
found = 0
for key, value in userDictionary.items():
    if value == searchValue:
        print("Found: " + str((key, value)))
        found = 1
        break

if not found:
    print("Not found")

print("Sorted dictionary" + str(sorted(userDictionary.items())))
