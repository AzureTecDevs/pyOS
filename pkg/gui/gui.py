import os
i = input("GUI Mode: tkinter, qt\n> ")
c = os.getcwd()
if i.lower() == "qt":
    os.system(f"python3 {c}/pkg/gui/qt.py")
else:
    os.system(f"python3 {c}/pkg/gui/tk.py")
