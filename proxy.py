import yaml
import  subprocess
import datetime
import re
import sys


ips=[]
mydic={}
log_file="proxy.log"
n = datetime.datetime.now()





def status(my_ip):
     command=["curl  -s -w '\n\n\nTotal time:\t%{time_total}'"," -x  http://%s:3128 'https://prpc-helloworld.appspot.com/' -H 'pragma: no-cache' -H 'accept-encoding: gzip, deflate, sdch, br' -H 'accept-language: en-US,en;q=0.8' -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'cache-control: no-cache' -H 'authority: prpc-helloworld.appspot.com' --compressed" % my_ip]
     ex_command=''.join(map(str, command))
     pipe = subprocess.Popen(ex_command, stdout=subprocess.PIPE, shell=True)
     #pipe = subprocess.check_output(ex_command,shell=True).communicate()
     #output = pipe.stdout.read()
     output=pipe.communicate()
     excode=pipe.returncode
     if excode > 0:
         raise ValueError(excode)
         #print str(excode)


     for line in output:
         print line







# needto check  curl -s -w '%{time_total}\n' -o /dev/null https://prpc-helloworld.appspot.com


my_file="proxy.yaml"
l=open(log_file,'a')
with open('proxy.yaml') as f:
    conf=yaml.load(f)
    err_count = 0
for i  in  conf:
    my_country = i.get('country')
    my_ip = i.get('ip')
    print "*************************** checking the connection to ", my_country , "server, with ip" , my_ip, "**********************************"
    try:
        status(my_ip)
    except Exception :
        print "******error occured  on  ", my_country ," server "
        l.write(' '.join(( str(n), 'error occured  on  ', str(my_country), 'server with IP', my_ip, '\n')))
        err_count+=1
        print err_count


    else:
        print "server", my_country , " is OKAY, thanks! "
        l.write(' '.join((str(n), 'server  ', str(my_country), 'is OKAY!!! \n')))
        # #adding check the time
        # for line in open(check, 'r'):
        #     if re.search(real,line):
        #         print line


print  "***** number of errors : " ,  err_count ,  "***************************"
l.close()




