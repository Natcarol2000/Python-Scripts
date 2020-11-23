from collections import defaultdict
import re
import string
import enchant

document_text=open('fr-text.txt','r')
text_string=document_text.read().lower()
errors=[ ]
valid_words=[ ]
invalid_words=[ ]
dic=enchant.Dict('fr_FR')
#match_pattern = re.findall(r'[\W_]+', text_string)
match_pattern = re.findall(r'\b[a-z|A-Z|é|è|â|à|ê|ù|ô|û|î|ë|ï|ü|ÿ]{1,15}\b', text_string)
#match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
#frequency={}

d=defaultdict(int)
for w in match_pattern:



    if  dic.check(w) is True:

        d[w]+=1
        valid_words.append(w)
    else:

        errors.append(w) 


for w in sorted(d, key=d.get):

    print(w, d[w])

for e in errors:

    if dic.check(e) is True:
        valid_words.append(e)
    else:
        invalid_words.append(e)



ntx=' '.join(valid_words)

print(invalid_words)
print(ntx)


        

        

    
    #count=frequency.get(word,0)
    #frequency[word] = count+1



    



#print(errors)

    




    
#frequency_list=sorted(frequency.keys())

#for words in frequency_list:

#print (words, frequency[words]))
