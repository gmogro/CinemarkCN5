import sql

cnn = sql.BaseDato("cinemar.db")

cnn.insert("pelicula","nombre,genero,fecha","'Digimon','Infantil','20/02/2022'")
cnn.insert("pelicula","nombre,genero,fecha","'Chuky','Terror','10/05/2020'")
cnn.insert("pelicula","nombre,genero,fecha","'Vikingos','Accion','10/07/2017'")


cnn.close()