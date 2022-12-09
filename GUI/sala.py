import tkinter as tk
from tkinter import DISABLED, Frame,ttk
from tkcalendar import DateEntry

from Proyecto.Reserva.pelicula import Pelicula

class Sala(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sala")
        self.geometry("960x600")
        self.iconbitmap(r'GUI/source/img/icon.ico')
        self.resizable(0,0)
        self.columnconfigure(1, weight=2)
        self.img = tk.PhotoImage(file = r"GUI/source/img/cuadrado.png")
        self.img2 = tk.PhotoImage(file = r"GUI/source/img/cuadrado_relleno.png")
        self.img_pantalla = tk.PhotoImage(file = r"GUI/source/img/pantalla.png")
        self.entrada_frame = tk.Frame(self, width=400, height=50, bg='white')
        self.botones_frame = tk.Frame(self, width=300, height=350, bg='white')
        self.total = tk.Frame(self, width=400, height=50)
        self._create_label_input()

    def _create_label_input(self):
        form_frame = tk.Frame(self)
        form_frame.pack()

        # Fecha pelicula
        fecha_pelicula_etiqueta = ttk.Label(form_frame, text='Fecha de Pelicula:')
        fecha_pelicula_etiqueta.grid(row=0, column=0,sticky='W', padx=5, pady=10)
        fecha_pelicula_entrada = DateEntry(form_frame)
        fecha_pelicula_entrada.grid(row=0, column=1, sticky='EW', padx=5, pady=10)

        pelicula = Pelicula()
        peliculas = pelicula.peliculas_select()
        
        # Pelicula
        pelicula_etiqueta = ttk.Label(form_frame, text='Pelicula :')
        pelicula_etiqueta.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        pelicula_entrada = ttk.Combobox(form_frame, values = peliculas)
        pelicula_entrada.grid(row=1, column=1, sticky='EW', padx=5, pady=10)

        pelicula_entrada.bind("<<ComboboxSelected>>",lambda event: self.show(event))

        form_frame = tk.Frame(self)
        form_frame.pack(side=tk.BOTTOM)
        #Aceptar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        aceptar_boton = ttk.Button(form_frame, text='Aceptar')
        aceptar_boton.pack(side=tk.LEFT,padx = 6, pady = 10)
        #Cancelar
        cancelar_boton = ttk.Button(form_frame, text='Cancelar')
        cancelar_boton.pack(side=tk.RIGHT,padx = 6, pady = 10)


    def show(self,event):

        self.entrada_frame.destroy()
        self.botones_frame.destroy()
        self.total.destroy()

        self.entrada_frame = tk.Frame(self, width=400, height=50)
        self.entrada_frame.pack()

        cb = tk.Label(self.entrada_frame, image=self.img_pantalla)
        cb.grid(row=0, column=0, ipady=10)

        self.botones_frame = tk.Frame(self, width=300, height=350)
        self.botones_frame.pack()

        for j in range(1,6):
            for i in range(10):
                cb = tk.Checkbutton(self.botones_frame,text = f"{j}-{i+1}", variable = f"{i}{j}" ,image=self.img,compound='left',
                                selectimage=self.img2,indicatoron=False)
                cb.grid(row = j, column = i,padx = 10)
        
        self.total = tk.Frame(self, width=400, height=50)
        self.total.pack()
        # total
        total_etiqueta = ttk.Label(self.total, text='Total :')
        total_etiqueta.grid(row=1, column=0, sticky='W', padx=25, pady=50)
        total_entrada = ttk.Entry(self.total)
        total_entrada.grid(row=1, column=1, sticky='EW', padx=25, pady=50)








