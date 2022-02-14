# Docker-webapp-with-python-cgi

STEP 1

# install and start  httpd service  
#yum install httpd -y
#systemctl start httpd

STEP 2

# put the python file in -> /var/www/cgi-bin
# put html file in -> /var/www/html

STEP 3
STOP FIREWALLD #systemctl stop firewalld 
set SELINUX -> permissive #setenorce 0
 
