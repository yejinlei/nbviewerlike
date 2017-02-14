#coding:UTF-8
import sys, os, socket, subprocess
from fetch import *

hostaddr = get_ip_address('eth0')

def startnotebook(port):
    cmd_var = r'jupyter notebook --no-browser /root/tmp --ip={} --port={} --notebook-dir=/root/tmp --NotebookApp.token=""'.format(hostaddr, port)
    child = subprocess.Popen(cmd_var, shell=True, universal_newlines=True)
    child.wait()

if __name__ == "__main__":
    if sys.argv[2] == 'download':
        Fetch().fetch_notebook(sys.argv[3], sys.argv[4])
        startnotebook(sys.argv[1])
    elif sys.argv[2] == 'create':
        os.makedirs('/root/tmp')
        startnotebook(sys.argv[1])
    else:
        pass
