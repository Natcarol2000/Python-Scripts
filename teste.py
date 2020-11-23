import re

wikifile = open('en-de-ref.txt') #opens file
sentences = wikifile.readlines()#reads file line by line

RegExp=re.compile("?<=origlang=de>.*?=</doc>")# matches and group the two parts of the pattern




for line in sentences:
    match=RegExp.findall(line)
    for word in match:
        print (word)
        
    





            
