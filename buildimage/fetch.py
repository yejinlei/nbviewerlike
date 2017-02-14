#coding:UTF-8
import sys, os, subprocess, fcntl, struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

class Fetch(object):
    def __init__(self):
        self.url = r'https://github.com/{}/{}.git'
        self.workdir = r'/root/tmp'

    def fetch_notebook(self, name, pro):
        try:
            os.mkdir(self.workdir)
            os.chdir(self.workdir)
            child = subprocess.Popen('git clone {} .'.format(self.url.format(name, pro)), shell=True, universal_newlines=True)
            child.wait()
        except Exception:
            return False
        else:
            return True
