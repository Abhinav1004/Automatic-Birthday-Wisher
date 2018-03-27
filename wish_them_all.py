import re
from fbchat import Client
from fbchat.models import *
import datetime

now = datetime.datetime.now()
k = now.strftime("%d-%m")
file = open("Database.txt", 'r')



for line in file:
    if k in line:
        patt1=r"([\w]+) ([\w]+):"+k
        mat=re.search(patt1,line)
        #print(mat.group())
        
        patt=r"([\w]+) ([\w]+)"
        match = re.search(patt,mat.group())
        
        if match:
            print(match.group())
            name=match.group()
            print("Match Found")
        
        client = Client('abhinavkrjha10@gmail.com', 'Abhinav10')
        users = client.searchForUsers(name)
        user = users[0]
        
        print("User's ID: {}".format(user.uid))
        #client.sendMessage('Happy Birthday '+name,thread_id=user.uid,thread_type=ThreadType.USER)
        client.sendLocalImage("cake.jpg", 'Happy Birthday ' + name, thread_id=user.uid, thread_type=ThreadType.USER)
        print("Message sent")
    else:
        pass