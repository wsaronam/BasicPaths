#Randy Lim 60847692 and Willy Saronamihardja 80408898. ICS 32 Lab 10 Project 1
from pathlib import Path


def input_one():
    """Takes an input and see if the path exists"""
    directory = Path(input())
    while directory.is_dir() != True:
        print('ERROR')
        directory = Path(input())
    if directory.is_dir() == True:
        print(directory)
        input_two(directory)



        
def input_two(directory:Path):
    '''Takes an input and determines which function
    to carry out according to the given input'''
    search = input()
    
    if search[0] == 'N':
        file = search[2:]
        path = Path("{}\{}".format(directory,file))
        if path.is_file():
            print(path)
            input_three(directory,file)
            
    elif search[0] == 'E':
        newsearch = search.replace('.', '')
        extension = newsearch[2:]
        for file in directory.iterdir():
            if extension in file.suffix:
                print(file)
            
    elif search[0] == 'S':
        all_files = []
        byte = int(search[2:])
        for file in directory.iterdir():
            if byte > file.stat().st_size:
                all_files.append(file)
                for filename in all_files:
                    print(filename)
                    
    else:
        print('ERROR')
        input_two(directory)



def input_three(directory: Path, file:str):
    '''Takes a user input and carries out the desired
    action according to the user input'''
    third = input()
    
    if third[0] == 'P':
        print(str(directory)+"\\"+str(file))
        
    elif third[0] == 'F':
        txt = open(file)
        print(txt.readline())
        txt.close()
##
##    elif third[0] == 'D':
##        
##
##    elif third[0] == 'T':

    else:
        print('ERROR')
        input_three(directory,file)
input_one()