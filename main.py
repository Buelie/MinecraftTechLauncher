
import os
import json
import webbrowser
import requests

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
    def build(self,auth_player_name : str = "test",version_name : str = "1.19.3",game_directory : str = "",assets_root : str = "",assets_index_name : str = "1.0",auth_uuid : str = "12345678-012345678921-3456709312X456",auth_access_token : str = " ",user_properties : str = "{}",user_type : str = "legacy"):
        default = "--username ${auth_player_name} --version ${version_name} --gameDir ${game_directory} --assetsDir ${assets_root} --assetIndex ${assets_index_name} --uuid ${auth_uuid} --accessToken ${auth_access_token} --userProperties ${user_properties} --userType ${user_type}"
        parameter = default.replace("${auth_player_name}",auth_player_name).replace("${version_name}",version_name)\
        .replace("${game_directory}",game_directory).replace("${assets_root}",assets_root)\
        .replace("${assets_index_name}",assets_index_name).replace("${auth_uuid}",auth_uuid)\
        .replace("${auth_access_token}",auth_access_token).replace("${user_properties}",user_properties)\
        .replace("${user_type}",user_type)
        return parameter

def StartGame():
    ver_cfg = ReadFile('config/cfg/ver.txt')
    par = JsonFile("config/cfg/main.json").Read()
    if par["JavaPath"] == True:
        command = '\"' + par["Java"] + '\\java.exe\"' + " -Xmx" + par["xmx"] + "m"\
        + " -Dfml.ignoreInvalidMinecraftCertificates=true" +\
        " -Dfml.ignorePatchDiscrepancies=true" + ' -Djava.library.path="'+\
        'Minecraft\\versions\\' + ver_cfg + "\\" + ver_cfg + '-natives"' + " " + game().build() +\
        " " +JsonFile(".minecraft/versions/"+ver_cfg+"/"+ver_cfg+".json").Read()["mainClass"]
        os.system(command)
        return command
    elif par["JavaPath"] == False:
        command = 'java' + " -Xmx" + par["xmx"] + "m"\
        + " -Dfml.ignoreInvalidMinecraftCertificates=true" +\
        " -Dfml.ignorePatchDiscrepancies=true" + ' -Djava.library.path="'+\
        'Minecraft\\versions\\' + ver_cfg + "\\" + ver_cfg + '-natives"' + " " + game().build() +\
        " " +JsonFile(".minecraft/versions/"+ver_cfg+"/"+ver_cfg+".json").Read()["mainClass"]
        os.system(command)
        return command
