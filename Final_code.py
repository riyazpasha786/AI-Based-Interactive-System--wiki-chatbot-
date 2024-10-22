import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize
from gtts import gTTS
import os

import os
import speech_recognition as sr
import pyttsx3
import time

import cv2
import pandas as pd

if os.path.isfile("welcome1.mp3"):
    os.remove("welcome1.mp3")
    
df = pd.read_csv("facedetails"+os.sep+"face.csv")
col_names = ['Id', 'Name', 'Date', 'Time']

xc=df['Id'].values

   
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

    
r = sr.Recognizer()

def CaptureFaces():
    Capture_Image.takeImages()

def Trainimages():
    Train_Image.TrainImages()

    
def speach():
    while(1):
        try:
            print('start speaking...')
            # use the microphone as source for input. 
            with sr.Microphone() as source1:                                
                r.adjust_for_ambient_noise(source1, duration=.5) 
                            
                audio2 = r.listen(source1) 
                print("Stop speaking until get response...!")
                            
                MyText = r.recognize_google(audio2) 
                MyText = MyText.lower()

                print("you: "+MyText)
                time.sleep(.2)
                break
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e)) 
                    
        except sr.UnknownValueError: 
            print("unknown error occured")
    return MyText

# The text that you want to convert to audio
mytext = ' Hello Welcome to Chat bot System'

SpeakText(mytext)

# for fetching wikipedia articles 
import wikipedia 
while(1):

        Id=Recognize.recognize_face()
        print(Id)
        if len(Id)>=1  and Id!='Unknown':
            #myobj = gTTS(text='Hi '+Id+ ' I am  Robot...How can I help you?', lang=language, slow=False)
            text='Hi '+Id+ ' I am  Robot...How can I help you?'
            time.sleep(.5)
            SpeakText(text)

        else:
            text='Hi I am  Robot. your new to me. Can i have your name?'
            time.sleep(.5)
            SpeakText(text)

            while (1):
                txt1=speach()
                text='Your response:'+txt1+' if yes say Continue else say no'
                SpeakText(text)
                txt2=speach()

                if txt2=='Continue' or txt2=='continue' or txt2=='CONTINUE':
                    text='Thank you  Show your face i will store your data'
                    SpeakText(text)
                    break

            if txt2=='Continue' or txt2=='continue' or txt2=='CONTINUE':
                Capture_Image.takeImages(txt1,str(len(xc)+1))
                text='Your data is saved successfully.  How am i help you further'
                Trainimages()
                SpeakText(text)
        while (1):
          txt2=speach()
          
          if txt2=='Exit' or txt2=='exit' or txt2=='EXIT':
              SpeakText('Thank you for using chatbot')
              break
          else:
              print(wikipedia.summary(txt2, sentences = 1))
              SpeakText(wikipedia.summary(txt2,sentences = 1))

    
