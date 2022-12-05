from BaseDatos import sql

class Pelicula:
    def __init__(self,nombre="",genero="",fecha="",estado = 1,id_pelicula = 0):
        self.__id_pelicula = id_pelicula
        self.__nombre = nombre
        self.__genero = genero
        self.__fecha = fecha
        self.__estado = estado
    
    @property
    def Idpelicula(self):
        return self.__id_pelicula

    @Idpelicula.setter
    def Idpelicula(self,pelicula):
        self.__id_pelicula = pelicula
        
    #getter y setter
    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def Estado(self):
        return self.__estado
    
    @Estado.setter
    def Estado(self,estado):
        self.__estado = estado
    
    def create_pelicula(self):
        cnn = sql.BaseDato("cinemar.db")
        cnn.insert("pelicula","nombre,genero,fecha",f"'{self.__nombre}','{self.__genero}','{self.__fecha}'")
    
    def get_all_pelicula(self):
        cnn = sql.BaseDato("cinemar.db")
        peliculas = cnn.select_all("pelicula","nombre,genero,fecha")
        return peliculas

    def update_pelicula(self,id,datos):
        cnn = sql.BaseDato("cinemar.db")
        for k,v in datos:
            cnn.update("pelicula",k,v,f"id_pelicula = {id}")
    
    def delete_pelicula(self,id):
        cnn = sql.BaseDato("cinemar.db")
        cnn.update("pelicula","estado",0,f"id_pelicula = {id}")
    
    
    def peliculas_destacadas():
        pass
    
    