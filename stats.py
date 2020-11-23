from collections import defaultdict
import nltk
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path

def stats():
    
    while True:
        try:
            file_to_open =Path(input("\nPlease, insert your file path: "))

            with open(file_to_open) as f:
                words = wordpunct_tokenize(f.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    print(words)
    print('\n\nThis text contains',len(words), 'tokens')


def sent():
    a=Path(input("\nPlease, insert your file path: "))

    with open(a, 'r', encoding='utf-8') as f:
        word=sent_tokenize(f.read())

    user=input('Create a folder?|Y/N: ')
    if user == 'Y':
        folder_path=Path(input('Enter your folder path: '))
        folder_name=input("\n\nName your folder: ")
        text_name=input("\n\nName your file: ")
        folder=os.path.join(folder_path, folder_name)
        os.makedirs(folder)
        file_name = text_name+'.txt'.format(folder_name)
        file = os.path.join(folder, file_name)
        with open(file, 'w') as t:
            for i in word:
                a='\n\n'+i
                t.write(a)
        t.close()
    else:
        folder_path=Path(input('Enter your folder path: '))
        text_name=input("\n\nName your file: ")
        folder=os.path.join(folder_path, text_name)
        with open(folder, 'w') as tx:
            for j in word:
                b='\n\n'+j
                tx.write(b)
    tx.close()
        
        

    print('\n\nThis text contains',len(word), 'sentences')

    


#stats()
sent()


    


            
                

    






