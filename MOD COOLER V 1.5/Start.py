import os
import shutil


print("Test mod kuler by Rubrik25")
print("Version V 1.5")

mmd = open("MMD.txt", "r")
mmdr = mmd.read()
print(mmdr)

conf = open("Conf.txt", "r")
confr = conf.read()
print(confr)
os.mkdir("mods")
os.chdir("mods")


if confr == "ru":
    for dirpath, dirnames, filenames in os.walk("."):
        for dirname in dirnames:
            print("Папка:", os.path.join(dirpath, dirname))
            
        for filename in filenames:
            print("Мод:", os.path.join(dirpath, filename))
        while(True):
            try:
                jq = input("Который мод тебе нужно установить: ")
                jqc = jq[2:]
                print(jqc)
                shutil.copy(os.getcwd()+ "\\" + jqc, mmdr)
            except:
                print("Проблема..")
if confr == "en":
    for dirpath, dirnames, filenames in os.walk("."):
        
        for dirname in dirnames:
            print("Folder:", os.path.join(dirpath, dirname))
            
        for filename in filenames:
            print("Mod:", os.path.join(dirpath, filename))
        while(True):
            try:
                jq = input("Wich mod you need to install: ")
                print(jq)
                jqc = jq[2:]
                print(jqc)
                shutil.copy(os.getcwd()+ "\\" + jqc, mmdr)
            except:
                print("Problem..")
