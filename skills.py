import os, webbrowser, sys, requests, subprocess, pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)


def speaker(text):
    engine.say(text)
    engine.runAndWait()

def browser():
    webbrowser.open('https://www.youtube.com', new=2)

def game():
    subprocess.Popen("C:/Program Files (x86)/Sid Meiers Civilization VI/Base/Binaries/Win64Steam/CivilizationVI.exe")

def offpc():
    os.system('shutdown -s')


def weather():
	try:
		params = {'q': 'Komendantsky aerodrom', 'units': 'metric', 'lang': 'ru', 'appid': '33ea817'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		
	except:
		speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')

def offBot():
    sys.exit()

def passive():
    pass