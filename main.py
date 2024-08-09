import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicli

recoginer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    print(command)
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open github" in command.lower():
        webbrowser.open("https://github.com")
    elif "open gmail" in command.lower():
        webbrowser.open("https://gmail.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicli.music[song]
        webbrowser.open(link)
    else:
        speak("Sorry, I didn't understand the command.")
if __name__ == "__main__":
    speak("Starting my bot..")
    #Lisiten for the wake word Roy
    while True:
        # r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Lisiting...")
                audio = recoginer.listen(source, timeout=6, phrase_time_limit=1)
            word = recoginer.recognize_google(audio).lower()
            # print(command)
            # print("You Said" + r.recognize_sphinx(audio))
            if  word == "roy" :
                speak("Yes Sir")
                print("Roy Active...")

                #Lisiten for command
                with sr.Microphone() as source:
                    audio = recoginer.listen(source)
                    command = recoginer.recognize_google(audio)
                    processCommand(command)
                    
                    
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print(f"Error: {e}")


