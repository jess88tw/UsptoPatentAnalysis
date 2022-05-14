import re
import os
import shutil

def is_folder_exist(file_path):
    regex = r"\/[A-Z,a-z,0-9]+$"
    match = re.findall(regex, str(file_path))

    if match != []:
        if os.path.isdir(str(file_path) + '/uspto_data'):
            print('Delete original files...')
            shutil.rmtree(''+ str(file_path) + '/uspto_data')
            print('Loading new files...')
            os.makedirs(str(file_path) + '/uspto_data')
            os.makedirs(str(file_path) + '/uspto_data/WebHtml')
        else:
            print('Loading new files...')
            os.makedirs(str(file_path) + '/uspto_data')
            os.makedirs(str(file_path) + '/uspto_data/WebHtml')
    else:
        print('Please input the right filepath:\n' + 'Ex: /Users/jess88tw/MyPython/data')