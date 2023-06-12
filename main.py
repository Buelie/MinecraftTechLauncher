import platform
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

GameUserName = "TestUserName"
ver = "MTC-急速启动-预览版-V0.0.5"
MainForm = tk.Tk()

print(os.listdir('plugin/'))

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

command = []
command.append(ReadFile('plugin/HtexdPiny.json')["command"])
plugin_id = []
plugin_id.append(ReadFile('plugin/HtexdPiny.json')["id"])
PluginName = []
PluginName.append("HtexdPiny")

def PluginWind():

    Main = tk.Toplevel()
    Main.geometry("600x450+374+182")
    Main.title('MinecraftTechLauncher') #设置标题
    Main.iconphoto(False,tk.PhotoImage(file='icon.png')) #设置窗口图标

    PluginLable = ttk.Label(Main,text="插件列表").pack()
    PluginList = ttk.Label(Main)
    PluginList.config(text=os.listdir('plugin/'))    
    PluginList.pack()
    PluginJH = ttk.Label(Main,text="激活插件")
    PluginEn = ttk.Entry(Main)
    PluginJH.pack()
    PluginEn.pack()
    print(command)

WriteJson = {"ver":{"minecraft":[]}} #文件写入预定义模板 [001]

def WriteFile(path,data:str = ""): #文件写入函数
    with open(path,'w+') as file:
        json.dump(data)

VerVar = tk.StringVar() #存放版本列表
VerVar.set(os.listdir('.minecraft/versions')) #存放版本列表注册到列表

VerMenu = tk.Listbox(MainForm,name='版本列表',listvariable=VerVar) #存放版本列表注册到列表

VerLen_L = ttk.Label(MainForm,text="游戏版本数量:").grid(row=0,column=1)
VerLen = ttk.Label(MainForm,text=str(len(os.listdir('.minecraft/versions')))).grid(row=0,column=2)

JavaPthLable = ttk.Label(MainForm,text='Java路径:').grid(row=3,column=0)
JavaPth = ttk.Entry(MainForm)

BigNC = ttk.Label(MainForm,text='最大内存:').grid(row=2,column=0)
BiggestNC = ttk.Entry(MainForm)

VL = ttk.Label(MainForm,text="版本名称(必须和json文件名一致):")
VER = ttk.Entry(MainForm)

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
                Satart = "java"+" "+"-XX:+UseG1GC "+"-XX:-UseAdaptiveSizePolicy "+\
                "-XX:-OmitStackTraceInFastThrow "+"-Dfml.ignoreInvalidMinecraftCertificates=True "+\
                "-Dfml.ignorePatchDiscrepancies=True "+"-Dlog4j2.formatMsgNoLookups=true "+\
                "-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump "+\
                "-Dminecraft.launcher.brand=MinecraftTechLauncher "+\
                "-Dminecraft.launcher.version=0.0.3 "+"-username"+GameUserName+" "
                if platform.version()[0:2] == '10':
                    WinTen = '-Dos.name=Windows 10 " -Dos.version=10.0 '+\
                    "-Xmn256m "+"-Xmx"+BiggestNC.get()+"m "+\
                    ReadFile('.minecraft/versions/'+VER.get()+'/'+VER.get()+'.json')['mainClass']+" "
                    SatartCS = Satart + WinTen
                else:
                    SatartCS = Satart + "-Xmn256m "+"-Xmx"+BiggestNC.get()+"m "+\
                    " "+ReadFile('.minecraft/versions/'+VER.get()+'/'+VER.get()+'.json')['mainClass']+" "
                print(SatartCS)
                messagebox.showinfo("拼接信息:",SatartCS)
                try:
                    os.system(SatartCS)
                except Exception as er:
                    messagebox.showerror("启动失败",er)
                    print(er)
                    return er
            except Exception as e:
                messagebox.showerror("拼接信息 - ERROR","拼接失败!!!\n"+str(e))
                print(e)
                return e
PluginCommandLable = ttk.Label(MainForm,text="执行命令:").grid(row=5,column=0)
PluginCommand = ttk.Entry(MainForm,width=30)

def Command():
    if PluginCommand.get() != "":
        try:
            if PluginCommand.get() == "/cfg start":
                Satart = "java"+" "+"-XX:+UseG1GC "+"-XX:-UseAdaptiveSizePolicy "+\
                "-XX:-OmitStackTraceInFastThrow "+"-Dfml.ignoreInvalidMinecraftCertificates=True "+\
                "-Dfml.ignorePatchDiscrepancies=True "+"-Dlog4j2.formatMsgNoLookups=true "+\
                "-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump "+\
                "-Dminecraft.launcher.brand=MinecraftTechLauncher "+\
                "-Dminecraft.launcher.version=0.0.3 "
                if platform.version()[0:2] == '10':
                    WinTen = '-Dos.name=Windows 10 " -Dos.version=10.0 '+\
                    "-Xmn256m "+"-Xmx"+BiggestNC.get()+"m "+\
                    ReadFile('.minecraft/versions/'+VER.get()+'/'+VER.get()+'.json')['mainClass']+" "
                    SatartCS = Satart + WinTen
                else:
                    SatartCS = Satart + "-Xmn256m "+"-Xmx"+BiggestNC.get()+"m "+\
                    " "+ReadFile('.minecraft/versions/'+VER.get()+'/'+VER.get()+'.json')['mainClass']+" "
                print(SatartCS)
                messagebox.showinfo("拼接信息:",SatartCS)
            elif PluginCommand.get()[0:5] == "/json":
                try:
                    messagebox.showwarning("警告","该功能未完善，可能导致启动器或游戏崩溃")
                    messagebox.showinfo("读取信息",str(ReadFile(PluginCommand.get()[6:-4])[PluginCommand.get()[-1:-3]]))
                except Exception as error:
                    messagebox.showerror("ERROR",error)
                    print(error)
            elif PluginCommand.get()[0:5] == "/java":
                try:
                    messagebox.showinfo("信息","已将默认Java路径更改为:"+PluginCommand.get()[6:-1])
                except Exception as error:
                    messagebox.ERROR("错误",error)
                    print(error)
            elif PluginCommand.get()[0:4] == "/ver":
                try:
                    if PluginCommand.get()[5:8] == "EXE":
                        messagebox.showinfo("查询","当前启动器版本为:"+ver+"\n状态码:001")
                    else:
                        messagebox.showerror("错误","未找到<Object>\n状态码:024")
                except Exception as error:
                    messagebox.showerror("错误",error)
                    print(error)
            elif PluginCommand.get()[0:9] == "/UserName":
                try:
                    GameUserName = PluginCommand.get()[10:-1]
                    messagebox.showinfo("信息","默认用户名已更改为:"+GameUserName)
                except Exception as error:
                    messagebox.showerror("错误",error)
                    print(error)
            else:
                pass
        except Exception as e:
            messagebox.showerror("ERROR",e)

PluginBtn = ttk.Button(MainForm,text="执行",command=Command).grid(row=5,column=3)
PluginCommand.grid(row=5,column=1)

VL.grid(row=4,column=0)
VER.grid(row=4,column=1)
BiggestNC.grid(row=2,column=1)
VerMenu.grid(row=0,column=0)
JavaPth.grid(row=3,column=1)
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
StarterMenu_2.add_command(label="高级设置",command=PluginWind)
MainMenu.add_cascade(label="下载",menu=StarterMenu_2)

StarterMenu_3 = tk.Menu(MainMenu,tearoff=False)
StarterMenu_3.add_command(label="开发者工具")
StarterMenu_3.add_separator()
StarterMenu_3.add_command(label="开发者设置")
MainMenu.add_cascade(label="开发者选项",menu=StarterMenu_3)
###############################################

MainForm.config(menu=MainMenu) #配置
MainForm.title('MinecraftTechLauncher') #设置标题
MainForm.geometry("600x450+374+182") #设置窗口大小
MainForm.attributes('-alpha',1) #TODO: 设置边栏透明
MainForm.resizable(False,False)
MainForm.iconphoto(False,tk.PhotoImage(file='icon.png'))
MainForm.mainloop() #进入窗口循环
