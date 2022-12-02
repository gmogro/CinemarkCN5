import sql


cnn = sql.DataBase("BaseDatos.db")


cnn.create_table("rol", "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                         "nombre TEXT,"+
                         "descripcion TEXT,"
                         "estado INTEGER"
                )

cnn.create_table("usuario", "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                            "nombre TEXT,"+
                            "apellido TEXT,"+
                            "correo TEXT,"+
                            "contrasena TEXT,"+
                            "rol_id INTEGER,"+
                            "estado INTEGER"
               )


cnn.create_table("pelicula", "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                            "nombre TEXT,"+
                            "descripcion TEXT,"+
                            "duracion TEXT,"+
                            "fecha_estreno TEXT,"+
                            "genero TEXT,"+
                            "estado INTEGER"
                )

cnn.create_table("sala", "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                            "numero INTEGER,"+
                            "capacidad INTEGER,"+
                            "estado INTEGER"
                )

cnn.create_table("funcion", "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                            "fecha TEXT,"+
                            "hora TEXT,"+
                            "pelicula_id INTEGER,"+ 
                            "sala_id INTEGER,"+
                            "estado INTEGER"
                )