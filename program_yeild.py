from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
import re
import os
import sys
from pathlib import Path


words = ['rien', '*', 'venue', 'pour', 'les','engage', '*', 'ment', 'trop', 'de', 'YIELD', 'peut','être','contre', '*', 'productif' ]

dic = ['Bien', '*', 'venue', 'pour', 'les','engage', '*', 'ment', 'trop', 'de', 'YIELD', 'peut','être','contre', '*', 'productif' ]

    
l=[ ]

def join_asterisk(ary):
    i, size = 0, len(ary)
    while i < size-2:
        if ary[i+1] == '*':
            if ary[i] + ary[i+2] in dic:
                yield ary[i] + ary[i+2]
                i+=2
            else:
                yield ary[i]
                i+=1
                l.append(ary[i] + ary[i+2])
    if i < size:
        yield ary[i]



print(list(join_asterisk(words)))



            
            
            
        
