
import os
import json

# 文件检测/初始化
if os.path.isdir('.minecraft/') == False:
    os.makedirs('.minecraft')
if os.path.isdir('config') == False:
    os.makedirs('config')
if os.path.isdir('config/cfg') == False:
    os.makedirs('config/cfg')
if os.path.isdir('config/res') == False:
    os.makedirs('config/res')
if os.path.isdir('config/plugin') == False:
    os.makedirs('config/plugin')
if os.path.isfile('config/cfg/main.json') == False:
    Test = {"Java":""}
    with open('config/cfg/main.json','w') as f:
        fe = json.dumps(Test)
        f.write(fe)
        f.close()
# 函数
class JsonFile:
    """
    读取/写入JSON文件的类
    Read方法是读写JSON文件
    Write方法是写入JSON文件
    """
    def __init__(self,path) -> None:
        self.path = path

    def Read(self):
        with open(self.path,'w',encoding='utf-8') as f:
            Data = json.load(f)
            f.close()
        return Data

    def Write(self):
        with open(self.path,'w',encoding='utf-8') as f:
            Data = json.dumps(f)
            f.close()
        return Data

# GUI
