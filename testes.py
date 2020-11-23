import nltk

from nltk.tokenize import word_tokenize


with open ('Fr-dictionary.txt') as d:
    dic = word_tokenize(d.read().lower())


x=['les', 'engage', 'président', 'de', 
'la', 'république', 'sont', 'aussi', 
'ceux', 'des', 'dirigeants', 'de', 'la', 
'société', 'ferroviaire', ',', 'a-t-il', 
'soutenu', 'de', 'élus', 'du', 'réunis', 
'à', '’', 'le', 'président', 'de', 'la', 
'république', ',', '(', 'à', 'droite', 
')', ',', 'aux', 'côtés', 'du', 'patron', 
'de', 'la', ',', 'guillaume', 'à', 'la', 
'gare', 'à', 'paris', ',', 'le', 
'juillet', 'der', '’', 'irrita', ',', 
'par', 'fois', ',', '’', 'usa', 'la', 
'face', 'aux', 'trains', 'supprimés', 
'aux', 'dessertes', 'abandonnées', 
'semble', 'avoir', 'aussi', 'saisi', 'le', 
'président', 'de', 'la', 'république', 
'.', 'devant', 'des', 'élus', 'du', ',', 
'réunis', 'mardi', 'février', 'à', '’', 
'le', 'cadre', 'du', 'grand', 'débat', 
',', 'a', 'eu', 'des', 'mots', 'très', 
'durs', 'contre', 'la', ',', 'qui', 'a', 
'fermé', 'la', 'ligne', '-', 'décembre', 
',', 'alors', 'que', 'le', 'chef', 'de', 
'’', '’', 'était', 'engagé', ',', 
'durant', 'un', 'déplacement', 'dans', 
'les', 'tué', 'en', 'avril', ',', 'à', 
'ce', '’', 'elle', 'reste', 'opération']

y=['ments', 'prési', 'républi', 'vant', 
'elysée', 'emmanuel', 'macron', 'cô', 
'pepy', 'montparnasse', 'geoffroy', 
'hasselt', '/', 'afp', 'tion', 'empare', 
'gers', 'més', 'elysée', 'emmanuel', 
'macron', 'epinal', 'etat', 'dépla', 
'cement', 'vosges', 'effec', 'nelle']



set_text=set()


cat_x_y = []
text = []

for word in x:
    if word in dic:
        text.append(word)
for i in range(len(x)):
    for word in y:
        cat_x_y.append(x[i]+word)

for word in cat_x_y:
    if word in dic:
        set_text.add(word)

print(x)
#print(list(set_text))

Y=list(set_text)
X=x
l = []

for x in X:
    for y in Y:
        if y.startswith(x):
            l.append(y)
            break
    else:
        l.append(x)

print(l)






