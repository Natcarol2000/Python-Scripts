from collections import defaultdict
import enchant
import string
words=['love', 'friend', 'car', 'apple', 'com', 'puter', 'vi']
myit = iter(words)
dic=enchant.Dict('en_UK')
lst=[]

errors=[]

for i in words:

   if  dic.check(i) is True:

      lst.append(i)

   if dic.check(i) is False:

      a= i + next(myit)

   if a is True:

      lst.append(a)

   else:

      continue

   


print (lst)

   


                 










                 

                 
                 
