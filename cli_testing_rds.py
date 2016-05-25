#!/usr/bin/python

__author__= " VIVEK SHARMA "

import os
import sys
import re
import string
import time
import ConfigParser
import datetime
from subprocess import Popen, PIPE, STDOUT
import subprocess
import random

###from update import update1
from modulevpcids import *
from modulecomputeids import *
from moduleiamids import *


ts=datetime.datetime.now()
date =  time.strftime("%Y/%m/%d") ;
#print ts


def test_create_delete_rds():

    masterusername = "master"
    masteruserpassword = "masterpass"
    allocatedstorage = "20"
    dbinstanceidentifier = "testdb"
    dbsnapshotidentifier = "testdb"

    cmd1 = "jcs rds create-db-instance --db-instance-identifier "+dbinstanceidentifier+" --db-instance-class c1.small --engine MySQL --allocated-storage "+str(allocatedstorage)+" --master-username "+masterusername+" --master-user-password "+masteruserpassword
    print cmd1
    p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command1out = p1.stdout.read()
    print command1out
    p1.wait()
    ret =  p1.returncode
    responsecapture(ret,cmd1)

    time.sleep(240)

    cmd2 = "jcs rds create-db-snapshot --db-instance-identifier "+dbinstanceidentifier+" --db-snapshot-identifier "+dbsnapshotidentifier
    print cmd2
    p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command2out = p2.stdout.read()
    print command2out
    p2.wait()
    ret =  p2.returncode
    responsecapture(ret,cmd2)

    time.sleep(240)

    cmd3 = "jcs rds describe-db-instances"
    print cmd3
    p3 = Popen(cmd3, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command3out = p3.stdout.read()
    print command3out
    p3.wait()
    ret =  p3.returncode
    responsecapture(ret,cmd3)


    cmd4 = "jcs rds describe-db-snapshots"
    print cmd4
    p4 = Popen(cmd4, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command4out = p4.stdout.read()
    print command4out
    p4.wait()
    ret =  p4.returncode
    responsecapture(ret,cmd4)

    cmd5 = "jcs rds delete-db-instance --db-instance-identifier "+dbinstanceidentifier+" --skip-final-snapshot"
    print cmd5
    p5 = Popen(cmd5, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command5out = p5.stdout.read()
    print command5out
    p5.wait()
    ret =  p5.returncode
    responsecapture(ret,cmd5)
    
    restoreddbinstanceidentifier = "restoreddbinstance"

    time.sleep(180)

    cmd6 = "jcs rds restore-db-instance-from-db-snapshot --db-instance-identifier "+restoreddbinstanceidentifier+" --db-snapshot-identifier "+dbsnapshotidentifier+" --db-instance-class c1.small "
    print cmd6
    p6 = Popen(cmd6, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command6out = p6.stdout.read()
    print command6out
    p6.wait()
    ret =  p6.returncode
    responsecapture(ret,cmd6)

    time.sleep(240)

    cmd7 = "jcs rds modify-db-instance --db-instance-identifier "+restoreddbinstanceidentifier+ " --new-db-instance-identifier "+dbinstanceidentifier
    print cmd7
    p7 = Popen(cmd7, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command7out = p7.stdout.read()
    print command7out
    p7.wait()
    ret =  p7.returncode
    responsecapture(ret,cmd7)

    time.sleep(15)

    cmd8 = "jcs rds delete-db-snapshot --db-snapshot-identifier "+dbsnapshotidentifier
    print cmd8
    p8 = Popen(cmd8, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command8out = p8.stdout.read()
    print command8out
    p8.wait()
    ret =  p8.returncode
    responsecapture(ret,cmd8)

    time.sleep(180)

    cmd9 = "jcs rds delete-db-instance --db-instance-identifier "+dbinstanceidentifier+" --skip-final-snapshot"
    print cmd9
    p9 = Popen(cmd9, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command9out = p9.stdout.read()
    print command9out
    p9.wait()
    ret =  p9.returncode
    responsecapture(ret,cmd9)

def responsecapture(ret,command):
    
    rdsf=0
    rdsp=0

    if ret !=0:
        print 'fail of command',command
        rdsf = rdsf + 1
###     update1(date,command[4:40] ,  'f', 'dss')
    else:
###     update1(date,command[4:40] ,  'p', 'dss')
        print 'pass of command',command
        rdsp = rdsp + 1

    print rdsf 
    print rdsp


     
if __name__ == '__main__':

    test_create_delete_rds()
    print "x"



