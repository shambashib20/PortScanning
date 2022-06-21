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
    
    