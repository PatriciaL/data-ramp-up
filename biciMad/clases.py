
##En este script diseñaras tus clases que luego importaremos en otro script para crear tus objetos pernalizados. 
##Hay que implementar dos clases
##Clase estacion: podremos iniciar tus objetos de tipo estacion, los cuales tendran ciertas propiedades como su nombre o ubicacion y alguna que otra funcion util


import math
import unidecode


class Estacion:
    
    '''
      Clase estacion utilizada en el programa para trabajar con datos de bicimad utilizada para definirlas clases que trabajaran en el programa
      de ejemplo. Parametros definidos dentro de la clase:
          name: 
            ¿Qué hace?: identifica la calle donde esta localizada la estacion de bicimad. 
            ¿Qué tipo de dato es?:  Es un str
          identificador: 
            ¿Qué hace?: localiza el id de la estacion asignado por el sistema de bicimad.
            ¿Qué tipo de dato es?: Es un str a pesar de ser un numero
          num_bicis: localiza el total de bicicletas acumuladas del total de bases de cada calle. 
            ¿Qué hace?: localiza el id de la estacion asignado por el sistema de bicimad.
            ¿Qué tipo de dato es?: Es un integer o numero entero
          address: numero concreto de localizacion de la base de bicicletas de bicimad
            ¿Qué hace?: numero concreto de localizacion de la base de bicicletas de bicimad
            ¿Qué tipo de dato es?: es un tipo de dato de texto que tiene numero 
          longitude: 
            ¿Qué hace?: registra la longitud geografica
            ¿Qué tipo de dato es?: es un tipo de dato geográfico, se utiliza como numerico
          latitude:
            ¿Qué hace?: registra la latitud geografica
            ¿Qué tipo de dato es?: es un tipo de dato geográfico, se utiliza como numerico
      '''
    
      # Constructor de la clase
    def __init__(self, name, identificador, num_bicis, address, longitude, latitude):  
      '''Vamos a definir atributos particulares para cada instancia''' 
      self.name = name
      self.identificador = identificador
      self.num_bicis = num_bicis
      self.address = address
      self.longitude = longitude
      self.latitude = latitude
     
    # Metodo propio de esta clase
      '''El metodo calcula la ditancia entre la estacion con la latitud y la longitud introducidas por el usuario
      El output sera en km'''
    def distancia(self, latitude, longitude):
        
        lat1, lon1 = self.latitude, self.longitude
        lat2, lon2 = latitude, longitude
        radius = 6371 #Km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin (dlon /2))
        b = 2 * math.atan2(math.sqtr(a), math.sqrt(1 - a))
        d = radius * c

        return d

#Ejemplo de instanciacion 

#alberto = Estacion(name, identificador, num_bicis, address, longitude, latitude)
#bernabeu= Estacion(name, identificador, num_bicis, address, longitude, latitude)



class ComunidadMadrid:
   # Constructor de la clase
  def __init__(self, estaciones):  
      '''Definimos como ''' 
      self.estaciones = estaciones #init cuyto parametro de entrada seran las estaciones. cuando creemos un objeto hay que introducir como argumento de entrada tipo lista
                                        #cuyo contenido sean todo objetos de tipo estacion
 
   #Metodo de la clase

  def get_ids(self):
      '''Este metodo no cuenta con parametros de entrada nos tiene que devolver una lista con los identificadores de estacion en formato int'''
        
        todas = [] #distingue todas los identificadores
        
        for i in self.estaciones: #
            todas.append(int(i.identificador))
        
        return todas
    
    
  def busca_estacion(self,estacion,tipo_busqueda):  
    '''Buscara el parametro estacion dentro de estaciones del objeto comunidad de matrid
    el tipo de busqueda puede ser por id donde buscara entre los identificadores de estacion
    O puede ser por name en cuyo caso busacra si el parametro de entrada estacion esta contenido en el nombre de alguna de las estaciones. Si no encuentra la estacion,
    devuelve el None y si la encuentra devuelve el objeto estacion completo'''

    
    
    for i in self.estaciones: #buscamos en el atributo estaciones en la lista
            
            if tipo_busqueda == "name": #si es exactamente el nombre
                est1 = unidecode.unidecode(estacion.lower()) #unidecode lo que hace es decodificar los tipos rarunos para corrgirlos
                est2 = unidecode.unidecode(i.name.lower())

                if est1 in est2:
                    return i
                    
            elif tipo_busqueda == "id":
                if int(estacion) == int(i.identificador):
                    return i
                
        return None

com = ComunidadMadrid([alberto,bernabeu])
