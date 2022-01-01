import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def run_alexa():
    command = take_command()
    #print(command)
    command = command.lower()
    if "play" in command:
        command = command.replace("play","")
        talk("Playing "+ command)
        if "by" in command:
            command = command.replace("by","")
        pywhatkit.playonyt(command)

def take_command():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa","")
                #print(command)
    except:
        pass
    return command


talk("Hi, I am your personal assistant")
talk("What can I do for you")
#talk("Hola, soy tu asistente personal")
#talk("Que puedo hacer por ti")
engine.runAndWait()
run_alexa()

#source_input = "waves.jpg"
#ascii_output = "ascii_waves.txt"vcyy



#pywhatkit.image_to_ascii_art(source_input, ascii_output)