import os
import termcolor as tc
import term as t
from time import sleep
import requests
import ext
import platform
os.system("clear")
t.write("█")
sleep(2)
os.system("clear")
welcome = tc.colored("Welcome to pyOS!", "blue")
tx = "(c) 2023 AzureTecDevs"
ver = tc.colored(f"Version 1.0.0 {tx}", "dark_grey")
print(f"{welcome}\n{ver}\n\n")
while True:
    i = input("$ ")
    try:
        if i.lower() == "python":
            os.system("python3")
        elif i.lower() == "help":
            print("""python  : Run Python            apps   : Open apps
exit    : Exit pyOS            reset   : Restart current session
clear   : Clear screen         pkg     : Install package
pkg run : Run package          pkg info: Get package info""")
        elif i.lower() == "reset":
            os.system("clear")
            os.system("python3 init.py")
        elif i.lower() == "pkg ins":
            z = input("Package Name: ")
            p = platform.linux_distribution()
            if p.lower() in ("fedora","debian"):
                os.system(f"python3 pkg/{z}/install/deb.py")
            else:
                os.system(f"python3 pkg/{z}/install/reg.py")
        elif i.lower() == "clear":
            os.system("clear")
            print(f"{welcome}\n{ver}\n\n")
        elif i.lower() == "apps":
            print(f"Apps:\nBASH")
        elif i.lower() == "pkg":
            z = input("Package Name: ").lower()
            if not os.path.exists(f'pkg/{z}'):
                os.mkdir(f'pkg/{z}')
            url = f'https://raw.githubusercontent.com/AzureTecDevs/pyOS/packages/pkg/{z}/{z}.py'
            r = requests.get(url, allow_redirects=True)
            open(f'pkg/{z}/{z}.py', 'wb').write(r.content)
            url = f'https://raw.githubusercontent.com/AzureTecDevs/pyOS/packages/pkg/{z}/about'
            r = requests.get(url, allow_redirects=True)
            open(f'pkg/{z}/about', 'wb').write(r.content)
        elif i.lower() == "pkg run":
            z = input("Package Name: ").lower()
            os.system(f'python3 pkg/{z}/{z}.py')
        elif i.lower() == "pkg info":
            z = input("Package Name: ").lower()
            f = ext.readFile(f'pkg/{z}/about')
            print(f'Description: {f[0]}\nAuthor: {z[1]}\nVersion: {f[0]}')
        elif i.lower() == "bash":
            os.system('python3 pkg/bash/bash.py')
    except:
        print('Fatal Error')
