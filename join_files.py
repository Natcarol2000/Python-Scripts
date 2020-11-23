
import sys
import os
from pathlib import Path

def join_texts():

    files_list=[]

    files_directory = Path(input('Enter the path of the files: '))

    for file in os.listdir(files_directory):
        for f in file:
            with open (file) as x:
                y=x.read()
                files_list.append(y)

    print(files_list)
        
      


    



join_texts()
