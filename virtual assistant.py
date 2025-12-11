#google text to speech
from gtts import gTTS
import speech_recognition as sr
import playsound
from time import ctime
import os
import re
import uuid#universal unique id
import smtplib
import webbrowser


def listen():
    r=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("start talking")
            audio=r.listen(source,phrase_time_limit=10)
    except OSError as e:
        print("No default input device available:", e)
        mics = sr.Microphone.list_microphone_names()
        if not mics:
            print("No microphone devices found. Attach or enable a microphone and try again.")
            return ""
        print("Available devices:")
        for i, name in enumerate(mics):
            print(f"{i}: {name}")
        idx = input("Enter device index to use (or press Enter to cancel): ").strip()
        if idx == "":
            return ""
        try:
            idx = int(idx)
        except ValueError:
            print("Invalid index.")
            return ""
        try:
            with sr.Microphone(device_index=idx) as source:
                print("start talking")
                audio=r.listen(source,phrase_time_limit=10)
        except Exception as e2:
            print("Failed to open chosen device:", e2)
            return ""
    data=""
    
    try:
        data=r.recognize_google(audio,language='en-US')
        print("you said:"+data)
    except sr.UnknownValueError:
        print ("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
listen()

def respond(String):
    print(String)
    tts=gTTS(text=String,lang='en')
    tts.save("speech.mp3")
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#start giving actions
#virtual assistant actions
def  Virtual_assistant(data):
    '''give your actions'''
    
    if "how are you" in data:
        listening=True
        respond("Good and going well")
        
    if "time" in data:
        listening=True
        respond(ctime())
        
    if "open google" in data.casefold():
        listening=True
        url="https://www.google.com/"
        webbrowser.open(url)
        respond("Success")
        
    if "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/'+data.replace("locate",""))
        result="Located"
        respond("Located {}".format(data.replace("locate","")))
        
    if "email" in data:
        listening =True
        respond("Whom should i send mail to?")
        to=listen().lower()
        edict={'eswar':'antlasaieswar123@gmail.com','sai':'pooja@codegnan.com'}
        #give mail ids
        toaddr=edict[to]
        respond("What is the subject?")
        subject=listen()
        respond("What should i tell that person?")
        message=listen()
        content='subject :{}\n\n{}'.format(subject,message)

        mail=smtplib.SMTP('smtp.gmail.com',587)
 
        mail.ehlo()
        mail.starttls()

        mail.login('antlasaieswar123@gmail.com','luwf ozdl mhcb jntf')

        mail.sendmail('antlasaieswar123@gmail.com',toaddr,content)

        mail.close()
        respond('Email Sent')
    if "stop" in data:
        listening=False
        print("Listening Stopped")
        respond ("Okay done take care...")
    try:
        return listening
    except UnboundLocalError:
        print("Time out")
        
respond ("Hey Eswar how are you")
listening =True
while listening ==True:
    data =listen()
    listening =Virtual_assistant(data)
