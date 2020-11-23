from xml.dom import minidom
xmldoc = minidom.parse(xml)
xml.close()
wlist = xmldoc.getElementsByTagName("W")

elements = xmldoc.getElementsByTagName("*")
#len(elements)
d = {}
for e in elements:
    if e.nodeName in d:
        d[e.nodeName] += 1
    else:
        d[e.nodeName] = 1
for k in d:
    print k, "\t\t",d[k], "times"

print """\nb) a frequency list of the lemma of the nouns in the file:\n"""

wordlist = []
LEMMA = {}
for indexGeral in range(wlist.length):
    slist = wlist[indexGeral].attributes["POS"].value
    noun_lemma = wlist[indexGeral].attributes["LEMMA"].value
    if slist == "N":
        wordlist.append(noun_lemma)
for word in wordlist:
    if word in LEMMA:
        LEMMA[word] += 1
    else:
        LEMMA[word] = 1
for word in LEMMA:
    print word, "\t\t", LEMMA[word]

raw_input("\nPress the enter key to exit.")
