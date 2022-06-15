'''Implementa una función que tenga las siguientes características:
#* Nombre: `dist_estaciones`
#* Input: (est1, est2, comunidad). Son dos objetos de tipo `int`, con dos indentificadores de estación, y otro de tipo `ComunidadMadrid`.
#* Output: la distancia entre ambas estaciones.'''

def dist_estaciones(est1, est2, comunidad):
    
    estacion1 = comunidad.busca_estacion(est1, "id") #busca_estacion es el metodo que hemos definido anteriormente 
    estacion2 = comunidad.busca_estacion(est2, "id")
    
    if estacion1 != None and estacion2 != None:        #si las dos estaciones existen
        return estacion1.distancia(estacion2.longitude, estacion2.latitude) #llamamos a la funcion distancia del metodo de la clase estacion
    
    else:
        return "Alguna de las estaciones no está en la base de datos"