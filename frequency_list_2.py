from collections import defaultdict
import re
import string
import enchant

document_text=open('fr-text.txt','r')
text_string=document_text.read().lower()
errors=[ ]
dic=enchant.Dict('en_UK')
#match_pattern = re.findall(r'[\W_]+', text_string)
match_pattern = re.findall(r'\b[a-zA-Z0-9_]{1,15}\b', text_string)
pat=r'[.?\-",]+'
#match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
#frequency={}

d=defaultdict(int)
for w in match_pattern:

    if  dic.check(w) is True:

        d[w] += 1
    else:

        continue 


for w in sorted(d, key=d.get):

    print(w, d[w])
        

    
    #count=frequency.get(word,0)
    #frequency[word] = count+1



    



#print(errors)

    




    
#frequency_list=sorted(frequency.keys())

#for words in frequency_list:

#print (words, frequency[words])
