#Randy Lim and Willy Saronamihardja. ICS 32 Lab 10 Project 1
from pathlib import Path
import shutil


def input_one():
    """Takes an input and see if the path exists"""
    directory = Path(input())
    if directory.is_dir() == False:
        print('ERROR')
        input_one()
    elif directory.is_dir() == True:
        print (directory)
        return directory



def input_two(directory:Path):
    '''Takes an input and determines which function
    to carry out according to the given input'''
    search = input()
    if search[0] == 'N':
        return (func_N(directory, search[2:]))
    elif search[0] == 'E':
        return (func_E(directory, search[2:]))
    elif search[0] == 'S':
        return (func_S(directory,search[2:]))
    else:
        print('ERROR')
        input_two(directory)



def func_N(directory: Path, search: str) -> 'list of directories':
    '''If user inputs N then finds all the files that are
    listed in the user input'''
    list_files= []
    path = Path(directory, search)
    for file in directory.iterdir():
        if file.is_dir():
            func_N(file, search)
    if path.is_file():
        print(path)
        list_files.append(path)
    elif list_files == []:
        print ('ERROR')
        input_two(directoryname)
        
    return list_files


        
def func_E(directory: Path, search: str):
    '''If user inputs E then finds all the files that have
    the suffix the user inputs'''
    list_files=[]
    newsearch = search.replace('.', '')
    extension = newsearch[2:]
    for file in directory.iterdir():
        if file.is_dir():
            list_files.extend(func_E(file,search))
        elif extension in file.suffix:
            print (file)
            list_files.append(file)
    if list_files == []:
        print ('ERROR')
        input_two(directoryname)
            
    return list_files



def func_S(directory: Path, search: str):
    '''If user inputs S then finds all the files that have
    bytes that are bigger than the user input'''
    list_files = []
    for file in directory.iterdir():
        if file.is_dir():
            list_files.extend(func_S(file,search))
        elif int(search) < file.stat().st_size:
            list_files.append(file)
    return list_files


    
def input_three(directorylist: 'List of Directories'):
    '''Takes a user input and carries out the desired
    action according to the user input'''
    third = input()
    print (directorylist)
    if third[0] == 'P':
        for directory in directorylist:
            print (directory)
        
    elif third[0] == 'F':
        for directory in directorylist:
            print (directory)
            with directory.open() as f:
                print (f.readline())
        
    elif third[0] == 'D':
        for directory in directorylist:
            workingdirectory = str(directory) + '.dup'
            shutil.copyfile(str(directory), workingdirectory)

        
    elif third[0] == 'T':
        for directory in directorylist:
            directory.touch()
        
    else:
        print('ERROR')
        input_three(directorylist)
        
directoryname = input_one()
finaldirectory = input_two(directoryname)
input_three(finaldirectory)

