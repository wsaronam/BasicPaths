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

def recall(path_):
    if path.is_dir()


def input_two (directory: Path) -> 'File':
    '''
    Specifies search characteristics that will be used in deciding whether
    files are "interesting" and should have action taken on them.  There are
    three different search characteristics; this function chooses one of them.
    '''
    search = input()
    if search[0] == 'N':
        filename = search[2:]
        thepath = "{}\{}".format(directory, filename)
        newpath = Path(thepath)
        if newpath.is_file() == True:
            return newpath
        else:
            print ('ERROR')
            input_two(directoryname)
            
            
            

            
    elif search[0] == 'E':
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
                


                
    elif search[0] == 'S':
        byte = int(search[2:])
        for file in directory.iterdir():
            if file.stat().st_size > byte:
                return file
              


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


