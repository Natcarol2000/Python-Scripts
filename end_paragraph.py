import nltk
from nltk.tokenize import word_tokenize
import re


with open ('text-test.txt') as tx:
    text = word_tokenize(tx.read().lower())



with open ('Fr-dictionary.txt') as fr:
    dic = word_tokenize(fr.read().lower())


ast=re.compile(r'[\*]+')
regex=list(filter(ast.match,text))


pat=re.compile(r'[.?\-",:;.?!»’()[]\d]+')
reg= list(filter(pat.match, text))


valid_words=[]
invalid_words=[]

last = None
for w in text:
    if w in regex:
        last=w
        print(w)
        break
    else:
        continue




    
