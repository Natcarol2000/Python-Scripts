import nltk
from nltk.tokenize import word_tokenize

with open ('french_dic.txt') as fr: #open french dictionary

    dic = word_tokenize(fr.read()) #save it to a variable

with open ('fr-text.txt') as tx:  #open text containing the separated words
    wordsT = word_tokenize(tx.read()) #save it to a variable

words_it = iter(wordsT) #make text iterable

out_file=open("sentence.txt","w") #defines name of output file
valid_words=[ ] #appends the words checked by a dictionary

invalid_words=[ ] #append the errors found

for word in words_it: #loops through the tokenized text
    if word in dic:
        valid_words.append(word) #append to a list the words checked 
    else:
        try:
            concacenated = word + next(words_it) #concatenates strings
            if concacenated in dic:
                valid_words.append(concacenated) #check if the concatenated strings is a valid word
        except StopIteration:
            pass
        else:
            invalid_words.append(word) #appends the invalid_words

print (valid_words)

a=' '.join(valid_words) #convert list into a string

print(a) #print converted list
print(invalid_words) #print errors found

out_file.write(a) #writes the output to a file

out_file.close()









