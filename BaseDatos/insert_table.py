import sql

db = sql.BaseDato("cinemar.db")

""" db.insert("rol","nombre,descripcion","'Administrador','Administrador del sistema'")
db.insert("rol","nombre,descripcion","'Vendedor','Vendedor de producto'")
db.insert("rol","nombre,descripcion","'Cliente','Cliente solo puede reservar entradas'")

db.insert("usuario","nombre,apellido,dni,email,password,idrol","'Mogro','Guillermo','12345678','gmogro@gmail.com','123456',1") """

""" db.insert("persona","nombre,dni,direccion,telefono,email,tipo_persona",
          "'Mogro Guillermo Cristian','12345678','Av. Siempre Viva 123','987654321','guillermo@test.com','Cliente'") """



db.insert("pelicula","nombre,genero,fecha","'Digimon','Infantil','20/02/2022'")
db.insert("pelicula","nombre,genero,fecha","'Chucky','Terror','10/05/2020'")
db.insert("pelicula","nombre,genero,fecha","'Vikingos','Accion','10/07/2017'")


db.close()
