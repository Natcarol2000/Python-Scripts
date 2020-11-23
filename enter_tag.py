from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path
import csv

def enter_tag():

    while True:
        try:
            file_to_open =Path(input("\nYOU CHOSE OPTION 3. Please, insert your file path: "))
            break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    print('\n\nREMINDER: Your text must be tagged using the following tag format: [@"string"@]')





    tag1=input('\n\nPlease, enter the string between the @ symbols of your first tag: ')
    tag2=input('\n\nPlease, enter the string between the @ symbols of your second tag: ')
    tagged_items=[]

    pat = re.compile(r'(?<=\%'+tag1+'\%).+?(?=\%'+tag2+'\%)', flags=re.DOTALL)


    with open(file_to_open, 'r', encoding="utf-8") as file:
        for i in pat.findall(file.read()):

            tagged_items.append(i)
            
    print('\n\nThis file contains',len(tagged_items), 'tagged items')

    q=input('\n\nCreate a folder for your files? | Y/N: ')

    if q == 'Y':
        folder_path=Path(input('\n\nEnter the directory of your new folder: '))
        folder_name=input("\n\nName your folder: ")
        folder=os.path.join(folder_path, folder_name)
        os.makedirs(folder)
        for j in range(len(tagged_items)):
            chap='Item'+str(j+1) +'.txt'
            file = os.path.join(folder, chap)
            with open(file, "w") as f:
                for item in tagged_items[j]:
                    f.write("%s" % str(item))
        print('\n\nTagged items 1 -',len(tagged_items), 'written to a file separately. Check your folder named',folder_name, 'in your directory')
    else:
        folder1_path=Path(input('\n\nEnter your chosen directory: '))
        for x in range(len(tagged_items)):
            chap1='Item'+str(x+1) +'.txt'
            fi = os.path.join(folder1_path, chap1)
            with open(fi, "w") as f:
                for item in tagged_items[x]:
                    f.write("%s" % str(item))
        print('\n\nTagged items 1 -',len(tagged_items), 'written to a file separately. Check your directory',folder1_path)
        


    

    


    

            


enter_tag()    
