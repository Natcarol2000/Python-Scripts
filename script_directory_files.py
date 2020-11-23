import os
import sys

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+ directory)

createFolder('./chapters/')
script_directory = os.path.dirname(sys.argv[0])
print(script_directory)
our_watched_folder = f'{script_directory}/chapters'
print(our_watched_folder)
print("Files in watch folder")
for file in os.listdir(our_watched_folder):
    print(file)

createFolder(directory)

