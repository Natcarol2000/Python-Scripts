import os
from pathlib import Path

def merge_texts():

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
        with open(file, 'r') as f:
            result.append(f.read())
            
    J=' '.join(result)


    user=input('\n\n1.Create a folder for your files \n\n2.Choose a directory \n\n3.Selection: ')

    if user == '1':
        folder_directory=Path(input('Please, enter the directory to save the merged files: '))
        folder_name=input('Please, name your folder: ')
        folder=os.path.join(folder_directory,folder_name)
        os.makedirs(folder)
        file_name=input('Name your file: ')
        file=os.path.join(folder,file_name)
        with open(file,'w') as fi:
            fi.write(J)
        fi.close()
    elif user == '2':
        directory_to_save=Path(input('Please, enter the directory to save the merged files: '))
        file_name=input('Name your file: ')
        file_merged=os.path.join(directory_to_save, file_name)
        out_file=open(file_merged + '.txt','w')
        out_file.write(J)
        out_file.close()
    else:
        print('No file saved')

merge_texts()
