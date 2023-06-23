
import os
import json
import tkinter as tk
import tkinter.ttk as ttk

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
    游戏相关类
    build方法由于构建游戏启动参数
    """
    jdk = "C:\\Program Files\\Java\\jdk-17\\bin\\java.exe"
    MinecraftPath = os.getcwd()+"\\.minecraft"

    def __init__(self,cfg : str = "") -> None:
        self.cfg = cfg

    # TODO:待完成MainClass的拼接
    def build(self,auth_player_name : str = "test",version_name : str = "1.0",game_directory : str = "",assets_root : str = "",assets_index_name : str = "1.0",auth_uuid : str = "12345678-012345678921-3456709312X456",auth_access_token : str = " ",user_properties : str = "{}",user_type : str = "legacy"):
        default = "--username ${auth_player_name} --version ${version_name} --gameDir ${game_directory} --assetsDir ${assets_root} --assetIndex ${assets_index_name} --uuid ${auth_uuid} --accessToken ${auth_access_token} --userProperties ${user_properties} --userType ${user_type}"
        parameter = default.replace("${auth_player_name}",auth_player_name).replace("${version_name}",version_name)\
        .replace("${game_directory}",game_directory).replace("${assets_root}",assets_root)\
        .replace("${assets_index_name}",assets_index_name).replace("${auth_uuid}",auth_uuid)\
        .replace("${auth_access_token}",auth_access_token).replace("${user_properties}",user_properties)\
        .replace("${user_type}",user_type)
        return parameter

# 调试模式
"""
while True:
    Input = input("MinecraftTechLauncher/sys64/py>")
    if Input == 'help':
        print("还没有搞好哦！")
    elif Input == 'close':
        quit()
    elif Input == "build":
        print(game().build())
    elif Input[0:3] == "cmd":
        os.system(Input[4:-1])
    elif Input[0:2] == "py":
        print(exec(Input[3:-1]))
"""

# GUI

MainWind = tk.Tk()

"""
菜单 >>>
一级菜单:<启动器> | <下载> | <高级> | <帮助>
二级菜单:[启动器]:<设置> | <插件> | <检测错误> | <退出>
        :[下载]:<游戏本体> | <Mod> | <资源包> | <整合包> | <光影包>
        :[高级]:<高级设置> | <插件> | <游戏参数> | <高级游戏设置>
        :[帮助]:<帮助(软件内)> | <帮助(软件外)>
"""
MainMenu = tk.Menu(MainWind,relief='solid')

Launcher = tk.Menu(MainMenu,tearoff=False)
Launcher.add_command(label="设置")
Launcher.add_command(label="插件")
Launcher.add_command(label="检查错误")
Launcher.add_command(label="退出",command=MainWind.quit)
MainMenu.add_cascade(label="启动器",menu=Launcher)

Download = tk.Menu(MainMenu,tearoff=False)
Download.add_command(label="游戏本体")
Download.add_command(label="Mod")
Download.add_command(label="资源包")
Download.add_command(label="整合包")
Download.add_command(label="光影包")
MainMenu.add_cascade(label="下载",menu=Download)



# - 分割线 -

MainWind.config(menu=MainMenu)
MainWind.title('MinecraftTechLauncher')
MainWind.geometry("600x450+374+182")
MainWind.resizable(False,False)
MainWind.mainloop()
