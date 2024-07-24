#automation using python
from sys import *
import os
import hashlib
import time
def DeleteFiles(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.value()))
    icnt=0;
    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt=0
    else:
        print("No Duplicate file found")

def hashfile(path,blocksize=1024):
    afile=open(path,"rb")
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
def findDup(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
    exits=os.path.isdir(path)
    dups={}
    if exits:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for filen in fileList:
                path=os.path.join(dirName,filen)
                file_hash=hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
        return dups
    else:
        print("Invalid path")
def printResults(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.value()))
    if len(results)>0:
        print("Duplicate found")
        print("The following file are duplicate:")
        for result in results:
            for subresult in result:
                print('\t\t%s'% subresult)
    else:
        print("No duplicate file found")
def main():
    print("Application name is:"+argv[0])
    if len(argv)!=2:
        print("Error Invalid Number of Argument")
        exit()
    if (argv[1]=="-h")or(argv[1]=="-H"):
        print("This script is used to traverse specific directory & delete Duplicate files")
        exit()
    if(argv[1]=="-u")or(argv)[1]=="-U":
        print("Usage:Application name Absolute path of Directory Extension")
        exit()
    try:
        arr={}
        StartTime=time.time()
        arr=findDup(argv[1])
        printResults(arr)
        DeleteFiles(arr)
        endTime=time.time()
        print("Took%s second to evaluate."%(endTime-StartTime))
    except ValueError:
        print("Error:Invalid datatype of Input")
    except Exception as E:
        print("Error:Invalid input",E)
if __name__=="__main__":
    main()





