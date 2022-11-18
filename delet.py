#!/usr/bin/env python3
import os
import shutil
import time
import sys

def dif(folders=[],show=False,na=[],returns=True,argv=False,argv_n=[]):
    """
    deletes all the files and folders inside the folders
    parameters:
    folders: enter the list of folders or a single folder string
    show : shows the files/folders deleted
    na: enter files not to be deleted
    returns: also returns the names of files and folders deleted
    argv: if argv is True takes the folders from the sys.argv
    argv_n: you can optionally enter the index of the folder in sys.argv
    """
    if folders==[] and argv==False:
       raise TypeError('list of folders is required')
    folder=[]
    if argv==True:
        if argv_n==[]:
            folder=sys.argv[1:]
        elif type(argv_n)!=list:
            raise AttributeError('argv_n must be a list')
        elif len(argv_n)>2 or len(argv_n)<0:
            raise AttributeError('lenghth of argv_n must be bigger then 0 and smaller than 2')
        elif not int(argv_n[0])<0:
            raise AttributeError(' first alue of argv_n must be bigger than zero')
        else:
            if len(argv_n)==2:
                folder=sys.argv[int(argv_n[0]):int(argv_n[1])]
            elif len(argv_n)==1:
                folder=sys.argv[int(argv_n[0]):]

    if type(folders)==str:
        folder.append(folders)
    if returns==True:
        tlen=0
        tdel=0
    if returns==True and show==True:
        deleted={'file':[],'folders':[]}
    elif type(folder)==list:
        folder+=folders
    for path in folder:
        try: 
            os.chdir(path)
        except FileNotFoundError as fe:
            print(fe)
            if path!=folder[-1]:    
                continue
            else:
                raise FileNotFoundError(fe)
        if returns==True:
            tlen+=len(os.listdir())
            print("IN :",os.getcwd())
        for x in os.listdir():
            try:
                if x not in na:
                    if os.path.isfile(x):
                        os.remove(x)
                        tdel+=1
                        if show==True and returns==True:
                            deleted['file'].append(x)

                    else:
                        shutil.rmtree(x)
                        tdel+=1
                        if show==True and returns==True:
                            deleted['folders'].append(x)
            except:
                pass
    if returns==True:
        print('deleted: {} out of total: {} '.format(tdel,tlen),end=" ")
    if show==True and returns==True:
         print('files deleted : {} & folders deleted : {} '.format(tuple(deleted['file']),tuple(deleted['folders'])))
        
def main():
        if len(sys.argv)>1:
                dif(show=True,argv=True)
        time.sleep(1)

if __name__=='main':
    main()
