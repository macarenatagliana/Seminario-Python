import random
import string

#EJERCICIO 1

def analisis_zen(zen_text):
    lista_oraciones = list(map(str, zen_text.split('\n')))
    for elem in lista_oraciones:
        lista_palabras_oraciones = elem.split() 
        if len(lista_palabras_oraciones) > 1:
            segunda_palabra = lista_palabras_oraciones[1]
            if segunda_palabra[0] in 'aeiou':
                print(elem)


#EJERCICIO 3

def codigo_conducta(palabra_clave, rules):
    reglas = rules.split("\n")
    encontre = True
    for regla in reglas:
        if palabra_clave.lower() in regla.lower():
            encontre = False
            print(regla)
    if encontre:
        print("No se encontraron reglas para esa palabra clave")



#EJERCICIO 4
def validacion_usuario(palabra_ingresada):
    if len(palabra_ingresada)>=5 and palabra_ingresada.isalnum() and any(c.isdigit() for c in palabra_ingresada):
        print("El nombre de usuario es válido.")
    else:
        print("El nombre de usuario no cumple con los requisitos.")


#EJERCICIO 5 
def velocidad_reaccion(tiempo):
    if (tiempo>200 and tiempo<500):
        print ("Categoria: Normal")
    else:
        if (tiempo<200):
            print("Cateogia: Rapido")
        else:
            print("Cateogoria: Lento")


#EJERCICIO 6
def menciones(descriptions,contMusica,contCharla,contEntreten):
    for description in descriptions:
        description_lower = description.lower()
        if 'música'in description_lower:
            contMusica+=1
        if 'charla 'in description_lower:
            contCharla+=1
        if 'entretenimiento' in description_lower:
            contEntreten+=1    
    print(" Menciones de 'música' : ", contMusica)
    print(" Menciones de 'charla': ", contCharla)
    print(" Menciones de 'entretenimiento': ", contEntreten)



#EJERCICIO 7
def generador_codigo(usuario,fecha):    
    if len(usuario)>15:
        print("Ingrese un nombre de usuario que no supere los 15 caracteres")
    else:
        print(usuario.upper(),'-',fecha.strftime(("%Y%m%d")),'-',''.join(random.choices(string.ascii_letters + string.digits, k=10)).upper())


#EJERCICIO 8
def son_anagramas(palabra1,palabra2):
    if set(palabra1.lower()) == set(palabra2.lower()): #set lo convierte a conjuntos, y el lower en minuscula
        print("Son anagramas.")
    else:
        print("No son anagramas.")


#EJERCICIO 9
def clear_name(clients):
    lista =[]
    for client in clients:
        if client:
            client = client.strip()
            lista.append(client.title())
    return lista


#EJERCICIO 10
# Función para calcular el puntaje de la ronda y encontrar el MVP
def ranking_ronda(ronda, listaMVP,kill,asistencias,muertes):
    maxMVP = ''
    maxPuntos = 0.0  # Para encontrar el mayor puntaje
    
    for jugador, stats in ronda.items(): # me qedo con un jugador
        resul = stats['deaths'] * muertes if stats['deaths'] else 0
        mvp = stats['kills'] * kill + stats['assists'] * asistencias + resul
        
        #imprimo los datos de la ronda junto con los puntos 
        print(f"{jugador} - Kills: {stats['kills']}, Assists: {stats['assists']}, Deaths: {stats['deaths']}, Puntos: {mvp}")
        
        # si hay valor para esa clave(jugador), le asigna el mvp sumando al que traia,sino lo crea
        listaMVP[jugador] = listaMVP.get(jugador, 0) + mvp
        
        # Determinar el jugador con el mayor puntaje
        if mvp > maxPuntos:
            maxPuntos = mvp
            maxMVP = jugador

    return maxMVP # retorno jugador con mejor mvp

#función para obtener el MVP final y su contador
def ranking_final(rounds,kill,asistencias,muertes):
    listaMVP = {} #diccionario para jugador,mvp
    contadorMVP = {jugador: 0 for ronda in rounds for jugador in ronda}  # cuenta cuántas veces cada jugador fue mvp
    
    #iterar sobre cada ronda
    for ronda_numero, ronda in enumerate(rounds, start=1):
        print(f"-Ranking Ronda {ronda_numero}")
        
        mvp_jugador = ranking_ronda(ronda, listaMVP,kill,asistencias,muertes)
        
        #incrementa el contador de MVP para el jugador correspondiente
        contadorMVP[mvp_jugador] += 1
        
        #jugador con el máximo puntaje de la ronda
        print(f"MVP de la ronda {ronda_numero}: {mvp_jugador}")
    
    print("\nRanking final:")
    #con sorted ordeno la lista, con reverse en true para hacerlo descendiente
    jugadores_ordenados = sorted(listaMVP.items(), key=lambda item: item[1], reverse=True)
    
    for jugador, total_puntos in jugadores_ordenados:
        kills = sum(ronda[jugador]['kills'] for ronda in rounds if jugador in ronda)
        assists = sum(ronda[jugador]['assists'] for ronda in rounds if jugador in ronda)
        deaths = sum(1 for ronda in rounds if jugador in ronda and ronda[jugador]['deaths'])
        mvp_count = contadorMVP[jugador]
        
        # Imprimir las estadísticas del jugador ordenadas por puntos totales
        print(f"{jugador} - Total Kills: {kills}, Total Assists: {assists}, Total Deaths: {deaths}, MVPs: {mvp_count}, Total Puntos: {total_puntos}")