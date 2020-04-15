import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from time import ctime


print('initializing Jarvis')

MASTER = 'Xander'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
	engine.say(text)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)

	if hour >= 0 and hour < 12:
		speak('Good Morning master..' + MASTER)

	elif hour >= 12 and hour < 18:
		speak('Good Afternoon master...' + MASTER)

	else:
		speak('Good Evening master...' + MASTER)
speak('initializing Jarvis...')
speak('I am Jarvis. How may i help you?')

def takeCommand ():
	r = sr.Recognizer()
	with sr.Microphone() as source: 
		print("listening...")
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language = 'en-us')
		print(f"you said :{query}\n")

	except Exception as e:
		print("say that again please")
		query = None

	return query.lower()
 

#main program starts here...
wishMe() 
query = takeCommand()	

 #logic for executing tasks

if "wikipedia" in query:
 	speak('searching wikipedia...')
 	query = query.replace("wikipedia", "")
 	results = wikipedia.summary(query, sentences = 2)
 	speak(results)

#if the spoken text contains "open youtube", then Jarvis opens www.youtube.com on your default browser.....
elif "open youtube" in query:
	webbrowser.open("www.youtube.com")

#if the spoken text contains "play music", then Jarvis opens play a song on your default music player.....
elif "play music" in query:
	songs_dir = r"C:\Users\user\Music\music"
	songs = os.listdir(songs_dir)
	os.startfile(os.path.join(songs_dir,songs[0]))

#if the spoken text contains "time", then Jarvis speaks the current time.....
elif "time" in query or "date" in query:
	speak(f"master {MASTER} the current date and time is {ctime()}")

#if the spoken text contains "sublime text", then Jarvis opens sublime Text .....
elif "sublime text" in query:
	os.startfile(r"C:\Program Files\Sublime Text 3\sublime_text.exe")