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

def test_create_delete_iam():

    
    username = 'test'

    
    cmd1 = "jcs --insecure iam create-user --name "+username
    print cmd1
    p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command1out = p1.stdout.read()
    print command1out
    p1.wait()
    ret =  p1.returncode
    responsecapture(ret,cmd1)

    cmd2 = "jcs --insecure iam list-users "
    print cmd2
    p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command2out = p2.stdout.read()
    print command2out
    p2.wait()
    ret =  p2.returncode
    responsecapture(ret,cmd2)
    
    newpassword = "ReliAn12!33" 
    shufflednewpassword = "".join(random.sample(newpassword, len(newpassword)))

    cmd3 = "jcs --insecure iam update-user --name "+username+ " --new-password "+str(shufflednewpassword)
    p3 = Popen(cmd3, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command3out = p3.stdout.read()
    print command3out
    p3.wait()
    ret =  p3.returncode
    responsecapture(ret,cmd3)
    
    cmd4 = "jcs --insecure iam get-user --name "+username 
    p4 = Popen(cmd4, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command4out = p4.stdout.read()
    print command4out
    p4.wait()
    ret =  p4.returncode
    responsecapture(ret,cmd4)

    cmd5 = "jcs --insecure iam get-user-summary --name "+username
    p5 = Popen(cmd5, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command5out = p5.stdout.read()
    print command5out
    p5.wait()
    ret =  p5.returncode
    responsecapture(ret,cmd5)


    groupname = "test"

    

    cmd7 = "jcs --insecure iam create-group --name "+groupname
    print cmd7
    p7 = Popen(cmd7, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command7out = p7.stdout.read()
    print command7out
    p7.wait()
    ret =  p7.returncode
    responsecapture(ret,cmd7)

    cmd8 = "jcs --insecure iam list-groups "
    print cmd8
    p8 = Popen(cmd8, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command8out = p8.stdout.read()
    print command8out
    p8.wait()
    ret =  p8.returncode
    responsecapture(ret,cmd8)

    cmd9 = "jcs --insecure iam get-group --name "+groupname
    p9 = Popen(cmd9, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command9out = p9.stdout.read()
    print command9out
    p9.wait()
    ret =  p9.returncode
    responsecapture(ret,cmd9)

    time.sleep(20)
    
    #policydocument = "{\"name\": \"test\", \"statement\": [{\"action\": [\"jrn:jcs:dss:*\"], \"resource\": [\"jrn:jcs:dss:*:*:*\"], \"effect\": \"allow\"}]}"

    cmd11 = 'jcs --insecure iam create-policy --policy-document "{name: test, statement: [{action: [jrn:jcs:dss:*], resource: [jrn:jcs:dss::*:*], effect: allow}]}"'
    p11 = Popen(cmd11, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command11out = p11.stdout.read()
    print command11out
    p11.wait()
    ret =  p11.returncode
    responsecapture(ret,cmd11)

    time.sleep(10)

    cmd12 = "jcs --insecure iam get-policy --name test"
    p12 = Popen(cmd12, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command12out = p12.stdout.read()
    print command12out
    p12.wait()
    ret =  p12.returncode
    responsecapture(ret,cmd12)

    time.sleep(20)

    #updatedpolicydocument = "{\"name\": \"test\", \"statement\": [{\"action\": [\"jrn:jcs:dss:*\"], \"resource\": [\"jrn:jcs:dss:*:*:*\"], \"effect\": \"allow\"}]}"
    cmd13 = 'jcs --insecure iam create-policy --policy-document "{\/"name\/": \/"test\/", \/"statement\/": [{\/"action\/": [\/"jrn:jcs:dss:*\/"], \/"resource\/": [\/"jrn:jcs:dss::*:*\/"], \/"effect\/": \/"allow\/"}]}"'
    p13 = Popen(cmd13, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command13out = p13.stdout.read()
    print command13out
    p13.wait()
    ret =  p13.returncode
    responsecapture(ret,cmd13)

    time.sleep(20)


    cmd14 = "jcs --insecure iam list-policies"
    p14 = Popen(cmd14, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command14out = p14.stdout.read()
    print command14out
    p14.wait()
    ret =  p14.returncode
    responsecapture(ret,cmd14)

       

    cmd16 = "jcs --insecure iam create-credential --user-name "+username
    p16 = Popen(cmd16, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command16out = p16.stdout.read()
    print command16out
    p16.wait()
    ret =  p16.returncode
    responsecapture(ret,cmd16)

    cmd17 = "jcs --insecure iam get-user-credential --user-name "+username+" | grep -v 'Request-Id: req-'"
    p17 = Popen(cmd17, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    accesskeyjson = p17.stdout.read()
    print accesskeyjson
    accesskey_value = get_accesskey_value(accesskeyjson)
    print accesskey_value
    p17.wait()
    ret =  p17.returncode
    responsecapture(ret,cmd17)

    cmd18 = "jcs --insecure iam delete-credential --access-key "+accesskey_value
    p18 = Popen(cmd18, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command18out = p18.stdout.read()
    print command18out
    p18.wait()
    ret =  p18.returncode
    responsecapture(ret,cmd18)

    
    cmd19 = "jcs --insecure iam assign-user-to-group --user-name "+username+" --group-name "+groupname
    p19 = Popen(cmd19, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command19out = p19.stdout.read()
    print command19out
    p19.wait()
    ret =  p19.returncode
    responsecapture(ret,cmd19)

    cmd20 = "jcs --insecure iam check-user-in-group --user-name "+username+" --group-name "+groupname
    p20 = Popen(cmd20, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command20out = p20.stdout.read()
    print command20out
    p20.wait()
    ret =  p20.returncode
    responsecapture(ret,cmd20)

    cmd21 = "jcs --insecure iam list-groups-for-user --name "+username
    p21 = Popen(cmd21, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command21out = p21.stdout.read()
    print command21out
    p21.wait()
    ret =  p21.returncode
    responsecapture(ret,cmd21)

    cmd22 = "jcs --insecure iam list-user-in-group --name "+groupname
    p22 = Popen(cmd22, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command22out = p22.stdout.read()
    print command22out
    p22.wait()
    ret =  p22.returncode
    responsecapture(ret,cmd22)
    
    updategroupname = "test"
    cmd23 = "jcs --insecure iam update-group --name "+groupname+" --new-name "+updategroupname+" --new-description 'The new description of the group' "
    p23 = Popen(cmd23, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command23out = p23.stdout.read()
    print command23out
    p23.wait()
    ret =  p23.returncode
    responsecapture(ret,cmd23)

    cmd24 = "jcs --insecure iam get-group-summary --name "+groupname
    p24 = Popen(cmd24, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command24out = p24.stdout.read()
    print command24out
    p24.wait()
    ret =  p24.returncode
    responsecapture(ret,cmd24)

    cmd26 = "jcs --insecure iam attach-policy-to-user --policy-name test --user-name "+username
    p26 = Popen(cmd26, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command26out = p26.stdout.read()
    print command26out
    p26.wait()
    ret =  p26.returncode
    responsecapture(ret,cmd26)
    
    cmd27 = "jcs --insecure iam detach-policy-from-user --policy-name test --user-name "+username 
    p27 = Popen(cmd27, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command27out = p27.stdout.read()
    print command27out
    p27.wait()
    ret =  p27.returncode
    responsecapture(ret,cmd27)

    cmd28 = "jcs --insecure iam attach-policy-to-group --policy-name test --group-name "+groupname
    p28 = Popen(cmd28, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command28out = p28.stdout.read()
    print command28out
    p28.wait()
    ret =  p28.returncode
    responsecapture(ret,cmd28)

    cmd29 = "jcs --insecure iam detach-policy-from-group --policy-name test --group-name "+groupname
    p29 = Popen(cmd29, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command29out = p29.stdout.read()
    print command29out
    p29.wait()
    ret =  p29.returncode
    responsecapture(ret,cmd29)

    cmd30 = "jcs --insecure iam get-policy-summary --name test"
    p30 = Popen(cmd30, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command30out = p30.stdout.read()
    print command30out
    p30.wait()
    ret =  p30.returncode
    responsecapture(ret,cmd30)

    ''''    
    policydocumentRBP = "{\"name\": \"testrbp\", \"statement\": [{\"action\": [\"jrn:jcs:dss:*\"], \"principle\": [\"jrn:jcs:iam:*:*:*\"], \"effect\": \"allow\"}]}"
    cmd31 = "jcs --insecure iam create-resource-based-policy --policy-document "+policydocumentRBP
    p31 = Popen(cmd31, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command31out = p31.stdout.read()
    print command31out
    p31.wait()
    ret =  p31.returncode
    responsecapture(ret,cmd31)

    cmd32 = "jcs --insecure iam list-resource-based-policies"
    p32 = Popen(cmd32, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command32out = p32.stdout.read()
    print command32out
    p32.wait()
    ret =  p32.returncode
    responsecapture(ret,cmd32)

    cmd33 = "jcs --insecure iam update-resource-based-policy --policy-document "+policydocumentRBP+" --name testrbp"
    p33 = Popen(cmd33, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command33out = p33.stdout.read()
    print command33out
    p33.wait()
    ret =  p33.returncode
    responsecapture(ret,cmd33)

    cmd34 = "jcs --insecure iam get-resource-based-policy --name testrbp"
    p34 = Popen(cmd34, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command34out = p34.stdout.read()
    print command34out
    p34.wait()
    ret =  p34.returncode
    responsecapture(ret,cmd34)

    resource_value = '"{\"resource\":[\"jrn:jcs:dss:*:*:*\"]}'

    cmd35 = "jcs --insecure iam attach-policy-to-resource --policy-name testrbp --resource "+resource_value
    p35 = Popen(cmd35, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command35out = p35.stdout.read()
    print command35out
    p35.wait()
    ret =  p35.returncode
    responsecapture(ret,cmd35)

    time.sleep(10)

    cmd36 = "jcs --insecure iam detach-policy-from-resource --policy-name testrbp --resource "+resource_value
    p36 = Popen(cmd36, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command36out = p36.stdout.read()
    print command36out
    p36.wait()
    ret =  p36.returncode
    responsecapture(ret,cmd36)

    cmd37 = "jcs --insecure iam get-resource-based-policy-summary --name testrbp"
    p37 = Popen(cmd37, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command37out = p37.stdout.read()
    print command37out
    p37.wait()
    ret =  p37.returncode
    responsecapture(ret,cmd37)

    '''

    ## delete policy 
    ## delete resource based policy 
    ## delete user from group 
    ## delete group 
    ## delete user 

    cmd15 = "jcs --insecure iam delete-policy --name test "
    p15 = Popen(cmd15, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command15out = p15.stdout.read()
    print command15out
    p15.wait()
    ret =  p15.returncode
    responsecapture(ret,cmd15)
    ''''
    cmd38 = "jcs --insecure iam delete-resource-based-policy --name testrbp"
    p38 = Popen(cmd38, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command38out = p38.stdout.read()
    print command38out
    p38.wait()
    ret =  p38.returncode
    responsecapture(ret,cmd38)
    '''
    cmd25 = "jcs --insecure iam remove-user-from-group --user-name "+username+" --group-name "+groupname
    p25 = Popen(cmd25, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command25out = p25.stdout.read()
    print command25out
    p25.wait()
    ret =  p25.returncode
    responsecapture(ret,cmd25)


    cmd10 = "jcs --insecure iam delete-group --name "+groupname
    p10 = Popen(cmd10, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command10out = p10.stdout.read()
    print command10out
    p10.wait()
    ret =  p10.returncode
    responsecapture(ret,cmd10)

    cmd6 = "jcs --insecure iam delete-user --name "+username
    p6 = Popen(cmd6, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    command6out = p6.stdout.read()
    print command6out
    p6.wait()
    ret =  p6.returncode
    responsecapture(ret,cmd6)


def responsecapture(ret,command):
    
    iamf=0
    iamp=0

    if ret !=0:
        print 'fail of command',command
        iamf = iamf + 1
###     update1(date,command[4:40] ,  'f', 'dss')
    else:
###     update1(date,command[4:40] ,  'p', 'dss')
        print 'pass of command',command
        iamp = iamp + 1

    print iamf 
    print iamp


     
if __name__ == '__main__':

    test_create_delete_iam()
    print "x"



