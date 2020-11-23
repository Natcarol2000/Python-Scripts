

from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path




while True:
    try:
        file3=Path(input('\nPlease, enter your file path: '))
        dic_to_open_ep=Path(input('\nPlease, enter your dictionary path: '))
        punc_dic_ep=Path(input('\nPlease, enter your punctuation dictionary path: ')) 
        with open (dic_to_open_ep,'r', encoding="utf-8") as ep:
            dic_ep = wordpunct_tokenize(ep.read())
        with open (punc_dic_ep, 'r', encoding='utf=8') as punc_ep:
            punc_dic_ep: wordpunct_tokenize(punc_ep.read())
        with open(file3,'r', encoding='utf-8') as e_p:
            file_e_p=wordpunct_tokenize(e_p.read())
            break
    except FileNotFoundError:
        print("\nFile not found. Better try again")
    except IsADirectoryError:
        print("\nIncorrect Directory path.Try again")
patt_ep=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b")
no= list(filter(patt_ep.match, file_e_p))

errors_ep=[]
text_ep=[]
Cap_nouns_ep=[]
named_entities_ep=[]

for EP in file_e_p:
    if EP in dic_ep:
        text_ep.append(EP)
    elif EP in punc_dic_ep:
        text_ep.append(EP)
    elif EP in no:
        Cap_nouns_ep.append(EP)
    else:
        errors_ep.append(EP)
            
for EPJ in Cap_nouns_ep:
    if EPJ not in dic_ep:
        named_entities_ep.append(EPJ) 
        
            
            
   
print('\n\nYourfile contains a total of', len(text_ep), 'tokens')
print('\n\nYour file contains a total of',len(errors_ep), 'tokens not found in dictionary')
print('\n\nYour file contains a total of', len(Cap_nouns_ep), 'capitalised words')
print('\n\nYour file contains a total of', len(named_entities_ep), 'proper nouns')

print('\n\nThe error percentage of this file is: ', 100*float(len(errors_ep))/float(len(text_ep)))
print('\n\nThe percentage of capitalised words is: ', 100*float(len(Cap_nouns_ep))/float(len(text_ep)))
print('\n\nThe percentage of named entities is: ', 100*float(len(named_entities_ep))/float(len(text_ep)))

print('\n\n',errors_ep)
print('\n\n',Cap_nouns_ep)
print('\n\n',named_entities_ep)

