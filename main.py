from tkinter import MULTIPLE, ttk
import tkinter as tk
import json

MainForm = tk.Tk()

def ReadFile(path):
    with open(path,'r') as file:
        data = json.load(file)
        file.close()
    return data

WriteJson = {"ver":{"minecraft":[]}}

def WriteFile(path,data:str = ""):
    with open(path,'w+') as file:
        json.dump(data)


Json_Ver = ReadFile('config/c.json')

VerVar = tk.StringVar() #存放版本列表
VerVar.set((ReadFile("config/c.json")['ver']['Minecraft'])) #存放版本列表注册到列表

VerMenu = tk.Listbox(MainForm,name='版本列表',listvariable=VerVar).grid(row=0,column=0) #存放版本列表注册到列表

StartGameBtn = ttk.Button(MainForm,text='启动游戏').grid(row=1,column=0) #启动游戏按钮

MainForm.iconphoto(False,tk.PhotoImage(file='icon.png'))
MainForm.title('MinecraftTechLauncher') #设置标题
MainForm.geometry("600x450+374+182") #设置窗口大小
MainForm.attributes('-alpha',1) #TODO: 设置边栏透明
MainForm.resizable(False,False)
MainForm.mainloop() #进入窗口循环
