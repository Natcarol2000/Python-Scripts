from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
import re
import os
import sys
from pathlib import Path


def frequency_list():
    while True:
        try:
            file_to_open =Path(input("\nPlease, insert your file path: "))

            with open(file_to_open) as f:
                freq = word_tokenize(f.read().lower())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    with open ('Fr-dictionary2.txt') as fr:
        dic = word_tokenize(fr.read().lower())


        errors=[ ]
        d=defaultdict(int)

    for w in freq:
        if  w not in dic:
            errors.append(w)
        else:
            d[w]+=1

    for w in sorted(d, key=d.get):
        print(w, d[w])

    print("errors found:", errors)

frequency_list()



    #count=frequency.get(word,0)
    #frequency[word] = count+1



    



#print(errors)

    




    
#frequency_list=sorted(frequency.keys())

#for words in frequency_list:

#print (words, frequency[words])
