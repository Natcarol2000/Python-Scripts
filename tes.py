from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path


def type_token():
    
    while True:
        try:
            file_to_open =Path(input("\n Please, insert your file path: "))

            with open(file_to_open,'r', encoding="utf-8") as f:
                words = wordpunct_tokenize(f.read())
            with open('/Users/nataliaresende/Dropbox/PYTHON/Dictionaries/Punctuation.txt','r', encoding="utf-8") as d:
                punct_dic=wordpunct_tokenize(d.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    punct_list=[]
    token_list=[]



    for i in words:
        if i in punct_dic:
            punct_list.append(i)
        else:
            token_list.append(i)



    print('\n',token_list)
    print('\n\n',punct_list)
    print('\n\n',set(token_list))
    


    print('\nThis text contains', len(token_list), 'tokens')
 
    print('\nThis text contains',len(set(token_list)), 'types')
    print('\nThe lexical richness (type/token ratio) of this text is: ',len(set(token_list))/len(token_list))

    us=input('Run this program again? \n1.Yes \n2.No \nSelection: ')

    if us=='1':
        type_token()
    else:
        print('Ok. Bye')



type_token()
            
            
