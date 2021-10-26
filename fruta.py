#Uva, Sandía, Manzana, Naranja, Mango, Ciruela, Arándano, Piña, Fresa, Níspero, Melón, Durazno, Pera, Kiwi, Mandarina, Jitomate, Pepino, Calabaza, Limón, Aguacate, Lichi, 
#Guanabana, Zarzamora, Castaña, Pistacho, Cereza, Tamarindo, Frambuesa, Tejocote, Papaya, Platano, Higo, Granada, Mamey 
import msvcrt
val=False
res=""
print("Piensa en una de estas frutas (Uva, Sandía, Manzana, Naranja, Mango, Ciruela, Arándano,\n"+
"Piña, Fresa, Níspero, Melón, Durazno, Pera, Kiwi,\n"+
"Mandarina, Jitomate, Pepino, Calabaza, Limón, Aguacate, Lichi,\n"+
"Guanabana, Zarzamora, Castaña, Pistacho, Cereza, Tamarindo, Frambuesa,\n"+
"Tejocote, Papaya, Platano, Higo, Granada, Mamey)\n")
temp=input("Estás listo? s/n\n")
if temp == "s": val=True 
while(val):
    temp=input("Tu fruta suele prepararse como agua fresca? s/n\n")
    #Sandía, Naranja, Piña, Fresa, Melón, Mandarina, Pepino, Limón, Tamarindo, Mandarina, Granada
    if temp=="s":
            temp=input("Tu fruta suele no tener cascara o tener una cascara comestible? s/n\n")
            if temp=="s":
                #Fresa, Pepino
                temp=input("Tu fruta suele ser dulce? s/n\n")
                if temp=="s":
                    res="Fresa"
                    val=False
                    break
                else:
                    res="Pepino"
                    val=False
                    break
            else:
                #Sandía, Naranja, Piña, Melón, Mandarina, Limón, Tamarindo, Granada
                temp=input("Tu fruta suele caer de árboles? s/n\n")
                if temp=="s":
                    #Naranja, Mandarina, Limón, Tamarindo, Granada
                    temp=input("Tu fruta es un cítrico? s/n\n")
                    if temp=="s":
                        #Naranja, Mandarina, Limón
                        temp=input("Tu fruta suele ser muy consumida por los mexicanos al comer casi cualquier cosa? s/n\n")
                        if temp=="s":
                            res="Limón"
                            val=False
                            break
                        else:
                            temp=input("Tu fruta suele ser regalada en posadas navideñas? s/n\n")
                            if temp=="s":
                                res="Mandarina"
                                val=False
                                break
                            else:
                                res="Naranja"
                                val=False                     
                                break
                    else:
                        #Tamarindo, Granada
                        temp=input("Tu fruta suele ser utilizado como un dulce en México? s/n\n")
                        if temp=="s":
                            res="Tamarindo"
                            break
                        else:
                            res="Granada"
                            val=False
                            break
                else:
                    #Sandía, Piña, Melón
                     temp=input("Tu fruta suele ser redonda? s/n\n")
                     if temp=="s":
                        temp=input("Tu fruta es comida con chile en polvo? s/n\n")
                        if temp=="s":
                            res="Sandía"
                            val=False
                            break
                        else:
                            res="Melón"
                            val=False
                            break
                     else:
                         res="Piña"
                         val=False
                         break
    else:
        #Uva, Manzana, Mango, Ciruela, Arándano, Níspero, Durazno, Pera, Kiwi, Jitomate, Calabaza, Aguacate, Lichi, 
        #Guanabana, Zarzamora, Castaña, Pistacho, Cereza, Frambuesa, Tejocote, Papaya, Platano, Higo, Mamey
        temp=input("Tu fruta suele tener un tamaño de 10 cm o menor? s/n\n")
        if temp=="s":
            #Uva, Manzana, Mango, Ciruela, Arándano, Níspero, Durazno, Pera, Kiwi, Jitomate, 
            #Aguacate, Lichi, Zarzamora, Castaña, Pistacho, Cereza, Frambuesa, Tejocote, Higo
            temp=input("Tu fruta es seca? s/n\n")
            if temp=="s":
                #Castaña, Pistacho
                temp=input("Tu fruta es vendida como botana en tiendas? s/n\n")
                if temp=="s":
                    res="Pistacho"
                    val=False
                    break
                else:
                    res="Castaña"
                    val=False
                    break
            else:
                #Uva, Manzana, Mango, Ciruela, Arándano, Níspero, Durazno, Pera, Kiwi, Jitomate, 
                #Aguacate, Lichi, Guanabana, Zarzamora, Cereza, Frambuesa, Tejocote, Higo
                temp=input("Tu fruta suele ser de 7 cm o menor? s/n\n")
                if temp=="s":
                    #Uva, Ciruela, Arándano, Níspero, Durazno, Kiwi, Lichi, Zarzamora, Cereza, Frambuesa, Higo,Tejocote
                    temp=input("Tu fruta suele ser encontrada en jugo? s/n\n")
                    if temp=="s":
                        #Uva, Ciruela, Arándano, Durazno
                        temp=input("Tu fruta suele tener 'hueso'? s/n\n")
                        if temp=="s":
                            #Ciruela, Durazno
                            temp=input("Tu fruta tiene 'pelos'? s/n\n")
                            if temp=="s":
                                res="Durazno"
                                val=False
                                break
                            else:
                                res="Ciruela"
                                val=False
                                break
                        else:
                            #Uva, Arándano
                            temp=input("Tu fruta puede convertirse en vino? s/n\n")
                            if temp=="s":
                                res="Uva"
                                val=False
                                break
                            else:
                                res="Arándano"
                                val=False
                                break
                    else:
                        #Níspero, Kiwi, Lichi, Zarzamora, Cereza, Frambuesa, Higo, Tejocote
                        temp=input("Tu fruta suele no tener cascara o tener una cascara comestible? s/n\n")
                        if temp=="s":
                            #Zarzamora, Cereza, Frambuesa, Higo, Tejocote
                            temp=input("Tu fruta suele tener 'hueso'? s/n\n")
                            if temp=="s":
                                #Cereza, Tejocote
                                temp=input("Tu fruta suele venderse sin su 'hueso'? s/n\n")
                                if temp=="s":
                                    res="Cereza"
                                    val=False
                                    break
                                else:
                                    res="Tejocote"
                                    val=False
                                    break
                            else:
                                #Zarzamora, Frambuesa, Higo
                                temp=input("Tu fruta es morada? s/n\n")
                                if temp=="s":
                                    #Zarzamora, Higo
                                    temp=input("Tu fruta suele ser preparada como mermelada? s/n\n")
                                    if temp=="s":
                                        res="Zarzamora"
                                        val=False
                                        break
                                    else:
                                        res="Higo"
                                        val=False
                                        break
                                else:
                                    #Frambuesa
                                    res="Frambuesa"
                                    val=False 
                                    break 
                        else:
                            #Níspero, Kiwi, Lichi
                            temp=input("Tu fruta tiene el nombre de un ave? s/n\n")
                            if temp=="s":
                                res="Kiwi"
                                val=False 
                                break
                            else:
                                temp=input("Tu fruta tiene más de un 'hueso'? s/n\n")
                                if temp=="s":
                                    res="Níspero"
                                    val=False
                                    break
                                else:
                                    res="Lichi"
                                    val=False
                                    break
                else:
                    #Manzana, Mango, Pera, Jitomate, Aguacate
                    temp=input("Tu fruta suele tener 'hueso'? s/n\n")
                    if temp=="s":
                        #Mango, Aguacate
                        temp=input("Tu fruta suele comerse sola? s/n\n")
                        if temp=="s":
                            #Mango
                            res="Mango"
                            val=False 
                        else:
                            res="Aguacate"
                            val=False
                            break
                    else:
                        #Manzana, Pera, Jitomate
                        temp=input("Tu fruta suele ser suave (Fácil del morder)? s/n\n")
                        if temp=="s":
                            #Pera, Jitomate
                            temp=input("Tu fruta suele usarse en ensaladas? s/n\n")
                            if temp=="s":
                                res="Jitomate"
                                val=False
                                break
                            else:
                                res="Pera"
                                val=False
                                break
                        else:
                            res="Aguacate"
                            val=False
                            break
        else:
            #Calabaza, Guanabana, Papaya, Mamey, Platano
            temp=input("Tu fruta suele ser utilizada en Halloween'? s/n\n")
            if temp=="s":
                res="Calabaza"
                val=False
                break
            else:
                #Guanabana, Papaya, Mamey, Platano
                temp=input("Tu fruta suele tener pulpa con tonalidades naranja/amarilla? s/n\n")
                if temp=="s":
                    temp=input("Tu fruta suele tener 'hueso'? s/n\n")
                    if temp=="s":
                        res="Mamey"
                        val=False  
                        break
                    else:
                        temp=input("Tu fruta suele comerse a manera de postre? s/n\n")
                        if temp=="s":
                            res="Platano"
                            val=False
                            break
                        else:
                            res="Papaya"
                            val=False
                            break
                else:
                    res="Guanabana"
                    val=False
                    break
print("Pensaste en... "+res)
msvcrt.getch()

                            


