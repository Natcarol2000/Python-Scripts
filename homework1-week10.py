a=u"Дорогой друг"
b=open("string1.txt","w")

import codecs
b.write(a.encode("koi8-r"))
b.close()

import sys
import codecs
try:
    g=codecs.open("string1.txt", encoding="koi8-r")
    h=g.readline()
    i=h
    print "Reading the string from the file: ", i
except:
    print "\nSorry but this file does not exist."
    sys.exit(0)

print """\n\n1-USING STRING METHODS:"""

r=len(i)
print "\na) Length of the string is: ", r

t=i[1:10]
print "\nb)Slicing the string: ", t

u=i[2:6]
print "\nc)Slicing the string: ", u

print "\nd)Concatening the slices: ", t+u

print """\n\n2-USING REGULAR EXPRESSIONS:"""

import re
l=i



n=re.search(".",l)

print "\na)",n

m=re.search("^",l)

print "\nb)", m

o=re.search("o|p",l)

print "\nc)",o























                 



