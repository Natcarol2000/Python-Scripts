import random
import re

plist1=["ca","ce","ci","co","con","pa","pe","pi","po","pon","ta","te","ti","to","ton","da","de","di","do","don","va","ve","vi","vo","von","ca","a","e","i","o"]
plist2=["ce","ci","co","cu","pe","pi","po","pu","te","ti","to","tu","ve","vi","vo","vu","me","mi","mo","mu","cer","cir","cor","cur","per","pir","por","pur","ter","tir","tor","tur","ver","vir","vor","vur","mer","mir","mor","mur","ces","cis","cos","cus","pes","pis","pos","pus","tes","tis","tos","tus","ves","vis","vos","vus","mes","mis","mos","mus"]
plist3=["tar","rar","car","mar","tar"]
slist1=["ca","ce","co","pa","pe","po","da","de","do","fa","fe","fo","ra","re","ro","va","ve","vo"]
slist2=["ca","ce","ci","co","cen","da","de","di","do","den","fa","fe","fi","fo","fen","ma","me","mi","mo","men","pa","pe","pi","po","pen","ta","te","ti","to","ten","va","ve","vi","vo","ven","cer","der","fer","mer","per","ter","ver","cor","dor","for","mor","por","tor","vor","ces","des","fes","mes","pes","tes","ves","cos","dos","fos","mos","pos","tos","vos"]
slist3=["cer","der","ver","ter"]
tlist1=["on","in","a","e","o","ca","ce","co","da","de","do","pa","pe","po","sa","se","so"]
tlist2=["cer","mer","fer","ter","ver","cir","mir","fir","tir","vir","cur","mur","fur","tur","vur","ces","mes","fes","tes","ves","cis","mis","fis","tis","vis","cus","mus","fus","tus","vus","ca","ce","ci","co","cu","ma","me","me","mi","mo","mu","fa","fe","fi","fo","fu","ta","te","ti","to","tu","va","ve","vi","vo","vu"]
tlist3=["bir","tir","dir","rir","jir","vir"]

number = 'sair'
running= True


while running:
    user=raw_input("Entre com a conjuga��o desejada para o pseudoverbo: digite P (primeira conjugação), S (segunda conjugação), T (terceira conjugação) ou digite 'sair' para terminar o programa: ")
    computerp1=random.choice(plist1)
    computerp11=random.choice(plist1)
    computerp12=random.choice(plist1)
    computerp2=random.choice(plist2)
    computerp21=random.choice(plist2)
    computerp22=random.choice(plist2)
    computerp3=random.choice(plist3)
    computerp31=random.choice(plist3)
    computerp32=random.choice(plist3)
    computers1=random.choice(slist1)
    computers11=random.choice(slist1)
    computers12=random.choice(slist1)
    computers2=random.choice(slist2)
    computers21=random.choice(slist2)
    computers22=random.choice(slist2)
    computers3=random.choice(slist3)
    computers31=random.choice(slist3)
    computers32=random.choice(slist3)
    computert1=random.choice(tlist1)
    computert11=random.choice(tlist1)
    computert12=random.choice(tlist1)
    computert2=random.choice(tlist2)
    computert21=random.choice(tlist2)
    computert22=random.choice(tlist2)
    computert3=random.choice(tlist3)
    computert31=random.choice(tlist3)
    computert32=random.choice(tlist3)
    list1=[]
    list2=[]
    list3=[]
    listP=[]
    listS=[]
    listT=[]
    pat='nm|nl|nrr|sr|nr|np|srr|ji'
    if user == number:
        print 'Você terminou o programa'
        running = False
    elif user == "P":
        list1.append(computerp1+computerp3)
        list1.append(computerp11+computerp31)
        list1.append(computerp12+computerp32)
        list1.append(computerp1+computerp2+computerp3)
        list1.append(computerp11+computerp21+computerp31)
        list1.append(computerp12+computerp22+computerp32)
        for i in list1:
            if re.search(pat,i) == None:
                listP.append(i)
                print listP
                continue

    elif user == "S":
        list2.append(computers1+computers3)
        list2.append(computers11+computers31)
        list2.append(computers12+computers32)
        list2.append(computers1+computers2+computers3)
        list2.append(computers11+computers21+computers31)
        list2.append(computers12+computers22+computers32)
        for i in list2:
            if re.search(pat,i) == None:
                listS.append(i)
                print listS
                continue

    elif user == "T":
        list3.append(computert1+computert3)
        list3.append(computert11+computert31)
        list3.append(computert12+computert32)
        list3.append(computert1+computert2+computert3)
        list3.append(computert11+computert21+computert31)
        list3.append(computert12+computert22+computert32)
        for i in list3:
            if re.search(pat,i) == None:
                listT.append(i)
                print listT
                continue
    else:
        print "comando n�o permitido, tente novamente"

print 'Até logo!'
        
            


