from collections import defaultdict
import re
import nltk
from nltk.tokenize import word_tokenize



with open('text-test.txt') as f:
    freq = word_tokenize(f.read())

with open ('Fr-dictionary_Upper_Low.txt') as fr:
    dic = word_tokenize(fr.read())


pat=re.compile(r"[.,:;?!'%-]|\b(\w'|w’)+\b|\w+(?:-\w+)+|\d+") #regular expression for words with apostrophes and separated by hyphen
reg= list(filter(pat.match, freq))
patt=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b") #regular expression for words that start with capital letters (ex: proper nouns)
c_n= list(filter(patt.match, freq))

Cap_nouns=[]
errors=[ ]

d=defaultdict(int)
d2=defaultdict(int)
d3=defaultdict(int)



for w in freq:
    d[w]+=1
    if w in reg:
        continue
    elif w in c_n:
        Cap_nouns.append(w)
    elif w not in dic:
        errors.append(w)


for w in sorted(d, key=d.get):
    print('word:',w, d[w])


display_errors=input('Display the list of items not found in Dict?" |Y/N: ')

for x in errors:
    if display_errors=='Y':
        d2[x]+=1


for x in sorted(d2, key=d2.get):
    print('Error:',x, d2[x])

display_Cap=input('Display list of Capitalised words not found in Dict?" |Y/N: ')


    
for y in Cap_nouns:
    if display_Cap =='Y':
        d3[y]+=1


for y in sorted(d3, key=d3.get):
    if y in dic:
        continue
    else:
        print('Capitalised word:',y, d3[y])    






