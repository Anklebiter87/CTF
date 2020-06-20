import os
import platform
from shlex import quote
from stat import S_IRWXU
from shutil import copy, move
from subprocess import Popen, PIPE


class Base():
    def __init__(self, base=None):
        self.newchallengeitems = ['exploit.py']
        self.newchallengedirs = ['ghidra', 'writeup']
        self.python_modules = ['pip','pwntools']
        self.packages = ['python3-pip', 'python3-dev', 'git', 'libssl-dev', 
                'libffi-dev']
        self.basedir = base

    def _copy_items(self):
        for i in self.newchallengeitems:
            path = os.path.join(self.basedir, 'utils', i)
            copy(path, '.')
            os.chmod(i, S_IRWXU)
    
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
        newdir = os.path.join(self.basedir, newprojectdir)
        os.mkdir(newdir)
        return newdir
    
    def newchallenge(self, newchallengepath):
        temp = "_temp-new"
        dirname = os.path.basename(newchallengepath)
        os.mkdir(temp)
        move(newchallengepath, os.path.join(temp,dirname))
        os.chdir(temp)
        self._make_new_dirs()
        self._copy_items()
        os.chdir('../')
        move(temp, dirname)
        return dirname

class Windows(Base):
    def __init__(self, base):
        Base.__init__(self, base)


class Linux(Base):
    def __init__(self, base):
        Base.__init__(self, base)

    def add_to_git(git_item, comment):
        cmd = quote(f"git add {git_item}")
        proc = self.execute_cmd(cmd)
        cmd = quote(f"git commit -m '{comment}'")
        proc = self.execute_cmd(cmd)

def check_os(basedir):
    os = platform.system()
    if os == 'Windows':
        os = Windows(basedir)
    else:
        os = Linux(basedir)
    return os
