'''
Created on Jul 6, 2017

@author: girish
'''
import getpass
import telnetlib
import os

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")

if password:
    tn.read_until(b"Password: ")

pipe = os.popen("dir","w") 
print (pipe)

