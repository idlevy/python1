import sys
import yaml
import json
import  subprocess


ips=[]
mydic={}




def status(my_ip):
    command = "time curl -x http://%s:3128 'https://prpc-helloworld.appspot.com/' -H 'pragma: no-cache' -H 'accept-encoding: gzip, deflate, sdch, br' -H 'accept-language: en-US,en;q=0.8' -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'cache-control: no-cache' -H 'authority: prpc-helloworld.appspot.com' --compressed" % my_ip
    #pipe = subprocess.check_output(command, stdout=subprocess.PIPE, shell=True)
    pipe = subprocess.check_output(command,  shell=True)



my_file="proxy.yaml"
with open('proxy.yaml') as f:
    conf=yaml.load(f)
    err_count = 0
for i  in  conf:
  #  print i
    mydic=i
    #print i
  #  print i.get('country')," : " ,i.get('ip')
    my_country = i.get('country')
    my_ip = i.get('ip')
    print "*************************** checking the connection to ", my_country , "server, with ip" , my_ip, "**********************************8"
    try:
        status(my_ip)
    except Exception :
        print "******error occured  on  ", my_country ," server *********"
        err_count+=1
        print err_count
    else:
        print "server", my_country , " is OKAY, thanks! "
print  "***** number of errors : " ,  err_count ,  "***************************"





