#!/usr/bin/python

__author__ = 'ido levy'

import sys
import os
from optparse import OptionParser
import subprocess

allow_ips=["10.45.100.214","10.45.112.214"]
blockcommad="iptables -A INPUT -p tcp --dport 22 -j REJECT"
eth0_rule="iptables -A INPUT -i eth0 -p tcp --dport 22 -j ACCEPT"
eth1_rule="iptables -A INPUT -i eth1 -p tcp --dport 22 -j ACCEPT"



output = subprocess.check_call(eth0_rule , stdout=subprocess.PIPE, shell=True)
if output == 1:
    print "eth0 rule added "
    
output=output = subprocess.check_call(eth1_rule , stdout=subprocess.PIPE, shell=True)
if output == 0:
    print "eth1 rule added " 
    
for ip in allow_ips:
    ipaddcommand = "iptables -A INPUT -p tcp -s {0} --dport 22 -j ACCEPT".format(ip)
    pipe = subprocess.check_call(ipaddcommand, stdout=subprocess.PIPE, shell=True)
    if pipe  == 0:
        print "rule for ip", ip,  "was  added "   
    
output = subprocess.check_call(blockcommad , stdout=subprocess.PIPE, shell=True)
if output == 0:
    print "block  rule added "
    
    
print "*******************script ended***************************"
