import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def input_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', '')
    except Exception as e:
        print(e)
    return command

def run_siri():
    command = input_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'search for' in command:
        search = command.replace('search for', '')
        pywhatkit.search(search)
    elif 'what is' in command:
        pywhatkit.search(command)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        talk('I did not understand that. Please repeat.')

while True:
    run_siri()
