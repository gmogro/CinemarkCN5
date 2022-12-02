from Proyecto.pelicula import Pelicula
from datetime import datetime,date

print("###########")
print("MENU")
print("###########")
runing = True
while runing:
    print("###########")
    print("Opciones")
    print("###########")
    #agregando las Opciones
    print("1 - Peliculas")
    print("2 - Funciones")
    opcion = int(input("Elija opcion : "))
    
    if opcion == 1:
        print("1 - Crear una pelicula")
        print("2 - Mostrar todas peliculas")
        print("3 - Actualizar una pelicula") 
        print("4 - Eliminar una pelicula") 
        sub_opcion = int(input("Elija opcion : "))
        if sub_opcion == 1:
           nombre = input("Nombre de la pelicula : ")
           genero = input("Genero de la pelicula : ")
           year = int(input('Ingrese el año de la pelicula'))
           month = int(input('Ingrese el mes de la pelicula'))
           day = int(input('Ingrese el dia de la pelicula'))
           fecha = date(year, month, day)
           #Esto si no quieren trabajar con clase
           #cnn = sql.BaseDato("cinemar.db")
           #cnn.insert("pelicula","nombre,genero,fecha",f"{self.__nombre},{self.__genero},{self.__fecha}")
           pelicula = Pelicula(nombre,genero,fecha)
           pelicula.create_pelicula()
        elif sub_opcion == 2:
           pelicula = Pelicula()
           print(pelicula.get_all_pelicula())
        elif sub_opcion == 3:
            pelicula = Pelicula()
            print("\tNombre\tGenero\tEstreno")
            id = 1
            for pel in pelicula.get_all_pelicula():
               print(f"{id} -  {pel[0]}\t - {pel[1]} - {pel[2]}")
            pelicula_select = input("Ingrese id de pelicula a actualizar : ")
            nombre = input("Nombre de la pelicula : ")
            genero = input("Genero de la pelicula : ")
            year = int(input('Ingrese el año de la pelicula'))
            month = int(input('Ingrese el mes de la pelicula'))
            day = int(input('Ingrese el dia de la pelicula'))
            fecha = date(year, month, day)
            datos = {"nombre":nombre,"genero":genero,"fecha":fecha}
            pelicula.update_pelicula(datos)
        elif sub_opcion == 4:
            pelicula = Pelicula()
            print("\tNombre\tGenero\tEstreno")
            id = 1
            for pel in pelicula.get_all_pelicula():
               print(f"{id} -  {pel[0]}\t - {pel[1]} - {pel[2]}")
               id += 1 
            pelicula_select = input("Ingrese id de pelicula a eliminar : ")
            pelicula.delete_pelicula(pelicula_select)
            
            
            
    
           
           