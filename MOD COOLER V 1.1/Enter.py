import os
import shutil


print("Test mod kuler by Rubrik25")
print("Version V 1.1")

mmd = open("MMD.txt", "r")
mmdr = mmd.read()
print(mmdr)

os.chdir("mods")
for dirpath, dirnames, filenames in os.walk("."):

    for dirname in dirnames:
        print("Папка:", os.path.join(dirpath, dirname))

    for filename in filenames:
        print("Мод:", os.path.join(dirpath, filename))

while(True):
    try:
        jq = input("Который мод тебе нужно установить: ")
        jqc = jq[2:]
        shutil.copy(os.getcwd()+ "\\" + jqc, mmdr)
    except:
        print("Проблема..")