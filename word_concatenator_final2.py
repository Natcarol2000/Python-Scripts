from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
import re
import os
import sys
from pathlib import Path


def main():
    while True:
        try:
            file_to_open =Path(input("\nPlease, insert your file path: "))

            with open(file_to_open) as f:
                words = word_tokenize(f.read().lower())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")
    
    with open ('Fr-dictionary2.txt') as fr:
        dic = word_tokenize(fr.read().lower())

    word_separator = '*'

    def join_asterisk(ary):

        for w1, w2, w3 in zip(words, words[1:], words[2:]):
            if w2 == word_separator:
                word = w1 + w3
                yield (word, word in dic)
            elif w1 != word_separator and w1 in dic:
                yield (w1, True)
   

    correct_words = []
    incorrect_words = []
    correct_words = [w for w, correct in join_asterisk(words) if correct]
    incorrect_words = [w for w, correct in join_asterisk(words) if not correct]
    text=' '.join(correct_words)
    print(correct_words)
    print('\n\n', text)
    user2=input('\nWrite text to a file? Type "Y" for yes or "N" for no:')

    text_name=input("name your file.(Ex. 'my_first_file.txt'): ")
    out_file=open(text_name,"w")

    if user2 =='Y':
        out_file.write(text)
        out_file.close()
    else:
        print('ok')


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

    with open ('Fr-dictionary_Upper_Low.txt') as fr:
        dic = word_tokenize(fr.read().lower())

    

        pat=re.compile(r"[.,:;?!'%-]|\b(\w'|w’)+\b|\w+(?:-\w+)+|\d+") #regular expression for words with apostrophes and separated by hyphen
        reg= list(filter(pat.match, freq))
        patt=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b") #regular expression for words that start with capital letters (ex: proper nouns)
        c_n= list(filter(patt.match, freq))
        errors=[ ]
        d=defaultdict(int)
        d2=defaultdict(int)
        d3=defaultdict(int)
        Cap_nouns=[]


    for w in freq:
        d[w]+=1
        if w in reg:
            continue
        elif w in c_n:
            Cap_nouns.append(w)
        elif w not in dic:
            errors.append(w)

    for w in sorted(d, key=d.get):
        print('word:',w, d[w])

    display_errors=input('Do you want to display the list of items not found in Dictionary?" |Y/N: ')

    for x in errors:
        if display_errors=='Y':
            d2[x]+=1

    for x in sorted(d2, key=d2.get):
        print('Error:', x, d2[x])


    display_Cap=input('Do you want to display the list of Capitalised words?" |Y/N: ')

    for y in Cap_nouns:
        if display_Cap =='Y':
            d3[y]+=1
        else:
            print('Ok')

    for y in sorted(d3, key=d3.get):
        print('Capitalised word:',y,d3[y])
         

    choice = input("\n\nDo you want to do this again or select another task? \n\nType Y if you want to do this again \n\nType 1 for another option  \n\nType ENTER to exit \n\nSelection:  ")

    if choice == 'Y':
        frequency_list()
    elif choice == '1':
        main()
    else:
        print("\n\nProgram terminates")


start=input("Please, select your task: \n\n1.Word Concatenation \n\n2.Frequency List \n\nSelection: ")

if start=='1':
    main()
elif start=='2':
    frequency_list()
   





            
        

  









            






            

        

        
        

