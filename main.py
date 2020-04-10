import random
import smtplib
import tkinter as tk
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def createWidget():
    emailLabel = Label(root , text = "Enter your email-id :",bg = "deepskyblue3")
    emailLabel.grid( row =0 ,column =1,padx= 5 ,pady=5)

    emailEntry = Entry(root, textvariable=emailid, width = 30)
    emailEntry.grid(row = 0 ,column =2 , padx=5,pady=5)
    
    sendOTPbutton=Button(root,text="send OTP",command = sendOTP,width=20)
    sendOTPbutton.grid(row=0,column =3 , padx=5,pady=5)
    
    root.msgLabel = Label(root,bg="deepskyblue3")
    root.msgLabel.grid(row =0, column=1,padx=5,pady=5,columnspan=3)

    otpLabel = Label(root,text="Enter the OTP:",bg="deepskyblue3")
    otpLabel.grid(row=2,column=1,padx=5,pady=5)

    root.otpEntry= Entry(root,textvariable=otp,width=30,show="*")
    root.otpEntry.grid(row=2,column=2,padx=5,pady=5)

    validOTPbutton=Button(root,text="validate OTP",command=validOTP,width=20)
    validOTPbutton.grid(row=2,column=3,padx=5,pady=5)


    root.otpLabel=Label(root,bg="deepskyblue3")
    root.otpLabel.grid(row=3,column =1,padx=5,pady=5,columnspan=3)

def sendOTP():

    root.genOTP=""

    recieverEmail = emailid.get()

    #genrating th e6 di
    # gits
    numbers="0123456789"
    for i in range(6):
        root.genOTP += numbers[int(random.random()*10)]

    otpMSG = "YOUR OTP IS :"+ root.genOTP
    message=MIMEMultipart()
    message['FROM']='OTP VALIDATOR (python_scripts)'
    message['TO']="receiverEmail"
    message['SUBJECT']="OTP VALIDATION"

    message.attach(MIMEText(otpMSG))
    
    #creating an smtp session to sent the email
    

    smtp = smtplib.SMTP("smtp.gmail.com",587)
    #start the tls for securities 
    smtp.starttls()
    #authenticating the sender using the login method
    smtp.login("your gmail","your gmail password")
    #sending the email with multipart message converted into string 
    smtp.sendmail("crypto2709@gmail.com",recieverEmail,message.as_string())
    #close the sesion
    smtp.quit()

    receiverEmail= '{}*******{}'.format(recieverEmail[0:2],recieverEmail[-10:])
    #success report 
    root.msgLabel.config(text="OTP HAS BEEN SENT TO "+recieverEmail)
def validOTP():
        
        #sort the user inpot otp
    userInputOTP = otp.get()
        #sorting system generated otp
    systemOTP = root.genOTP
         #validating otp 
    if userInputOTP == systemOTP:
        root.otpLabel.config(text = "otp validated successfully ")
    else:
        root.otpLabel.config(text="invalid otp")
root = tk.Tk()

    #giving the title and bg 
root.title("SIMPLE_EMAIL_OTP_VALIDATOR")
root.resizable(False,False)
root.config(background= "deepskyblue3")
     #creating tlinter variable
emailid=StringVar()
otp= StringVar()

     #calling the create widget function with argument bg color
createWidget()
    #calling the infinite loop
root.mainloop()