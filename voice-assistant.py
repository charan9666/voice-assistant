import pyttsx3
import webbrowser
import smtplib
import speech_recognition as sr
import wikipedia
import wolframalpha
import datetime
import os
import sys
import subprocess
from playsound import playsound
import boto3
import threading
import time
import google

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('PTRKX7-5VG5RGLTJQ')
voices = engine.getProperty('voices')
playsound('C:\\Users\\charan\\Desktop\\python projets\\AI\\audio.mpeg')
rain = "C:\\Users\\charan\\Desktop\\python projets\\AI\\Rainmeter\\Rainmeter.exe"




subprocess.Popen(rain)#rainmetter




def mp3_start_note():
 playsound(mp3_start_note)
 
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def to_be_posted(voice_note):
    for key in _dict.keys():
        if key in voice_note:
            return key

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

#now =  datetime.datetime.now()  

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning sir!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon sir!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening sir')

greetMe()

speak('Hello Sir, I am Jarvis!')
speak('How may I help you?')


   
def myCommand():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=3)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
                                                    #browsing program start from hear 
                                                    #to add some more
                                                    #add betwen start-end
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'hey Jarvis' in query or 'are you thre Jarvis' in query:
            replies['yes mr.charan', 'yes sir', 'i am online sir']
            speak(random.choice(replies))
            
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'charan' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 465)
                    server.ehlo()
                    server.starttls()
                    server.login("charansai.scs@gmail.com", 'charan000')
                    server.sendmail('ssrajinivas35@gmail.com', "srinu", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')  
                                                                                          #browsing end hear


                                                           #general_conversation start from hear  
                                                           #to add some more add betwen start to end
        elif 'nothing' in query or 'sleep' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

                                                           
        elif 'who are you' in query:
            messages = ['I am  Jarvis, your lovely personal assistant.',
                'Jarvis , didnt I tell you before?',
                'You ask that so many times! I am  Jarvis']
            speak(random.choice(messages))
        elif 'toss coin' in query:
            outcomes = ['heads','tails']    
            speak(random.choice(outcomes))
        elif 'how am i' in query:
            replies = [
               'You are goddamn handsome!',
               'My knees go weak when I see you.',
               'You look like the kindest person that I have met.']
            speak(random.choice(replies))
        elif 'where you born' in query or 'who is your father' in query or 'who develaped you' in query:         
            speak('I was created by a magician named charan, in india,')
        elif 'how are you' in query:
            speak('i am fine,thank you')
        elif 'love you' in query:
            replies = ['I love you too.','You are looking for love in the wrong place.']
            speak(random.choice(replies))
        elif 'marry me' in query:
            speak('I have been receiving a lot of marriage proposals recently.') 

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                                               #general_conversation end hear
                                                               #general_conversation end hear 
                                    





        elif  'play music'in query or 'play songs' in query or 'play audio' in query:
            music_dir ='C:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('wolframalpha says.')
                    speak(results)
                    
        
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('wikipedia says.')
                    speak(results)
                    
                    
            except:
                webbrowser.open('https://www.google.com/search?')
        speak('Next Command! Sir!')
       