import nltk
from nltk.tokenize import word_tokenize



with open ('Fr-dictionary.txt') as fr: #opening french dictionary

    dic = word_tokenize(fr.read().lower()) #stores first dictionary


#with open ('Fr-dictionary.txt') as fr2: #opening french dictionary

    #dic2 = word_tokenize(fr2.read().lower()) #stores second dictionary

with open ('fr-text.txt') as tx:  #opening text containing the separated words
    text_input = word_tokenize(tx.read().lower()) #stores the input text

words_it = iter(text_input) #interaction method

out_file=open("sentence.txt","w") #defining name of output file
valid_words=[ ] #empty list to append the words checked 
invalid_words=[ ] #empty list to append the errors found

for word in words_it: #looping through the tokenized text
    if word in dic:
        valid_words.append(word) #appending to a list the words checked 
    else:
        try:
            concatenated = word + next(words_it) #concatenating strings
            if concatenated in dic:
                valid_words.append(concatenated) #checking if the concatenated strings is a valid word
        except StopIteration:
            pass
        else:
            invalid_words.append(word) #appending the invalid_words

#print (text_input)

a=' '.join(valid_words) #converting list into a string

print(a) #print converted list
print(invalid_words) #print errors found
print(len(invalid_words))
print(len(text_input))
out_file.write(a) #writing the output to a file

out_file.close()










