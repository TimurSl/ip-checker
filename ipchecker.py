from random import randint
import os
import socket


def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0


#and then check the response...
f = open("ipservers.txt", 'w')

while True:
    checkip = str(randint(1,255)) + "." + str(randint(1,255)) + "." + str(randint(1,255)) + "." + str(randint(1,255))

    hostname = str(checkip)
    # response = os.system("ping -c 1 " + hostname)
    response = ping(hostname)

    if response == True and isOpen(hostname, 25565) == True:
        print(hostname + "is Minecraft java server!")
        f.write(hostname + "\n")