from time import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

nombre = "leo"

engine = pyttsx3.init()

voces = engine.getProperty('voices')

engine.setProperty('voice',voces[0].id)
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)
listener = sr.Recognizer()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()
def escuchar():
    try:
        with sr.Microphone(device_index=1) as source:
            print("Escuchando...")
            listener.adjust_for_ambient_noise(source)
            frase = listener.listen(source)
            rec = listener.recognize_google(frase,language="es-ES")
            rec = rec.lower()
            print(rec)

            if nombre in rec:
                rec = rec.replace(nombre,'')
                run(rec)
            else:
                hablar("No reconozco la orden")
    except:
        pass
def run(rec):
    if "reproduce" in rec:
        musica = rec.replace("reproduce",'')
        hablar("Reproduciendo " + musica)
        pywhatkit.playonyt(musica)
    elif "hora" in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        hablar("Son las " + hora)
    elif "busca" in rec:
        orden = rec.replace("busca",'')
        wikipedia.set_lang("es")
        info = wikipedia.summary(orden,1)
        hablar(info)    
    elif "adiós" in rec:
        hablar("Hasta pronto")
    elif "súplica" in rec:
        hablar("Ya pe profe, un puntito")
    else:
        hablar("No reconozco la orden")

escuchar()