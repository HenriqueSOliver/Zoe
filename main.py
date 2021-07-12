# Our main file > (Arquivo principal)

import speech_recognition as sr

#creating recognizer > (Criar um reconhecedor)
r = sr.Recognizer()

#open audio device > (Abrir o microfone)
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Define microfone como fonte de áudio

        print(r.recognizer_google(audio,language='pt'))