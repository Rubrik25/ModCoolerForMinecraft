import os
import shutil
import configparser
import tkinter as tk
from tkinter import filedialog as fd

lang_schemas = {
    'ru': 'Dont used',
    'ua': 'Dont used',
    'en': 'Dont used'
}

try:
    os.mkdir("flans")
    os.mkdir("mods")
except:
    pass

config = configparser.ConfigParser()
config.read("settings.ini")
lang = config["set"]["lang"]
mdr = config["set"]["mmd"]

root = tk.Tk()
root.title('Mods To Minecraft')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))

    filenames = fd.askopenfilenames(title='Open files', filetypes=filetypes)

    for i in filenames:
        shutil.copy(i, mdr)

    return filenames


open_button = tk.Button(root, text='Open Files', command=select_files)

open_button.pack(expand=True)

root.mainloop()
