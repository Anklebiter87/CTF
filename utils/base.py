import os
import platform
from shutil import copy

class Base():
    def __init__(self, base=None):
        self.newchallengeitems = ['']
        self.newchallengedirs = ['ghidra']
        self.basedir = base
        if base:
            self.ctfdir = os.path.join(self.basedir, "CTF")
        else:
            self.ctfdir = "CTF"

    def _copy_items(self):
        for i in self.newchallengeitems:
            path = os.path.join(self.ctfdir, 'utils', i)
            copy(path, '.')
    
    def _make_new_dirs(self):
        for i in self.newchallengedirs:
            os.mkdir(i)

    def newctf(self, newprojectdir):
        os.curdir
        newdir = os.path.join(self.ctfdir, newprojectdir)
        os.mkdir(newdir)
    
    def newchallenge(self, newchallengesetup):
        os.mkdir(newchallengesetup)
        os.chdir(newchallengesetup)
        self._make_new_dirs()
        self._copy_items()


class Windows(Base):
    def __init__(self, base):
        Base.__init__(self, base)


class Linux(Base):
    def __init__(self, base):
        Base.__init__(self, base)


def check_os():
    os = platform.system()
    if os == 'Windows':
        os = Windows()
    else:
        os = Linux()
    return os