# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:17:18 2018

@author: pujasingh88
"""
import smtplib 
#from getpass import getpass
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import pandas as pd

def OpenConnection(ServerName,PortNumber,UserName,Password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.verify(UserName)
    try:
        print(server.login(UserName, Password))
    except :
      print("Invalid Credentials")
    return server

def constructMessage(UserDetails):
    msg = MIMEMultipart() 
    msg['From'] = UserDetails[0]
    #print(msg['From'])
    msg['Subject'] = 'some relevant Subject'
    body = "Here Comes some sweet messages  "
    msg.attach(MIMEText(body, 'plain'))  
    filename = UserDetails[0].strip()+'.jpg'
    #print(UserDetails[2])
    attachment = open("C:\\Users\\pujasingh88\\Desktop\\"+UserDetails[2], "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p)
    #print(msg.as_string())
    return msg
    
    
def sendemail(UserName,ReceiverID,server,Message):
    try:
      server.sendmail(UserName,ReceiverID, Message.as_string())
    except:
      print("An error occured.")

def GetList(path):
    dflist=pd.read_csv(path)
    return dflist
    

if __name__=="__main__":
   UserName=input("Enter your Email Id here").strip()
   Password=input("Enter your Password").strip()
   ServerName='smtp.gmail.com'
   PortNumber=587
   Server=OpenConnection(ServerName,PortNumber,UserName,Password)
   Path=input("Enter the full path of the csv file").strip()
   DetailList=GetList(Path)
   for row_index,row in DetailList.iterrows():
       #print(row)
       MSG=constructMessage(row)
       sendemail(UserName,row[1],Server,MSG)
   print('Emails Sent')

   
   
   
    