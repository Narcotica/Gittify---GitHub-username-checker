import requests#
import os
from colored import fg
color = fg("dark_slate_gray_1")
os.system("title Gittify - Akiko#4200")

print(color + """

 ██████╗ ██╗████████╗████████╗██╗███████╗██╗   ██╗
██╔════╝ ██║╚══██╔══╝╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
██║  ███╗██║   ██║      ██║   ██║█████╗   ╚████╔╝ 
██║   ██║██║   ██║      ██║   ██║██╔══╝    ╚██╔╝  
╚██████╔╝██║   ██║      ██║   ██║██║        ██║   
 ╚═════╝ ╚═╝   ╚═╝      ╚═╝   ╚═╝╚═╝        ╚═╝   
                                                  
Akiko#4200
""")

file = open("unclaimed.txt", "w")
file.write("")
filename = input("Enter Wordfile (with.txt)\n>")
filepath = filename
print("""

""")

with open(filepath) as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        r = requests.get("https://github.com/nikhilweeddde")
        r2 = requests.get("https://github.com/" + line.strip())

        if r2.text == r.text:
            print("[+] " + str(line.strip()))
            filewrite = open("unclaimed.txt", "a")
            filewrite.write("https://github.com/" + line.strip() + "\n")
        else:
            print("[-]" + str(line.strip()))
    print("Unclaimed names saved in unclaimed.txt")
    input("Press ENTER to close...")
