#Automatic Birthday wisher on facebook User Interactive

from fbchat import Client
from fbchat.models import *
import datetime
from tkinter import *
from tkinter import messagebox
import tkinter as tk

#need more improvement
def user_details():
    global user
    global pswrd
    user = username.get()
    pswrd = password.get()
    print(user)
    print(pswrd)

#Get Current Date
now = datetime.datetime.now()
k=now.strftime("%d-%m")
print(k)

def friend_details():
    global name
    global dob
    name=friend.get()
    dob=friend_dob.get()
    file = open("Database.txt","a")

    file.write( "\n"+ name + ":"+dob)
    print("Entry Added")
    file.close()
    file = open("Database.txt", 'r')
    cont = file.read()
    print(cont)
    pattern = k
    if k in cont:
       print("Match Found")
       client = Client('abhinavkrjha10@gmail.com','Abhinav10')
       users = client.searchForUsers(name)
       user = users[0]
       print("User's ID: {}".format(user.uid))
       client.sendMessage('Testing api',thread_id=user.uid,thread_type=ThreadType.USER)
       print("Message sent")
    else:
      pass


#------Tkinter

def raise_frame(frame):
    frame.tkraise()


win = Tk()


f1= Frame(win)
f2=Frame(win)
f=Frame(win)

for frame in(f,f1,f2):
    frame.grid(row=0,column=0,sticky='news')



win.wm_title("AUTOMATED BIRTHDAY WISHER")
win.config(background="#708090")
win.geometry("520x310")
f=Frame(win,height = 350, width = 500)
f.grid(row=0,column=0,padx=95,pady=10)

photo0=PhotoImage(file='hbd2.gif')
lable = Label(f,image=photo0)
lable.grid(row=0,column=0,padx=10,pady=0)
#----Frame 1


lable = Label(f1,text="Username : ")
lable.grid(row=1,column=0,padx=0,pady=10)
username = Entry(f1,width=40)
username.grid(row=1,column=20,padx=10,pady=30)

lable = Label(f1,text="Password : ")
lable.grid(row=3,column=0,padx=10,pady=2)
password = Entry(f1,width=40)
password.grid(row=3,column=20,padx=10,pady=40)
submit = Button(f1,text="Submit",command=user_details)
submit.grid(row=5,column=20,padx=10,pady=50)

lable = Label(f2,text="FRIEND'S NAME : ")
lable.grid(row=3,column=0,padx=10,pady=2)
friend = Entry(f2,width=40)

friend.grid(row=3,column=20,padx=10,pady=40)
friend.get()


lable = Label(f2,text="FRIEND'S DOB : ")
lable.grid(row=4,column=0,padx=10,pady=2)
friend_dob = Entry(f2,width=40)
friend_dob.grid(row=4,column=20,padx=10,pady=40)
friend_dob.get()
submit1 = Button(f2,text="Submit",command=friend_details)
submit1.grid(row=5,column=20,padx=10,pady=50)

#----main window buttons

Button1 = Button(f,text="Enter Account Details",command=lambda :raise_frame(f1))
Button1.grid(row=1,column=0,padx=0,pady=40)
Button2 =Button(f,text="Add new Friend",command=lambda:raise_frame(f2))
Button2.grid(row=1,column=1,padx=0,pady=40)

win.mainloop()
