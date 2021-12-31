import os
import shutil
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

lang = config["Set"]["lang"]
mdr = config["Set"]["mmd"]

print("Mod cooler by Rubrik25")
print("Version V 2.0")
print('''
1 - Mods
2 - Flans
''')
try:
    os.mkdir("flans")
    os.mkdir("mods")
except:
    None
if(lang == "ru"):
    ft = int(input('Номер:'))
    if ft == 1:
        os.chdir('mods')
        ddr = mdr + '\\mods\\'
    elif ft == 2:
        os.chdir('flans')
        ddr = mdr + '\\flans\\'
    for dirpath, dirnames, filenames in os.walk("."):
        for dirname in dirnames:
            print("Папка:", os.path.join(dirpath, dirname))
            
        for filename in filenames:
            print("Мод:", os.path.join(dirpath, filename)[2:])
        while(True):
            try:
                jq = input("Который мод тебе нужно установить: ")
                jqc = jq
                print(jqc)
                shutil.copy(os.getcwd()+ "\\" + jqc, ddr)
            except:
                print("Проблема..")
if(lang == "en"):
    ft = int(input('Number:'))
    if ft == 1:
        os.chdir('mods')
        ddr = mdr + '\\mods\\'
    elif ft == 2:
        os.chdir('flans')
        ddr = mdr + '\\flans\\'
    for dirpath, dirnames, filenames in os.walk("."):
        for dirname in dirnames:
            print("Folder:", os.path.join(dirpath, dirname))
        for filename in filenames:
            print("Mod:", os.path.join(dirpath, filename)[2:])
        while(True):
            try:
                jq = input("Wich mod you need to install: ")
                jqc = jq
                print(jqc)
                shutil.copy(os.getcwd()+ "\\" + jqc, ddr)
            except:
                print("Error..")
