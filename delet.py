#!/usr/bin/env python3
import shutil
import os
import time
def dif(folders,show=False,na=[],returns=True):
    """
    deletes all the files and folders inside the folders
    parameters:
    show : shows the files/folders deleted
    na: enter files not to be deleted
    returns: also returns the names of files and folders deleted
    """
    folder=[]
    if type(folders)==str:
        folder.append(folders)
    else:
        folder=folders
    if returns==True:
        tlen=0
        tdel=0
    if returns==True and show==True:
        deleted={'file':[],'folders':[]}
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
        try:
            dif(("C:/Windows/Temp","C:/Users/Admin/AppData/Local/Temp"),show=True)
        except:
            dif(("/mnt/c/Windows/Temp","/mnt/c/Users/Admin/AppData/Local/Temp"))
        time.sleep(0.5)

if __name__=="__main__":
    main()
