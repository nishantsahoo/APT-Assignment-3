import random
article = ['a', 'an', 'the']
noun = ['team', 'photograph', 'New York', 'New Delhi', 'India', 'jigsaw', 'country']
preposition = ['at', 'for', 'in', 'of', 'with', 'above', 'along', 'behind', 'before', 'near', 'next to', 'than']
verb = ['sleep', 'thought', 'ride', 'swim', 'walk', 'talk', 'run', 'read', 'call', 'play']

for i in range(0, 5):
    finalList = []
    randomValArticle = random.randrange(0, len(article))
    randomValNoun = random.randrange(0, len(noun))
    randomValPreposition = random.randrange(0, len(preposition))
    randomValVerb = random.randrange(0, len(verb))
    articleVal = article[randomValArticle].title()
    finalList.append(articleVal)
    finalList.append(noun[randomValNoun])
    finalList.append(verb[randomValVerb])
    finalList.append(preposition[randomValPreposition])
    randomValArticle = random.randrange(0, len(article))
    randomValNoun = random.randrange(0, len(noun))
    finalList.append(article[randomValArticle])
    finalList.append(noun[randomValNoun])
    finalString = " ".join(finalList)
    finalString += "."
    print(finalString)
