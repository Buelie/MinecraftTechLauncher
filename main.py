from ttkbootstrap.constants import *
import os
import json
from ttkbootstrap import Style
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import webbrowser
import requests
#1641780513
# 文件检测/初始化
if os.path.isdir('.minecraft/assets') == False:
    os.makedirs('.minecraft/assets')
if os.path.isdir('.minecraft/resourcepacks') == False:
    os.makedirs('.minecraft/resourcepacks')
if os.path.isdir('.minecraft/saves') == False:
    os.makedirs('.minecraft/saves')
if os.path.isdir('.minecraft/mods') == False:
    os.makedirs('.minecraft/mods')
if os.path.isdir('.minecraft/logs') == False:
    os.makedirs('.minecraft/logs')
if os.path.isdir('.minecraft/libraries') == False:
    os.makedirs('.minecraft/libraries')
if os.path.isdir('.minecraft/versions') == False:
    os.makedirs('.minecraft/versions')
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
if os.path.isfile('config/cfg/ver.txt') == False:
    with open('config/cfg/plugin.json','w') as f:
        f.write('{\n"$PluginList":["api.json"]\n}')
        f.close()
if os.path.isfile('config/cfg/ver.txt') == False:
    with open('config/cfg/ver.txt','w') as f:
        f.write("")
        f.close()
if os.path.isfile('config/cfg/username.txt') == False:
    with open('config/cfg/username.txt','w') as f:
        f.write("test")
        f.close()
if os.path.isfile('config/cfg/main.json') == False:
    Test = {"Java":"C:\\Program Files\\Java\\jdk-17\\bin","xmx":"1024","JavaPath":True}
    with open('config/cfg/main.json','w') as f:
        fe = json.dumps(Test)
        f.write(fe)
        f.close()

PluginList = os.listdir("config/plugin/")

# 函数/类
def ReadFile(path):
    with open(path,'r') as f:
        data = f.read()
        f.close()
    return data
class JsonFile:
    """
    读取/写入JSON文件的类
    Read方法是读写JSON文件
    Write方法是写入JSON文件
    """
    def __init__(self,path) -> None:
        self.path = path

    def Read(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = json.load(f)
            f.close()
        return Data

    def Write(self):
        with open(self.path,'w',encoding='utf-8') as f:
            Data = json.dumps(f)
            f.close()
        return Data

    def FileRead(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = f.read()
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
    def build(self,auth_player_name : str = str(JsonFile("config/cfg/username.txt").FileRead()),version_name : str = JsonFile("config/cfg/ver.txt").FileRead(),game_directory : str = "",assets_root : str = "",assets_index_name : str = "1.0",auth_uuid : str = "12345678-012345678921-3456709312X456",auth_access_token : str = " ",user_properties : str = "{}",user_type : str = "legacy"):
        default = "--username ${auth_player_name} --version ${version_name} --gameDir ${game_directory} --assetsDir ${assets_root} --assetIndex ${assets_index_name} --uuid ${auth_uuid} --accessToken ${auth_access_token} --userProperties ${user_properties} --userType ${user_type}"
        parameter = default.replace("${auth_player_name}",auth_player_name).replace("${version_name}",version_name)\
        .replace("${game_directory}",game_directory).replace("${assets_root}",assets_root)\
        .replace("${assets_index_name}",assets_index_name).replace("${auth_uuid}",auth_uuid)\
        .replace("${auth_access_token}",auth_access_token).replace("${user_properties}",user_properties)\
        .replace("${user_type}",user_type)
        return parameter

PluginListTwo = JsonFile('config/cfg/plugin.json').Read()["$PluginList"]

def PluginWind():
    PluginWindFram = tk.Toplevel()
    PluginWindFram.geometry("600x450+374+182")
    PluginWindFram.title("MTC/MTL - 插件")
    PluginWindFram.resizable(False,False)

    PluginLable = ttk.Label(PluginWindFram,text="插件列表").pack()
    List = tk.Listbox(PluginWindFram)
    for item in PluginList:
        List.insert("end",item)
    List.pack()
    PluginLableTwo = ttk.Label(PluginWindFram,text="已激活插件列表").pack()
    ListTwo = tk.Listbox(PluginWindFram)
    for item in PluginListTwo:
        ListTwo.insert("end",item)
    ListTwo.pack()


def HelpExterior():
    answer = tk.messagebox.askokcancel('确定前往官网获取帮助','选择确定查看，选择取消关闭')
    if answer:
        webbrowser.open('https://github.com/Buelie/MinecraftTechLauncher/')
    else:
        pass

def Settings():
    WindMain = tk.Toplevel()
    WindMain.geometry("600x450+374+182")
    WindMain.title("MTC/MTL - 设置")
    WindMain.resizable(False,False)

    Slb = ttk.Label(WindMain,text="主题样式 : ").grid(row=0,column=0)
    Sle = ttk.Entry(WindMain)
    def a():
        try:
            MainWind = Style(theme=Sle.get()).master
            tkinter.messagebox.showinfo(title="提示",message="修改成功!")
        except Exception as e:
            print(e)
            tkinter.messagebox.showwarning(title="错误",message="样式不可用")
            tkinter.messagebox.showwarning(title="错误",message=str(e))
    Sle.grid(row=0,column=1)
    Sln = ttk.Button(WindMain,text="应用",command=a).grid(row=0,column=2)

    NameSetLabel = ttk.Label(WindMain,text="默认用户名 : ").grid(row=1,column=0)
    NameSet = ttk.Entry(WindMain)
    def b():
        try:
            with open("config/cfg/username.txt",'w') as f:
                f.write(NameSet.get())
                f.close()
            UserName = JsonFile("config/cfg/username.txt").FileRead()
            MainWind.title(f'MinecraftTechLauncher - 当前用户名:{str(UserName)}')
            tkinter.messagebox.showinfo(title="提示",message="修改成功!")
        except Exception as e:
            print(e)
            tkinter.messagebox.showwarning(title="错误",message=str(e))
    NameSet.grid(row=1,column=1)
    NameSetBtn = ttk.Button(WindMain,text="应用",command=b).grid(row=1,column=2)

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

MainWind = Style(theme='cyborg').master
UserName = JsonFile("config/cfg/username.txt").FileRead()

"""
子窗口
"""
def DownloadWind():
    Wind = tk.Toplevel()
    Wind.geometry("600x450+374+182")
    Wind.title("MTC/MTL - 下载")

MainFrame = tk.Frame(MainWind).pack()

version_manifest_json = requests.get("https://bmclapi2.bangbang93.com/mc/game/version_manifest.json")
VerLable = tk.Label(MainFrame,text="版本列表:",font=("楷体",16),bg="#333333",fg="#FFF").pack()

"""
版本列表
VerVar变量用于获取目录下所有版本
"""
VerVar = tk.StringVar() 
VerVar.set(os.listdir('.minecraft/versions'))
VerList = tk.Listbox(MainFrame,listvariable=VerVar).pack()

VerActive = ttk.Label(MainFrame,text="当前选中版本:"+str(ReadFile('config/cfg/ver.txt')),font=("楷体",16)).pack()
VerLen = ttk.Label(MainFrame,text="版本数量:"+str(len(os.listdir('.minecraft/versions'))),font=("楷体",16)).pack()

"""
启动游戏按钮
绑定StartGame函数
"""
def StartGame():
    try:
        ver_cfg = ReadFile('config/cfg/ver.txt')
        par = JsonFile("config/cfg/main.json").Read()
        if par["JavaPath"] == True:
            command = '\"' + par["Java"] + '\\javaw.exe\"' + " -Xmx" + par["xmx"] + "m"\
            + " -Dfml.ignoreInvalidMinecraftCertificates=true" +\
            " -Dfml.ignorePatchDiscrepancies=true" + ' -Djava.library.path="'+\
            'Minecraft\\versions\\' + ver_cfg + "\\" + ver_cfg + ' -natives"' + " " + game().build() +\
            " " +JsonFile(".minecraft/versions/"+ver_cfg+"/"+ver_cfg+".json").Read()["mainClass"]
            os.system(command)
            return command
        elif par["JavaPath"] == False:
            command = 'java' + " -Xmx" + par["xmx"] + "m"\
            +" -Dfml.ignoreInvalidMinecraftCertificates=true" +\
            " -Dfml.ignorePatchDiscrepancies=true" + ' -Djava.library.path="'+\
            'Minecraft\\versions\\' + ver_cfg + "\\" + ver_cfg + ' -natives"' + " " + game().build() +\
            " " +JsonFile(".minecraft/versions/"+ver_cfg+"/"+ver_cfg+".json").Read()["mainClass"]
            os.system(command)
            print(command)
            return command
        tkinter.messagebox.showinfo(title="提示",message="启动成功,拼接参数如下:\n"+str(command))
    except Exception as e:
        print(e)
        tkinter.messagebox.showwarning(title="错误",message=str(e))

#print(version_manifest_json.text)
#print(JsonFile("config/cfg/main.json").Read()["Java"])
StartGameBtn = ttk.Button(MainFrame,text="启动游戏",width=30,command=StartGame).pack()

"""
菜单 >>>
一级菜单:<启动器> | <下载> | <高级> | <帮助>
二级菜单:[启动器]:<设置> | <插件> | <检测错误> | <退出>
        :[下载]:<游戏本体> | <Mod> | <资源包> | <整合包> | <光影包>
        :[高级]:<高级设置> | <插件> | <游戏参数> | <高级游戏设置>
        :[帮助]:<帮助(软件内)> | <帮助(软件外)>
"""
MainMenu = tk.Menu(MainWind,relief='solid',bg="#333333")

Launcher = tk.Menu(MainMenu,tearoff=False)
Launcher.add_command(label="设置",command=Settings)
Launcher.add_command(label="插件",command=PluginWind)
Launcher.add_command(label="检查错误")
Launcher.add_command(label="退出",command=MainWind.quit)
MainMenu.add_cascade(label="启动器",menu=Launcher)

Download = tk.Menu(MainMenu,tearoff=False)
Download.add_command(label="游戏本体",command=DownloadWind)
Download.add_command(label="Mod",command=DownloadWind)
Download.add_command(label="资源包",command=DownloadWind)
Download.add_command(label="整合包",command=DownloadWind)
Download.add_command(label="光影包",command=DownloadWind)
MainMenu.add_cascade(label="下载",menu=Download)

Senior = tk.Menu(MainMenu,tearoff=False)
Senior.add_command(label="高级设置")
Senior.add_command(label="插件",command=PluginWind)
Senior.add_command(label="游戏参数")
Senior.add_command(label="高级游戏设置")
MainMenu.add_cascade(label="高级",menu=Senior)

Help = tk.Menu(MainMenu,tearoff=False)
Help.add_command(label="帮助(软件内)")
Help.add_command(label="帮助(软件外)",command=HelpExterior)
MainMenu.add_cascade(label="帮助",menu=Help)

# - 分割线 -

MainWind.config(menu=MainMenu,bg="#060606")
MainWind.title(f'MinecraftTechLauncher - 当前用户名:{str(UserName)}')
MainWind.geometry("600x450+374+182")
MainWind.resizable(False,False)
MainWind.mainloop()
