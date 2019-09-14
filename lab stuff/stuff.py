# Willy Saronamihardja 80408898, Randy Lim 60847692

from pathlib import Path


def input_one() -> Path:
    '''
    Input the path of the directory in which the search for files should be
    rooted.
    '''
    directory = Path(input())
    while directory.is_dir() != True:
        print ('ERROR')
        directory = Path(input())
    if directory.is_dir() == True:
        return directory


'''
    furnc_foo

        if is dir:
            func_foo
        else
            file
'''

def recall(path: Path):
    if path.is_dir():
        recall(path)
    else:
        return path


def function_n(path: Path, search: str):
    filename = search[2:]
    thepath = "{}\{}".format(path, filename)
    newpath = Path(thepath)
    if path.is_dir():
        function_n(path, search)
    if newpath.is_file() == True:
        return newpath
    else:
        print ('ERROR')
        input_two(directoryname)


def function_e(directory: Path, search: str):
    newsearch = search.replace('.', '')
    extension = newsearch[2:]
    count = 0
    for file in directory.iterdir():
        if extension in file.suffix:
            count += 1
            return file
            if count == 0:
                print ('ERROR')
                input_two(directoryname)


def function_s(directory: Path, search: str):
    byte = int(search[2:])
    for file in directory.iterdir():
        if file.stat().st_size > byte:
            return file


def input_two (i: Path) -> 'File':
    '''
    Specifies search characteristics that will be used in deciding whether
    files are "interesting" and should have action taken on them.  There are
    three different search characteristics; this function chooses one of them.
    '''
    search = input()
    if search[0] == 'N':
        function_n(i, search)                                                
    elif search[0] == 'E':
        function_e(i, search)                                
    elif search[0] == 'S':
        function_s(i, search)              
    else:
        print ('ERROR')
        input_two (directoryname)




def input_three (file: 'File') -> None:
    '''
    Specifies the action that should be taken on each of the interesting
    files found in the search.
    '''
    answer = input()
    

                
directoryname = input_one()
input_two (directoryname)


