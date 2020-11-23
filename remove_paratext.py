import re


def extract_paratext():

    us=input('Enter book name or file name: ')

    file=open(us,'r')
    text=file.read()

    no_tags=open(us + '_no_tags'+'.txt','w')



    pat=re.compile(r'(\[@PARAST@\]).+?(\[@PARAFN@\])')

   
    s = re.sub(pat, '', text)

    no_tags.write(s)

    no_tags.close()


    

    
              

extract_paratext()
        
        

        
