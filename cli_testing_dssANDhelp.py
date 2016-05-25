#!/usr/bin/python

__author__= " VIVEK SHARMA "

import os
import sys
import re
import string
import time
import ConfigParser
import datetime
###from update import update1
from modulecomputeids import *
from modulevpcids import *

 
ts=datetime.datetime.now()
date =  time.strftime("%Y/%m/%d") ; 
print ts

## DSS ## 
dssf=0
dssp=0
with open('dss', 'r') as f:

        commands = f.readlines()
        print commands
        for command in commands:
                command = command.strip("/n")
                print command
                ret = os.system(command + "> /dev/null 2>&1")
                if ret !=0:
                        print 'fail of command'
			dssf = dssf + 1
###			update1(date,command[4:40] ,  'f', 'dss')
                else:
###			update1(date,command[4:40] ,  'p', 'dss')
                        print 'pass of command'
			dssp = dssp + 1


## HELP FOR ALL SERVICES ##
helpf=0
helpp=0
with open('help', 'r') as f:
        commands = f.readlines()
#        print commands
        for command in commands:
                command = command.strip("/n")
#                print command

                ret = os.system(command)

                if ret !=0:
                        print 'fail of command'
			helpf = helpf + 1 
###			update1(date,command[4:40] ,  'f', 'dss')
                else:
			helpp = helpp + 1
                        print 'pass of command'
###			update1(date,command[4:40] ,  'p', 'help')

tf=datetime.datetime.now()
print tf
te = (tf - ts).total_seconds() 

''''
totalf=dssf+vpcf+iamf+computef+helpf
totalp=dssp+vpcp+iamp+computep+helpp
total=totalf+totalp
print "-------------------------------------------------------------------"
print "########### summary ##########"
print "Testing started : " , ts 
print "Total no of CLI requests = %d "%(total)
print "No of CLI request failed = %d "%(totalf) 
print "No of CLI request passed = %d "%(totalp)
print "Testing completed : " , tf
print "Total time taken to test = %d seconds "%(te)
print "############# END ###########"
print "-------------------------------------------------------------------"
'''

if __name__ == '__main__':
    print "x"

