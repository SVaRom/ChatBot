import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    cont=0
    print("Test para saber si tienes COVID")
    print("Por favor conteste en Sí o No")
    print("¿Tuvo usted algún contacto a menos de 2 metros durante un mínimo de 15 minutos o convive/cuida a alguna persoa con COVID-19 sin medidas de protección?")
    audio=r.listen(source)
    text=r.recognize_google(audio, language='es-MX')
    print("Respuesta: {}".format(text))
    if text == "sí":
         cont=cont+1
    print("¿Presenta usted algún síntoma? (Tos, fiebre, diarrea, perdida sabor u olfato, fatiga, etc...)")
    audio=r.listen(source)
    text=r.recognize_google(audio, language='es-MX')
    print("Respuesta: {}".format(text))
    if text == "sí":
         cont=cont+1
    print("De ser sí su respuesta anterior ¿hace más de 14 días que comenzaron los síntomas?")
    audio=r.listen(source)
    text=r.recognize_google(audio, language='es-MX')
    print("Respuesta: {}".format(text))
    if text == "sí":
         cont=cont+1
    print("¿Tiene dificultad repentina para respirar o nota falta de aire?")
    audio=r.listen(source)
    text=r.recognize_google(audio, language='es-MX')
    print("Respuesta: {}".format(text))
    if text == "sí":
         cont=cont+1
    print("¿Presenta fiebre de más de 37,7ºC?")
    audio=r.listen(source)
    text=r.recognize_google(audio, language='es-MX')
    print("Respuesta: {}".format(text))
    if text == "sí":
         cont=cont+1
    if cont>=3:
        print("Puede que usted tenga covid, acuda al centro de salud más cercano\n")
    elif cont<3:
           print("No tienes covid, solo cuidese\n")

        
        


