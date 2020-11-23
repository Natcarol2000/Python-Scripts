from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path

def merge_dic():
    while True:
        try:
            dic1_to_open =Path(input("\nYOU CHOSE OPTION 1. Please, insert the file path of your first dictionary: "))
            with open(dic1_to_open) as f:
                dic1 = word_tokenize(f.read())
                break         
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")


    while True:
        try:
            dic2_to_open =Path(input("\nYOU CHOSE OPTION 1. Please, insert the file path of your second dictionary: "))
            with open(dic2_to_open) as dic:
                dic2 = word_tokenize(dic.read())
                break         
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    extra_words=[]
    a=open('extra_words.txt','w')


    for i in dic1:
        if i not in dic2:
            extra_words.append(i)
        else:
            continue


    print('The number of words not found in the first dictionary is',len(extra_words))


    for j in extra_words:
        a.write(j)
        '\n'
    a.close()

    print('words not found in dic 1 written to a file. Check your directory')

merge_dic()
        

            

    

    
