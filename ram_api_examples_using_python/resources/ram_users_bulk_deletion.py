# Written by Guda Pradeep on 21/11/2018

#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkram.request.v20150501 import DeleteUserRequest
from aliyunsdkram.request.v20150501 import ListGroupsForUserRequest
from aliyunsdkram.request.v20150501 import RemoveUserFromGroupRequest
from bs4 import BeautifulSoup




import csv

# Construct an Aliyun Client for initiating a request
# Set AccessKeyID and AccessKeySevcret when constructing the Aliyun Client
# RAM is a Global Service, and its API ingress is located in the East China 1 (Hangzhou) region. Enter "cn-hangzhou" in "Region"

clt = client.AcsClient('<AccessKey ID>','<Access Key Secret>','<Region ID>')

with open('ram_user_deletion_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:

            line_count += 1
        else:

            # Construct a "ListGroupsForUser" request0
            request0 = ListGroupsForUserRequest.ListGroupsForUserRequest()

            # Set the UserName parameter
            request0.set_UserName(row[0])

            # Initiate a request and obtain the response0
            response0 = clt.do_action(request0)

            print (response0)
            y=BeautifulSoup(response0,features="html.parser")
            group_names = y.find_all('groupname')
            print(group_names)

            for groupname in group_names:
                print(groupname.get_text())

                # Construct a "DeleteUser" request1
                request1 = RemoveUserFromGroupRequest.RemoveUserFromGroupRequest()

                # Set the UserName parameter
                request1.set_UserName(row[0])

                # Set the GroupName parameter
                request1.set_GroupName(groupname.get_text())

                # Initiate a request and obtain the response0
                response1 = clt.do_action(request1)

                print (response1)

            # Construct a "DeleteUser" request2
            request2 = DeleteUserRequest.DeleteUserRequest()

            # Set the UserName parameter
            request2.set_UserName(row[0])

            # Initiate a request and obtain the response0
            response2 = clt.do_action(request2)

            print (response2)



