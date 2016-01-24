#!/usr/bin/python

import subprocess
import os.path
import sys
import shutil
import datetime
import re
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-o", "--option", dest="option",help="Choose option", metavar="<stop/start>")
(options, args) = parser.parse_args()


if options.option == 'start':
	print 'aaaaa'
if options.option == 'stop':
	print 'bbbbb'
	
'''
stopm=u'su - smsc -c stopm'
FNULL = open(os.devnull, 'w') #fwd out put  of command to /dev/null
a='smsc'
os.chdir('/var/tmp')
root_dir = os.path.expanduser(os.path.join('~smsc', 'site/config/'))
archive_name = os.path.expanduser(os.path.join('~','/var/tmp/backup_smsc'))
print archive_name
print root_dir
make_archive(archive_name,'gztar',root_dir)
'''
