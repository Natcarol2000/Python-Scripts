import re


wikifile = open('wiki-file.txt') #opens file
sentences = wikifile.readlines()#reads file line by line

RegExp=re.compile("\([^|]+?)\s*\|\s*(.*)\]")# matches and group the two parts of the pattern

out_file=open("new-wiki.txt","w") # creates a new file 
text="" # receives the text not matched by RE

for match in sentences: #loops trough the lines of the text 
    a=RegExp.search(match) #searches for the patterns
    if a==None: #establishes a condition for text not matched by pattern 
        text=match # attach the rest of the text in an empty string
    else: #otherwise
        url=a.group(2) # store second part of RE
        original=a.group(1) # store first part of RE
        inverted_text="[" + url  + " | " + original  + "]" # invert the parts
        text=RegExp.sub(inverted_text, match) # substitutes by the lines
    out_file.write(text) # write everything into a new file

out_file.close() # close the new file





    
   

             
                         
