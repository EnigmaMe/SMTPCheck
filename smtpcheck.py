#SMTPCheck Developed by @BeefOverflow
import smtplib
print("SMTPCheck - Checks the authenticity of SMTP credentials against a host")
host = raw_input("\nEnter your hostname (Example: domain.net:587):\n")
username = raw_input("Enter your username:\n")
password = raw_input("Enter your password\n")
print("\n[*] Connecting to SMTP Server")
server = smtplib.SMTP(host)
print("\033[33mConnected with the following:\n")
print "\033[32mHostname: ", host
print "\nUsername: ", username
print "\nPassword: ", password
print("\n\033[31m[*]SERVER RESPONSE:\033[0m\n")
print(server.login(username,password))
server.quit()
