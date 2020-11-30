import zipfile
import subprocess
import os
from tkinter import filedialog
import random

os.system('cls')
while True:
    try:
        os.mkdir('archive')
    except:
        print('')

    print('SELECT IMAGES: ')
    const = filedialog.askopenfilenames()
    for i in const:
        indfile = str(i)
        indfile = indfile.replace('/', '\\')
        subprocess.run(f'move "{indfile}" ".\\archive"', shell=True)

    listfiles = os.listdir("archive")
    if len(listfiles) != 0:
        myzip = zipfile.ZipFile('archive.rar', 'w')
        for j in listfiles:
            myzip.write(f'archive\\{j}')
        myzip.close()
    else:
        os.rmdir('archive')
        break
    askpermission = input('Do you want to set Thumbnail Manually or want automatics?: (Y) yes, want manually (N) No, want automatic\n').lower()
    if askpermission == 'y':
        for x in listfiles:
            subprocess.run(f'del archive\\"{x}"', shell=True)
        print('\nSELECT THUMNAIL YOU WANT\n')
        askfile = str(filedialog.askopenfilename())
        askfile = askfile.replace('/', '\\')
        subprocess.run(f'copy /b "{askfile}" + ".\\archive.rar" "{askfile}"', shell=True)
        print('\nSuccessfully Merged Files | Check the Thubnail Images (ext RAR for Archive and JPG or ANY IMG FORMAT for Image)')
        subprocess.run('del archive.rar', shell=True)
        subprocess.run('rmdir archive', shell=True)
    elif askpermission == 'n':
        randomNumber = random.randint(0, len(listfiles) - 1)
        subprocess.run(f'copy /b "archive\\{listfiles[randomNumber]}" + ".\\archive.rar" "archive\\{listfiles[randomNumber]}"', shell=True)
        subprocess.run('del archive.rar', shell=True)
        for l in listfiles:
            if l == listfiles[randomNumber]:
                print(' ')
            else:
                subprocess.run(f'del "archive\\{l}"', shell=True)
        subprocess.run("rmdir archive", shell=True)
        print(f'\nSuccessfully Merged Files | Check the {listfiles[randomNumber]} Within the Archive Folder(ext RAR for Archive and JPG or ANY IMG FORMAT for Image)')
    else:
        print('Error Occured: Wrong Command Line\nCheck Archive Folder for you files')
        subprocess.run('del archive.rar', shell=True)
    
    askper = input('Wanna add more? (Y) Yes (N) No: ').lower()
    if askper == 'y':
        pass
    else:
        break
