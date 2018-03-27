from fbchat import Client
from fbchat.models import *

fhand = open('log.txt','r')
for line in fhand:
	email,password = line.split()
fhand.close()

client = Client(email,password)
while not client.isLoggedIn():
	client.login(email,password)
print(client.uid)
message = input('Enter the message')
fhand = open('users.txt','r')
for line in fhand:
	users = client.searchForUsers(line)
	user =users[0]
	
	print("User's ID: {}".format(user.uid))
	print("User's name: {}".format(user.name))
	print("User's profile picture url: {}".format(user.photo))
	print("User's main url: {}".format(user.url));print()
	
	client.send(Message(text = message),thread_id = user.uid,thread_type = ThreadType.USER)
client.logout()
