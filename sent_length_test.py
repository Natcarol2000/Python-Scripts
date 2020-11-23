from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path

def sent_lgth():

    
        
    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 8: CALCULATE SENTENCE LENGTH. Please, insert your file path: "))
            with open(file_to_open,'r', encoding="utf-8") as f:
                words = sent_tokenize(f.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")
    print('\n\n This file contains',len(words),'sentences in total')

    sent_number=1

    wordcounts = []
    with open(file_to_open) as f:
        text = f.read()
        sentences = sent_tokenize(text)
        for sentence in sentences:
            w = word_tokenize(sentence)
            wordcounts.append(len(w))

    average_wordcount = sum(wordcounts)/len(wordcounts)

    a='The longest sentence of this file contains',max(wordcounts), 'tokens'
    b='The shortest sentence of this file contains',min(wordcounts),'tokens'
    c='The mean sentence length of this file is: ',average_wordcount
    print(a)
    print(b)
    print(c)

sent_lgth()
