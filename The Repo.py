import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) female voice = 1 , male voice = 0
engine.setProperty('voice', voices[0].id)


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

    speak("I am repo what can i do for you?")       

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
        print("Say that again please...")  
        return "None"
    return query

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

        elif 'open gaana' in query:
            webbrowser.open("gaana.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play 945' in query:
            webbrowser.open("youtube.com/watch?v=2We3pc01xOI")

        elif 'open github' in query:
            webbrowser.open("https://github.com/")

        #spotify
        elif 'open music player' in query:
            codePath = "C:\\Users\\ASUS\\OneDrive\\Desktop\\Spotify.lnk"
            os.startfile(codePath)

        # Whatsapp   
        elif 'open messenger' in query:
            codePath = "C:\\Users\\ASUS\\OneDrive\\Desktop\\WhatsApp.lnk"
            os.startfile(codePath)        

        elif 'play music' in query:
            music_dir =r"C:\Users\ASUS\Music\AI Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        #pycharm
        elif 'open code' in query:
            codePath = "C:\\Users\\Public\\Desktop\\PyCharm Community Edition 2023.2.1.lnk"
            os.startfile(codePath)