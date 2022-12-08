import sql

cnn = sql.BaseDato("cinemar.db")

cnn.create_table("pelicula","id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT,"+
                            "nombre TEXT(100),"+
                            "genero TEXT(100),"+
                            "fecha datetime,"+
                            "estado INTEGER(1) DEFAULT 1"
                )

cnn.create_table("funcion","id_funcion INTEGER PRIMARY KEY AUTOINCREMENT,"+
                        "fecha datetime,"+
                        "id_sala INTEGER,"+
                        "id_pelicula INTEGER,"+
                        "estado INTEGER(1) DEFAULT 1"
                )

cnn.create_table("sala","id_sala INTEGER PRIMARY KEY AUTOINCREMENT,"+
                    "tipo_sala TEXT,"+
                    "cantidad_butaca INTEGER,"+
                    "estado INTEGER(1) DEFAULT 1"
                )

cnn.create_table("butaca","id_butaca INTEGER PRIMARY KEY AUTOINCREMENT,"+
                          "id_sala INTEGER,"+
                          "serie TEXT(1),"+
                          "numero INTEGER,"+
                          "estado INTEGER(1) DEFAULT 1"
                )

cnn.create_table("descuento","id_descuento INTEGER PRIMARY KEY AUTOINCREMENT,"+
                          "dia TEXT,"+
                          "porcentaje INTEGER,"+   
                          "estado INTEGER(1) DEFAULT 1"                       
                )

cnn.create_table("rol","id_rol INTEGER PRIMARY KEY AUTOINCREMENT,"+
                        "nombre TEXT,"+
                        "descripcion TEXT,"+
                        "estado INTEGER(1) DEFAULT 1"
                )

cnn.create_table("usuario","id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,"+
                          "nombre TEXT,"+
                          "apellido TEXT,"+
                          "dni TEXT(11)," + 
                          "email TEXT,"+
                          "password TEXT,"+
                          "estado INTEGER(1) DEFAULT 1"
                )

cnn.create_table("persona","id_persona INTEGER PRIMARY KEY AUTOINCREMENT," +
                        "nombre TEXT(50)," +
                        "apellido TEXT(50)," +
                        "dni TEXT(11)," + 
                        "direccion TEXT(50)," +
                        "fecha_nacimiento TEXT(20)," +
                        "telefono TEXT(9)," +
                        "email TEXT(50)," +
                        "tipo_persona TEXT(20) DEFAULT 'Cliente'," +
                        "tipo_responsabilidad TEXT(30),"+
                        "estado INTEGER DEFAULT 1"
                ) 

cnn.create_table("reserva","id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,"+
                          "id_funcion INTEGER,"+
                          "id_usuario TEXT,"+
                          "fecha datetime,"+
                          "total REAL,"+
                          "cantidad INTEGER,"+
                          "estado INTEGER(1) DEFAULT 1"
                )

cnn.create_table("tarjeta","id_tarjeta INTEGER PRIMARY KEY AUTOINCREMENT,"+
                          "codigo TEXT,"+
                          "fecha datetime,"+
                          "id_usuario INTEGER,"+
                          "estado INTEGER(1) DEFAULT 1"
                )

cnn.close()