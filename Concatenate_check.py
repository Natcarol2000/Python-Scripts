from collections import defaultdict
import re
import string
import enchant

document_text=open('test-list.txt','r')
text_string=document_text.read().lower()

lst=[ ]
errors =[ ]

dic=enchant.Dict('en_UK')
#match_pattern = re.findall(r'[\W_]+', text_string)
match_pattern = re.findall(r'\b[a-zA-Z0-9_]{1,15}\b', text_string)
#match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
#frequency={}

d=defaultdict(int)



for w in match_pattern:

    if dic.check(w) is True:

        lst.append(w)
    else:

        a=list(map(''.join, zip(*([iter(lst)]*2))))

        dic.check(a)


    
        


    
  

    







        

        
    
    #count=frequency.get(word,0)
    #frequency[word] = count+1



    



#print(errors)

    




    
#frequency_list=sorted(frequency.keys())

#for words in frequency_list:

#print (words, frequency[words])
