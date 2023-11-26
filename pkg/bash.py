import os
print("Type 'EXIT' to exit BASH")
pr = "$"
while True:
    o = input(f"BASH {pr} ")
    if not o.lower() == "exit":
        os.system(o)
    else:
        break
