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
#    	mCommad =u'ps -ef |pgrep -i omni'
my_host=gethost()
print my_host

def stop():
	print "mmmmmm"

if (re.search('.+mre.+',my_host)) or (re.search('.+sem.+',my_host)):
    print " this is Router(MRE) Unit"
    t=check_monitor('monitor')
    Mypname=t[1]
    print Mypname
    if t[0] == 0:
	a=Mypname
	print "{0} process is up and running".format(a)
        startp=subprocess.Popen(stopm, shell=True,stdout=FNULL)
        startp.wait()
        print "monitor process stoped on " +  my_host
    else:
       a=Mypname
       print '{0} process is down on '.format(a) +  my_host +': nothing to do'
