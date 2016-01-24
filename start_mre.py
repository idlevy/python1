#!/usr/bin/python


__author__ = 'idlevy'

import os
import subprocess
import shutil
import time
import sys
from ido import check_monitor

startm=u'su - smsc -c startm'
file1='/home/smsc/site/trace/MRE/start_MRE.1.1.log'
FNULL='/dev/null'


a=check_monitor('monitor')
print a
pname = a[1]
if a[0] == 1:
        print pname +" is down"
else:
	#to remove after testing.
	tmpProc=subprocess.call('su - smsc -c stopm',shell=True)
	print 'stoping monitor process'
	time.sleep(15)



print "reset log file and starting monitor process"
shutil.copy(FNULL,file1)
proc=subprocess.Popen(startm,shell=True,stdout=subprocess.PIPE)
time.sleep(10)


#verifying MRE is up
w=open(file1,'r')
t=1
'''for line in w:
        if 'MRE Started' in line:
           print('unit started succesfuly')
           break
        else:
           time.sleep(0.05)
	   t=t+1
	   if t == 5:
	 	print t
		print  ' mre is not up  after seconds \n'
  		print ' please check logs'
		t = 100
		sys.exit(1)'''
log=w.readlines()
tail = log[:-3

w.close()

z=open(file1,'r')
line1=z.readlines()
print line1[-1]
