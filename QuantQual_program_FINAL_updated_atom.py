from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import sys
from pathlib import Path



def main():
    u=input('If you want to return to options, type "1": ')
    while True:
        if u == '1':
            menu()
            break
        else:
            break



    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 4: CONCATENATE WORDS. Please, insert your file path: "))
            with open(file_to_open,'r', encoding="utf-8") as f:
                words = wordpunct_tokenize(f.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

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
    user2=input('\n\n1.Create a folder for the file \n\n2.Select a directory for your files \n\n3.Go to menu \n\nSelection: ')


    if user2 =='1':
        folder_path=Path(input('Enter your folder path and add the name of the new folder: '))
        text_name=input("\n\nName your file. Extension not needed: ")

        try:
            os.makedirs(folder_path)
        except FileExistsError:
            print('This folder already exists. Try another name')

        file_name = text_name+'.txt'
        file = os.path.join(folder_path, file_name)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(final_text)
        print('\n\nText named',file_name +'was written to a file. Check your directory', folder_path)

    elif user2 =='2':

        folder_path=Path(input('Enter your chosen directory path: '))
        text_name=input("\n\nName your file. Extension not needed: ")
        file_name=text_name+'.txt'
        folder=os.path.join(folder_path, file_name)
        with open(folder,'w',encoding='utf-8') as text:
            text.write(final_text)
        print('\n\nText named', file_name +'was written to a file. Check your directory')
    else:
        print('\nOk')



    while True:
        choice = input('\n\n1.Run this program again \n\n2.Return to options \n\n3.Exit \n\nSelection: ')

        if choice == '1':
            main()
            break
        elif choice == '2':
            menu()
            break
        elif choice == '3':
            print("\n\nProgram Terminates")
            break
        else:
            print('\n\nIncorrect option. Try again')


def frequency_list():

    def punc_freq():

        while True:
            try:
                punc_file_to_open =Path(input("\nYOU SELECTED OPTION 5: FREQUENCY LISTS. Please, insert your file path: "))
                punc_dic_to_open=Path(input('\nPlease, enter the path of your punctuation dictionary: '))
                with open(punc_file_to_open,'r', encoding="utf-8") as f:
                    freq = wordpunct_tokenize(f.read())
                with open (punc_dic_to_open,'r', encoding="utf-8") as fr:
                    dic = wordpunct_tokenize(fr.read())
                    break
            except FileNotFoundError:
                print("\nFile not found. Better try again")
            except IsADirectoryError:
                print("\nIncorrect Directory path.Try again")
        punc=[]
        words=[]
        d1=defaultdict(int)

        for p in freq:
            if p not in dic:
                words.append(p)
            elif p in dic:
                punc.append(p)

        user=input('\n\n1.Create a folder for the file \n\n2.Select a directory for your files \n\n3.Go to menu \n\nSelection: ')

        for i in punc:
            d1[i]+=1
        if user == '1':
            punc_folder_path=Path(input('\n\nEnter the folder path and add the name of the new folder: '))

            punc_file_name=input('\n\nName your file. Extension not needed: ')
            f_name=punc_file_name+'.txt'
            try:
                os.makedirs(punc_folder_path)
            except FileExistsError:
                print('This folder already exists. Try another name.')
            punc_file=os.path.join(punc_folder_path,f_name)
            punc_fi=open(punc_file,'w',encoding='utf-8')
            for p1 in sorted(d1, key=d1.get):
                print(p1,d1[p1])
                k=p1
                fr=d1[p1]
                row=k+' '+str(fr)+'\n'
                punc_fi.write(row)
            punc_fi.close()
            print('\n\nFrequency list named',f_name,'written to a file. Check your directory', punc_folder_path)
        elif user =='2':
            punc_folder1_path=Path(input('\n\nEnter yor chosen directory: '))
            punc_file1_name=input('\n\nName your file. Extension not needed: ')
            f1_name=punc_file1_name+'.txt'
            punc_file1_path=os.path.join(punc_folder1_path, f1_name)
            punc_fi1=open(punc_file1_path,'w', encoding='utf-8')
            for p2 in sorted(d1, key=d1.get):
                #print(p2,d1[p2])
                k1=p2
                fr1=d1[p2]
                punc_row1=k1+' '+str(fr1)+'\n'
                punc_fi1.write(punc_row1)
            punc_fi1.close()
            print('\n\nFrequency list named',f1_name,'written to a file. Check your directory', punc_folder1_path)
        else:
            print('\nOk')



    def word_freq():

        while True:
            try:
                file_to_open =Path(input("\nPlease, insert your file path: "))
                with open(file_to_open,'r', encoding="utf-8") as f:
                    freq = wordpunct_tokenize(f.read())
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

        d=defaultdict(int)
        d2=defaultdict(int)
        d3=defaultdict(int)

        for w in freq:
            d[w]+=1
            if w in reg:
                continue
            elif w in c_n:
                continue


        user=input('\n\n1.Create a folder for the file \n\n2.Select a directory for your files \n\n3.Go to menu \n\nSelection: ')

        if user == '1':
            folder_path=Path(input('\n\nEnter your folder path and add the name of your new folder: '))

            file_name=input('\n\nName your file. Extension not needed: ')

            try:
                os.makedirs(folder_path)
            except FileExistsError:
                print('This folder already existis. Try another name.')

            f_name=file_name+'.txt'
            file=os.path.join(folder_path,f_name)
            fi=open(file,'w', encoding='utf-8')
            for w1 in sorted(d, key=d.get):
                k=w1
                fr=d[w1]
                row=k+' '+str(fr)+'\n'
                fi.write(row)
            fi.close()
            print('\n\nFrequency list named',f_name,'written to a file. Check your directory named', folder_path)
        elif user == '2':
            folder1_path=Path(input('\n\nEnter your chosen directory: '))
            file1_name=input('\n\nName your file. Extension not needed: ')
            f1_name=file1_name +'.txt'
            file1_path=os.path.join(folder1_path, f1_name)
            fi1=open(file1_path,'w', encoding='utf-8')
            for w2 in sorted(d, key=d.get):
                k1=w2
                fr1=d[w2]
                row1=k1+' '+str(fr1)+'\n'
                fi1.write(row1)
            fi1.close()
            print('\n\nFrequency list named',f1_name,'written to a file. Check your directory', folder1_path)
        else:
            print('Ok')

    def error_freq():
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
        errors=[ ]
        d=defaultdict(int)
        d2=defaultdict(int)
        d3=defaultdict(int)

        for w in freq:
            d[w]+=1
            if w in reg:
                continue
            elif w in c_n:
                Cap_nouns.append(w)
            elif w not in dic:
                errors.append(w)

        display_errors=input('\n\nWrite the list of items not found in Dict to a file?" |\n1.Yes \n2.No: ')
        folder_setup=input('\n\n1.Create a folder for the file \n\n2.Select a directory for your files \n\n3.Go to menu \n\nSelection: ')

        for x1 in errors:
            d2[x1]+=1

        if display_errors == '1' and folder_setup == '1':
            folder2_path=Path(input('\n\nEnter your folder path and add the name of your new folder: '))

            file2_name=input('\n\nName your file. Extension not needed: ')
            try:
                os.makedirs(folder2_path)
            except FileExistsError:
                print('This folder already exists. Try another name.')
            f2_name=file2_name+'.txt'

            file2=os.path.join(folder2_path,f2_name)
            fi2=open(file2,'w', encoding='utf-8')
            for x2 in sorted(d2, key=d2.get):
                we=x2
                fre=str(d2[x2])
                row2= we+' '+str(fre)+'\n'
                fi2.write(row2)
            fi2.close()
            print("\n\nFrequency list named",f2_name, 'written to a file.Check your directory', folder2_path)
        elif display_errors == '1' and folder_setup == '2':
            folder3_path=Path(input('\n\nEnter the directory path: '))
            file3_name=input('\n\nName your file. Extension not needed: ')
            f3_name=file3_name+'.txt'
            file3_path=os.path.join(folder3_path, f3_name)
            fi3=open(file3_path,'w', encoding='utf-8')
            for x3 in sorted(d2, key=d2.get):
                k2=x3
                fr2=d2[x3]
                row3=k2+' '+str(fr2)+'\n'
                fi3.write(row3)
            fi3.close()
            print('\n\nFrequency list named',file3_name,'written to a file. Check your directory:', folder3_path)
        else:
            print('\nOk')

    def cap_freq():
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
            fi2=open(file2,'w', encoding='utf-8')
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
            fi3=open(file3_path,'w', encoding='utf-8')
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


def separate_chapters ():
    u=input('If you want to return to options, type "1": ')
    while True:
        if u == '1':
            menu()
            break
        else:
            break

    print('\n\nREMINDER: TO RUN THIS PROGRAM YOUR BOOK CHAPTERS MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@CHAPST@] AND [@CHAPFN@]')

    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 3: SEPARATE CHAPTERS. Please, insert your file path: "))
            break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    pat = re.compile(r'(?<=\[@CHAPST@\]).+?(?=\[@CHAPFN@\])', flags=re.DOTALL)
    my_chapters=[]


    with open(file_to_open, 'r', encoding="utf-8") as file:
        for i in pat.findall(file.read()):
            my_chapters.append(i)

    print('\n\nThis book contains',len(my_chapters), 'chapters')



    folder_path=Path(input('\n\nEnter your folder path and add the name of your new folder: '))
    try:
        os.makedirs(folder_path)
    except FileExistsError:
        print('This Folder already Exists. Try another name.')

    for j in range(len(my_chapters)):
        chap='Chapter'+str(j+1) +'.txt'
        file = os.path.join(folder_path, chap)

        with open(file, "w", encoding='utf-8') as f:
            for item in my_chapters[j]:
                f.write("%s" % str(item))
            print('\n\n', chap)

    print('\n\nChapters 1 -',len(my_chapters), 'written to a file separately. Check your directory',folder_path)




    while True:

        choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2.Type '2' to return to options \n\n3.Type '3' to exit \n\n Selection: ")

        if choice == '1':
            separate_chapters()

        elif choice == '2':
            menu()

        elif choice == '3':
            break
            print("\n\nProgram Terminates")

        else:
            print('\n\nIncorrect option. Try again')



def separate_paratext ():

    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break

    print('\n\nREMINDER: TO RUN THIS PROGRAM YOUR PARATEXTUAL INFORMATION MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@PARAST@] AND [@PARAFN@]')

    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 2: SEPARATE PARATEXT. Please, insert your file path: "))
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


    folder_path=Path(input('\n\nEnter your folder path and add the name of your new folder: '))

    try:
        os.makedirs(folder_path)
    except FileExistsError:
        print('This folder already exists. Try another name.')

    for j in range(len(my_paratext)):
        para='Paratext'+str(j+1) +'.txt'
        file = os.path.join(folder_path, para)

        with open(file, "w+", encoding='utf-8') as f:
            for item in my_paratext[j]:
                f.write("%s" % str(item))
            print('\n\n', para)

    print("\n\nParatexts written to a file separately. Check in your directory", folder_path)

    while True:

        choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2. Type '2' to return to options \n\n3.Type '3' to exit \n\n Selection: ")

        if choice == '1':
            separate_paratext()

        elif choice == '2':
            menu()
        elif choice == '3':
            print("\n\nProgram Terminates")
            break
        else:
            print('\n\nIncorrect option. Try again')



def remove_paratext():

    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break

    print('\n\nREMINDER: TO RUN THIS PROGRAM YOUR PARATEXTUAL INFORMATION MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@PARAST@] AND [@PARAPFN@]')

    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 3: REMOVE PARATEXT. Please, insert your file path: "))

            with open(file_to_open,'r', encoding="utf-8") as t:
                text=t.read()
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")


    pat=re.compile(r'(\[@PARAST@\]).+?(\[@PARAFN@\])', flags=re.DOTALL)


    s = re.sub(pat, '', text)

    user=input('\n\n1.Create a folder for the file \n\n2.Select a directory for your files \n\n3.Go to menu \n\n.Selection: ')


    if user == '1':
        folder_path=Path(input('\n\nEnter your folder path: '))

        file_name=input('\n\nName your file. Extension not needed: ')
        fil_name=file_name+'.txt'
        try:
            os.makedirs(folder_path)
        except FileExistsError:
            print("This folder already exists. Try another name.")
        file=os.path.join(folder_path,fil_name)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(s)
        print('\n\nText named', fil_name, 'written to a file. Check folder named',folder_path, 'in your directory')
    elif user == '2':
        folder_path=Path(input('\n\nEnter your chosen directory: '))
        file_name=input('\n\nName your file. Extension not needed: ')
        f_name=file_name+'.txt'
        file_path=os.path.join(folder_path, f_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(s)
        print('\n\nText named', f_name, 'written to a file. Check folder: ', folder_path)
    else:
        print('Ok')




    while True:

        choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2.Type '2' to return to options \n\n3.Type '3' to exit \n\nSelection: ")

        if choice == '1':
            remove_paratext()
        elif choice == '2':
            menu()
        elif choice == '3':
            print("\n\nProgram Terminates")
            break
        else:
            print('\n\nIncorrect option. Try again')


def sent():
    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break

    a=Path(input("\nYOU SELECTED OPTION 6: SPLIT TEXT INTO SENTENCES. Please, enter your file path: "))

    with open(a, 'r', encoding='utf-8') as f:
        word=sent_tokenize(f.read())

    user=input('\n\nCreate a folder?|\1.Yes \n2.No: ')
    if user == '1':
        folder_path=Path(input('Enter your folder path and add the name of your new folder: '))

        text_name=input("\n\nName your file. Extension not needed: ")

        try:
            os.makedirs(folder_path)
        except FileExistsError:
            print("This folder already exists. Try another name.")
        file_name = text_name +'.txt'
        file = os.path.join(folder_path, file_name)
        with open(file, 'w', encoding='utf-8') as t:
            for i in word:
                a='\n\n'+i
                t.write(a)
        t.close()
    else:
        folder_path=Path(input('Enter your folder path: '))
        text_name=input("\n\nName your file. Extension not needed: ")
        t_name=text_name+'.txt'
        folder=os.path.join(folder_path, t_name)
        with open(folder, 'w', encoding='utf-8') as tx:
            for j in word:
                b='\n\n'+j
                tx.write(b)
        tx.close()



    print('\n\nThis text contains',len(word), 'sentences')

    while True:

            choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2. Type '2' to return to options \n\n3.Type '3' to exit \n\n Selection: ")

            if choice == '1':
                sent()
            elif choice == '2':
                menu()
            elif choice == '3':
                print("\n\nProgram Terminates")
                break
            else:
                print('\n\nIncorrect option. Try again')

def enter_tag():

    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break

    print('\n\nREMINDER: YOUR TEXT MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@"anystringhere"@]. The program is case sensitive.')

    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 7: ENTER TAG. Please, insert your file path: "))
            break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")




    tag1=input('\n\nPlease, enter the string between the @ symbols of your first tag: ')
    tag2=input('\n\nPlease, enter the string between the @ symbols of your second tag: ')
    tagged_items=[]

    pat = re.compile(r'(?<=\[@'+tag1+'@\]).+?(?=\[@'+tag2+'@\])', flags=re.DOTALL)
    #pat = re.compile(r'(?<=\%'+tag1+'\%).+?(?=\%'+tag2+'\%)', flags=re.DOTALL)


    with open(file_to_open, 'r', encoding="utf-8") as file:
        for i in pat.findall(file.read()):

            tagged_items.append(i)

    print('\n\nThis file contains',len(tagged_items), 'tagged items')

    q=input('\n\n1.Create a folder for your files \n\n2.Select a directory for your files \n\n3.Go to main menu \n\nSelection: ')

    if q == '1':
        folder_path=Path(input('\n\nEnter your folder path and add the name of your new folder: '))

        try:
            os.makedirs(folder)
        except FileExistsError:
            print('This folder already exists. Try another name.')
        for j in range(len(tagged_items)):
            chap='Item'+ str(j+1) +'.txt'
            file = os.path.join(folder_path, chap)
            with open(file, "w", encoding='utf-8') as f:
                for item in tagged_items[j]:
                    f.write("%s" % str(item))
        print('\n\nTagged items 1 -',len(tagged_items), 'written to a file separately. Check your folder directory',folder_path)
    elif q =='2':
        folder1_path=Path(input('\n\nEnter your chosen directory: '))
        for x in range(len(tagged_items)):
            chap1='Item'+'0'+ str(x+1) +'.txt'
            fi = os.path.join(folder1_path, chap1)
            with open(fi, "w", encoding='utf-8') as f:
                for item in tagged_items[x]:
                    f.write("%s" % str(item))
        print('\n\nTagged items 1 -',len(tagged_items), 'written to a file separately. Check your directory',folder1_path)
    else:
        print('Ok')


    while True:
        choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2. Type '2' to return to options \n\n3.Type '3' to exit \n\n Selection: ")

        if choice == '1':
            enter_tag()
        elif choice == '2':
            menu()
        elif choice == '3':
            print("\n\nProgram Terminates")
            break
        else:
            print('\n\nIncorrect option. Try again')

def sent_lgth():

    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break

    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 8: CALCULATE SENTENCE LENGTH. Please, insert your file path: "))
            with open(file_to_open,'r', encoding="utf-8") as f:
                words = sent_tokenize(f.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")
    print('\n\n This file contains',len(words),'sentences in total')

    sent_number=1

    wordcounts = []
    with open(file_to_open) as f:
        text = f.read()
        sentences = sent_tokenize(text)
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

    sent_number=1



    u=input('\n\nPrint number of tokens per sentence or save to a file? \n\n1.Print \n\n2.Create a folder to your file \n\n3.Choose a directory to your file \n\n4.Press any key to continue \n\nSelection: ')
    if u == '1':
        for t in words:
            a=word_tokenize(t)
            print('\n\nSentence',sent_number,'contains',len(a), 'tokens')
            sent_number +=1
    elif u == '2':
        folder_path=Path(input('\n\nEnter the directory of your new folder: '))

        try:
            os.makedirs(folder_path)
        except FileExistsError:
            print('This folder already exists. Try again.')
        text_name=input("\n\nName your file. Extension not needed: ")
        file_name = text_name +'.txt'
        file = os.path.join(folder_path, file_name)
        with open(file, 'w', encoding='utf-8') as t1:
            for y in words:
                x=word_tokenize(y)
                pr='\nSentence '+str(sent_number)+' contains '+str(len(x))
                sent_number +=1
                t1.write(pr)
            t1.close()
    elif u == '3':
        folder_path=Path(input('Enter your folder path: '))
        text_name=input("\n\nName your file. Extension not needed: ")
        file_name=text_name +'.txt'
        folder=os.path.join(folder_path, file_name)
        with open(folder, 'w', encoding='utf-8') as tx:
            for s in words:
                j=word_tokenize(s)
                pr2='\nSentence '+str(sent_number)+' contains '+str(len(j))
                sent_number +=1
                tx.write(pr2)
            tx.close()
    else:
        print('\n\nNo file saved')

    while True:
        choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2. Type '2' to return to options \n\n Selection: ")

        if choice == '1':
            sent_lgth()
        elif choice == '2':
            menu()
            break
        else:
            print('\n\nIncorrect option. Try again')

def percent():

    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break

    while True:
        try:
            punc_file_to_open =Path(input("\nYOU SELECTED OPTION 9: CALCULATE ERROR PERCENTAGE. Please, insert your file path: "))
            punc_dic_to_open=Path(input('\nPlease, insert your dictionary path: '))
            with open(punc_file_to_open,'r', encoding="utf-8") as f:
                freq = wordpunct_tokenize(f.read())
            with open (punc_dic_to_open,'r', encoding="utf-8") as fr:
                dic = wordpunct_tokenize(fr.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    punc=open('/Users/nataliaresende/Dropbox/PYTHON/Dictionaries/Punctuation.txt', 'r',encoding='utf-8')
    punc_dic=punc.read()
    patt=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b|\d+")
    c_n= list(filter(patt.match, freq))


    errors=[]
    text=[]
    Cap_nouns=[]
    named_entities=[]

    for i in freq:
        if i in dic:
            text.append(i)
        elif i in punc_dic:
            text.append(i)
        elif i in c_n:
            Cap_nouns.append(i)
        else:
            errors.append(i)

    for j in Cap_nouns:
        if j not in dic:
            named_entities.append(j)




    print('\n\nYourfile contains a total of', len(text), 'tokens')
    print('\n\nYour file contains a total of',len(errors), 'tokens not found in dictionary')
    print('\n\nYour file contains a total of', len(Cap_nouns), 'capitalised words')
    print('\n\nYour file contains a total of', len(named_entities), 'proper nouns')

    print('\n\nThe error percentage of this file is: ', 100*float(len(errors))/float(len(text)))
    print('\n\nThe percentage of capitalised words is: ', 100*float(len(Cap_nouns))/float(len(text)))
    print('\n\nThe percentage of named entities is: ', 100*float(len(named_entities))/float(len(text)))

    user=input('\n\n1. Print the list of errors\n\n2. Type "2" Print the list of capitalised nouns \n\n3. Print list of errors, capitalised nouns and named entities \n\n4. Go to main menu \n\n5. run this program again \n\nSelection: ')

    if user =='1':
        print(errors)
    elif user == '2':
        print(Cap_nouns)
    elif user =='3':
        print('\n\n',errors)
        print('\n\n',Cap_nouns)
        print('\n\n',named_entities)
    else:
        print('Incorrect option. Try again')

    us=input('Save lists to a file?|Y/N: ')



    while True:
        us=input('Run this program again?|Y/N: ')

        if us == 'Y':
            percent()
        else:
            menu()


def merge_texts():

    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break

    while True:
        try:
            files_directory=Path(input("\nYOU SELECTED OPTION 10: MERGE FILES. Please, insert the directory path of the files: "))
            break
        except IsADirectoryError:
            print("\nIncorrect directory path.Try again")


    result = []

    Number_Chap=input('How many files do you want to merge? ')

    for chapter in range(int(Number_Chap)):
        file = os.path.join(files_directory, 'chapter{}.txt'.format(chapter+1))
        with open(file, 'r', encoding="utf-8") as f:
            result.append(f.read())

    J=' '.join(result)


    user=input('\n\n1.Create a folder for your files \n\n2.Choose a directory \n\n3.Selection: ')

    if user == '1':
        folder_directory=Path(input('Please, enter your folder path and add the new of the new folder: '))

        try:
            os.makedirs(folder_directory)
        except FileExistsError:
            print('This folder already exists. Try another name.')
        file_name=input('Name your file. Extension not needed: ')
        file_name1=file_name+'.txt'
        file=os.path.join(folder_directory,file_name1)
        with open(file,'w', encoding='utf-8') as fi:
            fi.write(J)
        fi.close()
    elif user == '2':
        directory_to_save=Path(input('Please, enter the directory to save the merged files: '))
        file_name=input('Name your file. Extension not needed: ')
        file_merged=os.path.join(directory_to_save, file_name)
        out_file=open(file_merged + '.txt','w', encoding='utf-8')
        out_file.write(J)
        out_file.close()
    else:
        print('No file saved')


    while True:
        us=input('Run this program again?|Y/N: ')

        if us == 'Y':
            merge_texts()
        else:
            menu()



def automatic ():

    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break



    book_name=input('\nYOU SELECTED OPTION 11: AUTOMATIC PROCESSING. Please, enter your book title: ')

    while True:
        try:
            language_dic_path=Path(input('Enter the path of your language dictionary: '))
            punctuation_dic_path=Path(input('Enter the path of your punctuation dictionary: '))
            with open (language_dic_path, 'r', encoding='utf-8') as ldp:
                language_dic=wordpunct_tokenize(ldp.read())
            with open (punctuation_dic_path, 'r', encoding='utf-8') as pdp:
                punctuation_dic=wordpunct_tokenize(pdp.read())
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    #separate paratext
    print('\n\nSEPARATING PARATEXT')

    print('\n\nREMINDER: TO RUN THIS PROGRAM YOUR PARATEXTUAL INFORMATION MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@PARAST@] AND [@PARAFN@]')


    pat = re.compile(r'(?<=\[@PARAST@\]).+?(?=\[@PARAFN@\])', flags=re.DOTALL)
    my_paratext=[]

    while True:
        try:
            file_to_open =Path(input("\nPlease, enter your file path: "))
            break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    with open(file_to_open, 'r', encoding="utf-8") as file:
                for i in pat.findall(file.read()):
                    my_paratext.append(i)




    print('Your book has',len(my_paratext), 'paratext instances')


    while True:
        try:
            path=Path(input('\nPlease, enter your folder path: '))
            break
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")



    paratext_folder='PARATEXT'

    book_path=os.path.join(path,book_name)
    folder_path=os.path.join(book_path,paratext_folder)


    os.makedirs(folder_path)



    for j in range(len(my_paratext)):
        para='Paratext'+str(j+1) +'.txt'
        file = os.path.join(folder_path, para)

        with open(file, "w+", encoding='utf-8') as f:
            for item in my_paratext[j]:
                f.write("%s" % str(item))
            #print('\n\n', para)

    print("\n\nParatexts written to a file separately. Check in your directory", folder_path)

    #remove paratext

    print('\n\nREMOVING PARATEXTUAL INFORMATION \n\nREMINDER: TO RUN THIS PROGRAM YOUR PARATEXTUAL INFORMATION MUST BE TAGGED USING THE FOLLOWING TAG FORMAT: [@PARAST@] AND [@PARAPFN@]')

    with open(file_to_open, 'r', encoding="utf-8") as file:
        a=file.read()


    pat=re.compile(r'(\[@PARAST@\]).+?(\[@PARAFN@\])', flags=re.DOTALL)


    s = re.sub(pat, '', a)

    remove_file_name='NO_PARATEXT'


    folder1_path=os.path.join(book_path, remove_file_name)




    os.makedirs(folder1_path)


    file1_name=book_name
    fil1_name=file1_name + '.txt'
    new_file=os.path.join(folder1_path, fil1_name)


    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(s)
        print('\n\nText named', fil1_name, 'written to a file. Check folder named',folder1_path, 'in your directory')


    #separate chapters


    print('\n\nSEPARATING CHAPTERS')


    pat = re.compile(r'(?<=\[@CHAPST@\]).+?(?=\[@CHAPFN@\])', flags=re.DOTALL)
    my_chapters=[]


    with open(new_file, 'r', encoding="utf-8") as fil:
        for i in pat.findall(fil.read()):
            my_chapters.append(i)

    print('\n\nThis book contains',len(my_chapters), 'chapters')

    separate_chapters_name='CHAPTERS'

    folder2_path=os.path.join(book_path, separate_chapters_name)

    try:
        os.makedirs(folder2_path)
    except FileExistsError:
        print('This Folder already Exists. Try another name.')

    for j in range(len(my_chapters)):
        chap='Chapter'+str(j+1) +'.txt'
        file = os.path.join(folder2_path, chap)

        with open(file, "w", encoding='utf-8') as c:
            for item in my_chapters[j]:
                c.write("%s" % str(item))
            #print('\n\n', chap)

    print('\n\nChapters 1 -',len(my_chapters), 'written to a file separately. Check your directory',folder2_path)

    #Merge files

    print('\n\nMERGING CHAPTERS')

    files_directory=folder2_path

    Number_Chap=len(my_chapters)



    result = []



    for chapter in range(int(Number_Chap)):
        file = os.path.join(files_directory, 'chapter{}.txt'.format(chapter+1))
        with open(file, 'r', encoding="utf-8") as f:
            result.append(f.read())

    J=' '.join(result)

    merge_folder='MERGED'



    folder_directory=os.path.join(folder1_path, merge_folder)

    try:
        os.makedirs(folder_directory)
    except FileExistsError:
        print('This folder already exists. Try another name.')
    file_name=book_name
    file_name1=file_name+'.txt'
    file_p=os.path.join(folder_directory,file_name1)
    with open(file_p,'w', encoding='utf-8') as fi:
        fi.write(J)
    fi.close()
    print('Chapters merged into a file named',file_name1, 'check directory', file_p)



    #concatenate words

    print('\n\nCONCATENATING WORDS')

    with open(file_p,'r', encoding='utf=8') as conc:
        words = wordpunct_tokenize(conc.read())

    dic=language_dic


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


    for x in l:
        if x=='~':
            l.remove(x)
        elif x=='$':
            l.remove(x)
        else:
            continue




    CONCATENATED_FOLDER='CONCATENATED_WORDS'
    folder3_path=os.path.join(folder1_path, CONCATENATED_FOLDER)
    text3_name=book_name


    try:
        os.makedirs(folder3_path)
    except FileExistsError:
        print('This folder already exists. Try another name')

    file_name3 = text3_name+'.txt'
    file3 = os.path.join(folder3_path, file_name3)

    with open(file3, 'w', encoding='utf-8') as f3:
        f3.write(text)

    print('\n\nText named',file_name3, 'was written to a file. Check your directory', folder3_path)

    #frequency lists -punctuation

    print('\n\nCREATING PUNCTUATION FREQUENCY LIST')

    with open(file3,'r', encoding='utf-8') as p:
        pu=p.read()

    dic_p=punctuation_dic


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

    punct_list_folder='FREQUENCY_LISTS'

    punc_folder_path=os.path.join(book_path, punct_list_folder)

    f_name='PUNCTUATION_FREQUENCY_LIST.txt'
    try:
        os.makedirs(punc_folder_path)
    except FileExistsError:
        print('This folder already exists. Try another name.')
    punc_file=os.path.join(punc_folder_path,f_name)
    punc_fi=open(punc_file,'w', encoding='utf-8')
    for p1 in sorted(d1, key=d1.get):
        kr=p1
        r=d1[p1]
        row=kr+' '+str(r)+'\n'
        punc_fi.write(row)
    punc_fi.close()
    print('\n\nFrequency list named',f_name,'written to a file. Check your directory', punc_folder_path)

    #Word Frequency list

    print('\n\nCREATING WORD FREQUENCY LIST')

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






    enter_name='WORD_FREQUENCY_LIST'


    final_name=enter_name+'.txt'
    file_final=os.path.join(punc_folder_path,enter_name)
    fiw=open(file_final,'w', encoding='utf-8')
    for w1 in sorted(df, key=df.get):
        kw=w1
        fw=df[w1]
        roww=kw+' '+str(fw)+'\n'
        fiw.write(roww)
    fiw.close()
    print('\n\nFrequency list named',final_name,'written to a file. Check your directory named', file_final)

    #Error list

    print('\n\nCREATING ERROR FREQUENCY LIST')

    with open(file3,'r', encoding='utf-8') as er:
        e_f=wordpunct_tokenize(er.read())

    dicc=language_dic




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




    file2_name_errors='ERROR_FREQUENCY_LIST'


    f2_name_errors=file2_name_errors+'.txt'
    file2_errors=os.path.join(punc_folder_path,f2_name_errors)

    fi2_errors=open(file2_errors,'w', encoding='utf-8')
    for x2 in sorted(d2, key=d2.get):
        we=x2
        wre=str(d2[x2])
        row2= we+' '+str(wre)+'\n'
        fi2_errors.write(row2)
    fi2_errors.close()
    print("\n\nFrequency list named",f2_name_errors, 'written to a file.Check your directory', file2_errors)

    #Split text into sentences -

    print('\n\nSPLITING TEXT INTO SENTENCES')

    with open(file3,'r', encoding='utf-8') as s:
       sent=sent_tokenize(s.read())



    s_name=book_name

    sentence_split_folder='SENTENCE_SPLIT'

    sentence_split_path=os.path.join(folder3_path,sentence_split_folder)

    try:
        os.makedirs(sentence_split_path)
    except FileExistsError:
        print('This folder already exists. Try another name.')




    s_file_name = s_name +'.txt'
    s_file = os.path.join(sentence_split_path,s_file_name)
    with open(s_file, 'w', encoding='utf-8') as ts:
        for i in sent:
            a='\n\n'+i
            ts.write(a)
        ts.close()
        print('\n\nText named', s_name, 'split into sentences written to a file. Check your directory', s_file)

    #Calculate sentence length

    print('\n\nCALCULATING SENTENCE LENGTH')

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

    sentence_split='SENTENCE_LENGTH'


    folder_s_path=os.path.join(folder3_path, sentence_split)

    try:
        os.makedirs(folder_s_path)
    except FileExistsError:
        print('This folder already exists. Try again.')
    stext_name='SENTENCE_LENGTH'
    sfile_name = stext_name +'.txt'
    sfile = os.path.join(folder_s_path, sfile_name)
    with open(sfile, 'w', encoding='utf-8') as t1:
        for y in words_s:
            x=word_tokenize(y)
            pr='\nSentence '+str(sent_number)+' contains '+str(len(x))+ ' tokens'
            sent_number +=1
            t1.write(pr)
        t1.close()
        print('\n\nFile named',sfile_name,'written to a file.Check your directory',folder_s_path)



    #Calculate error percentage


    with open(file3,'r',encoding='utf-8') as e_p:
        freq = wordpunct_tokenize(e_p.read())


    pat_ep=re.compile(r"^[A-Z][a-z]+\b|^[A-Z]+\b")
    c_n_ep= list(filter(pat_ep.match, freq))

    errors_ep=[]
    text_ep=[]
    Cap_nouns_ep=[]
    named_entities_ep=[]

    for i in freq:
        if i in language_dic:
            text_ep.append(i)
        elif i in punctuation_dic:
            text_ep.append(i)
        elif i in c_n_ep:
            Cap_nouns_ep.append(i)
        else:
            errors_ep.append(i)

    for j in Cap_nouns_ep:
        if j not in language_dic:
            named_entities_ep.append(j)



    print('\n\nYourfile contains a total of', len(text_ep), 'tokens')
    print('\n\nYour file contains a total of',len(errors_ep), 'tokens not found in dictionary')
    print('\n\nYour file contains a total of', len(Cap_nouns_ep), 'capitalised words')
    print('\n\nYour file contains a total of', len(named_entities_ep), 'proper nouns')

    print('\n\nThe error percentage of this file is: ', 100*float(len(errors_ep))/float(len(text_ep)))
    print('\n\nThe percentage of capitalised words is: ', 100*float(len(Cap_nouns_ep))/float(len(text_ep)))
    print('\n\nThe percentage of named entities is: ', 100*float(len(named_entities_ep))/float(len(text_ep)))

    while True:
        us=input('Run this program again?|Y/N: ')

        if us == 'Y':
            percent()
        else:
            menu()

def lex_info():

    u=input('If you want to return to options, type "1": ')

    while True:
        if u == '1':
            menu()
            break
        else:
            break




    def lex_dens():

        while True:
            try:
                file_to_open =Path(input("\nYOU SELECTED OPTION 12: LEXICAL INFORMATION. Please, insert your file path: "))
                with open(file_to_open,'r', encoding="utf-8") as f:
                    words = word_tokenize(f.read())
                    break
            except FileNotFoundError:
                print("\nFile not found. Better try again")
            except IsADirectoryError:
                print("\nIncorrect Directory path.Try again")
        #print(words)
        #print('\n\n',set(words))



        print('\nThis text contains', len(words), 'tokens')

        print('\nThis text contains',len(set(words)), 'types')
        print('\nThe lexical richness (type/token ratio) of this text is: ',len(set(words))/len(words))



    def percentage():

        while True:
            try:
                file_to_open =Path(input("\nYOU SELECTED OPTION 12: LEXICAL INFORMATION. Please, insert your file path: "))
                with open(file_to_open,'r', encoding="utf-8") as f:
                    words_p = wordpunct_tokenize(f.read())
                    break
            except FileNotFoundError:
                print("\nFile not found. Better try again")
            except IsADirectoryError:
                print("\nIncorrect Directory path.Try again")

        us=input('Enter word to calculate its percentage: ')

        print('This word occurs', words_p.count(us), 'in this text')

        print('The percentage of occurrence of this word in this text is: ',100 * words_p.count(us) / len(words_p))



    u=input('Select your task:\n1.Calculate lexical richness  \n2.Calculate word percentage in a text \nSelect: ')

    if u =='1':
        lex_dens()
    elif u =='2':
        percentage()
    else:
        print('Program terminates')


    while True:
        us=input('Run this program again?|\n1.Yes \n2.No: ')
        if us == '1':
            lex_info()
        else:
            menu()

def items_search():
    while True:
        try:
            file_to_open =Path(input("\nYOU SELECTED OPTION 13: ITEMS SEARCH. Please, insert your file path: "))
            f= Path(input("\nEnter your list of items for search: "))
            with open(f,'r', encoding="utf-8") as f:
                s = wordpunct_tokenize(f.read())
            with open(file_to_open,'r', encoding="utf-8") as fi:
                wds = fi.read()
                break
        except FileNotFoundError:
            print("\nFile not found. Better try again")
        except IsADirectoryError:
            print("\nIncorrect Directory path.Try again")

    count=[]

    propn_found={y: re.subn(r"\b{}\b".format(y), "", wds)[1] for y in s if y in wds}


    for i in propn_found:
        if propn_found[i] !=0:
            count.append(propn_found[i])
            print (i, propn_found[i])


    #print('\n\n',propn_found)
    #print('\n\nList of frequency of each item', count)
    print('\n\nThere are', sum(count), 'items in this file')


    user=input("Run this program again? | \n1.Yes \n2.No \nSelection: ")


    if user =='1':
        items_search()
    else:
        menu()








def menu():

    while True:

        start=input("\n\nPlease, select your task: \n\n1.SEPARATE PARATEXT \n\n2.REMOVE PARATEXT \n\n3.SEPARATE CHAPTERS \n\n4.CONCATENATE WORDS \n\n5.FREQUENCY LISTS \n\n6.SPLIT TEXT INTO SENTENCES \n\n7.ENTER TAG \n\n8.CALCULATE SENTENCE LENGTH \n\n9.CALCULATE ERROR PERCENTAGE \n\n10.MERGE FILES \n\n11.AUTOMATIC PROCESSING \n\n12.LEXICAL INFO \n\n13.ITEMS SEARCH \n\n14.EXIT \n\nSelection: ")

        if start=='1':
            separate_paratext()
        elif start =='2':
            remove_paratext()
        elif start =='3':
            separate_chapters()
        elif start == '4':
            main()
        elif start == '5':
            frequency_list()
        elif start == '6':
            sent()
        elif start=='7':
            enter_tag()
        elif start =='8':
            sent_lgth()
        elif start == '9':
            percent()
        elif start == '10':
            merge_texts()
        elif start == '11':
            automatic()
        elif start == '12':
            lex_info()
        elif start == '13':
            items_search()
        elif start == '14':
            print('\nGOOD BYE')
            break

        else:
            print('Incorrect option. Try again')








menu()
