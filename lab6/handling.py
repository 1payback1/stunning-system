import os
import string

#1
def list_directories_files(path):
    try:
        all_items = os.listdir(path)
        directories = [x for x in all_items if os.path.isdir(os.path.join(path, x))]
        files = [x for x in all_items if os.path.isfile(os.path.join(path, x))]
        print(directories + files)

    except:
        print(f'The specified path {path} does not exist')
    
#2
def access_to_path(path):
    try:
        if os.path.exists(path):
            print(f'{path} exists.')
            os.access(path, os.R_OK)
            os.access(path, os.W_OK)
            os.access(path, os.X_OK)
            print(f'{path} is readable, writable, executable.')
        else:
            print(f'{path} does not exist.')
    except:
        print(f'error accessing to {path}.')
    
#3
def test_path(path):
    try:
        if os.path.exists(path):
            print(f'{path} exists.')
            file_name = os.path.basename(path)
            directory_portion = os.path.dirname(path)
            print(f'File name: {file_name}')
            print(f'Directory portion: {directory_portion}')
        else:
            print(f'{path} does not exist')
    except:
        print('Unknown error')

#4
def count_lines(path_to_the_file):
    try:
        with open(path_to_the_file) as file:
            sum = 0
            data = file.readlines()
            for line in data:
                sum += 1
            print(f'The number of lines in file is {sum}')
    except:
        print('Unknown error')

#5
def write_list_to_file(path_to_the_file, list):
    try:
        with open(path_to_the_file, 'a') as file:
            for item in list:
                file.write(str(item) + '\n')
    except:
        print('Unknown error')

#6
def create_files():
    try:
        for letter in string.ascii_uppercase:
            file_name = f'{letter}.txt'
            f = open(file_name, 'x')
            f.close()
    except:
        print('Unknown error')
    
#7
def copy_content(source_file, destination_file):
    try:
        with open(source_file) as file:
            data = file.read()
        with open(destination_file, 'w') as file:
            file.write(data)
    except:
        print('Unknown error')

#8
def delete_file(path_to_the_file):
    try:
        if os.path.exists():
            if os.access(path_to_the_file, os.W_OK):
                os.remove(path_to_the_file)
                print(f'File {path_to_the_file} has been deleted')
            else:
                print(f'No access to {path_to_the_file}')
        else:
            print('File not found')
    except:
        print('Unknown error')