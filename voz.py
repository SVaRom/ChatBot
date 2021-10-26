import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init()
r=sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Dí algo perra")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio, language='es-MX')
        print("Dijiste: {}".format(text))

    except:
        engine.say("No entendí")
