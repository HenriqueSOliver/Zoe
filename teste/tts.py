import pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say("Oi, família Dahora! Eu sou a Zoe!")
engine.say("Sou uma assistente virtual em I.A, criada por Henrique Oliveira")
engine.runAndWait()

'''
for voice in voices:
    print(engine.setProperty('voice', voices[0].id))'''