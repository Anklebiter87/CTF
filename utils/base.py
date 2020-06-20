import os
import platform
from shutil import copy
from subprocess import Popen, PIPE

class Base():
    def __init__(self, base=None):
        self.newchallengeitems = ['challenge.py']
        self.newchallengedirs = ['ghidra']
        self.python_modules = ['pip','pwntools']
        self.packages = ['python3-pip', 'python3-dev', 'git', 'libssl-dev', 
                'libffi-dev']
        self.basedir = base

    def _copy_items(self):
        for i in self.newchallengeitems:
            path = os.path.join(self.ctfdir, 'utils', i)
            copy(path, '.')
    
    def _make_new_dirs(self):
        for i in self.newchallengedirs:
            os.mkdir(i)

    def installer(self):
        pass
    
    def execute_cmd(self, cmd):
        proc = Popen(cmd, stdin=PIPE, stdout=PIPE)
        proc.wait()
        return proc.returncode

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


def check_os(basedir):
    os = platform.system()
    if os == 'Windows':
        os = Windows(basedir)
    else:
        os = Linux(basedir)
    return os
