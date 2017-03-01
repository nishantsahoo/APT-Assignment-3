sentence = input('Enter the sentence: ')
wordList = sentence.split(' ')
pigList = []
for each in wordList:
    pigList.append(each[1:] + each[0] + "ay")
print(" ".join(pigList))
