#!/usr/bin/python3

import cgi 
import subprocess


print("content-type: text/html")
print()

f= cgi.FieldStorage()
cmd = f.getvalue("x")

if("run" in cmd ) or ("launch" in cmd ): 
    print(subprocess.getoutput("sudo docker run -d --name test centos:latest"))
elif("stop" in cmd ): 
    print(subprocess.getoutput("sudo docker stop test")
elif("download" in cmd ) or ("pull" in cmd ):
    print(subprocess.getoutput("sudo docker pull centos:latest)
elif("terminate" in cmd ) or ("remove" in cmd):
    print(subprocess.getoutput("sudo rm test") 
elif("show" in cmd) or ("images" in cmd):
    print(subprocess.getoutput("sudo docker images")
else: 
    print("please wait for this feature we are working on it :")
