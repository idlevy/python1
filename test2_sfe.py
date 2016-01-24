#!/usr/bin/python

import subprocess
import os.path
import sys
import shutil
import datetime
import re
from optparse import OptionParser



stopm=u'su - smsc -c stopm'
startm=u'su - smsc -c startm'
stop_omni=u'su- smsc -c Terminate 0'
start_omni=u'su- smsc -c go.nored &'

 
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
    if pname == omni:
    	mCommad =u'ps -ef |pgrep -i omni'

def check_cluster():
	return os.path.isdir('/opt/VRTS/bin')


def get_vsfe(my_host):
	b=my_host
	scommnad=u'hastatus -sum |grep '+ my_host + '|grep ONLINE|grep vsfe' 
	return scommand

my_host=gethost()
print my_host

e=get_vsfe('smsc')
print e


#stoping process
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
if (re.search('.+sfe.+',my_host)):
	print "this  is SFE Unit. checking if Vertas exist"
	
tt=check_cluster()

