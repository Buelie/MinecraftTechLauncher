from tkinter import MULTIPLE, ttk
import tkinter as tk
import json

MainForm = tk.Tk()

def DownTovM(): #游戏本体下载子窗口
    DownFarm = tk.Toplevel()
    DownFarm.title('MinecraftTechLauncher') #设置标题
    DownFarm.geometry("600x450+374+182") #设置窗口大小
    DownFarm.iconphoto(False,tk.PhotoImage(file='icon.png')) #设置窗口图标
    Ver_List = tk.StringVar()
    Ver_List.set("1.16.5")

    VerList = tk.Listbox(DownFarm,listvariable=Ver_List).pack()
    NullBtn = ttk.Radiobutton(DownFarm,text="安装原版").pack()
    ForgeBtn = ttk.Radiobutton(DownFarm,value='forge',text="安装Forge").pack()
    FabricBtn = ttk.Radiobutton(DownFarm,value='fabric',text="安装Fabric").pack()
    DownBtn = ttk.Button(DownFarm,text="下载游戏本体").pack()

def ReadFile(path): #读取文件函数
    with open(path,'r') as file:
        data = json.load(file)
        file.close()
    return data

WriteJson = {"ver":{"minecraft":[]}} #文件写入预定义模板 [001]

def WriteFile(path,data:str = ""): #文件写入函数
    with open(path,'w+') as file:
        json.dump(data)

Json_Ver = ReadFile('config/c.json')

VerVar = tk.StringVar() #存放版本列表
VerVar.set((ReadFile("config/c.json")['ver']['Minecraft'])) #存放版本列表注册到列表

VerMenu = tk.Listbox(MainForm,name='版本列表',listvariable=VerVar).grid(row=0,column=0) #存放版本列表注册到列表

StartGameBtn = ttk.Button(MainForm,text='启动游戏').grid(row=1,column=0) #启动游戏按钮

VerLen_L = ttk.Label(MainForm,text="游戏版本数量:").grid(row=0,column=1)
VerLen = ttk.Label(MainForm,text=str(len(ReadFile("config/c.json")['ver']['Minecraft']))).grid(row=0,column=2)
################# 启动器菜单栏 #################
MainMenu = tk.Menu(MainForm,relief='solid')

StarterMenu_1 = tk.Menu(MainMenu,tearoff=False)
StarterMenu_1.add_command(label="设置")
StarterMenu_1.add_command(label="退出",command=MainForm.quit)
StarterMenu_1.add_separator()
StarterMenu_1.add_command(label="高级设置")
MainMenu.add_cascade(label="启动器",menu=StarterMenu_1)

StarterMenu_2 = tk.Menu(MainMenu,tearoff=False)
StarterMenu_2.add_command(label="模组")
StarterMenu_2.add_command(label="资源包")
StarterMenu_2.add_command(label="数据包")
StarterMenu_2.add_separator()
StarterMenu_2.add_command(label="整合包")
StarterMenu_2.add_command(label="游戏本体",command=DownTovM)
StarterMenu_2.add_separator()
StarterMenu_2.add_command(label="高级设置")
MainMenu.add_cascade(label="下载",menu=StarterMenu_2)
###############################################

MainForm.config(menu=MainMenu) #配置
MainForm.title('MinecraftTechLauncher') #设置标题
MainForm.geometry("600x450+374+182") #设置窗口大小
MainForm.attributes('-alpha',1) #TODO: 设置边栏透明
MainForm.resizable(False,False)
MainForm.iconphoto(False,tk.PhotoImage(file='icon.png'))
MainForm.mainloop() #进入窗口循环
