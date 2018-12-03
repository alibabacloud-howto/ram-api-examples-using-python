# Written by Guda Pradeep on 26/11/2018


#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkram.request.v20150501 import ListUsersRequest
from aliyunsdkram.request.v20150501 import GetUserRequest
from aliyunsdkram.request.v20150501 import ListGroupsForUserRequest
from bs4 import BeautifulSoup as bs
import csv


# Construct an Aliyun Client for initiating a request
# Set AccessKeyID and AccessKeySevcret when constructing the Aliyun Client
# RAM is a Global Service, and its API ingress is located in the East China 1 (Hangzhou) region. Enter "cn-hangzhou" in "Region"

clt = client.AcsClient('<AccessKey ID>','<Access Key Secret>','<Region ID>')

#with open('employee_file.csv', mode='w') as ram_user_list:
    #csv_writer = csv.writer(ram_user_list, delimiter=',' , quoting=csv.QUOTE_MINIMAL)
    # Construct a "ListUsers" request0

request0 = ListUsersRequest.ListUsersRequest()

    # Set the UserName parameter
request0.set_MaxItems(1000)

response0 = clt.do_action(request0)
#print (response0)



root = bs(response0,features="html.parser")
#print (root)

Ram_Users = open('ram_user_list.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Ram_Users)
ram_users_head = []
#print (ram_users_head)
count = 0
#print ('count')
users = root.find_all('user')
for user in users:
    #print (user)
    user_list = []
    #print (user_list)
    #print (count)
    if count == 0:
        username = 'username'
        ram_users_head.append(username)
        updatedate = 'updatedate'
        ram_users_head.append(updatedate)
        userid = 'userid'
        ram_users_head.append(userid)
        displayname = 'displayname'
        ram_users_head.append(displayname)
        createdate = 'createdate'
        ram_users_head.append(createdate)
        comments = 'comments'
        ram_users_head.append(comments)
        lastlogindate = 'lastlogindate'
        ram_users_head.append(lastlogindate)
        groupname = 'groupname'
        ram_users_head.append(groupname)
        csvwriter.writerow(ram_users_head)
        count = count + 1

    username = user.username
    user_list.append(username.get_text())
    updatedate = user.updatedate
    user_list.append(updatedate.get_text())
    userid = user.userid
    user_list.append(userid.get_text())
    displayname = user.displayname
    user_list.append(displayname.get_text())
    createdate = user.createdate
    user_list.append(createdate.get_text())
    comments = user.comments
    user_list.append(comments.get_text())

    request1 = GetUserRequest.GetUserRequest()
    request1.set_UserName(username.get_text())
    response1 = clt.do_action(request1)
    lastlogindate_root = bs(response1,features="html.parser")
    lastlogindate = lastlogindate_root.find('lastlogindate')
    user_list.append(lastlogindate.get_text())
    #print (lastlogindate.get_text())


    request2 = ListGroupsForUserRequest.ListGroupsForUserRequest()
    request2.set_UserName(username.get_text())
    response2 = clt.do_action(request2)
    groupname_root = bs(response2,features="html.parser")
    #print (groupname_root)
    groupnames = groupname_root.find_all('groupname')
    final_names = ''
    for groupname in groupnames:
        #group_list =
        #print('start')
        group_list = groupname.get_text()
        final_names = final_names + group_list + ", "
    #print(final_names)

    user_list.append(final_names)
    csvwriter.writerow(user_list)

Ram_Users.close()

print('Output file Ram_User_List.csv has been generated in your current directory')






