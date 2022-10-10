#!/usr/bin/env python3
import shutil
import os
import time
def dif(folders,show=False,na=[]):
    """
    deletes all the files and folders inside the folders
    parameters:
    show : shows the files/folders deleted
    na: enter files not to be deleted
    """
    folder=[]
    if type(folders)==str:
        folder.append(folders)
    else:
        folder=folders
    tlen=0
    tdel=0
    if show:
        deleted={'file':[],'folders':[]}
    for path in folder:
        try: 
            os.chdir(path)
        except FileNotFoundError as e:
            print(e)
            continue
        tlen+=len(os.listdir())
        print("IN :",os.getcwd())
        for x in os.listdir():
            try:
                if x not in na:
                    if os.path.isfile(x):
                        os.remove(x)
                        tdel+=1
                        if show:
                            deleted['file'].append(x)

                    else:
                        shutil.rmtree(x)
                        tdel+=1
                        if show:
                            deleted['folders'].append(x)
            except FileNotFoundError  as e:

                print(e)
    
    print('deleted: {} out of total: {} '.format(tdel,tlen))
    if show:
         print('files deleted : {} \n folders deleted : {} '.format(tuple(deleted['file']),tuple(deleted['folders'])))

def main():
        try:
            dif(("C:/Windows/Temp","C:/Users/Admin/AppData/Local/Temp"))
        except:
            dif(("/mnt/c/Windows/Temp","/mnt/c/Users/Admin/AppData/Local/Temp"))
        time.sleep(0.5)

if __name__=="__main__":
    main()
