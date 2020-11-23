
from collections import defaultdict
import re
import string
import enchant

document_text=open('test-list.txt','r')
text_string=document_text.read().lower()


lst=[]
text=""
errors=[]

dic=enchant.Dict('en_US')
d=defaultdict(int)
match_pattern = re.findall(r'\b[a-zA-Z0-9_]{1,15}\b', text_string)

for w in match_pattern:

    lst.append(w)

for i in lst:

    if dic.check(i) is True:
        text=i
    else:

        errors.append(i)

        #list(map(''.join, zip(*([iter(w)]*2))))

        #errors.append(a)



print (text)


#a=list(map(''.join, zip(*([iter(lst)]*2))))




    




            
