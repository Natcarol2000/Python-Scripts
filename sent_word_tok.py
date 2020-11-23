from pathlib import Path
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
import re

def sent_length():
    while True:
        try:
            file_to_open =Path(input("\nYOU CHOSE OPTION 1. Please, insert your file path: "))
            with open(file_to_open) as f:
                words = sent_tokenize(f.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")
    print('\n\n This file contains',len(words),'sentences in total')

    sent_number=1

    for t in words:
        a=word_tokenize(t)
        print('\n\nSentence',sent_number,'contains',len(a), 'tokens')
        sent_number+=1
        

    wordcounts = []

    with open(file_to_open) as f:
        text = f.read()
        sentences = sent_tokenize(text)
        for sentence in sentences:
            words = word_tokenize(sentence)
            wordcounts.append(len(words))

    average_wordcount = sum(wordcounts)/len(wordcounts)


    

    print ('\n\n The longest sentence of this file contains',max(wordcounts), 'tokens')
    print ('\n\n The shortest sentence of this file contains',min(wordcounts),'tokens')
    print('\n\n The mean sentence length of this file is: ',average_wordcount)


def percent():

    while True:
        try:
            punc_file_to_open =Path(input("\nYOU CHOSE OPTION 2. Please, insert your file path and wait for instructions: "))
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

    punc=open('/Users/nataliaresende/Dropbox/PYTHON/Dictionaries/Punctuation.txt', 'r',encoding='utf-8')
    punc_dic=punc.read()
    patt=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b")
    c_n= list(filter(patt.match, freq))

    errors=[]
    text=[]
    Cap_nouns=[]
    named_entities=[]

    for i in freq:
        if i in dic:
            text.append(i)
        elif i in punc_dic:
            text.append(i)
        elif i in c_n:
            Cap_nouns.append(i)
        else:
            errors.append(i)
            
    for j in Cap_nouns:
        if j not in dic:
            named_entities.append(j) 
        
            
            
   
    print('\n\nYourfile contains a total of', len(text), 'tokens')
    print('\n\nYour file contains a total of',len(errors), 'tokens not found in dictionary')
    print('\n\nYour file contains a total of', len(Cap_nouns), 'capitalised words')
    print('\n\nYour file contains a total of', len(named_entities), 'proper nouns')

    print('\n\nThe error percentage of this file is: ', 100*float(len(errors))/float(len(text)))
    print('\n\nThe percentage of capitalised words is: ', 100*float(len(Cap_nouns))/float(len(text)))
    print('\n\nThe percentage of named entities is: ', 100*float(len(named_entities))/float(len(text)))

    user=input('\n\n1. Print the list of errors\n\n2. Type "2" Print the list of capitalised nouns \n\n3. Print list of errors, capitalised nouns and named entities \n\n4. Go to main menu \n\n5. run this program again \n\nSelection: ') 

    if user =='1':
        print(errors)
    elif user == '2':
        print(Cap_nouns)
    elif user =='3':
        print('\n\n',errors)
        print('\n\n',Cap_nouns)
        print('\n\n',named_entities)
    else:
        print('Incorrect option. Try again')

    while True:
        us=input('Run this program again?|Y/N: ')

        if us == 'Y':
            percent()
        else:
            menu()

        

    

#percent()
sent_length()

