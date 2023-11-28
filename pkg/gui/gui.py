import os
i = input("GUI Mode: tkinter, qt")
if i.lower() == "qt":
    os.system("python3 pkg/gui/qt.py")
else:
    os.system("python3 pkg/gui/tk.py")
