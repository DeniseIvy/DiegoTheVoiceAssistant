import speech_recognition as sr
import pywhatkit as kit
import datetime
import webbrowser
import pyttsx3
import time
import subprocess

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices',)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            talk(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice = r.listen(source)
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            talk('Sorry I did not get that')
        except sr.RequestError:
            talk('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if 'name' in voice_data:
        print('Hi, my name is Diego the Digital Assistant.')
        talk('Hi, my name is Diego the Digital Assistant.')
    if 'time' in voice_data:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is' + time)
        print('The current time is' + time)
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        talk('Here is what I found' + search)
    if 'location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp:'
        webbrowser.get().open(url)
        talk('Here is the location of' + location)
    if 'play' in voice_data:
        song = voice_data.replace('play', '')
        talk('playing' + song)
        print('playing' + song)
        kit.playonyt(song)
    if 'open google' in voice_data:
            url = "http://google.com"
            webbrowser.open(url, new=2)

        # Opening the Desktop Application
    if 'notepad' in voice_data:
        subprocess.Popen(['notepad.exe'])
        talk('Opening the notepad')
    if 'calculator' in voice_data:
        subprocess.Popen(['calculator.exe'])
        talk('Opening the calculator')
    if 'paint' in voice_data:
        subprocess.Popen(['mspaint.exe'])
        talk('Opening the paint')
        # CLosing the app
    if 'exit' in voice_data:
        exit()
    return respond

time.sleep(1)
print('Hi, I am Diego the Digital Assistant. How can I help you?')
talk('Hi, I am Diego the Digital Assistant. How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
