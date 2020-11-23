import nltk
from nltk.tokenize import word_tokenize
import re

with open ('text-test.txt') as fr:
    words = word_tokenize(fr.read().lower())

with open ('Fr-dictionary.txt') as fr:
    dic = word_tokenize(fr.read().lower())

l=[ ]
errors=[ ]

for n,word in enumerate (words):
    l.append(word)
    if word == "*":
        print(words[n-1], words[n+1])
        exp = words[n-1] + words[n+1]
        if exp in dic:  
            l.append(exp)
            errors.append(words[n-1])
            errors.append("*")
            errors.append(words[n+1])
        else:
            continue

print(l)
print(errors)


l=frozenset(l)
errors=frozenset(errors)

c=l.difference(errors)

print(list(c)) 



#['la', 'engagement', 'les', 'de']

#['les','engage', '*', 'ment', 'de','la']
            






            






            

        

        
        

