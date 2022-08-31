#!/usr/bin/env python3

import shutil
import os
import time
def delo(paths):
    tlen=0
    tdel=0
    for path in paths:
        os.chdir(path)
        tlen+=len(os.listdir())
        print("IN :",os.getcwd())
        for x in os.listdir():
            try:
                if os.path.isfile(x):
                    os.remove(x)
                    tdel+=1

                else:
                    shutil.rmtree(x)
                    tdel+=1

            except:
                pass
    print('deleted: ',tdel," out of total: ",tlen)

def main():
    if __name__=="__main__":
        delo(("C:/Windows/Temp","C:/Users/Admin/AppData/Local/Temp"))
        time.sleep(3)
if __name__=="__main__":
    main()
