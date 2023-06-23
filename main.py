
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

class game:
    """
    启动游戏类
    build方法由于构建游戏启动参数并启动游戏
    """
    jdk = "C:\\Program Files\\Java\\jdk-17\\bin\\java.exe"

    def __init__(self,cfg : str = "") -> None:
        self.cfg = cfg

    # TODO:待完成
    def build(self,auth_player_name : str = "test",version_name : str = "",game_directory : str = "",assets_root : str = "",assets_index_name : str = "",auth_uuid : str = "12345678-012345678921-3456709312X456",auth_access_token : str = "",user_properties : str = "",user_type : str = "legacy"):
        pass
# GUI
