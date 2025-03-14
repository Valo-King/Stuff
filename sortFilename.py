import os , shutil

def filesetFind(directory):
    if os.path.isdir(directory):
        fileset = os.listdir(directory)
        break
    elif directory == 'CWD' or directory == 'cwd' or directory == '.':
        fileset = os.listdir(os.getcwd())
        break
    else:
        print("Not a directory.")
        return
    return fileset

def fileOperations(fileset):
    dirList = ''.join(x for x.split(seperator, 1)[0] in fileset)
    dedup = list(dict.fromkeys(dirList)
    for i in dedup:
        os.makedirs(f"{os.getcwd()}/head/{i}")
        shutil.copy(x for x in fileset , f"{os.getcwd()}/head/{i}")

while True:
    seperator = input('File seperator? ')
    fileOperations(filesetFind(input('Where am I looking? ')))
