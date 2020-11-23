from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path



def automatic ():

    #separate paratext

    print('\n\nREMINDER: TO RUN THIS PROGRAM YOUR PARATEXTUAL INFORMATION MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@PARAST@] AND [@PARAFN@]')

    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 12: SEPARATE PARATEXT. Please, insert your file path: "))
            break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")
        except NotADirectoryError:
            print('\nThis is not a directory. Better try again')

    pat = re.compile(r'(?<=\[@PARAST@\]).+?(?=\[@PARAFN@\])', flags=re.DOTALL)
    my_paratext=[]
    
    

    with open(file_to_open, 'r', encoding="utf-8") as file:
        for i in pat.findall(file.read()):
            my_paratext.append(i)
                

    print('Your book has',len(my_paratext), 'paratext instances')


    folder_path=Path(input('Enter your folder path and add the name of the new folder: '))

    try:
        os.makedirs(folder_path)
    except FileExistsError:
        print('This folder already exists. Try another name.')
        
    for j in range(len(my_paratext)):
        para='Paratext'+str(j+1) +'.txt'
        file = os.path.join(folder_path, para)
            
        with open(file, "w+") as f:
            for item in my_paratext[j]:
                f.write("%s" % str(item))
            #print('\n\n', para)
  
    print("\n\nParatexts written to a file separately. Check in your directory", folder_path)

    #remove paratext

    print('\n\nREMOVE PARATEXT \n\nREMINDER: TO RUN THIS PROGRAM YOUR PARATEXTUAL INFORMATION MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@PARAST@] AND [@PARAPFN@]')

    with open(file_to_open, 'r', encoding="utf-8") as file:
        a=file.read()

 
    pat=re.compile(r'(\[@PARAST@\]).+?(\[@PARAFN@\])', flags=re.DOTALL)

   
    s = re.sub(pat, '', a)

    remove_file_name='NO_PARATEXT'

 
    folder1_path=os.path.join(folder_path, remove_file_name)
    
    

    try:
        os.makedirs(folder1_path)
    except FileExistsError:
        print('This folder already exists. Try another name.')

    file1_name=input('Name your file. Extension not needed: ')
    fil1_name=file1_name + '.txt'
    new_file=os.path.join(folder1_path, fil1_name)

    
    with open(new_file, 'w') as f:
        f.write(s)
        print('\n\nText named', fil1_name, 'written to a file. Check folder named',folder1_path, 'in your directory')


        

    #separate chapters


    print('\n\nSEPARATE CHAPTERS')


    pat = re.compile(r'(?<=\[@CHAPST@\]).+?(?=\[@CHAPFN@\])', flags=re.DOTALL)
    my_chapters=[]


    with open(new_file, 'r', encoding="utf-8") as fil:
        for i in pat.findall(fil.read()):
            my_chapters.append(i)

    print('\n\nThis book contains',len(my_chapters), 'chapters')

    folder2_path=Path(input('Enter your folder path and add the name of the new folder: '))

    try:
        os.makedirs(folder2_path)
    except FileExistsError:
        print('This Folder already Exists. Try another name.')

    for j in range(len(my_chapters)):
        chap='Chapter'+str(j+1) +'.txt'
        file = os.path.join(folder2_path, chap)
            
        with open(file, "w") as c:
            for item in my_chapters[j]:
                c.write("%s" % str(item))
            #print('\n\n', chap)

    print('\n\nChapters 1 -',len(my_chapters), 'written to a file separately. Check your directory',folder2_path)

    #merge_chapters

    print('\n\nMERGE CHAPTERS')

    files_directory=folder2_path
           
    result = []
    
    Number_Chap=input('How many files do you want to merge? ')
    
    for chapter in range(int(Number_Chap)):
        file = os.path.join(files_directory, 'chapter{}.txt'.format(chapter+1))
        with open(file, 'r', encoding="utf-8") as f:
            result.append(f.read())
            
    J=' '.join(result)



    folder_directory=Path(input('Please, enter your folder path and add the new of the new folder: '))
        
    try:
        os.makedirs(folder_directory)
    except FileExistsError:
        print('This folder already exists. Try another name.')
    file_name=input('Name your file. Extension not needed: ')
    file_name1=file_name+'.txt'
    file_p=os.path.join(folder_directory,file_name1)
    with open(file_p,'w') as fi:
        fi.write(J)
    fi.close()
    print('Chapters merged into a file named',file_name1, 'check directory', file_p)


    #concatenate words

    print('\n\nCONCATENATE WORDS')

    with open(file_p,'r', encoding='utf=8') as conc:
        words = wordpunct_tokenize(conc.read())

    while True:
        try:
            dic_to_open=Path(input('\nPlease, enter your dictionary path: '))

            with open(dic_to_open) as d:
                dic=wordpunct_tokenize(d.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")


    l=[ ]
    errors=[ ]
    
    for n,word in enumerate (words):
        l.append(word)
        if word == "$":
            exp = words[n-1] + words[n+1]
            if exp in dic:
                l.append(exp)
                l.append("~")
                errors.append(words[n-1])
                errors.append(words[n+1])
            else:
                continue

    for i, w in enumerate(l):
        if w == "$":
            l.remove(l[i-1])
        else:
            continue

    for i, w in enumerate(l):
        if w == "~":
            l.remove(l[i+1])
        else:
            continue


    text=' '.join(l)

    e=len(errors)
    print('\n',float(e/2),'WORDS WERE CONCATENATED IN TEXT')
    user=input('\nRemove $ and ~ from text? \n1.Yes  \n2.No  \nSelection: ')


    if user=='1':
        sign=re.compile(r'$|~', flags=re.DOTALL)
        s = re.sub(sign, '', text)
    elif user=='2':
        print('Ok')

    #for x in l:
        #if user=='1' and x=='~':
            #l.remove(x)
        #elif user=='2' and x=='$':
            #l.remove(x)
        #else:
            #continue


    

    folder3_path=Path(input('Enter your folder path and add the name of the new folder: '))
    text3_name=input("\n\nName your file. Extension not needed: ")
    
    try:
        os.makedirs(folder3_path)
    except FileExistsError:
        print('This folder already exists. Try another name')
            
    file_name3 = text3_name+'.txt'
    file3 = os.path.join(folder3_path, file_name3)
            
    with open(file3, 'w') as f3:
        f3.write(text)

    print('\n\nText named',file_name3, 'was written to a file. Check your directory', folder3_path)

    #frequency lists -punctuation

    print('\n\nCREATE PUNCTUATION FREQUENCY LIST')

    with open(file3,'r', encoding='utf-8') as p:
        pu=p.read()

    while True:
        try:
            punc_dic_to_open=Path(input('\nPlease, insert your punctuation dictionary path: '))
            with open (punc_dic_to_open,'r', encoding="utf-8") as pr:
                dic_p = wordpunct_tokenize(pr.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")
    punc=[]
    words=[]
    d1=defaultdict(int)

    for p in pu:
        if p not in dic_p:
            words.append(p)
        elif p in dic_p:
            punc.append(p)

    for i in punc:
        d1[i]+=1
 
    punc_folder_path=Path(input('\n\nEnter the folder path and add the name of the new folder: '))        
    punc_file_name=input('\n\nName your file. Extension not needed: ')
    f_name=punc_file_name+'.txt'
    try:
        os.makedirs(punc_folder_path)
    except FileExistsError:
        print('This folder already exists. Try another name.')
    punc_file=os.path.join(punc_folder_path,f_name)
    punc_fi=open(punc_file,'w')
    for p1 in sorted(d1, key=d1.get):
        kr=p1
        r=d1[p1]
        row=kr+' '+str(r)+'\n'
        punc_fi.write(row)
    punc_fi.close()
    print('\n\nFrequency list named',f_name,'written to a file. Check your directory', punc_folder_path)

    #Word Frequency list

    print('\n\nCREATE WORD FREQUENCY LIST')

    with open(file3,'r', encoding='utf-8') as wr:
        w_f=wordpunct_tokenize(wr.read())


    pat1=re.compile(r"[.,:;?!'%-]|\d+") #regular expression for words with apostrophes and separated by hyphen
    a_h= list(filter(pat1.match, w_f))
    pat2=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b") #regular expression for words that start with capital letters (ex: proper nouns)
    c_l= list(filter(pat2.match, w_f))

    Cap_letters=[]

    df=defaultdict(int)

    for w in w_f:
        df[w]+=1
        if w in a_h:
            continue
        elif w in c_l:
            continue


    enter_path=Path(input('\n\nEnter your folder path and add the name of your new folder: '))
           
    enter_name=input('\n\nName your file. Extension not needed: ')         
    try:
        os.makedirs(folder_path)
    except FileExistsError:
        print('This folder already existis. Try another name.')
            
    final_name=enter_name+'.txt'    
    file_final=os.path.join(enter_path,enter_name)
    fiw=open(file_final,'w')
    for w1 in sorted(df, key=df.get):
        kw=w1
        fw=df[w1]
        roww=kw+' '+str(fw)+'\n'
        fiw.write(roww)
    fiw.close()
    print('\n\nFrequency list named',final_name,'written to a file. Check your directory named', enter_path)

    #Error list

    print('\n\nCREATE ERROR FREQUENCY LIST')

    with open(file3,'r', encoding='utf-8') as er:
        e_f=wordpunct_tokenize(er.read())


    while True:
        try:
            dic_to_open_errors=Path(input('\nPlease, insert your dictionary path: '))
            with open (dic_to_open_errors,'r', encoding="utf-8") as err:
                dicc = word_tokenize(err.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")


    pa=re.compile(r"[.,:;?!'%-]|\d+") #regular expression for words with apostrophes and separated by hyphen
    p_match= list(filter(pa.match, e_f))
    pa1=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b") #regular expression for words that start with capital letters (ex: proper nouns)
    e_l= list(filter(pa1.match, e_f))

    Cap_n=[]
    errors=[ ]
    d2=defaultdict(int)

    for e in e_f:
        d2[w]+=1
        if e in p_match:
            continue
        elif e in e_l:
            Cap_n.append(e)
        elif e not in dicc:
            errors.append(e)


    for x1 in errors:
        d2[x1]+=1


    folder2_path_errors=Path(input('\n\nEnter your folder path and add the name of your new folder: '))
  
    file2_name_errors=input('\n\nName your file. Extension not needed: ')
    try:
        os.makedirs(folder2_path_errors)
    except FileExistsError:
        print('This folder already exists. Try another name.')

    f2_name_errors=file2_name_errors+'.txt'
    file2_errors=os.path.join(folder2_path_errors,f2_name_errors)

    fi2_errors=open(file2_errors,'w')
    for x2 in sorted(d2, key=d2.get):
        we=x2
        wre=str(d2[x2])
        row2= we+' '+str(wre)+'\n'
        fi2_errors.write(row2)
    fi2_errors.close()
    print("\n\nFrequency list named",f2_name_errors, 'written to a file.Check your directory', folder2_path_errors)

    #Split text into sentences

    print('\n\nSPLIT TEXT INTO SENTENCES')

    with open(file3,'r', encoding='utf-8') as s:
       sent=sent_tokenize(s.read())

    s_path=Path(input('Enter your folder path and add the name of your new folder: '))
        
    s_name=input("\n\nName your file. Extension not needed: ")
        
    try:
        os.makedirs(s_path)
    except FileExistsError:
        print("This folder already exists. Try another name.")
    s_file_name = s_name +'.txt'
    s_file = os.path.join(s_path, s_file_name)
    with open(s_file, 'w') as ts:
        for i in sent:
            a='\n\n'+i
            ts.write(a)
        ts.close()
        print('\n\nText named', s_name, 'split into sentences written to a file. Check your directory', s_path)

    #Calculate sentence length

    print('\n\nCALCULATE SENTENCE LENGTH')

    with open(file3,'r', encoding="utf-8") as v:
        words_s = sent_tokenize(v.read())

    print('\n\n This file contains',len(words_s),'sentences in total')
                

    


    sent_number=1

    wordcounts = []
    
    with open(file3,'r',encoding='utf-8') as s_l:
        text_l = s_l.read()
        sentences = sent_tokenize(text_l)
        for sentence in sentences:
            w = word_tokenize(sentence)
            wordcounts.append(len(w))

    average_wordcount = sum(wordcounts)/len(wordcounts)

    a='The longest sentence of this file contains',max(wordcounts), 'tokens'
    b='The shortest sentence of this file contains',min(wordcounts),'tokens'
    c='The mean sentence length of this file is: ',average_wordcount
    print(a)
    print(b)
    print(c)


    folder_s_path=Path(input('\n\nEnter the directory of your new folder: '))
        
    try:
        os.makedirs(folder_s_path)
    except FileExistsError:
        print('This folder already exists. Try again.')
    stext_name=input("\n\nName your file. Extension not needed: ")
    sfile_name = stext_name +'.txt'
    sfile = os.path.join(folder_s_path, sfile_name)
    with open(sfile, 'w') as t1:
        for y in words_s:
            x=word_tokenize(y)
            pr='\nSentence '+str(sent_number)+' contains '+str(len(x))
            sent_number +=1
            t1.write(pr)
        t1.close()
        print('\n\nFile named',sfile_name,'written to a file.Check your directory',folder_s_path)
            
    
    


automatic()
