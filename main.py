import speech_recognition as sr 
import webbrowser
import pyttsx3

recoginer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Start MY Bot.....")
    #Lisiten for the wake word Roy
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Lisiting...")
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(command)
            # print("You Said" + r.recognize_sphinx(audio))
        except sr.UnknownValueError :
            print("Could Not Understand")
        except sr.RequestError as e:
            print("Error : {0}".format(e))



