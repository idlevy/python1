import fileinput
import datetime
import sys
import re
import os
import subprocess



today=datetime.datetime.today().isoweekday()+1
weekend_oncall="matan"
ticks={}



def new_ocall(today):
    if today == 7: #Sunday
        new_oncall="ido"
    elif today == 1: #monday
        new_oncall="yariv"
    elif today == 2: #tuesday
        new_oncall = "nir"
    elif today == 3: #wednsday
        new_oncall = "matan"
    elif today == 4: #thursday
        new_oncall = "guy"
    else: #friday-suterday
        new_oncall = weekend_oncall
    return  new_oncall


def myfile(path):
    flist=list()
    for (dirname, dirs, files)  in os.walk(path):
        for filename in files:
            if filename.endswith('.tick'):
                thefile=os.path.join(dirname,filename)
                flist.append(thefile)
                ticks[filename] = thefile #new
   # return flist
    return ticks #new



new_oncall = new_ocall(today)
print "todays on-call is:" , new_oncall
print today


def replaceAll(file):
    found = False
    for line in fileinput.input(file, inplace = 1):
        if "replace" in line:
            oncall = (re.search(r"([a-z]*)", line.split("_", 1)[1])).group()
            line = line.replace(oncall , new_oncall )
            found = True
        sys.stdout.write(line)
    return found



new_oncall = new_ocall(today)

a=myfile("./critical-alerts")
for k,v in a.iteritems():
    checkme=replaceAll(v)
    tickname= k.split(".")[0]
    filename=v
    r=open(v,'r')
    if checkme is True: # check if file should be chnaged.
        for line in r:
            if "|query" in line:
                w=re.findall(r"[\w']+", line)
                command="kapacitor define %s -tick %s   -dbrp %s.%s -type batch" % (tickname, filename,w[6],w[7])
                print  "following command is about to be run: ", command
                pipe=subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
                output = pipe.communicate()
                excode = pipe.returncode
                print excode, output
                break





