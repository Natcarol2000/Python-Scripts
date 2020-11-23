import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

with open ('fr-text.txt') as tx2:  #opening text containing the separated words
    text_input = word_tokenize(tx2.read().lower()) #stores the input text


with open ('Fr-dictionary.txt') as fr:  #opens the dictionary
    dic = word_tokenize(fr.read().lower()) #stores the first dictionary

pat=re.compile(r'[.?\-",:;.?!»’\'()quls\d]+|\w+(?:-\w+)+')
reg= list(filter(pat.match, text_input))
    
words_it = iter(text_input) #interaction method

out_file1=open("finaltext.txt","w") #defining name of output file
valid_words1=[ ] #empty list to append the words checked 
invalid_words1=[ ] #empty list to append the errors found

for w in words_it: #looping through the tokenized text
    if w in dic:
        valid_words1.append(w)
    elif w in reg:
        valid_words1.append(w)#appending to a list the words checked 
    else:
        try:
            concatenated = w + next(words_it) #concatenating strings
            if concatenated in dic:
                valid_words1.append(concatenated) #checking if the concatenated strings is a valid word
        except StopIteration:
            pass
        else:
            invalid_words1.append(w) #appending the invalid_words


print(valid_words1)
print(invalid_words1)
print (len(invalid_words1))

x=valid_words1
y=invalid_words1

cat_x_y = []
text = []



#for each word in x check if they are in the dictonary 
for word in x:
    if word in dic:
        text.append(word)
#same for y
for word in y:
    if word in dic:
        text.append(word)

#for each word in x I want to add y and put it in cat_x_y
for i in range(len(x)):
    for word in y:
        cat_x_y.append(x[i]+word)

#for each word in y I want to add x and put it in cat_x_y
for j in range(len(y)):
    for word in x:
        cat_x_y.append(y[j]+word)

#remove duplicate in the cat_x_y:
cat_x_y = list(dict.fromkeys(cat_x_y))

#for each word in cat_x_y add the to text if they are in the dictionary
for word in cat_x_y:
    if word in dic:
        text.append(word)

#remove duplicate from text
text = list(dict.fromkeys(text))
print(text)

text_set=set(text)
x_set=set(x)


