import os
import shutil
import glob
import shutil

def join1():

    files_directory = input('Enter the path of the files: ')
    files = glob.glob(files_directory + '/*.txt')
    result = []
    for file in files:
        with open(file, 'r') as f:
            result.append(f.read())


    join_file=' '.join(result)

    out_file=open('joined_text.txt','w')
    out_file.write(join_file)

    out_file.close()


def join2():
    app = QtGui.QApplication(sys.argv)
    first_file = unicode(QtGui.QFileDialog.getOpenFileName()[0])
    app.quit()
    pathname = first_fname[:(first_fname.rfind('/') + 1)]
    file_list = [f for f in os.listdir(pathname) if f.lower().endswith('.txt')]
    file_list.sort() #you will need to be careful here - this will do alphabetically so you might need to change chapter1.txt to chapter01.txt etc


def join3():
    
    files = [f for f in os.listdir('/Users/nataliaresende/Dropbox/PYTHON/Le Monastere') if '.txt' in f]
    with open('output.txt', 'w') as output:
        for item in files:
            with open(item, 'r') as current:
                shutil.copyfileobj(current, output)
                output.write(b'\n')



join3()

    




    



    

        



