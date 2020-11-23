import nltk
from nltk.tokenize import word_tokenize
import re

with open ('fr-text.txt') as tx: #opening text containing the separated words

    text = word_tokenize(tx.read().lower()) #stores the text with the separated words


with open ('Fr-dictionary.txt') as fr:  #opens the dictionary
    dic = word_tokenize(fr.read().lower()) #stores the first dictionary

pat=re.compile(r'[.?\-",:;.?!»’()quls\d]+|\w+(?:-\w+)+')
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

out_file.write(a) #writing the output to a file

out_file.close()

#print (a)

#print (invalid_words)
#print(len(invalid_words))


with open ('newtext.txt') as tx1:
    dic2 = word_tokenize(tx1.read().lower()) #stores second dictionary

with open ('fr-text.txt') as tx2:  #opening text containing the separated words
    text_input = word_tokenize(tx2.read().lower()) #stores the input text

words_it = iter(text_input) #interaction method

out_file1=open("finaltext.txt","w") #defining name of output file
valid_words1=[ ] #empty list to append the words checked 
invalid_words1=[ ] #empty list to append the errors found

for w in words_it: #looping through the tokenized text
    if w in dic:
        valid_words1.append(w)
    elif w in dic2:
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




a1=' '.join(valid_words1) #converting list into a string


out_file1.write(a1) #writing the output to a file
out_file1.close()



#print(a1) #print list converted into text
print(valid_words)
#print(invalid_words1)
#print(len(invalid_words))


x=valid_words1
y=invalid_words1




s_text=set()
cat_x_y = []



for j in range(len(x)):
    for i in y:
        cat_x_y.append(x[j]+i)

for i in cat_x_y:
    if i in dic:
        s_text.add(i)

new_conc=list(s_text)


X=x
Y=new_conc

l = []

for x in X:
    for y in Y:
        for i in x:
            if i in y:
                l.append(i)
            else:
                l.append(x)


print(l)






