import requests, os, threading, random, time
from colorama import Fore, Back, Style
from pystyle import Colors, Colorate, Center

clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
users = open('check.txt', 'r').read().split('\n')
count = 0
proxyDebug = False
os.system(f"title Tiktok Username Checker - Starting...")
clear()

# Vanity Generator Logo
logo = """
████████╗██╗██╗░░██╗████████╗░█████╗░██╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
╚══██╔══╝██║██║░██╔╝╚══██╔══╝██╔══██╗██║░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
░░░██║░░░██║█████═╝░░░░██║░░░██║░░██║█████═╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
░░░██║░░░██║██╔═██╗░░░░██║░░░██║░░██║██╔═██╗░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
░░░██║░░░██║██║░╚██╗░░░██║░░░╚█████╔╝██║░╚██╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
░░░╚═╝░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝"""

def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

def check():
    global count
    session = requests.Session()
    while True:
        for line in users:
            proxy = random.choice(open("proxies.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
            if proxyDebug == True:
                print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.GREEN}{proxyDict}{Fore.RESET}")
            else:
                pass
            r = session.get(f'https://www.tiktok.com/@{line}', headers={'Connection': 'keep-alive', 'User-Agent': 'TikTok 25.7.4 rv:174014 (iPhone; iOS 16.0; sv_SE) Cronet'}, timeout=60)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Free: " + line)
                with open ("free.txt", "a") as f:
                    f.write(line + "\n")
                    count += 1
            elif r.status_code == 404:
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Taken: "+ line)
                with open ("taken.txt", "a") as f:
                    f.write(line + "\n")
                    count += 1
            elif r.status_code == 429:
                print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}] {Fore.RESET}Ratelimited: " + line + ". Sleeping for 30 seconds...")
                with open ("ratelimited.txt", "a") as f:
                    f.write(line + "\n")
                    count += 1
                time.sleep(30)
            else:
                print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}] {Fore.RESET}Error: " + line)
                with open ("error.txt", "a") as f:
                    f.write(line + "\n")
                    count += 1
            os.system(f"title Tiktok Username Checker - Checked {count}/{len(users)} - Remaining: {len(users)-count}")


clear()
printLogo()
print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Found {Fore.GREEN}{len(users)}{Fore.RESET} accounts to check.")
try:
    while True:
        check()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting. If it keeps, just close the program.")
    os.system(f"title Tiktok Username Checker - Exiting. If it keeps, just close the program.")
    time.sleep(1)
    exit()