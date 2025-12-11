import random
import math
import smtplib  

digits = "0123456789@abcdefghijklmnopqrstuvwxyz"
otp = ""

for i in range(6):
    otp += digits[math.floor(random.random() * len(digits))]

msg = otp

e = smtplib.SMTP("smtp.gmail.com", 587)
e.starttls()
e.login("antlasaieswar123@gmail.com", "luwf ozdl mhcb jntf")

user = "antlasaieswar123@gmail.com"
emailid = input("enter the mail you want to send the otp:")

e.sendmail(user, emailid, msg)

while True:
    a = input("enter the otp:")
    if a == otp:
        print("otp is correct")
        break
    else:
        print("wrong otp")
        e = smtplib.SMTP("smtp.gmail.com", 587)
        e.starttls()
        e.login(user, "luwf ozdl mhcb jntf")
        e.sendmail(user, emailid, msg)

        
            
    
        
