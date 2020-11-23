import re
while True:
    roman = raw_input("Enter a roman numeral from I to X: ") # ask user for input
    a=re.compile(r"I|II|III|IV|V|VI|VII|VIII|IX|X|")#pattern matches the input
    if roman == "I": # if-elif-else structure establishes the conditions and substitutes the input for the equivalent arabic numeral 
        b=a.sub("1",roman) 
        print b
        continue
    elif roman =="II":
        c=a.sub("2", roman[0])
        print c
        continue
    elif roman=="III":
        d=a.sub("3",roman[0:1])
        print d
        continue
    elif roman=="IV":
        k=a.sub("4",roman[0])
        print k
        continue
    elif roman=="V":
        e=a.sub("5",roman)
        print e
        continue
    elif roman=="VI":
        f=a.sub("6",roman[0])
        print f
        continue
    elif roman=="VII":
        g=a.sub("7",roman[0:1])
        print g
        continue
    elif roman=="VIII":
        h=a.sub("8",roman[0:1])
        print h
        continue
    elif roman=="IX":
        i=a.sub("9",roman[0])
        print i
        continue
    elif roman=="X":
        j=a.sub("10",roman)
        print j
        continue
    else:
        print "Invalid roman number" # stops the loop if the input is invalid the loop stops
        break

    



    
















    

