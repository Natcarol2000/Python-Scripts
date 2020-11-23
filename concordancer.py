from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
from nltk import *
import re
import os
import sys
from pathlib import Path

def concordancer():

        while True:
            try:
                file_to_open =Path(input("\nYOU SELECTED OPTION 12: LEXICAL INFORMATION. Please, insert your file path: "))
                with open(file_to_open,'r', encoding="utf-8") as f:
                    words = f.read()
                    break
            except FileNotFoundError:
                print("\nFile not found. Better try again")
            except IsADirectoryError:
                print("\nIncorrect Directory path.Try again")

        user=input('Enter the word: ')

        print('\n\n',words.concordance(user))
        print('\n\n', words.similar(user))

concordancer()

