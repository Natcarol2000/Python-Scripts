import nltk
from nltk.tokenize import word_tokenize



with open ('french_dic.txt') as fr: #opening text containing the separated words

    text = word_tokenize(fr.read().lower()) #stores the text with the separated words


with open ('Fr-dictionary.txt') as tx:  #opens the dictionary
    dic = word_tokenize(tx.read().lower()) #stores the first dictionary



out_file=open("newtext.txt","w") #defining name of output file
valid_words=[ ] #empty list to append the words checked 
invalid_words=[ ] #empty list to append the errors found

for word in text: #looping through the tokenized text
    if word not in dic:
        invalid_words.append(word) #appending to a list the words checked 
    else:
        valid_words.append(word) #appending the invalid_words

#print (text_input)

a=' '.join(valid_words) #converting list into a string

#print(a) #print converted list
#print(invalid_words) #print errors found

out_file.write(a) #writing the output to a file

out_file.close()

print ('checking done')
print(a)
print (invalid_words)


with open ('newtext.txt') as tx1:
    dic2 = word_tokenize(tx1.read().lower()) #stores second dictionary



with open ('fr-text.txt') as tx2:  #opening text containing the separated words
    text_input = word_tokenize(tx2.read().lower()) #stores the input text

words_it = iter(text_input) #interaction method

out_file1=open("sentencenew.txt","w") #defining name of output file
valid_words1=[ ] #empty list to append the words checked 
invalid_words1=[ ] #empty list to append the errors found

for w in words_it: #looping through the tokenized text
    if w in dic2:
        valid_words1.append(w) #appending to a list the words checked 
    else:
        try:
            concatenated = word + next(words_it) #concatenating strings
            if concatenated in dic2:
                valid_words1.append(concatenated) #checking if the concatenated strings is a valid word
        except StopIteration:
            pass
        else:
            invalid_words1.append(word) #appending the invalid_words

#print (text_input)

a1=' '.join(valid_words1) #converting list into a string


out_file1.write(a1) #writing the output to a file

out_file1.close()



print(a1) #print list converted into text

print(len(invalid_words))
