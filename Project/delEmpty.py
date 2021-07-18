import os
from os import path

def delEmpty(path):
    for file in os.listdir(path):
        filee = path+"/" + file
        try:
            if len(os.listdir(filee)) == 0:
                os.removedirs(filee)
                print(f"成功删除{filee}")
            elif os.path.isfile(filee):
                if os.path.getsize(filee) == 0:
                    os.remove(filee)
                    print(f"成功删除{filee}")
            else:
                delEmpty(filee)
        except Exception as e:
            # print(e)
            pass

if __name__ == "__main__":   
    path = input("输入盘符：") 
    path = path + ':'
    delEmpty(path)
