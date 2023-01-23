import os

def deleteFiles(directory):
    filelist = [ f for f in os.listdir(directory) if not f.endswith(".gitignore") ]
    for f in filelist:
        os.remove(os.path.join(directory, f))

def deleteTemporaryFiles():
    print("Deleting temporary files")
    deleteFiles("../assets/images")
    deleteFiles("../assets/audio")