opc=True
cont=0
while(opc):
    temp=input("¿Tuvo usted algún contacto a menos de 2 metros durante un mínimo de 15 minutos o convive/cuida a alguna persoa con COVID-19 sin medidas de protección? s/n \n")
    if temp == 's':
        cont=cont+1
    temp=input("¿Presenta usted algún síntoma? (Tos, fiebre, diarrea, perdida sabor u olfato, fatiga, etc...) s/n \n")
    if temp == 's':
        cont=cont+1
    temp=input("¿Hace más de 14 días que comenzaron los síntomas? s/n \n")
    if temp == 's':
        cont=cont+1
    temp=input("¿Tiene dificultad repentina para respirar o nota falta de aire? s/n \n")
    if temp == 's':
        cont=cont+1
    temp=input("¿Presenta fiebre de más de 37,7ºC? s/n \n")
    if temp == 's':
        cont=cont+1
    if cont>=3:
        print("Puede que usted tenga covid, es necesario que se acerque al centro de salud más cercano \n")
    elif cont<3:
        print("No tienes covid, solo cuidate y evita besos de 3\n")
    temp=input("¿Te gustaría repetir el TEST? s/n\n")
    if temp == 'n':
        opc=False
    
    



        

