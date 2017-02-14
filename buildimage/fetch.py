#coding:UTF-8
import sys, os, subprocess

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
