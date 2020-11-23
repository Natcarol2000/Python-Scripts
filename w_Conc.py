import nltk
from nltk.tokenize import word_tokenize

import re

with open ('fr-text.txt') as tx: #opening text containing the separated words

    text = tx.read().lower()#stores the text with the separated words


with open ('Fr-dictionary.txt') as fr:  #opens the dictionary
    dic = word_tokenize(fr.read().lower()) #stores the first dictionary

pat=re.compile(r'[.?\-",:;.?!»’\'()quls\d]+|\w+(?:-\w+)+')
reg= re.findall(pat,text)
out_file=open("newtext.txt","w") #defining name of output file
valid_words='' #empty list to append the words checked 
invalid_words=[ ] #empty list to append the errors found

for word in text:
    if word in reg:
        valid_words=word
    elif word in dic:
        valid_words=word #appending to a list the words checked 
    else:
        invalid_words.append(word) #appending the invalid_words




 #print converted list
#print(invalid_words) #print errors found

out_file.write(valid_words) #writing the output to a file

out_file.close()

print ('new text written')

print (invalid_words)
print(len(invalid_words))


with open ('newtext.txt') as tx1:
    dic2 = word_tokenize(tx1.read().lower()) #stores second dictionary

with open ('fr-text.txt') as tx2:  #opening text containing the separated words
    text_input = tx2.read().lower() #stores the input text

words_it = iter(text_input) #interaction method

out_file1=open("finaltext.txt","w") #defining name of output file
valid_words1='' #empty list to append the words checked 
invalid_words1=[ ] #empty list to append the errors found

for w in words_it: #looping through the tokenized text
    if w in dic2:
        valid_words1=w
    elif w in dic:
        valid_words1=w #appending to a list the words checked 
    else:
        try:
            concatenated = w + next(words_it) #concatenating strings
            if concatenated in dic2 or dic:
                valid_words1=concatenated #checking if the concatenated strings is a valid word
        except StopIteration:
            pass
        else:
            invalid_words1.append(w) #appending the invalid_words

 #converting list into a string


out_file1.write(valid_words1) #writing the output to a file

out_file1.close()



print(valid_words1) #print list converted into text

print(len(invalid_words1))
