#Este sera el archivo ejecutable del programa
'''El script main tiene que ser un programa interactivo que vaya preguntando al usuario. Vamos paso a paso:
* Importa tus clases y funciones al principio del script
* Descomenta las líneas de código que hay tras el importado de datos, de manera que crees una lista con todas las estaciones, con sus datos.
* Crea un objeto llamado `comunidad`, que sea de tipo `ComunidadMadrid`
* Lo que viene a partir de ahora es un `while True:`. Que se ejecutará siempre, a no ser que en algún punto del `while` haya un `break`. Ahora vemos dónde ponerlo.
* Al principio del `while` hay que preguntar al usuario qué desea hacer, mediante un menú sencillo:

    Escoge una opcion: 
    1. Busca estacion (nombre)
    2. Calcula distancia (entre ids)
    3. Salir del programa
    
Son las tres opciones que tiene el usuario para introducir: 1,2,3

* **Si introduce 3**: Pon un mensaje de despedida y sal del `while`. Aquí va el `break`! Te recomiendo que empieces por aquí para que no se te quede el `while` en un bucle infinito. Asegúrate que el menú funciona bien y después implementa las funcionalidades de cada opción.

* **Si introduce 1**: tienes que buscar la estación (por nombre) entre todas las estaciones del objeto `comunidad`. Si la encuentras, imprime por pantalla su nombre, preguntale al usuario "¿Qué más deseas hacer?", y que el programa vuelva al menú con las tres opciones. Si no la encuentra, ponlo también por pantalla con un print, y que el programa vuelva al menú.

* **Si introduce 2**: hay que pedirle al usuario dos inputs, que serán dos enteros con los dos ids de estación. Con esos ids calcula la distancia entre ambas estaciones.

* **En cualquier otro caso**: imprime por pantalla que la respuesta no es valida, y vuelve al menu inicial.'''

import os  #importa el sistema operativo
os.getcwd() #invoca el working directori


# Leemos los datos
import pandas as pd #es la forma normal de hacer pandas
from clases import Estacion, ComunidadMadrid
from funciones import dist_estaciones

df = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx") #definimos la variable del data frame, que nos va a permitir 

tot_est = [] #esto es una lista vacia

for index, row in df.iterrows(): #iteramos sobre las filas del data frame que es una estructura de datos
    estacion = Estacion(row[0], row[3], row[1], row[6], row[4], row[5]) #nos va creando nuevas instancias del tipo estacion, invoca a los selfs, son los indices de los atributos creados en la clase
    tot_est.append(estacion)  #


comunidad = ComunidadMadrid(tot_est) #estamos metiendo todas las estaciones 


while True:
    
    resp_usu1 = input("Escoge una opcion: \n1. Busca estacion\
                      \n2. Calcula distancia \n3. Salir del programa\n")
    
    try:
        resp_usu1 = int(resp_usu1)  #pasamos a entero la respuesta del usuario
    except:                   #le decimos que introduzca un numero 
        print("Respuesta no valida. Por favor introduce 1, 2 o 3")
        continue  #le decimos que continue
        
    # Elige buscar una estacion por nombre
    if resp_usu1 == 1:
        resp_usu2 = input("Muy bien, introduce el nombre de la estacion")
        busqueda = comunidad.busca_estacion(resp_usu2, "name") #invocamos la clase y la funcion dentro de esta
        if busqueda == None:
            print("Esta estacion no está en la base de datos")
        else:
            print("¡Estacion encontrada! La estación es",busqueda.name,"\n\n\n¿Qué más deseas hacer?")

    #depsues de esta iteracion volveria a ejecutar
    #        
    elif resp_usu1 == 2:
        resp_usu3_1 = int(input("Introduce el identificador de la primera estacion "))
        resp_usu3_2 = int(input("Introduce el identificador de la segunda estacion "))
        
        distancia = dist_estaciones(resp_usu3_1, resp_usu3_2, comunidad)
        
        if type(distancia) == str: 
            print(distancia)
        else:
            print("Las estaciones introducidas están a una distancia de", round(distancia, 2), "km") #redondear la distancia a un float de dos posiciones
    
    elif resp_usu1 == 3:   #cuando le introduce un tres, salimos del bucle con el break 
        print("¡Hasta la próxima!")
        break
    
    else:
        print("Respuesta no valida. Por favor introduce 1, 2 o 3")
    
        
        