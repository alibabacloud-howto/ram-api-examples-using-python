# Written by Guda Pradeep on 19/11/2018

#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkram.request.v20150501 import CreateUserRequest
from aliyunsdkram.request.v20150501 import AddUserToGroupRequest
from aliyunsdkram.request.v20150501 import CreateLoginProfileRequest


import csv

# Construct an Aliyun Client for initiating a request
# Set AccessKeyID and AccessKeySevcret when constructing the Aliyun Client
# RAM is a Global Service, and its API ingress is located in the East China 1 (Hangzhou) region. Enter "cn-hangzhou" in "Region"

clt = client.AcsClient('<AccessKey ID>','<Access Key Secret>','<Region ID>')


with open('ram_user_creation_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:

            line_count += 1
        else:
            # Construct a "CreateUser" request0
            request0 = CreateUserRequest.CreateUserRequest()

            # Set the UserName parameter
            request0.set_UserName(row[0])

            request0.set_DisplayName(row[1])

            request0.set_Comments(row[2])


            # Initiate a request and obtain the response0
            response0 = clt.do_action(request0)

            print (response0)

            request1 = AddUserToGroupRequest.AddUserToGroupRequest()
            for groupname in row[3].split(','):
                # Construct a "AddUserToGroup" request1

                #print (row[3])
                #print (groupname)
                # Set the UserName parameter
                request1.set_UserName(row[0])

                #request1.set_GroupName(row[3])
                request1.set_GroupName(groupname)

                response1 = clt.do_action(request1)

                print (response1)


            # Construct a "CreateLoginProfileRequest" request2
            request2 = CreateLoginProfileRequest.CreateLoginProfileRequest()

            # Set the UserName parameter
            request2.set_UserName(row[0])

            request2.set_Password(row[4])

            request2.set_PasswordResetRequired(row[5].lower())

            request2.set_MFABindRequired(row[6].lower())

            response2 = clt.do_action(request2)

            print (response2)

            line_count += 1


