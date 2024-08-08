import speech_recognition as sr 
import webbrowser
import pyttsx3

recoginer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    # print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    
if __name__ == "__main__":
    speak("Start MY Bot.....")
    #Lisiten for the wake word Roy
    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
             print("Lisiting...")
             audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            # print(command)
            # print("You Said" + r.recognize_sphinx(audio))
            if (word.lower()== "roy"):
                speak("Yes Sir")
                #Lisiten for command
                with sr.Microphone() as source:
                    print("Roy Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except sr.RequestError as e:
            print("Error : {0}".format(e))



