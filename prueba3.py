import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Escuchando...")
        frase = listener.listen(source)
        rec = listener.recognize_google(frase,language="es-ES")
        rec = rec.lower()
        print(rec)
except:
    pass
#print (sr.Microphone.list_microphone_names())