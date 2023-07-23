import pyttsx3
import speech_recognition as sr;
import datetime
import wikipedia
import webbrowser
import os
# import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    mins=int(datetime.datetime.now().minute)

    if hour>=0 and hour <12:
        speak("Good Morning ")
        # speak("the time is ")
        # speak(hour)
        # speak("o,clock and ")
        # speak(mins)
        # speak(" minute now")


    elif hour>=12 and hour <18:
        speak("GOOD Afternoon")
        # speak("the time is ")
        # if hour>12:
        #      t=hour-12
        #      speak(t)
        #      speak("o,clock and ")
        #      speak(mins)
        #      speak(" minute now")
        # else:
        #      speak(hour)
        #      speak("o,clock and ")
        #      speak(mins)
        #      speak(" minute now")
    else :
        speak("GOOD Night")
        # speak("the time is ")
        # t=hour-12
        # speak(t)
        # speak("o,clock and ")
        # speak(mins)
        # speak(" minute now")

    
    
    speak("I am jarvis sir , Please tell me how may I help you")


def takeCommand():
    
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
 
    except Exception as e :
        print("repeate again ")
        return "None"
    return query

# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('smmanmohan2000@gmail.com','manmohan')
#     server.sendmail('smmanmohan2000@gmail.com',to,content)
#     server.close()
    
    

    

if __name__ == "__main__":

 while True:
    speak("Manmohan is a good boy")
    wishMe()
    query=takeCommand().lower()

    # Logic for executing tasks based on query
    
    if 'wikipedia' in query:
        speak("Searching Wikipedia..")
        query=query.replace("wikipedia","")
        results=wikipedia.summary (query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        speak(" wait I just opening the youtube")
    elif 'open google' in query:
        webbrowser.open("google.com")
        speak(" wait I just opening the google")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
        speak(" wait I just opening the stackoverflow")

    elif 'open codestudio' in query:
        webbrowser.open("codestudio.com")
        speak(" wait I just opening the codestudio")
    elif 'play music' in query:
        music_dir='D:\\songs' 
        songss=os.listdir(music_dir)
        print(songss)
        os.startfile(os.path.join(music_dir,songss[1]))
        speak(" wait I just playing  the song")
    elif 'the time' in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,The time is {strtime}")

        # hou=int(datetime.datetime.hour)
        # if(hou>12):
        #     h=(hou-12)
        #     speak(f"sir,The time is {h} {strtime}")
        # else:
        #     speak(f"sir,The time is {hou} {strtime}")
    elif 'open vs code' in query:
        filepath="C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(filepath)
        speak(" wait I just  opening the vs code")
    elif 'what can you do' in query:
        speak('Sir I can do many things! Like opening web browsers like google, YouTube, delta step, I can also search anything in Wikipedia! I can also open Microsoft word, excel, PowerPoint and paint folder. I can even play music ')
    elif 'stop' in query:
        speak("Exiting the program")
        exit()
    elif 'shutdown pc' in query:
        filepath="D:\\homes"
        os.startfile(filepath)
        speak(" wait I just  shutdowning your pc")
        
    
    # elif 'email to manmohan' in query:
    #     try:
    #         speak("What should I say")
    #         content=takeCommand()
    #         to="rsrachnasharma2003@gmail.com"
    #         sendEmail(to,content)
    #     except Exception as e:
    #         print(e)
    #         speak("Sorry the email fail to send ")
    
    