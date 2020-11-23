import re # imports RE module
string = raw_input("Enter a string: ")# Ask user for input
pat = re.match(r"^([bcdfghjklmnpqrstvwxyz]*)(\w*)$", string) # parttern divide string into two parts, first part matches the consonants
a=pat.group(2)+ pat.group(1)+"ay"  # invert the parts and add "ay"

print "The Pig Latin string is: ", a # print the string inverted 



