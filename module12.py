from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path



def automatic ():

    #u=input('If you want to return to options, type "1": ')
    
    #while True:
        #if u == '1':
            #menu()
            #break
        #else:
            #break

    print('\n\nREMINDER: TO RUN THIS PROGRAM YOUR PARATEXTUAL INFORMATION MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@PARAST@] AND [@PARAFN@]')

    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 12: SEPARATE PARATEXT. Please, insert your file path: "))
            break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

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
            print('\n\n', para)
  
    print("\n\nParatexts written to a file separately. Check in your directory", folder_path)

    print('\n\nREMOVE PARATEXT \n\nREMINDER: TO RUN THIS PROGRAM YOUR PARATEXTUAL INFORMATION MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@PARAST@] AND [@PARAPFN@]')

 
    pat=re.compile(r'(\[@PARAST@\]).+?(\[@PARAFN@\])', flags=re.DOTALL)

   
    s = re.sub(pat, '', file)

 
    folder1_path=Path(input('Enter your folder path and add the name of the new folder: '))
    
    

    try:
        os.makedirs(folder1_path)
    except FileExistsError:
        print('This folder already exists. Try another name.')

    file1_name=input('Name your file. Extension not needed: ')
    fil1_name=file1_name + '.txt'
    new_file=os.path.join(folde1_path, fil1_name)

    
    with open(new_file, 'w') as f:
        f.write(s)
        print('\n\nText named', fil1_name, 'written to a file. Check folder named',folder1_path, 'in your directory')


    print('\n\nSEPARATE CHAPTERS \n\nREMINDER: TO RUN THIS PROGRAM YOUR BOOK CHAPTERS MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@CHAPST@] AND [@CHAPFN@]')


    pat = re.compile(r'(?<=\[@CHAPST@\]).+?(?=\[@CHAPFN@\])', flags=re.DOTALL)
    my_chapters=[]
    

    with open(file_to_open, 'r', encoding="utf-8") as file:
        for i in pat.findall(file.read()):
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
            
        with open(file, "w") as f:
            for item in my_chapters[j]:
                f.write("%s" % str(item))
            print('\n\n', chap)

    print('\n\nChapters 1 -',len(my_chapters), 'written to a file separately. Check your directory',folder_path)

    print('\n\nCONCATENATE WORDS \n\nREMINDER: TO RUN THIS PROGRAM YOUR TEXT MUST CONTAIN A DOLLAR SIGN ($) AT THE END OF EACH LINE BREAK')

    

    while True:
        try:
            file1_to_open=Path(input("\nYOU SELECTED OPTION 12: SEPARATE PARATEXT. Please, insert your file path: "))
            with open(file1_to_open, 'r', encoding='utf-8') as x:
                wor=wordpunct_tokenize(x.read())
            break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")
    
    while True:
        try:
            dic1_to_open=Path(input('\nPlease, enter your dictionary path: '))

            with open(dic1_to_open,'r', encoding="utf-8") as d:
                dic=wordpunct_tokenize(d.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")


    l=[ ]
    errors=[ ]
    for n,word in enumerate (wor):
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
    #print('\n\n',text)
    e=len(errors)
    print('\n',float(e/2),'WORDS WERE CONCATENATED IN TEXT',errors)
    user=input('\nRemove $ and ~ from text? \n1.Yes  \n2.No  \nSelection: ')

    for x in l:
        if user=='1' and x=='~':
            l.remove(x)
        elif user=='2' and x=='$':
            l.remove(x)
        else:
            continue


    final_text=' '.join(l)


        
    #print('\n\n', final_text)

         

    folder3_path=Path(input('Enter your folder path and add the name of the new folder: '))
    text3_name=input("\n\nName your file. Extension not needed: ")
    
    try:
        os.makedirs(folder3_path)
    except FileExistsError:
        print('This folder already exists. Try another name')
            
    file3_name = text3_name+'.txt'
    file3 = os.path.join(folder3_path, file3_name)
            

    with open(file3, 'w') as f:
        f.write(final_text)
        print('\n\nText named',file3_name +'was written to a file. Check your directory', folder3_path)


    print('\n\nFREQUENCY LISTS')

    while True:
        try:
            punc_dic_to_open=Path(input('Enter your punctutation dictionary: '))
            with open (punc_dic_to_open,'r', encoding="utf-8") as fr:
                dic_punc = wordpunct_tokenize(fr.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")


    with open(file1_to_open,'r', encoding="utf-8") as f:
        freq = wordpunct_tokenize(f.read())
        
    punc=[]
    words1=[]
    d1=defaultdict(int)

    for p in freq:
        if p not in dic_punc:
            words1.append(p)
        elif p in dic_punc:
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
        print(p1,d1[p1])
        k=p1
        fr=d1[p1]
        row=k+' '+str(fr)+'\n'
        punc_fi.write(row)
        punc_fi.close()
    print('\n\nFrequency list named',f_name,'written to a file. Check your directory', punc_folder_path)
        

       
    with open(file1_to_open,'r', encoding="utf-8") as fi:
        freq1 = wordpunct_tokenize(fi.read())
                    

    pat=re.compile(r"[.,:;?!'%-]|\d+") #regular expression for words with apostrophes and separated by hyphen
    reg= list(filter(pat.match, freq))

    patt=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b") #regular expression for words that start with capital letters (ex: proper nouns)
    c_n= list(filter(patt.match, freq))



    Cap_nouns=[]
        
    d=defaultdict(int)
    d2=defaultdict(int)
    d3=defaultdict(int)

    for w in freq1:
        d[w]+=1
        if w in reg:
            continue
        elif w in c_n:
            continue


    folder4_path=Path(input('\n\nEnter your folder path and add the name of your new folder: '))
           
    file4_name=input('\n\nName your file. Extension not needed: ')
                
    try:
        os.makedirs(folder_path)
    except FileExistsError:
        print('This folder already existis. Try another name.')
            
    f_name=file4_name+'.txt'    
    file=os.path.join(folder4_path,f_name)
    fi=open(file,'w')
    for w1 in sorted(d, key=d.get):
        k=w1
        fr=d[w1]
        row=k+' '+str(fr)+'\n'
        fi.write(row)
        fi.close()
    print('\n\nFrequency list named',f_name,'written to a file. Check your directory named', folder4_path)


        
    
    while True:
        try:
            file1_to_open =Path(input("\nPlease, insert your file path: "))
            dic1_to_open=Path(input('\nPlease, insert your dictionary path: '))
            with open(file1_to_open,'r', encoding="utf-8") as f1:
                frequ = wordpunct_tokenize(f1.read())
            with open (dic_to_open,'r', encoding="utf-8") as fr1:
                dicc = word_tokenize(fr1.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    pat=re.compile(r"[.,:;?!'%-]|\d+") #regular expression for words with apostrophes and separated by hyphen
    reg1= list(filter(pat.match, freq))
    patt=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b") #regular expression for words that start with capital letters (ex: proper nouns)
    c_n1= list(filter(patt.match, freq))

    Cap_nouns=[]
    errors1=[ ]
    d=defaultdict(int)
    d2=defaultdict(int)
    d3=defaultdict(int)

    for w in frequ:
        d[w]+=1
        if w in reg1:
            continue
        elif w in c_n1:
            Cap_nouns.append(w)
        elif w not in dic:
            errors1.append(w)
            


    for x1 in errors:
        d2[x1]+=1

  
    folder2_path=Path(input('\n\nEnter your folder path and add the name of your new folder: '))
  
    file2_name=input('\n\nName your file. Extension not needed: ')
    try:
        os.makedirs(folder2_path)
    except FileExistsError:
        print('This folder already exists. Try another name.')

    f2_name=file2_name+'.txt'
    file2=os.path.join(folder2_path,f2_name)

    fi2=open(file2,'w')

    for x2 in sorted(d2, key=d2.get):
        we=x2
        fre=str(d2[x2])
        row2= we+' '+str(fre)+'\n'
        fi2.write(row2)
        fi2.close()
    print("\n\nFrequency list named",f2_name, 'written to a file.Check your directory', folder2_path)

  
    
    while True:
        try:
            file_to_open =Path(input("\nPlease, insert your file path: "))
            dic_to_open=Path(input('\nPlease, insert your dictionary path: '))
            with open(file_to_open,'r', encoding="utf-8") as f:
                freq = wordpunct_tokenize(f.read())
            with open (dic_to_open,'r', encoding="utf-8") as fr:
                dic = word_tokenize(fr.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    pat=re.compile(r"[.,:;?!'%-]|\d+") #regular expression for words with apostrophes and separated by hyphen
    reg= list(filter(pat.match, freq))
    patt=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b") #regular expression for words that start with capital letters (ex: proper nouns)
    c_n= list(filter(patt.match, freq))
    Cap_nouns=[]

    d3=defaultdict(int)
        
    for w in freq:
        if w in c_n:

    Cap_nouns.append(w)

    #continuar


        display_Cap=input('\n\nWrite the list of capitalised words to a file?" |\n1.Yes \n2.No: ')
        folder_setup=input('\n\n1.Create a folder for the file \n\n2.Select a directory for your files \n\n3.No file saved \n\nSelection: ')

        for y in Cap_nouns:
            if y not in dic:
                d3[y]+=1

        if display_Cap == '1' and folder_setup == '1':
            folder2_path=Path(input('\n\nEnter your folder path and the add the name of your new folder: '))
            file2_name=input('\n\nName your file. Extension not needed: ')
            fi2_name= file2_name +'.txt'
            try:
                os.makedirs(folder2_path)
            except FileExistsError:
                print('This folder already exists. Try another name.')
            file2=os.path.join(folder2_path,fi2_name)
            fi2=open(file2,'w')
            for x2 in sorted(d3, key=d3.get):
                we=x2
                fre=str(d3[x2])
                row2= we+' '+str(fre)+'\n'
                fi2.write(row2)
            fi2.close()
            print("\n\nFrequency list named",file2_name, 'written to a file.Check your directory', folder2_path)
        elif display_Cap == '1' and folder_setup == '2':
            folder3_path=Path(input('\n\nEnter the directory path: '))
            file3_name=input('\n\nName your file. Extension not needed: ')
            fi3_name=file3_name+'.txt'
            file3_path=os.path.join(folder3_path, fi3_name)
            fi3=open(file3_path,'w')
            for x3 in sorted(d3, key=d3.get):
                k2=x3
                fr2=d3[x3]
                row3=k2+' '+str(fr2)+'\n'
                fi3.write(row3)
            fi3.close()
            print('\n\nFrequency list named',file3_name,'written to a file. Check your directory:', folder3_path)
        else:
            print('\nOk')

    u=input('If you want to return to options, type "1": ')
    while True:
        if u == '1':
            menu()
            break
        else:
            break

    

    main_question=input('Select your task: \n\n1.List word frequency \n\n2.List error frequency \n\n3.List proper nouns frequency \n\n4.List punctuation frequency \n\nSelection: ')

    while True:
        if main_question == '1':
            word_freq()
            break
        elif main_question == '2':
            error_freq()
            break
        elif main_question == '3':
            cap_freq()
            break
        elif main_question == '4':
            punc_freq()
            break
        else:
            print('\n\nIncorrect option. Try again')
            break
        



    while True:
        choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2.Type '2' to return to options \n\n3.Type '3' to exit \n\n Selection: ")

        if choice == '1':
            frequency_list()
        elif choice == '2':
            menu()
        elif choice == '3':
            print("\n\nProgram Terminates")
            break
        else:
            print('\n\nIncorrect option. Try again')
            
   
automatic()
