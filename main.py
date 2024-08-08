import speech_recognition as sr 
import webbrowser
import pyttsx3

recoginer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hi i am chayan")

