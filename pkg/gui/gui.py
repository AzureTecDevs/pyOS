import os
i = input("GUI Mode: tkinter, qt")
if i.lower() == "qt":
    os.system("python3 qt.py")
else:
    os.system("python3 tk.py")
