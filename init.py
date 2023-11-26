import os
import termcolor as tc
import term as t
from time import sleep
os.system("clear")
print("_")
s = t.getSize()
t.pos(s[0], s[1])
sleep(2)
os.system("clear")
welcome = tc.colored("Welcome to pyOS!", "blue")
tx = "(c) 2023 AzureTec"
ver = tc.colored(f"Version 3.12 {tx}", "dark_grey")
print(f"{welcome}\n{ver}\n\n")
while True:
    i = input("$ ")
    if i.lower() == "python":
        os.system("python3")
    elif i.lower() == "help":
        print("""
python : Run Python       apps   : Open apps
exit   : Exit Python3     reset  : Restart current session"
clear  : Clear screen""")
    elif i.lower() == "reset":
        os.system("clear")
        os.system("python3 init.py")
    elif i.lower() == "clear":
        os.system("clear")
        print(f"{welcome}\n{ver}\n\n")
    elif i.lower() == "apps":
        print(f"Apps:\nBASH")
    elif i.lower() == "bash":
        print("Type 'EXIT' to exit BASH")
        pr = "$"
        while True:
            o = input(f"BASH {pr} ")
            if not o.lower() == "exit":
                os.system(o)
            else:
                break
        
