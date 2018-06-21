import re
import os
import socket

def get_ip():
    '''retrieve local ip'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def hostname_to_IP(device):
    '''issue arp -a and return ip address of specified hostname'''
    scan = None
    f = os.popen('arp -a')
    for line in f.readlines():
        if device in line:
            scan = line
            break
    denji_ip = re.search('\(([^)]+)', scan).group(1)
    is_valid = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", denji_ip)
    if is_valid:
        return denji_ip
    else:
        return 0