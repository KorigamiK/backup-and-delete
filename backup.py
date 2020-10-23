import os
import zipfile
import sys
import shutil

def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)
                    


def make_backup(directory, option_remove_auto='n', option_move_auto= 'n'):
    folders = list(os.walk(cur_dir))[0][1]
    print('these folders will be affected:\n ',folders)
    for i in folders:
        working_folder = os.path.join(directory,i)
        zip_file_name = 'zip'+i+'.zip'
    #______________________________________________________________       
        print('Zipping {}'.format(i))
        if not os.path.exists(os.path.join(directory, zip_file_name)):
            make_zipfile('zip'+i+'.zip' , working_folder)
            print('zip file created')
        else :
            print('zipping has already been done moving on')
    #______________________________________________________________         
        print('Removing {}'.format(i))
        try:
            if option_remove_auto == 'y':
                shutil.rmtree(working_folder)
                print('Successfully zipped and deleted {}'.format(i))
            else:
                if input('want to the folder now? y/n: ')== 'y':
                    shutil.rmtree(working_folder)
                    print('Successfully zipped and deleted {}'.format(i))
                else:
                    print('Did not remove the folder')
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
    #______________________________________________________________
        if option_move_auto == 'y':
            option2 = 'y'
            if option2=='y':
                print()
                continue
            else:
                break
        else :
            option2 = 'move to the next folder? y/n: '       
            if option2=='y':
                print()
                continue
            else:
                break
                break
            
    print('YAY your back up is done or aborted!')
    
# os.chdir('./..') to got to parent directory
cur_dir = os.getcwd()
print('Current directory is',cur_dir)
mode = input('Do you WANT to delete folders without a prompt (for automation but veryy risky)\nOnly do this if you trust this script y/n: ')
move = input('Do you WANT to move to next folder automatically (Do this if you really trust this sript) y/n: ')
if input('want to give custom directory (y) or use the directory in which script is placed (n)? y/n: ') == 'n':
    make_backup(cur_dir,mode,move)
else :
    make_backup(r'{}'.format(input('Give the directory path: ')), mode, move)
