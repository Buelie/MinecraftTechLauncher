from tkinter import MULTIPLE, ttk
import tkinter as tk
import json
import os
import webbrowser
import sys
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import *
import tkinter.colorchooser
import subprocess
from tkinter import messagebox

MainForm = tk.Tk()

def SettingMain():
    
    class Stdout():	# 重定向类
        def __init__(self):
        	# 将其备份
            self.stdoutbak = sys.stdout		
            self.stderrbak = sys.stderr
            # 重定向
            sys.stdout = self
            sys.stderr = self

        def write(self, info):
            # info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
            JavaPathL.insert('end', info)# 在多行文本控件最后一行插入print信息
            JavaPathL.update()# 更新显示的文本，不加这句插入的信息无法显示
            JavaPathL.see(tk.END)# 始终显示最后一行，不加这句，当文本溢出控件最后一行时，不会自动显示最后一行

        def restoreStd(self):
            # 恢复标准输出
           sys.stdout = self.stdoutbak
           sys.stderr = self.stderrbak

    def jp():
        #a = os.popen('where java')

        b = subprocess.Popen('where java')
        a = b.stdout.read()
        b.wait()
        b.stdout.close()
        return a
    
    SetMain = tk.Toplevel()
    SetMain.title('MinecraftTechLauncher')
    SetMain.geometry("600x450+374+182") #设置窗口大小
    SetMain.iconphoto(False,tk.PhotoImage(file='icon.png'))

    JavaPathLable = ttk.Label(SetMain,text='Java路径:').grid(row=0,column=0)
    JPath = os.system('where java')
    JavaPathL = ttk.Label(SetMain,text=jp)
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

VerMenu = tk.Listbox(MainForm,name='版本列表',listvariable=VerVar) #存放版本列表注册到列表

VerLen_L = ttk.Label(MainForm,text="游戏版本数量:").grid(row=0,column=1)
VerLen = ttk.Label(MainForm,text=str(len(ReadFile("config/c.json")['ver']['Minecraft']))).grid(row=0,column=2)

JavaPthLable = ttk.Label(MainForm,text=' | Java路径:').grid(row=1,column=3)
JavaPth = ttk.Entry(MainForm)

BigNC = ttk.Label(MainForm,text='最大内存:').grid(row=1,column=1)
BiggestNC = ttk.Entry(MainForm)

def startgame():
    if JavaPth.get() == "":
        messagebox.showerror("错误","请填写Java路径")
    else:
        if VerMenu.curselection() == ():
            messagebox.showerror("错误","请选择版本")
        elif BiggestNC.get() == "":
            messagebox.showerror("错误","请填写最大内存")
        else:
            messagebox.showinfo("提示","启动成功")
            try:
                SatartCS = JavaPth.get() + ""
            except Exception as e:
                print(e)
                return e

BiggestNC.grid(row=1,column=2)
VerMenu.grid(row=0,column=0)
JavaPth.grid(row=1,column=4)
StartGameBtn = ttk.Button(MainForm,text='启动游戏',command=startgame).grid(row=1,column=0) #启动游戏按钮
################# 启动器菜单栏 #################
MainMenu = tk.Menu(MainForm,relief='solid')

StarterMenu_1 = tk.Menu(MainMenu,tearoff=False)
StarterMenu_1.add_command(label="设置")
StarterMenu_1.add_command(label="退出",command=MainForm.quit)
StarterMenu_1.add_separator()
StarterMenu_1.add_command(label="高级设置",command=SettingMain)
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
