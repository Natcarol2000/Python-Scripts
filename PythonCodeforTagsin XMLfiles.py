#!/bin/env python
#-*- encoding:utf-8 -*-

import re


def distFreq(SET, LIST):
    '''Returns a list with tuples Frequencies, Key'''

    freqX = []
    
    for x in SET:
        freqX.append((LIST.count(x), x))

    return freqX

def main():

    xmlFile = open(r'test.xml','rU') #opens the file
    xmlTest = [l[:-1] for l in xmlFile] #save the file to a list of lines
    xmlFile.close() #close the file
    
    del(xmlFile)
    
    xmlTest = xmlTest[1]
    tags = re.findall(r'<(\w+)[\s>]',xmlTest) #Find the tags
    lemmas = re.findall(r'<W[^>]+LEMMA="([^"]+)"[^>]+POS="N">',xmlTest)#find lemmas
    
    tagSet = set(tags)
    lemSet = set(lemmas)

    #Counts the tags and lemmas
    freqT = distFreq(tagSet,tags)
    freqL = distFreq(lemSet,lemmas)

    #Displays the results
    print "***** TAGS *****"
    freqT.sort(reverse=True)
    for i in freqT:
        print i[1]+" : "+ str(i[0])
    
    print
    print
    print "*****NOUN LEMMAS*****"
    freqL.sort(reverse=True)
    for i in freqL:
        print i[1]+" : "+ str(i[0])
    
if __name__ == "__main__": main()
