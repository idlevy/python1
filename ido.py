
#!/usr/bin/python

import subprocess
import os.path
import sys
import shutil
import datetime
import re
from optparse import OptionParser



stopm=u'su - smsc -c stopm'
FNULL = open(os.devnull, 'w') #fwd out put  of command to /dev/null

def gethost():
    command = u'hostname'.format()
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    host=pipe.stdout.read().rstrip('\n')
    return host

def check_monitor(pname = 'monitor'):
    if pname == 'monitor':
        mCommand= u'ps -ef |pgrep ' +  pname
        t=subprocess.call(mCommand, shell=True,stdout=FNULL)
        return (t,pname)
#   if pname == omni:
#       mCommad =u'ps -ef |pgrep -i omni'
