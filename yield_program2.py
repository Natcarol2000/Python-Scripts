# That look better to me (just in case you change it later)
import nltk
from nltk.tokenize import word_tokenize

word_separator = '*'

with open('fr-text.txt') as f:
   words = word_tokenize(f.read().lower())

with open ('Fr-dictionary2.txt') as fr:
   dic = word_tokenize(fr.read().lower())

def join_asterisk(ary):
   for w1, w2, w3 in zip(words, words[1:], words[2:]):
      if w2 == word_separator:
         word = w1 + w3
         yield (word, word in dic)
      elif w1 != word_separator and w1 in dic: 
         yield (w1, True)


correct_words = []
incorrect_words = []
#for word, is_correct in join_asterisk(words):
  #if is_correct:
    #correct_words.append(word)
  #else:
    #incorrect_words.append(word)




correct_words = [w for w, correct in join_asterisk(words) if correct]
incorrect_words = [w for w, correct in join_asterisk(words) if not correct]
print(correct_words)
print(incorrect_words)
