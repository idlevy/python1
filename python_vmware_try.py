from pysphere import VIServer

def connect_to_server(ip,user,pw):
	server=VIServer()
	server.connect(ip,user,pw)
	try:
		server.is_connected()
		


from pysphere import VIServer
server=VIServer()
server.connect("10.45.86.152","root","Cmv5@rootVM%")
vms=server.get_registered_vms()
vms



def get all hostnames(System_name)
	for vm in vms:
		vms=server.get_registered_vms()
		if System_name in vm:
             vm1=server.get_vm_by_path(vm)
             print vm1.get_property('hostname')
			 
			 
 
mvas-omu-app1a
smsc-sfe4
smsc-sfe3
smsc-cdrpp2
smsc-cdrpp1
smsc-sfe1
mvas-omu-db1a
smsc-sem1
mvas-omu-db1b
smsc-sem2
smsc-mre1
smsc-mre2
smsc-map1
mvas-omu-app1a
smsc-map2
mvas-omu-app1b
smsc-sfe2
smsc-mre3