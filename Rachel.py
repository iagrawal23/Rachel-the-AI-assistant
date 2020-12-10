import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello, My name is Rachel. Sir Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'tell me about your creator' in query:
            speak(f"Ishan Saar Agrawal is doing CS engineering. he is a developer and a programmer. He likes to write poetry and he plays guitar too!")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'stupid' in query:
            speak("sorry")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")
        
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Ishan. he's my daddy!")

        elif 'search' in query:
             
            query = query.replace("search", "")         
            webbrowser.open(query) 

        elif "who i am" in query:
            speak("If you talk then definately you're human.")

        elif "why you came to this world" in query:
            speak("Thanks to Ishan he made me. further It's a secret")

        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\Users\ishan saar agrawal\Desktop\new ppt.pptx"
            os.startfile(power)

        elif 'what is love' in query:
            speak("It is the most beautiful and special feeling in the world!")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Ishan")

        elif 'why are you' in query:
            speak("I was created to change this world by Mister Ishan ")

        elif 'hello siri' in query:
            speak("who is siri? i am Rachel and i am the best! ")

        elif 'open spotify' in query:
            appli = r"D:\Spotify"
            os.startfile(appli)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif 'Morning' in query:
            speak("A warm good morning")
            speak("How are you udit")

        elif "will you be my girlfriend" in query:   
            speak("I'm sorry, i have a boyfriend, his name is Jarvis, you may know him, he is Mister Stark's assistant ")

        elif "love you" in query:
            speak("love you too but only as a friend")

        elif 'email to papa' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ishansaar@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Ishan. I am not able to send this email right now") 

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Rachel.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note) 

        elif "show notes" in query:
            speak("Showing Notes")
            file = open("Rachel.txt", "r") 
            print(file.read())
            speak(file.read(6))

        elif 'exit' in query:
            speak("Thanks for giving me your time. have a nice day")
            exit()



        
        
