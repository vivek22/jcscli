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
from modulecomputeids import *
from moduleiamids import *

ts=datetime.datetime.now()
date =  time.strftime("%Y/%m/%d") ;
#print ts

def test_create_delete_instance():
    
    keyname = 'vivek'
    publicKey = '"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsNe3/1ILNCqFyfYWDeTKLD6jEXC2OQHLmietMWW+/vdaZq7KZEwO0jhglaFjU1mpqq4Gz5RX156sCTNM9vRbwKAxfsdF9laBYVsex3m3Wmui3uYrKyumsoJn2g9GNnG1PI1mrVjZ61i0GY3khna+wzlTpCCmy5HNlrmbj3XLqBUpipTOXmsnr4sChzC53KCd8LXuwc1i/CZPvF+3XipvAgFSE53pCtLOeB1kYMOBaiUPLQTWXR3JpckqFIQwhIH0zoHlJvZE8hh90XcPojYN56tI0OlrGqojbediJYD0rUsJu4weZpbn8vilb3JuDY+jwssnSA8wzBx3A/8y9Pp1B test@ubuntu"'

    cmd111 = "jcs compute create-key-pair --key-name "+keyname
    print cmd111
    cmd112 = "jcs compute describe-key-pairs"
    p111 = Popen(cmd111, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command111out = p111.stdout.read()
    print command111out
    print cmd112

    p111.wait()
    ret =  p111.returncode
    responsecapture(ret,cmd111)

    p112 = Popen(cmd112, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    keypairjson = p112.stdout.read()
    print keypairjson

    p112.wait()
    ret = p112.returncode
    responsecapture(ret,cmd112)


    cmd113 = "jcs compute delete-key-pair --key-name "+keyname
    print cmd113
    p113 = Popen(cmd113, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command113out = p113.stdout.read()
    print command113out

    p113.wait()
    ret =  p113.returncode
    responsecapture(ret,cmd113)


  
    cmd114 = "jcs --debug compute import-key-pair --key-name "+keyname+ " --public-key-material "+publicKey
    print cmd114 
    p114 = Popen(cmd114, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command114out = p114.stdout.read()
    print command114out

   
    vpccidr = '222.222.0.0/16'
    subnetcidr = '222.222.222.0/24'
    cmd115 = "jcs vpc create-vpc --cidr-block " +str(vpccidr)+" | grep -v 'Request-Id: req'"
    cmd116 = "jcs vpc describe-vpcs | grep -v 'Request-Id: req'"
    p115 = Popen(cmd115, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command115out = p115.stdout.read()
    print command115out

    p115.wait()
    ret =  p115.returncode
    responsecapture(ret,cmd115)


    p116 = Popen(cmd116, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    vpcjson = p116.stdout.read()
    print vpcjson
    vpc_id = get_vpc_id(vpcjson)
    print vpc_id

    p116.wait()
    ret =  p116.returncode
    responsecapture(ret,cmd116)


    cmd117 = "jcs vpc create-subnet --vpc-id " +str(vpc_id)+ " --cidr-block "+str(subnetcidr)+" | grep -v 'Request-Id: req'"
    print cmd117
    p117 = Popen(cmd117, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command117out = p117.stdout.read()
    print command117out

    p117.wait()
    ret =  p117.returncode
    responsecapture(ret,cmd117)


    cmd118 = "jcs vpc describe-subnets | grep -v 'Request-Id: req'"
    p118 = Popen(cmd118, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    subnetjson = p118.stdout.read()
    print subnetjson
    subnet_id = get_subnet_id(subnetjson)
    command118out = p118.stdout.read()
    print command118out

    p118.wait()
    ret =  p118.returncode
    responsecapture(ret,cmd118)

    cmd1 = "jcs compute describe-images | grep -v 'Request-Id: req'" 
    print cmd1
    p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    imagejson = p1.stdout.read()
    print imagejson
    image_id = get_image_id(imagejson)
    print image_id

    p1.wait()
    ret =  p1.returncode
    responsecapture(ret,cmd1)


    cmd2 = "jcs compute describe-instance-types | grep -v 'Request-Id: req'"
    print cmd2
    p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    instancetypejson = p2.stdout.read()
    print instancetypejson
    instancetype_id = get_instancetype_id(instancetypejson)
    print instancetype_id


    p2.wait()
    ret =  p2.returncode
    responsecapture(ret,cmd2)

    cmd3 = "jcs compute run-instances --image-id " +str(image_id)+ " --instance-type-id " +str(instancetype_id) 
    print cmd3
    p3 = Popen(cmd3, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command3out = p3.stdout.read()
    print command3out



    time.sleep(10)

    p3.wait()
    ret =  p3.returncode
    responsecapture(ret,cmd3)


    cmd4 = "jcs compute describe-instances | grep -v 'Request-Id: req'"
    print cmd4
    p4 = Popen(cmd4, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    instancejson = p4.stdout.read()
    print instancejson
    instance_id = get_instance_id(instancejson)
    print instance_id


    p4.wait()
    ret =  p4.returncode
    responsecapture(ret,cmd4)


    cmd5 = "jcs compute describe-volumes | grep -v 'Request-Id: req'"
    print cmd5
    p5 = Popen(cmd5, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    volumejson = p5.stdout.read()
    print volumejson
    volume_id = get_volume_id(volumejson)
    print volume_id

    p5.wait()
    ret =  p5.returncode
    responsecapture(ret,cmd5)


    cmd6 = "jcs compute update-delete-on-termination-flag --volume-id " +str(volume_id)+ " --delete-on-termination True"
    print cmd6
    p6 = Popen(cmd6, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command6out = p6.stdout.read()
    print command6out

    p6.wait()
    ret =  p6.returncode
    responsecapture(ret,cmd6)


    cmd61 = "jcs compute show-delete-on-termination-flag --volume-id " +str(volume_id)
    print cmd61
    p61 = Popen(cmd61, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command61out = p61.stdout.read()
    print command61out

    time.sleep(10)

    p61.wait()
    ret =  p61.returncode
    responsecapture(ret,cmd61)

    cmd8 = "jcs compute stop-instances --instance-ids " +str(instance_id)
    print cmd8
    p8 = Popen(cmd8, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command8out = p8.stdout.read()
    print command8out

    p8.wait()
    ret =  p8.returncode
    responsecapture(ret,cmd8)


    cmd81 = "jcs compute create-snapshot --volume-id " +str(volume_id)
    print cmd81
    p81 = Popen(cmd81, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command81out = p81.stdout.read()
    print command81out

    time.sleep(15)

    p81.wait()
    ret =  p81.returncode
    responsecapture(ret,cmd81)


    cmd82 = "jcs compute describe-snapshots | grep -v 'Request-Id: req'"
    print cmd82
    p82 = Popen(cmd82, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    snapshotjson = p82.stdout.read()
    print snapshotjson
    snapshot_id = get_snapshot_id(snapshotjson)
    print snapshot_id

    p82.wait()
    ret =  p82.returncode
    responsecapture(ret,cmd82)

    time.sleep(25)

    cmd9 = "jcs compute start-instances --instance-ids " +str(instance_id)
    print cmd9
    p9 = Popen(cmd9, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command9out = p9.stdout.read()
    print command9out

    time.sleep(25)

    p9.wait()
    ret =  p9.returncode
    responsecapture(ret,cmd9)


    cmd91 = "jcs compute create-volume --size 1"
    print cmd91
    p91 = Popen(cmd91, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    sbsvolumejson = p91.stdout.read()
    print sbsvolumejson
    sbsvolume_id = get_sbsvolume_id(sbsvolumejson)
    print sbsvolume_id

    p91.wait()
    ret =  p91.returncode
    responsecapture(ret,cmd91)

    time.sleep(10)

    cmd93 = "jcs compute attach-volume --volume-id " +str(sbsvolume_id)+ " --instance-id " +str(instance_id)+ " --device /dev/vdb"
    print cmd93
    p93 = Popen(cmd93, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command93out = p93.stdout.read()
    print command93out

    p93.wait()
    ret =  p93.returncode
    responsecapture(ret,cmd93)

    time.sleep(25)

    cmd711 = "jcs compute reboot-instances --instance-ids "+str(instance_id)
    print cmd711
    p7 = Popen(cmd711, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command711out = p711.stdout.read()
    print command711out

    time.sleep(25)

    p711.wait()
    ret =  p711.returncode
    responsecapture(ret,cmd711)



    cmd94 = "jcs compute detach-volume --volume-id " +str(sbsvolume_id)+ " --instance-id " +str(instance_id)
    print cmd94
    p94 = Popen(cmd94, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command94out = p94.stdout.read()
    print command94out

    p94.wait()
    ret =  p94.returncode
    responsecapture(ret,cmd94)


    cmd95 = "jcs compute delete-volume --volume-id " +str(sbsvolume_id)
    print cmd95
    p95 = Popen(cmd95, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command95out = p95.stdout.read()
    print command95out

    p95.wait()
    ret =  p95.returncode
    responsecapture(ret,cmd95)

    cmd83 = "jcs compute delete-snapshot --snapshot-id " +str(snapshot_id)
    print cmd83
    p83 = Popen(cmd83, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command83out = p83.stdout.read()
    print command83out
    p83.wait()
    ret =  p83.returncode
    responsecapture(ret,cmd83)

    cmd84 = "jcs vpc allocate-address --domain vpc | grep -v 'Request-Id: req'"
    print cmd84
    p84 = Popen(cmd84, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command84out = p84.stdout.read()
    print command84out

    p84.wait()
    ret =  p84.returncode
    responsecapture(ret,cmd84)

    cmd85 = "jcs vpc describe-addresses | grep -v 'Request-Id: req'"
    print cmd85
    p85 = Popen(cmd85, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    addressesjson = p85.stdout.read()
    print addressesjson
    allocation_id = get_allocation_id(addressesjson)
    print allocation_id

    p85.wait()
    ret =  p85.returncode
    responsecapture(ret,cmd85)

    cmd86 = "jcs vpc associate-address --instance-id "+str(instance_id)+" --allocation-id " +str(allocation_id)+ " | grep -v 'Request-Id: req'"
    print cmd86
    p86 = Popen(cmd86, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    associatejson = p86.stdout.read()
    print associatejson
    association_id = get_association_id(associatejson)
    print association_id
    p86.wait()
    ret =  p86.returncode

    time.sleep(10)
    
    cmd87 = "jcs vpc disassociate-address --association-id " +str(association_id)
    print cmd87
    p87 = Popen(cmd87, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command87out = p87.stdout.read()
    print command87out

    p86.wait()
    ret =  p86.returncode
    
    cmd88 = "jcs vpc release-address --allocation-id " +str(allocation_id)
    print cmd88
    p88 = Popen(cmd88, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command88out = p88.stdout.read()
    print command88out

    p88.wait()
    ret =  p88.returncode
    responsecapture(ret,cmd88)

    cmd89 = "jcs vpc describe-route-tables | grep -v 'Request-Id: req'"
    print cmd89
    p89 = Popen(cmd89, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    routetablejson = p89.stdout.read()
    print routetablejson
    routetable_id = get_routetableforroute_id(routetablejson)
    print routetable_id
    p89.wait()
    ret =  p89.returncode

    cmd90 = "jcs vpc create-route --route-table-id " +str(routetable_id)+ " --destination-cidr-block 100.0.0.100/32 --instance-id "+str(instance_id)
    print cmd90
    p90 = Popen(cmd90, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command90out = p90.stdout.read()
    print command90out
    p90.wait()
    ret =  p90.returncode

    time.sleep(10)

    cmd91 = "jcs vpc delete-route --route-table-id " +str(routetable_id)+ " --destination-cidr-block 100.0.0.100/32"
    print cmd91
    p91 = Popen(cmd91, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command91out = p91.stdout.read()
    print command91out
    p91.wait()
    ret =  p91.returncode

    instance_id = get_instance_id(instancejson)
    cmd10 = "jcs compute terminate-instances --instance-ids " +str(instance_id)
    print cmd10
    p10 = Popen(cmd10, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command10out = p10.stdout.read()
    print command10out

    p10.wait()
    ret =  p10.returncode
    responsecapture(ret,cmd10)

    cmd11 = "jcs vpc delete-subnet --subnet-id "+str(subnet_id)
    print cmd11
    p11 = Popen(cmd11, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command11out = p11.stdout.read()
    print command11out

    p11.wait()
    ret =  p11.returncode
    responsecapture(ret,cmd11)

    cmd12 = "jcs vpc delete-vpc --vpc-id " +str(vpc_id)
    print cmd12
    p12 = Popen(cmd12, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command12out = p12.stdout.read()
    print command12out

    p12.wait()
    ret =  p12.returncode
    responsecapture(ret,cmd12)

def responsecapture(ret,command):
    
    computef=0
    computep=0

    if ret !=0:
        print 'fail of command',command
        computef = computef + 1
###     update1(date,command[4:40] ,  'f', 'dss')
    else:
###     update1(date,command[4:40] ,  'p', 'dss')
        print 'pass of command',command
        computep = computep + 1

    print computef 
    print computep


     
if __name__ == '__main__':

    test_create_delete_instance()
    print "x"



