import os
import stat
import shutil
import pathlib

def handleError(func, path, exc_info):
    print('Handling Error for file ' , path)
    print(exc_info)
    # Check if file access issue
    if not os.access(path, os.W_OK):
       # Try to change the permision of file
       os.chmod(path, stat.S_IWUSR)
       # call the calling function again
       func(path)

rootdir = pathlib.Path().resolve()
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        try:
            shutil.rmtree(f'{d}/node_modules', onerror=handleError)
        except Exception as e:
            print(e)
        try:
            shutil.rmtree(f'{d}/.idea', onerror=handleError)
        except Exception as e:
            print(e)
input("Press Enter")