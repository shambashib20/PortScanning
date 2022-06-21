import socket 
from IPy import IP
import threading

ports = []  # to store open ports
banners = [] # to store open port banner

def port_scanner(target,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            target_ip = IP(target) # check if target is an IP address
        except:
            target_ip = socket.gethostbyname(target)  #check if the target is a domain name or localhost
        

        s.connect((target_ip, port))
        try: 
            #get banner name
            banner_name = banner(s).decode()
            ports.append(port)

            #store banner_name in banners list
            banners.append(banner_name.strip())
        except:
            pass
    except:
        pass

# get the banner name
def banner(s):
    return s.recv(1024)

# scan for the first 5051 ports
for port in range(1, 5051):
    thread = threading.Thread(target= port_scanner, args=[target, port])
    thread.start()

with open("vulnerable_banners.txt", "r") as file:
    data = file.read()
    for i in range(len(banners)):
        if banners[i] in data:
            print(f"[!] Vulenrablity found: {banners[i]} on port {ports[i]}")
