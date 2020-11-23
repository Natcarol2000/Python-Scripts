import nltk
from nltk.tokenize import word_tokenize
import re

with open ('fr-text.txt') as tx: #opening text containing the separated words

    text = word_tokenize(tx.read().lower()) #stores the text with the separated words


with open ('Fr-dictionary.txt') as fr:  #opens the dictionary
    dic = word_tokenize(fr.read().lower()) #stores the first dictionary

pat=re.compile(r'[.?\-",:;.?!»’\'()quls\d]+|\w+(?:-\w+)+')
reg= list(filter(pat.match, text))
out_file=open("newtext.txt","w") #defining name of output file
valid_words=[ ] #empty list to append the words checked 
invalid_words=[ ] #empty list to append the errors found

for word in text:
    if word in reg:
        valid_words.append(word)
    elif word in dic:
        valid_words.append(word)#appending to a list the words checked 
    else:
        invalid_words.append(word) #appending the invalid_words



a=' '.join(valid_words) #converting list into a string


#print(invalid_words) #print errors found

#out_file.write(a) #writing the output to a file

#out_file.close()

print ('output file:', a)

#print ('valid words', valid_words)
print ('invalid words:', invalid_words)

print('number of invalid words', len(invalid_words))
