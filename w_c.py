x=['les', 'engage', 'président', 'de', 'la', 'république', 'sont', 'aussi', 'ceux', 'des', 'dirigeants', 'de', 'la', 'société', '»', 'ferroviaire', ',', 'a-t-il', 'soutenu', 'de', 'élus', 'du', 'grand-est', 'réunis', 'à', 'l', '’', 'le', 'président', 'de', 'la', 'république', ',', '(', 'à', 'droite', ')', ',', 'aux', 'côtés', 'du', 'patron', 'de', 'la', 'sncf', ',', 'guillaume', 'à', 'la', 'gare', 'à', 'paris', ',', 'le', '1er', 'juillet', '2017.', 'der', '’', 'irrita', ',', 'par', 'fois', ',', 's', '’', 'usa', 'la', 'sncf', 'face', 'aux', 'trains', 'suppri', 'aux', 'dessertes', 'abandonnées', 'semble', 'avoir', 'aussi', 'saisi', 'le', 'président', 'de', 'la', 'république', '.', 'devant', 'des', 'élus', 'du', 'grand-est', ',', 'réunis', 'mardi', '26', 'février', 'à', 'l', '’', 'le', 'cadre', 'du', 'grand', 'débat', ',', 'a', 'eu', 'des', 'mots', 'très', 'durs', 'contre', 'la', 'sncf', ',', 'qui', 'a', 'fermé', 'la', 'ligne', 'saint-dié', '-', '23', 'décembre', '2018', ',', 'alors', 'que', 'le', 'chef', 'de', 'l', '’', '’', 'était', 'engagé', ',', 'durant', 'un', 'déplacement', 'dans', 'les', 'tué', 'en', 'avril', '2018', ',', 'à', 'ce', 'qu', '’', 'elle', 'reste', 'opération']
y=['ments', 'prési', 'républi', 'vant', 'elysée', 'emmanuel', 'macron', 'cô', 'pepy', 'montparnasse', 'geoffroy', 'hasselt', '/', 'afp', 'tion', 'empare', 'gers', 'més', 'elysée', 'emmanuel', 'macron', 'epinal', 'etat', 'dépla', 'cement', 'vosges', 'effec', 'nelle']

iter_x=iter(x)
iter_y=iter(y)
dic=set(['engagements','opérationnelle','chef','elysée'])
in_dic=set()
text=[ ]
errors=[ ]
for i in iter_x:
    if i in dic:
        text.append(i)
    else:
        for j in iter_y:
            try:
                concatenated = i + j
                if concatenated in dic:
                    text.append(concatenated)

            else:
                continue




print(text)
print(errors)
