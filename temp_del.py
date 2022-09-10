#!/usr/bin/env python3
import shutil
import os
import time
def dif(folders,show=False):
    # dif : deletes all inside the folders
    tlen=0
    tdel=0
    if show==True:
        deleted={'file':[],'folders':[]}
    for path in folders:
        os.chdir(path)
        tlen+=len(os.listdir())
        print("IN :",os.getcwd())
        for x in os.listdir():
            try:
                if os.path.isfile(x):
                    os.remove(x)
                    tdel+=1
                    if show==True:
                        deleted['file'].append(x)

                else:
                    shutil.rmtree(x)
                    tdel+=1
                    if show==True:
                        deleted['folders'].append(x)
            except:
                pass
    
    print('deleted: {} out of total: {} '.format(tdel,tlen))
    if show==True:
         print('files deleted : {} \n folders deleted : {} '.format(tuple(deleted['file']),tuple(deleted['folders'])))

def main():
        #delo(("C:/Windows/Temp","C:/Users/Admin/AppData/Local/Temp"))
        dif(('C:/Users/Admin/OneDrive/Desktop/b','C:/Users/Admin/OneDrive/Desktop/a'),show=True)
        time.sleep(0.5)

if __name__=="__main__":
    main()
