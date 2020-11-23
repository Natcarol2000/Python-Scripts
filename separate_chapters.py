import re


file = open('text1_scott.txt') #opens file
sentences = file.readlines()#reads file line by line

RegExp=re.compile(r"[\@introS\].[\@introEnd\@]")# matches and group the two parts of the pattern

out_file=open("text1_scott_chapters.txt","w") # creates a new file 
non_text=""
text=""

for match in file: #loops trough the lines of the text 
    a=RegExp.search(match) #searches for the patterns
    if a==None: #establishes a condition for text not matched by pattern 
        non_text=match # attach the rest of the text in an empty string
    else:
        text=match#otherwise


print(text)

    


    
   

             
                         
