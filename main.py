import requests#
import os, sys
try:
    from colored import fg
    color = fg("dark_slate_gray_1")
except ImportError:
    color=""

PRINT_DATA = True
UNCLAIMED = "unclaimed.txt"

def clear():
    if sys.platform=="win32":
        os.system("cls")
        os.system("title Gittify - Akiko#4200")
    else:
        # Program's name comes on by default
        os.system("clear")


def _end(big=False):
    if big is True:
        print_c("\n||=======================================>\n")
    else:
        print_c("\n||--------------------------------------->\n")
 

def print_c(string):
    if PRINT_DATA is True:
        print(string)
    return


def banner():
    return print(color + """

 ██████╗ ██╗████████╗████████╗██╗███████╗██╗   ██╗
██╔════╝ ██║╚══██╔══╝╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
██║  ███╗██║   ██║      ██║   ██║█████╗   ╚████╔╝ 
██║   ██║██║   ██║      ██║   ██║██╔══╝    ╚██╔╝  
╚██████╔╝██║   ██║      ██║   ██║██║        ██║   
 ╚═════╝ ╚═╝   ╚═╝      ╚═╝   ╚═╝╚═╝        ╚═╝   
                                                  
                | Akiko#4200 |
""")




def main():
    if not os.path.exists(UNCLAIMED):
        f = open(UNCLAIMED,"w")
        f.close()
    
    
    namefile = input("[*] Enter Wordfile: ")
    _end(big=True)
    try:
        with open(namefile,"r") as fp:
            final_list = fp.read().split("\n")
    except FileNotFoundError:
        sys.exit(f"[!] {namefile} was not found!")

    available = []
    non = []
    unknown = []
    for n in final_list:
        n = n.strip()
        try:
            r = requests.get("https://github.com/{}".format(n),timeout=3)
        except:
            _end()
            sys.exit("\n[!] A good internet connection is requied!")
        if r.status_code==404:
            print_c("  [+] {} is available!".format(n))
            with open(UNCLAIMED, "a") as f:
                f.write(f"{n}\n")
            available.append(n)
        elif r.status_code==200:
            print_c(f"  [-] {n.strip()} is taken...")
            non.append(n)
        else:
            print_c(f"  [?] {n} - Unknown response {r.status_code}")
            unknown.append(n)
    
    _end()
    print(f"  [+] {len(available)} names are available!")
    print(f"  [-] {len(non)} names are taken!")
    print(f"  [?] {len(unknown)} names returned an invalid response!")
    print(f"  [*] Total of {len(available)+len(non)+len(unknown)} names checked!")
    _end()
    print("[+] All available names saved in {}".format(UNCLAIMED))
    _end()
    input("[*] Press [ENTER] to exit...")
    
    
    
if __name__=="__main__":
    try:
        clear()
        banner()
        main()
    except KeyboardInterrupt:
        sys.exit("\n[!] KEYBOARD INTERRUPT!")
