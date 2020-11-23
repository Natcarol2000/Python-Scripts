from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path
import csv

def punc_freq():
    while True:
        try:
            punc_file_to_open =Path(input("\nPlease, insert your file path and wait for instructions: "))
            punc_dic_to_open=Path(input('\nPlease, insert your dictionary path: '))
            with open(punc_file_to_open,'r', encoding="utf-8") as f:
                freq = wordpunct_tokenize(f.read())
            with open (punc_dic_to_open,'r', encoding="utf-8") as fr:
                dic = wordpunct_tokenize(fr.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    
    punc=[]
    words=[]
    d1=defaultdict(int)

    for p in freq:
        if p not in dic:
            words.append(p)
        elif p in dic:
            punc.append(p)
            
    user=input('\n\nCreate a new folder to your frequency lists? | Y/N: ')

    for i in punc:
        d1[i]+=1
    if user == 'Y':
        punc_folder_path=Path(input('\n\nEnter the path to create a new folder: '))
        punc_folder_name=input('\n\nName your folder: ')
        punc_file_name=input('\n\nName your file: ')
        punc_file_path=os.path.join(punc_folder_path, punc_folder_name)
        os.makedirs(punc_file_path)
        punc_file=os.path.join(punc_file_path,punc_file_name)
        punc_fi=open(punc_file,'w')
        for p1 in sorted(d1, key=d1.get):
            print(p1,d1[p1])
            k=p1
            fr=d1[p1]
            row=k+' '+str(fr)+'\n'
            punc_fi.write(row)
        punc_fi.close()
        print('\n\nFrequency list named',punc_file_name,'written to a file. Check your directory named', punc_folder_name)
    else:
        punc_folder1_path=Path(input('\n\nEnter your folder path: '))
        punc_file1_name=input('\n\nName your file: ')
        punc_file1_path=os.path.join(punc_folder1_path, punc_file1_name)
        punc_fi1=open(punc_file1_path,'w')
        for p2 in sorted(d1, key=d1.get):
            print(p2,d1[p2])
            k1=p2
            fr1=d1[p2]
            punc_row1=k1+' '+str(fr1)+'\n'
            punc_fi1.write(punc_row1)
        punc_fi1.close()
        print('\n\nFrequency list named',punc_file1_name,'written to a file. Check your directory', punc_folder1_path)


punc_freq()

        


