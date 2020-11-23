import re
import nltk
from nltk.tokenize import word_tokenize
import re


def separate_chapters ():

    us=input('\n\nEnter the name of the book or file: ')

    pat = re.compile(r'(?<=\[@CHAPST@\]).+?(?=\[@CHAPFN@\])')
    my_chapters=[]
    

    with open(us, 'r', encoding="utf-8") as file:
        for i in pat.findall(file.read()):
            my_chapters.append(i)

    print('\n\nThis book contains',len(my_chapters), 'chapters')
    
    for j in range(len(my_chapters)):
        chap=us+'_Chapter'+str(j+1) +'.txt'
        with open(chap, "w+") as f:
            for item in my_chapters[j]:
                f.write("%s" % str(item))
            print('\n\n', chap)

    print('\n\nChapters 1 -',len(my_chapters), 'written to a file separately. Check your directory')

    join_chapters=input('\n\nJoin chapters?: ')


    

    if join_chapters =='Y':
        All_chapters_file=input('\n\nName your output file: ')
        Book=open(All_chapters_file,'w')
        for x in my_chapters:
            a=''.join(x)
            Book.write(a)
        Book.close()
        print("\n\nFile named", All_chapters_file, 'written to a file. Check your directory')
    else:
        print('Ok')


    

    choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2. Type '2' to return to options \n\n3.Type Enter to exit \n\n Selection: ")

    if choice == '1':
        separate_chapters()
    elif choice == '2':
        menu()
    else:
        print("\n\nProgram Terminates")

    
      
def separate_paratext ():

    us=input('\n\nTo separate paratext from book, enter file name: ')

    pat = re.compile(r'(?<=\[@PARAST@\]).+?(?=\[@PARAFN@\])')
    my_paratext=[]
    Book=''
    out_file=open('Waverley_no_Paratext.txt','w')


    with open(us, 'r', encoding="utf-8") as file:
        for i in pat.findall(file.read()):
            my_paratext.append(i)
                

    print('Your book has',len(my_paratext), 'paratext instances')
         

    for j in range(len(my_paratext)):
        chap=us+'_Paratext'+str(j+1) +'.txt'
        with open(chap, "w+") as f:
            for item in my_paratext[j]:
                f.write("%s" % str(item))

    print("\n\nParatexts written to a file separately. Check your directory")

    choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2. Type '2' to return to options \n\n3.Type Enter to exit \n\n Selection: ")

    if choice == '1':
        separate_paratext()
    elif choice == '2':
        menu()
    else:
        print("\n\nProgram Terminates")



def remove_paratext():

    us=input('\n\nTo remove paratext from a file, enter file name: ')

    file=open(us,'r')
    text=file.read()

    no_tags=open(us + '_no_paratext_tags'+'.txt','w')



    pat=re.compile(r'(\[@PARAST@\]).+?(\[@PARAFN@\])')

   
    s = re.sub(pat, '', text)

    no_tags.write(s)

    no_tags.close()

    print('\n\nText named', us + '_no_paratext_tags'+'.txt', 'written to a file. Check your directory')

    choice = input("\n\nDo you want to do this again, return to options or exit? | \n\n1.Type '1' to run this program again \n\n2. Type '2' to return to options \n\n3.Type Enter to exit \n\n Selection: ")

    if choice == '1':
        remove_paratext()
    elif choice == '2':
        menu()
    else:
        print("\n\nProgram Terminates")


def menu():

    start=input("Please, select your task: \n\n1.Separate Chapters \n\n2.Separate Paratext \n\n3.Remove Paratext \n\nSelection: ")


    if start=='1':
        separate_chapters()
    elif start=='2':
        separate_paratext()
    elif start =='3':
        remove_paratext()



menu()

    
   
    
 

    


    











            
