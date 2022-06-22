lang = input("Lang : ")
mmd = input("Mmd : ")
sets = f"# settings.ini\n" \
       f"[set]\n" \
       f"lang={lang}\n" \
       f"; lang\n" \
       f"mmd={mmd}\n" \
       f";  minecraft folder\n"
with open("settings.ini", 'w') as file:
    file.write(sets)
