#!/usr/bin/python
import sys
import os, fnmatch
import shutil
import time
from pysphere import VIServer

ip="10.45.86.152"
user="root"
pw="Cmv5@rootVM%"
System_name="T001"
attempt ="NO"

#need to add option to run the script ( create snapshot/revert to snapshot )


server=VIServer()
server.connect(ip,user,pw)


vms=server.get_registered_vms()

mm=1
newdic={}
for vm in vms:
     if System_name in vm:
     	dd=vm
     	newdic[mm]=dd
     	mm=mm+1

for k, v in newdic.iteritems():
    print k ,  v



cur_mvs=[]
cur_mvs=raw_input("please enter mvs  list you want to creat snapshots. sepetered by space : ")

cur_mvs_list=map(int,cur_mvs.split())

print "vms to snap: ", cur_mvs

print cur_mvs_list
print "*********************************************"
print "this are the vms you selected: "

for i in cur_mvs_list:
	print newdic[i]

print "**********************************************"

goon=raw_input("Press Enter to Continue")

if goon !="":
	print  "you didn't write  ... aboring"
	sys.exit("some error message")



def get_status(vm_path):
	vm1=server.get_vm_by_path(vm_path)
	s= vm1.get_status(basic_status=True)
	print vm_path ,"is",  vm1.get_status(basic_status=True)
	return s


def get_prop(vm_path):
	vm1=server.get_vm_by_path(vm_path)
	print vm1.get_property('ip_addresses')


def get_snpst(vm_path):
	vm1=server.get_vm_by_path(vm_path)
	snp_list=vm1.get_snapshots()
#	print snp_list
	for snp in snp_list:
		print snp.get_name()
		sh=snp.get_name()
		return sh


def shut_down_guest(vm_path):
	vm1=server.get_vm_by_path(vm_path)
	vm1.shutdown_guest()
	print "shuting down guest of ", vm_path	
	attempt="yes"
	return attempt

def power_on_vm(vm_path):
	vm1=server.get_vm_by_path(vm_path)
	print "powering on vm : ", vm_path
	vm1.power_on()

def revert_to_snapshot(vm_path,snap_name):
	vm1=server.get_vm_by_path(vm_path)
	vm1.revert_to_named_snapshot(snap_name)
	

for i in cur_mvs_list:
	attempt="no"
	ii=newdic[i]
	s=get_status(ii)
	snp=get_snpst(ii)
	print "******snapshot name is :" , snp
	print "status **************** ", s
	for i in range(1,4):
		s=get_status(ii)
		print "status within loop is : *********************" , s
		if "ON" in s:
			if attempt=="yes":
				time.sleep(20)
				continue
			else:
				print "powering off VM"
# shuting down guest if its powered on and creat_snap is es
			
	        		shut_down_guest(ii)
				print "shutingdown guest"
				time.sleep( 30 )
				attempt="yes"   #***** flag to avoid trying to to stop the VM again*****
				print "**************** this is attempt : ", attempt
		elif "OFF" in s:	
			revert_to_snapshot(ii,snp)			
			print "*************",ii, "was reverted to snapshot ",snp 
			break 
