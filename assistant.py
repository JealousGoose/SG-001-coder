import subprocess
import wolframalpha
import pyttsx3
import tkinter
from PIL import Image
import json
import requests
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import pywhatkit
import urllib.request
import json
import gtts
from playsound import playsound
import pyautogui

def playaudio(audio):
    playsound(audio)

def speak(audio):
    audio = gtts.gTTS(text = audio, lang = 'en', slow = False)
    audio.save("textaudio.mp3")
    playaudio("textaudio.mp3")
    os.remove("textaudio.mp3")

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("How can i help you????")
	speak("I am your Assistant")
	speak(assname)
	
#def usrname():
	#speak("What should i call you sir")
	#uname = takeCommand()
	#speak("Welcome Mister")
	#speak(uname)
	#columns = shutil.get_terminal_size().columns
	
	#print("#####################".center(columns))
	#print("Welcome Mr.", uname.center(columns))
	#print("#####################".center(columns))
	
	#speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-np')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query
	
def WolfRam(query):
	api_key = "UQ9938-Q43WH53XUU"
	requester = wolframalpha.Client(api_key)
	requested = requester.query(query)
	
	try:
		answer = next(requested.results).text
		return answer
	except:
		speak('an error occoured')
		print('An error occoured...')

def calculator(query):
	Term = str(query)
	Term = Term.replace("multiply", "*")
	Term = Term.replace("divide", "/")
	Term = Term.replace("add", "*")
	Term = Term.replace("minus", "*")
	Term = Term.replace("subtract", "-")
	Term = Term.replace("plus", "+")
	Term = Term.replace("into", "*")
	Term = Term.replace("calculate", "")
	Final = str(Term)
	try:
		result = WolfRam(Final)
		speak(Term + "is equal to" + result)
		print(Term + "=" + result)
	except:
		speak("Sorry, an error occoured.")
		print("Sorry, an error occoured.")

def temp(query):
	Term = str(query)
	Term = Term.replace("temperature", "")
	Term = Term.replace("in", "")
	temp_query = str(Term)
	if 'outside' in temp_query:
		var1 = "Temperature in Kathmandu"
		answer = WolfRam(var1)
		speak(f"{var1} is {answer}")
	else:
		var2 = "Temperature In" + temp_query
		answ = WolfRam(var2)
		speak(f"{var2} is {answ}")

def DateConverter(query):
	date = query.replace(" and ","-")
	date = date.replace(" and ","-")
	date = date.replace("and","-")
	date = date.replace("and","-")
	date = date.replace(" ","")
	return str(date)

def NasaNews(Date):
	Api_Key = "Ra7hi9SfpbThBXWDHtYNvcTy9OvBvuXpyuyLIZ3X"
	speak("extracting data")
	Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
	params = {'date':str(Date)}
	r = requests.get(Url, params = params)
	Data = r.json()
	info = Data.get('explanation')
	title = Data.get('title')
	FileName = str(Date) + '.jpg'
	print(FileName)
	Image_Url = Data.get('url')
	Image_r = requests.get(Image_Url)
	with open(FileName,'wb') as f:
		f.write(Image_r.content)
	path_1 = "C:\\Users\\COMPAQ\\Documents\\" + str(FileName)
	path_2 = "C:\\Users\\COMPAQ\\Pictures\\" + str(FileName)
	os.replace(path_1, path_2)
	print(f"Title:{title}")
	speak(f"Title:{title}")
	img = Image.open(path_2)
	img.show()
	print(f"according to nasa: {info}")
	speak(f"according to nasa: {info}")

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	clear()	
	wishMe()
	#usrname()
	
	while True:
		query = takeCommand().lower()
		
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			music_dir="E:\\Audio"

			songs = os.listdir(music_dir)
			
			random = os.startfile(os.path.join(music_dir, songs[random.randrange(0,len(songs)-1)]))

		elif 'the time' in query:
			strTime = datetime.datetime.now()
			speak(strTime.strftime("%A"))

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Gaurav.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
		
		elif "who i am" in query:
			speak("If you talk then definately your human.")

		elif "why you came to world" in query:
			speak("Thanks to Gaurav. further It's a secret")

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Gaurav")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Mister Gaurav ")

		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			query = query.replace("seconds", '')
			query = query.replace("second", '')
			query = query.replace("for", '')
			query = query.replace("stop listening",'')
			query = query.replace("don't listen",'')
			query = query.replace(" ", ' ')
			time.sleep(int(query))
			speak("okay")

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "weather" in query:
			
			# Google Open weather website
			# to get API of Open weather
			api_key = "Api key"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()
			
			if x["cod"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
			else:
				speak(" City Not Found ")
		
		elif "open wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		elif "on youtube" in query: 
			query=query.replace("on youtube","")
			query=query.replace("play","")
			pywhatkit.playonyt(query)
           
		elif "launch" in query:
			speak("What website should i open for you?")
			name=takeCommand()
			web="https://www."+name+".com"

		elif "call sani" in query or "call saini" in query:
			speak("trying to call..")
			print("Calling......")
			webbrowser.open("https://www.facebook.com/videocall/incall/?peer_id=100007920451548&call_id=2341157218&is_caller=true&audio_only=false&nonce=on8cdeixjy6p&initialize_video=true")

		elif "fuck" in query or "shit" in query or "f***" in query or "lamo" in query or "a**" in query or "lmao" in query:
			speak("haha Rough words on me, I'm already into that shit")

		elif "temperature" in query:
			speak(temp(query))
			
		elif "calculate" in query:
			speak(calculator(query))

		elif "space news" in query:
			speak('can you please tell me the date?')
			date = takeCommand()
			Value = DateConverter(date)
			NasaNews(Value)

		elif "my location" in query or "where am i" in query or "my place" in query:
			ip = "202.51.76.41"
			url = "http://ip-api.com/json/"
			response = urllib.request.urlopen(url + ip)
			data = response.read()
			values = json.loads(data)
			speak("According to your ip:" + values["query"])
			speak("Your city is:" + values['city'])
			speak("Your country is:" + values['country'])
			speak("Your isp is:" + values['isp'])
			speak("region you are right now in is:" + values['region'])
			speak("your timezone is:" + values['timezone'])

			print("Your Ip adress is:" + values["query"])
			print("Your city is:" + values['city'])
			print("Your ISP is:" + values['isp'])
			print("Your country is:" + values['country'])
			print("region you are right now in is:" + values['region'])
			print("your timezone is:" + values['timezone'])
    
		elif "take a screenshot" in query:
			speak("capturing screen")
			print("Capturing screen....")
			im1 = pyautogui.screenshot()
			im1.save('my_screenshot.png')
			print('Successfully captured screen!')
			print("Screenshot saved as: " + im1)
			


