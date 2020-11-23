from collections import defaultdict
import re
import string
import enchant


d=[ 'love', 'friend', 'car', 'apple', 'vi', 'computer']

words=['love', 'friend', 'car', 'apple', 'com', 'puter', 'vi']
words_it = iter(words)

valid_words = []

for word in words_it:
    if word in d:
        valid_words.append(word)
    else:
         try:
            concacenated = word + next(words_it)
            if concacenated in d:
                valid_words.append(concacenated)
                except StopIteration:
                    pass

print(valid_words)
# ['love', 'friend', 'car', 'apple', 'computer']
