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

###from update import update1
from modulevpcids import *
from moduleiamids import *
from modulecomputeids import *

ts=datetime.datetime.now()
date =  time.strftime("%Y/%m/%d") ;
#print ts

## VPC ##

def test_create_delete_vpc():
    
    vpccidr = '222.222.0.0/16'
    cmd1 = "jcs vpc create-vpc --cidr-block " +str(vpccidr)+" | grep -v 'Request-Id: req'" 
    cmd2 = "jcs vpc describe-vpcs | grep -v 'Request-Id: req'"

    p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command1out = p1.stdout.read()
    print command1out

    p1.wait()
    ret =  p1.returncode
    responsecapture(ret,cmd1)


    p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    myjson = p2.stdout.read()
    print myjson 
    vpc_id = get_vpc_id(myjson)
    print vpc_id


    p2.wait()
    ret =  p2.returncode
    responsecapture(ret,cmd2)


    cmd3 = "jcs vpc delete-vpc --vpc-id " +str(vpc_id)+" | grep -v 'Request-Id: req'"
    p3 = Popen(cmd3, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command3out = p3.stdout.read()
    print command3out

    p3.wait()
    ret =  p3.returncode
    responsecapture(ret,cmd3)


def test_create_delete_subnet():

    vpccidr = '222.222.0.0/16'
    subnetcidr = '222.222.222.0/24'
    cmd1 = "jcs vpc create-vpc --cidr-block " +str(vpccidr)+" | grep -v 'Request-Id: req'"
    cmd2 = "jcs vpc describe-vpcs | grep -v 'Request-Id: req'"
    p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command1out = p1.stdout.read()
    print command1out

    p1.wait()
    ret =  p1.returncode
    responsecapture(ret,cmd1)


    p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    vpcjson = p2.stdout.read()
    print vpcjson
    vpc_id = get_vpc_id(vpcjson)
    print vpc_id

    p2.wait()
    ret =  p2.returncode
    responsecapture(ret,cmd2)


    cmd3 = "jcs vpc create-subnet --vpc-id " +str(vpc_id)+ " --cidr-block "+str(subnetcidr)+" | grep -v 'Request-Id: req'"
    print cmd3
    p3 = Popen(cmd3, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command3out = p3.stdout.read()
    print command3out

    p3.wait()
    ret =  p3.returncode
    responsecapture(ret,cmd3)


    cmd4 = "jcs vpc describe-subnets | grep -v 'Request-Id: req'"
    p4 = Popen(cmd4, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    subnetjson = p4.stdout.read()
    print subnetjson
    subnet_id = get_subnet_id(subnetjson)
    command4out = p4.stdout.read()
    print command4out

    p4.wait()
    ret =  p4.returncode
    responsecapture(ret,cmd4)

    cmd5 = "jcs vpc delete-subnet --subnet-id " +str(subnet_id)+" | grep -v 'Request-Id: req'"
    p5 = Popen(cmd5, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command5out = p5.stdout.read()
    print command5out

    p5.wait()
    ret =  p5.returncode
    responsecapture(ret,cmd5)

    cmd6 = "jcs vpc delete-vpc --vpc-id " +str(vpc_id)+" | grep -v 'Request-Id: req'"
    p6 = Popen(cmd6, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command6out = p6.stdout.read()
    print command6out

    p6.wait()
    ret =  p6.returncode
    responsecapture(ret,cmd6)


def test_create_delete_sg_sgrule():

    vpccidr = '222.222.0.0/16'
    cmd1 = "jcs vpc create-vpc --cidr-block " +str(vpccidr)+" | grep -v 'Request-Id: req'"
    cmd2 = "jcs vpc describe-vpcs | grep -v 'Request-Id: req'"
    p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command1out = p1.stdout.read()
    print command1out

    p1.wait()
    ret =  p1.returncode
    responsecapture(ret,cmd1)

    p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    vpcjson = p2.stdout.read()
    print vpcjson
    vpc_id = get_vpc_id(vpcjson)
    print vpc_id

    p2.wait()
    ret =  p2.returncode
    responsecapture(ret,cmd2)

    cmd3 = "jcs vpc create-security-group --group-name WebServerSG --group-description Web-Servers --vpc-id " +str(vpc_id)
    p3 = Popen(cmd3, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command3out = p3.stdout.read()

    p3.wait()
    ret =  p3.returncode
    responsecapture(ret,cmd3)


    cmd4 = "jcs vpc describe-security-groups | grep -v 'Request-Id: req'"
    p4 = Popen(cmd4, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    securitygroupjson = p4.stdout.read()
    print securitygroupjson
    securitygroup_id = get_securitygroup_id(securitygroupjson)
    print securitygroup_id

    p4.wait()
    ret =  p4.returncode
    responsecapture(ret,cmd4)

    cmd5= "jcs vpc authorize-security-group-ingress --group-id " +str(securitygroup_id)+ " --protocol tcp --port 80 --cidr 10.0.0.0/24"
    p5 = Popen(cmd5, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command5out = p5.stdout.read()
    print command5out

    p5.wait()
    ret =  p5.returncode
    responsecapture(ret,cmd5)

    cmd6= "jcs vpc revoke-security-group-ingress --group-id " +str(securitygroup_id)+ " --protocol tcp --port 80 --cidr 10.0.0.0/24"
    p6 = Popen(cmd6, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command6out = p6.stdout.read()
    print command6out

    p6.wait()
    ret =  p6.returncode
    responsecapture(ret,cmd6)

    cmd7= "jcs vpc authorize-security-group-egress --group-id " +str(securitygroup_id)+ " --protocol tcp --port 80 --cidr 10.0.0.0/24"
    p7 = Popen(cmd7, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command7out = p7.stdout.read()
    print command7out

    p7.wait()
    ret =  p7.returncode
    responsecapture(ret,cmd7)

    cmd8= "jcs vpc revoke-security-group-egress --group-id " +str(securitygroup_id)+ " --protocol tcp --port 80 --cidr 10.0.0.0/24"
    p8 = Popen(cmd8, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command8out = p8.stdout.read()
    print command8out

    p8.wait()
    ret =  p8.returncode
    responsecapture(ret,cmd8)

    cmd9= "jcs vpc delete-security-group --group-id " +str(securitygroup_id) 
    p9 = Popen(cmd9, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command9out = p9.stdout.read()
    print command9out

    p9.wait()
    ret =  p9.returncode
    responsecapture(ret,cmd9)

    cmd10 = "jcs vpc delete-vpc --vpc-id " +str(vpc_id)+" | grep -v 'Request-Id: req'"
    p10 = Popen(cmd10, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command10out = p10.stdout.read()
    print command10out

    p10.wait()
    ret =  p10.returncode
    responsecapture(ret,cmd10)


def test_create_delete_routetable():

    vpccidr = '222.222.0.0/16'
    subnetcidr = '222.222.222.0/24'
    cmd1 = "jcs vpc create-vpc --cidr-block " +str(vpccidr)+" | grep -v 'Request-Id: req'"
    cmd2 = "jcs vpc describe-vpcs | grep -v 'Request-Id: req'"
    p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command1out = p1.stdout.read()
    print command1out

    p1.wait()
    ret =  p1.returncode
    responsecapture(ret,cmd1)

    p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    vpcjson = p2.stdout.read()
    print vpcjson
    vpc_id = get_vpc_id(vpcjson)
    print vpc_id

    p2.wait()
    ret =  p2.returncode
    responsecapture(ret,cmd2)

    cmd3 = "jcs vpc create-subnet --vpc-id " +str(vpc_id)+ " --cidr-block "+str(subnetcidr)+" | grep -v 'Request-Id: req'"
    print cmd3
    p3 = Popen(cmd3, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command3out = p3.stdout.read()
    print command3out

    p3.wait()
    ret =  p3.returncode
    responsecapture(ret,cmd3)

    cmd4 = "jcs vpc describe-subnets | grep -v 'Request-Id: req'"
    p4 = Popen(cmd4, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    subnetjson = p4.stdout.read()
    print subnetjson
    subnet_id = get_subnet_id(subnetjson)
    command4out = p4.stdout.read()
    print command4out

    p4.wait()
    ret =  p4.returncode
    responsecapture(ret,cmd4)


    cmd5 = "jcs vpc create-route-table --vpc-id " +str(vpc_id)+" | grep -v 'Request-Id: req'"
    print cmd5
    p5 = Popen(cmd5, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    routetablejson = p5.stdout.read()
    routetable_id = get_routetable_id(routetablejson)
    print routetable_id
    p5.wait()
    ret =  p5.returncode
    responsecapture(ret,cmd5)

    p5.wait()
    ret =  p5.returncode
    responsecapture(ret,cmd5)


    cmd6 = "jcs vpc describe-route-tables | grep -v 'Request-Id: req'"
    p6 = Popen(cmd6, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command6out = p6.stdout.read()
    print command6out

    p6.wait()
    ret =  p6.returncode
    responsecapture(ret,cmd6)


    cmd7 = "jcs vpc associate-route-table --route-table-id " +str(routetable_id)+ " --subnet-id " +str(subnet_id)+" | grep -v 'Request-Id: req'"
    p7 = Popen(cmd7, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    associationjson = p7.stdout.read()
    print associationjson
    association_id = get_association_id(associationjson)
    print association_id
    command7out = p6.stdout.read()
    print command7out

    p7.wait()
    ret =  p7.returncode
    responsecapture(ret,cmd7)


    cmd8 = "jcs vpc disassociate-route-table --association-id " +str(association_id)+ " | grep -v 'Request-Id: req'"
    p8 = Popen(cmd8, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command8out = p8.stdout.read()
    print command8out

    p8.wait()
    ret =  p8.returncode
    responsecapture(ret,cmd8)


    cmd9 = "jcs vpc delete-route-table --route-table-id " +str(routetable_id)+" | grep -v 'Request-Id: req'"
    p9 = Popen(cmd9, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command9out = p9.stdout.read()
    print command9out

    p9.wait()
    ret =  p9.returncode
    responsecapture(ret,cmd9)


    cmd10 = "jcs vpc delete-subnet --subnet-id " +str(subnet_id)+" | grep -v 'Request-Id: req'"
    p10 = Popen(cmd10, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command10out = p10.stdout.read()
    print command10out

    p10.wait()
    ret =  p10.returncode
    responsecapture(ret,cmd10)

    cmd11 = "jcs vpc delete-vpc --vpc-id " +str(vpc_id)+" | grep -v 'Request-Id: req'"
    p11 = Popen(cmd11, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command11out = p11.stdout.read()
    print command11out

    p11.wait()
    ret =  p11.returncode
    responsecapture(ret,cmd11)


def test_create_delete_addresses():

    cmd1 = "jcs vpc allocate-address --domain vpc | grep -v 'Request-Id: req'"
    print cmd1
    p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command1out = p1.stdout.read()
    print command1out

    p1.wait()
    ret =  p1.returncode
    responsecapture(ret,cmd1)


    cmd2 = "jcs vpc describe-addresses | grep -v 'Request-Id: req'"
    print cmd2
    p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    addressesjson = p2.stdout.read()
    print addressesjson
    allocation_id = get_allocation_id(addressesjson)
    print allocation_id

    p2.wait()
    ret =  p2.returncode
    responsecapture(ret,cmd2)


    cmd3 = "jcs vpc release-address --allocation-id " +str(allocation_id)+ " | grep -v 'Request-Id: req'"
    print cmd3
    p3 = Popen(cmd3, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command3out = p3.stdout.read()
    print command3out

    p3.wait()
    ret =  p3.returncode
    responsecapture(ret,cmd3)


def responsecapture(ret,command):

    vpcf=0
    vpcp=0

    if ret !=0:
        print 'fail of command',command
        vpcf = vpcf + 1
###     update1(date,command[4:40] ,  'f', 'dss')
    else:
###     update1(date,command[4:40] ,  'p', 'dss')
        print 'pass of command',command
        vpcp = vpcp + 1

    print vpcf
    print vpcp




if __name__ == '__main__':
    test_create_delete_vpc()
    test_create_delete_subnet()
    test_create_delete_sg_sgrule()
    test_create_delete_routetable()
    test_create_delete_addresses()
    print "x"


