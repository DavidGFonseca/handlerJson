from json import dump,load
from os.path import isfile

class HandlerJson:

    def writeJson(self,filePath,*args):

        if args:
            data = {"username":f"{args[0]}","email":f"{args[1]}","password":f"{args[2]}"}
        with open(filePath,'w') as f:
            dump(data, f, indent=2)

    def readJson(self,filePath):
        if isfile(filePath):
            with open(filePath,'r') as f:
                data = load(f)
                return data
        else:
            return False
