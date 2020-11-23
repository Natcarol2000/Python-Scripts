import re
while True:
    roman_number = input("Enter Roman Numeral: ")
    b = re.compile(r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
    c = b.match(roman_number)
    if c:
        print ("Valid Roman Number")
        break
    else:
        print ("Invalid Roman Number.Try again")
        continue

dic_roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
arabic=0
for i in range(len(roman_number)-1):
    if dic_roman[roman_number[i+1]] > dic_roman[roman_number[i]]:
        arabic -= dic_roman[roman_number[i]]
    else:
        arabic += dic_roman[roman_number[i]]
arabic += dic_roman[roman_number[len(roman_number)-1]]
print (arabic)




    




    


            
    
    




    
    

    
        
    
    



