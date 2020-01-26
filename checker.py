#!/usr/bin/python3
import sys
import telnetlib
import socket

def check_port(ip):
  print("[-] Scanning %s at 23/TCP"  %(ip))
  address=(ip,23)
  s_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s_connection.settimeout(0.6)
  return s_connection.connect_ex(address)

info=open('creds','r')
timeout=2
log=open('log','a')
for line in info:
  payload=line.split(':')
  if len(payload) == 3:
    HOST=line.split(':')[0]
    user=line.split(':')[1]
    password=line.split(':')[2].replace('\n','')
    if check_port(HOST) == 0:
      string="[!] Hostname: %s is UP." %(HOST)
      print("\t[-] Testing Username:%s Password:%s" %(user,password))
      try: 
        tn=telnetlib.Telnet(HOST,timeout)
        print('login')
        tn.read_until("login: ")
        tn.write(user + "\n")
        print('password')
        tn.read_until("Password: ")
        tn.write(password + "\n")
        print('command')
        tn.write("id"+'\n')
        tn.write("exit\n")
        log.write(string+'\n')
        print(tn.read_all())
      except Exception as error: 
        print("Error: %s" %(error))
        continue
    else: 
#    print("[!] %s 23/TCP CLOSED" %(HOST))
      pass
  else:
    pass
