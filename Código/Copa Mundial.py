# ===  Copa Mundial  === #

# Librerías

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

#--- colores ---#
azul = "#0E1DC4"
blanco = "#FFFFFF"
negro = "#0D0D0D"
verde_neon = "#00FF00"
gris = "#242424"
rojo = "#F40B0B"
gris_claro = "#CFCFCF"
turqueza = "#37B8B1"
amarillo = "#FFFC40"
anaranjado = "#FF7300"
verde = "#009929"
celeste = "#00C3EB"
azul_oscuro = "#003262"

lista_paises = []
lista_selecciones = []
lista_jugadores = []
lista_entrenadores = []


class Pais:

    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):

        if not (isinstance(codigo_fifa, str) and isinstance(nombre, str) and isinstance(continente, str)):
            print("Error: los parámetros deben ser str")
            return 
        elif not isinstance(ranking_fifa, int):
            print( "Error: el parámetro debe ser int")
            return 

        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa

    def mostrar_datos(self):
        print("Código FIFA del País: " + self.codigo_fifa)
        print("Nombre del País: " + self.nombre)
        print("Continente: " + self.continente)
        print("Ranking FIFA: " + str(self.ranking_fifa))
        print("")

    def actualizar_datos(self, codigo_fifa, nombre, continente, ranking_fifa):

        if not (isinstance(codigo_fifa, str) and isinstance(nombre, str) and isinstance(continente, str)):
            print("Error: los parámetros deben ser str")
            return 
        elif not isinstance(ranking_fifa, int):
            print( "Error: el parámetro debe ser int")
            return
        
        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa

    
        

    

class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        if not (isinstance(nombre, str) and isinstance(apellido, str) and isinstance(fecha_nacimiento, str) and isinstance(nacionalidad, str)):
            print("Error: los parámetros deben ser str")
            return

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad

    def mostrar_datos(self):
        print("Nombre: " + self.nombre + " " + self.apellido)
        print("Fecha de Nacimiento: " + self.fecha_nacimiento)
        print("Nacionalidad: " + self.nacionalidad)
        print("")


class Entrenador(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)

        if not (isinstance(licencia, str) and isinstance(sistema_juego, str)):
            print("Error: los parámetros deben ser str")
            return 
        elif not isinstance(experiencia_anios, int):
            print("Error: el parámetro debe ser int")
            return 

        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego

    def mostrar_datos(self):
        print("Nombre: " + self.nombre + " " + self.apellido)
        print("Fecha de Nacimiento: " + self.fecha_nacimiento)
        print("Nacionalidad: " + self.nacionalidad)
        print("Licencia: " + self.licencia)
        print("Experiencia: " + str(self.experiencia_anios))
        print("Sistema de Juego: " + self.sistema_juego)
        print("")

    def actualizar_datos(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego):
        if not (isinstance(nombre, str) and isinstance(apellido, str) and isinstance(fecha_nacimiento, str) and isinstance(nacionalidad, str)):
            print("Error: los parámetros deben ser str")
            return
        if not (isinstance(licencia, str) and isinstance(sistema_juego, str)):
            print("Error: los parámetros deben ser str")
            return 
        elif not isinstance(experiencia_anios, int):
            print("Error: el parámetro debe ser int")
            return

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego


class Futbolista(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)

        if not isinstance(posicion, str):
            print("Error: el parpametro debe ser str")
            return
        elif not (isinstance(dorsal, int) and isinstance(total_tarjetas_amarillas, int) and isinstance(total_tarjetas_rojas, int) and isinstance(goles, int) and isinstance(asistencias, int) and isinstance(puntaje_individual, int)):
            print( "Error: los parámetros deben ser int")
            return

        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.goles = goles
        self.asistencias = asistencias
        self.puntaje_individual = puntaje_individual

    def mostrar_datos(self):
        print("Nombre: " + self.nombre + " " + self.apellido)
        print("Fecha de Nacimiento: " + self.fecha_nacimiento)
        print("Nacionalidad: " + self.nacionalidad)
        print("Dorsal: " + str(self.dorsal))
        print("Posicion: " + self.posicion)
        print("Tarjetas Amarillas: " + str(self.total_tarjetas_amarillas))
        print("Tarjetas Rojas: " + str(self.total_tarjetas_rojas))
        print("Goles: " + str(self.goles))
        print("Asistencias: " + str(self.asistencias))
        print("Puntaje Individual: " + str(self.puntaje_individual))
        print("")

    def actualizar_datos(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):
        if not (isinstance(nombre, str) and isinstance(apellido, str) and isinstance(fecha_nacimiento, str) and isinstance(nacionalidad, str)):
            print("Error: los parámetros deben ser str")
            return
        if not isinstance(posicion, str):
            print("Error: el parpametro debe ser str")
            return
        elif not (isinstance(dorsal, int) and isinstance(total_tarjetas_amarillas, int) and isinstance(total_tarjetas_rojas, int) and isinstance(goles, int) and isinstance(asistencias, int) and isinstance(puntaje_individual, int)):
            print( "Error: los parámetros deben ser int")
            return
        
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.goles = goles
        self.asistencias = asistencias
        self.puntaje_individual = puntaje_individual

    def registrar_gol(self):
        self.goles += 1

    def registrar_asistencia(self):
        self.asistencias += 1

    def registrar_tarjetas(self, tipo):
        if not isinstance(tipo, str):
            print("Error: el parámetro debe ser de tipo str")
            return 
        
        if tipo == "amarilla":
            self.total_tarjetas_amarillas += 1
        elif tipo == "roja":
            self.total_tarjetas_rojas += 1
        else:
            return "Error: ingrese el tipo de tarjeta (amarilla o roja)"
        
        

class Seleccion:

    def __init__(self, codigo_equipo, pais, entrenador):
        
        if not isinstance(codigo_equipo, str):
            print("Error: el parámetro debe ser str")
            return
       

        self.codigo_equipo = codigo_equipo
        self.total_goles_a_favor = 0
        self.total_goles_en_contra = 0
        self.total_tarjetas_amarillas = 0
        self.total_tarjetas_rojas = 0
        self.fuerza_equipo = 0
        self.pais = pais
        self.entrenador = entrenador
        self.jugadores = []

    def mostrar_datos(self):
        print("Código de la Selección: " + self.codigo_equipo)
        print("País: " + self.pais.nombre)
        print("Entrenador: " + self.entrenador.nombre)
        print("Jugadores:")
        for futbolista in self.jugadores:
            print("Nombre: " + futbolista.nombre + " " + futbolista.apellido)
            print("Dorsal: " + str(futbolista.dorsal))
            print("")
        print("Goles a Favor: " + str(self.total_goles_a_favor))
        print("Goles en Contra: " + str(self.total_goles_en_contra))
        print("Tarjetas Amarillas: " + str(self.total_tarjetas_amarillas))
        print("Tarjetas Rojas: " + str(self.total_tarjetas_rojas))
        print("Fuerza de equipo: " + str(self.fuerza_equipo))
        print("")

    def agregar_jugador(self, futbolista):

        if len(self.jugadores) < 23:
            self.jugadores += [futbolista]
        else:
            return "Error: La plantilla ya cuenta con 23 jugadores"
        
    def eliminar_jugador(self, dorsal):
        lista_sin_jugador = []
        for jugador in self.jugadores:
            if jugador.dorsal != dorsal:
                lista_sin_jugador += [jugador]

        self.jugadores = lista_sin_jugador

    def asignar_entrenador(self, entrenador):

        self.entrenador = entrenador

    #def registrar_resultado(self,):
    #def calcular_fuerza_equipo(self):

class Partido:

    def __init__(self, id_partido, equipo_1, equipo_2, goles_equipo1, goles_equipo2, fase, fecha):
        if not (isinstance(fase, str) and isinstance(fecha, str)):
            print( "Error: los parámetros deben ser str")
            return
        elif not (isinstance(goles_equipo1, int) and isinstance(goles_equipo2, int)):
            print("Error: los parámetros deben ser int")
            return
        
        self.id = id_partido
        self.goles_equipo1 = goles_equipo1
        self.goles_equipo2 = goles_equipo2
        self.fase = fase
        self.fecha = fecha 
        equipo_1 = Seleccion()
        equipo_2 = Seleccion()
        

class Grupo:

    def __init__(self, nombre_grupo, equipos, partidos):

        if not isinstance(nombre_grupo, str):
            print("Error: el parámetro debe ser str")
            return

        self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []

class Fase:

    def __init__(self, nombre_fase, partidos):

        if not isinstance(nombre_fase, str):
            print("Error: el parámetro debe ser str")
            return 

        self.nombre_fase = nombre_fase
        self.partidos = []


class Mundial:

    def __init__(self, nombre, anio, paises, selecciones, grupos, fases, campeon):
        
        if not isinstance(nombre, str):
            print("Error: el parámetro debe ser str")
            return
        elif not isinstance(anio, int):
            print("Error: el parámetro debe ser int")
            return

        self.nombre = nombre
        self.anio = anio
        self.paises = []
        self.selecciones = []
        self.fases = []
        self.campeon = Seleccion()
        

#===== Interfas Gráfica =====#





class Pantalla_Principal(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("1535x930+-7+-0")
        self.title("Ventana")
        self.resizable(False, False)

        self.fondo()
        self.botones()


    def fondo(self):

        imagen_fondo = Image.open("pantalla_principal.png")
        imagen_fondo = imagen_fondo.resize((1535, 930))

        self.fondo = ImageTk.PhotoImage(imagen_fondo)
        label_fondo = tk.Label(self, image=self.fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    def botones(self):

        self.admin_paises_selecciones = tk.Button(self,
                                             text= "Administrar Países \ny Selecciones",
                                             font=(30),
                                             command= self.paises_selecciones)
        self.admin_paises_selecciones.place(x=457, y=328, width=292, height=125)

        self.admin_entrenadores_jugadores = tk.Button(self,
                                             text= "Administrar Entrenadores \ny Jugadores",
                                             font=(30),
                                             command= self.entrenadores_jugadores)
        self.admin_entrenadores_jugadores.place(x=774, y=328, width=292, height=125)
        
        self.config_mundial = tk.Button(self,
                                   text= "Configurar Mundial Países \n(Grupos)",
                                   font=(30),
                                   command= self.configurar_mundial)
        self.config_mundial.place(x=457, y=480, width=292, height=125)    

        self.boton_estadisticas = tk.Button(self,
                                 text= "Estadísticas / Ranking",
                                 font=(30),
                                 command= self.estadísticas)
        self.boton_estadisticas.place(x=774, y=480, width=292, height=125)

        self.jugar = tk.Button(self,
                          text= "Jugar Mundial",
                          font=(30),
                          command= self.jugar_mundial)
        self.jugar.place(x=517, y=636, width=481, height=71)

        self.registrar = tk.Button(self,
                                   text= "➕ Registrar País",
                                   font= ("Arial Balck", 20, "bold"),
                                   fg=blanco,
                                   bg=azul,
                                   activeforeground=negro,
                                   activebackground=azul,
                                   relief="raised",
                                   bd=5,
                                   cursor="hand2",
                                )
        self.registrar.place(x=40, y=80, width=400, height=60)

    def paises_selecciones(self):

        self.withdraw()
        Administrar_Paises_Selecciones()

    def entrenadores_jugadores(self):

        self.withdraw()
        Administrar_Entrenadores_Jugadores()

    def configurar_mundial(self):

        self.withdraw()
        Configuracion_Mundial()

    def jugar_mundial(self):
        self.withdraw()
        Jugar_Mundial()

    def estadísticas(self):

        self.withdraw()
        Estadisticas()

    
        
class Administrar_Paises_Selecciones(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        
        self.geometry("1535x930+-7+-0")
        self.title("Administrar Países y Selecciones")
        self.resizable(False, False)

        #self.fondo()

        self.labels()
        self.frames()

    """def fondo(self):

        imagen_fondo = Image.open("paises_selecciones.png")
        imagen_fondo.resize((1535, 930))

        self.fondo = ImageTk.PhotoImage(imagen_fondo)
        label_fondo = tk.Label(self, image=self.fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)"""

    def labels(self):
        
        label_azul = tk.Label(self,
                              bg=azul_oscuro)
        label_azul.place(x=0, y=0, width=300, height=1535)

        label_titulo1 = tk.Label(self,
                                 text="Administración",
                                 font=("Arial", 17, "bold"),
                                 bg=azul_oscuro,
                                 fg=blanco)
        label_titulo1.place(x=30, y=10, width=200, height=30)

        label_titulo2 = tk.Label(self,
                                 text="Países y Selecciones",
                                 font=("Arial", 11, "bold"),
                                 bg=azul_oscuro,
                                 fg=blanco)
        label_titulo2.place(x=30, y=40, width=200, height=20)

        label_texto = tk.Label(self,
                 text="Registre y Cree sus Paises y Selecciones aquí",
                 font=("Arial", 10, "bold"),
                 anchor="w")
        label_texto.place(x=320, y=40, width=600, height=20)
        

    def frames(self):

        frame_principal1 = tk.Frame(self,
                                    bd=1,
                                    relief="solid")
        frame_principal1.place(x=250, y=80, width=600, height=800)



        label_paises = tk.Label(self,
                                text="🌐 Países",
                                font=("Arial", 16),
                                fg=azul,
                                anchor="w")
        label_paises.place(x=270, y=84, width=200, height=30)

        frame_registrar_paises = tk.Frame(self,
                                          bd=1,
                                          relief="solid")
        frame_registrar_paises.place(x=270, y=120, width=560, height=300)

        label_registrar = tk.Label(self,
                                   text= "Registrar / Editar Paises",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_registrar.place(x=280, y=130, width=300, height=30)

        label_codigo = tk.Label(self,
                                   text= "Código FIFA:",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_codigo.place(x=280, y=170, width=300, height=30)

        label_nombre_pais = tk.Label(self,
                                   text= "Nombre del País:",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_nombre_pais.place(x=280, y=210, width=300, height=30)

        label_continente = tk.Label(self,
                                   text= "Continente:",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_continente.place(x=280, y=250, width=300, height=30)

        label_ranking = tk.Label(self,
                                   text= "Ranking FIFA:",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_ranking.place(x=280, y=290, width=300, height=30)


        self.entry_codigo = tk.Entry(self,
                                fg=gris,
                                insertwidth=1,
                                bd=1,
                                highlightcolor=azul,
                                highlightthickness=1)
        self.entry_codigo.insert(0, "Ej: CRC")
        self.entry_codigo.place(x=500, y=170, width=200, height=30)

        self.entry_codigo.bind("<FocusIn>", self.borrar_codigo)
        self.entry_codigo.bind("<FocusOut>", self.restaurar_codigo)


       
        self.entry_nombre = tk.Entry(self,
                                fg=gris,
                                insertwidth=1,
                                bd=1,
                                highlightcolor=azul,
                                highlightthickness=1)
        self.entry_nombre.insert(0, "Ej: Costa Rica")
        self.entry_nombre.place(x=500, y=210, width=300, height=30)

        self.entry_nombre.bind("<FocusIn>", self.borrar_nombre)
        self.entry_nombre.bind("<FocusOut>", self.restaurar_nombre)


        self.seleccion = tk.StringVar()

        continentes = ["América", "Europa", "África", "Oceanía"]
        self.conbobox_continente = ttk.Combobox(self,
                                          values=continentes,
                                          state="readonly",
                                          textvariable=self.seleccion)
        self.conbobox_continente.set("Seleccione un Continente")
        self.conbobox_continente.place(x=500, y=250, width=300, height=30)

        self.spinbox_ranking = tk.Spinbox(self,
                                     from_=1,
                                     to=100,
                                     width=300)

        self.spinbox_ranking.place(x=500, y=290, width=300, height=30)

        self.boton_añadir_pais = tk.Button(self,
                                           text="➕ Añadir País",
                                           font=("Arial", 14),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w",
                                           command=self.añadir)
        self.boton_añadir_pais.place(x=300, y=350, width=160, height=40)

        self.boton_guardar = tk.Button(self,
                                           text="💾 Guardar Cambios",
                                           font=("Arial", 14),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=azul,
                                           anchor="w")
        self.boton_guardar.place(x=480, y=350, width=170, height=40)

        self.boton_limpiar = tk.Button(self,
                                  text="🧹Limpiar",
                                  font=("Arial", 14),
                                  bd=2,
                                  relief= "groove",
                                  fg=gris,
                                  bg=amarillo,
                                  anchor="w")
        self.boton_limpiar.place(x=680, y=350, width=100, height=40)





        

        frame_paises_registrados = tk.LabelFrame(self,
                                          text="Nombre del Pais:",
                                          font=("Arial", 14),
                                          fg=azul,
                                          bd=1,
                                          relief="solid")
        frame_paises_registrados.place(x=270, y=460, width=560, height=400)







        

        frame_principal2 = tk.Frame(self,
                                    bd=1,
                                    relief="solid")
        frame_principal2.place(x=900, y=80, width=600, height=800)
    
    def borrar_codigo(self, event):
        if self.entry_codigo.get() == "Ej: CRC":
            self.entry_codigo.delete(0, "end")

    def restaurar_codigo(self, event):
        if self.entry_codigo.get() == "":
            self.entry_codigo.insert(0, "Ej: CRC")

    def borrar_nombre(self, event):
        if self.entry_nombre.get() == "Ej: Costa Rica":
            self.entry_nombre.delete(0, "end")

    def restaurar_nombre(self, event):
        if self.entry_nombre.get() == "":
            self.entry_nombre.insert(0, "Ej: Costa Rica")

    def añadir(self):


        global lista_paises
        codigo_fifa = self.entry_codigo.get()
        nombre = self.entry_nombre.get()
        continente = self.seleccion.get()
        ranking_fifa = int(self.spinbox_ranking.get())

        nuevo_pais = Pais(codigo_fifa, nombre, continente, ranking_fifa)
        lista_paises += [nuevo_pais]

        for pais in lista_paises:
            pais.mostrar_datos()


    #def actualizar(self):

    #def limpiar_selecciones(self):

        



    


class Administrar_Entrenadores_Jugadores(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("1535x930+-7+-0")
        self.resizable(False, False)

class Configuracion_Mundial(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("1535x930+-7+-0")
        self.resizable(False, False)
###JuSTIN
"""
Nombre: Jugar_Mundial
Entrada: no recibe datos directamente desde el usuario en esta primera versión
Salida: crea una ventana gráfica para la sección de jugar el mundial
Restricciones: 
"""
class Jugar_Mundial(tk.Toplevel):

    """
    Nombre: __init__
    Entrada: no recibe parámetros adicionales
    Salida: inicializa la ventana Jugar Mundial
    Restricciones: se debe llamar desde la pantalla principal del programa
    """
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.geometry("1535x760+-7+-0")
        self.title("Jugar Mundial")
        self.resizable(False, False)
        self.config(bg=blanco)

        self.menu_lateral()
        self.pantalla_titulo()
        self.estado_torneo()
        self.simular_mundial()
        self.resultados_recientes()
        self.tabla_grupo()
        self.campeon_actual()
        self.llave_eliminatoria()

    """
    Nombre: menu_lateral
    Entrada: no recibe parámetros
    Salida: crea el menú lateral izquierdo de la ventana
    Restricciones: usa colores globales previamente definidos
    """
    def menu_lateral(self):
        frame_menu = tk.Frame(self,
                              bg=azul_oscuro)
        frame_menu.place(x=0, y=0, width=300, height=760)

        label_titulo = tk.Label(self,
                                text="Copa Mundial",
                                font=("Arial", 24, "bold"),
                                bg=azul_oscuro,
                                fg=blanco)
        label_titulo.place(x=25, y=45, width=250, height=40)

        label_subtitulo = tk.Label(self,
                                   text="Simulación del Torneo",
                                   font=("Arial", 14, "bold"),
                                   bg=azul_oscuro,
                                   fg=blanco)
        label_subtitulo.place(x=25, y=85, width=250, height=30)

        boton_inicio = tk.Button(self,
                                 text="Inicio",
                                 font=("Arial", 14, "bold"),
                                 bg=azul_oscuro,
                                 fg=blanco,
                                 bd=1,
                                 relief="solid",
                                 anchor="w")
        boton_inicio.place(x=25, y=160, width=250, height=50)

        boton_paises = tk.Button(self,
                                 text="Países y Selecciones",
                                 font=("Arial", 13, "bold"),
                                 bg=azul_oscuro,
                                 fg=blanco,
                                 bd=1,
                                 relief="solid",
                                 anchor="w")
        boton_paises.place(x=25, y=225, width=250, height=50)

        boton_jugadores = tk.Button(self,
                                    text="Entrenadores y Jugadores",
                                    font=("Arial", 12, "bold"),
                                    bg=azul_oscuro,
                                    fg=blanco,
                                    bd=1,
                                    relief="solid",
                                    anchor="w")
        boton_jugadores.place(x=25, y=290, width=250, height=50)

        boton_configurar = tk.Button(self,
                                     text="Configurar Mundial",
                                     font=("Arial", 13, "bold"),
                                     bg=azul_oscuro,
                                     fg=blanco,
                                     bd=1,
                                     relief="solid",
                                     anchor="w")
        boton_configurar.place(x=25, y=355, width=250, height=50)

        boton_jugar = tk.Button(self,
                                text="Jugar Mundial",
                                font=("Arial", 14, "bold"),
                                bg=azul,
                                fg=blanco,
                                bd=1,
                                relief="solid",
                                anchor="w")
        boton_jugar.place(x=25, y=420, width=250, height=50)

        boton_estadisticas = tk.Button(self,
                                       text="Estadísticas",
                                       font=("Arial", 14, "bold"),
                                       bg=azul_oscuro,
                                       fg=blanco,
                                       bd=1,
                                       relief="solid",
                                       anchor="w")
        boton_estadisticas.place(x=25, y=485, width=250, height=50)

        label_decoracion = tk.Label(self,
                                    text="COPA\nMUNDIAL\n2026",
                                    font=("Arial", 28, "bold"),
                                    bg=azul_oscuro,
                                    fg=celeste)
        label_decoracion.place(x=25, y=610, width=250, height=120)

    """
    Nombre: pantalla_titulo
    Entrada: no recibe parámetros
    Salida: muestra el título y subtítulo de la pantalla
    Restricciones: debe existir la ventana Jugar Mundial
    """
    def pantalla_titulo(self):
        label_titulo = tk.Label(self,
                                text="Jugar Mundial",
                                font=("Arial", 32, "bold"),
                                bg=blanco,
                                fg=azul_oscuro,
                                anchor="w")
        label_titulo.place(x=340, y=25, width=500, height=55)

        label_subtitulo = tk.Label(self,
                                   text="Simule la fase de grupos y las rondas eliminatorias",
                                   font=("Arial", 14),
                                   bg=blanco,
                                   fg=gris,
                                   anchor="w")
        label_subtitulo.place(x=345, y=78, width=700, height=30)

    """
    Nombre: estado_torneo
    Entrada: no recibe parámetros
    Salida: crea el panel de estado general del torneo
    Restricciones:
    """
    def estado_torneo(self):
        frame_estado = tk.LabelFrame(self,
                                     text=" Estado del Torneo ",
                                     font=("Arial", 14, "bold"),
                                     fg=azul_oscuro,
                                     bg=blanco,
                                     bd=1,
                                     relief="solid")
        frame_estado.place(x=340, y=120, width=390, height=205)

        label_fase = tk.Label(frame_estado,
                              text="Fase actual:",
                              font=("Arial", 12),
                              bg=blanco,
                              anchor="w")
        label_fase.place(x=25, y=25, width=180, height=25)

        self.label_fase_actual = tk.Label(frame_estado,
                                          text="Sin iniciar",
                                          font=("Arial", 12, "bold"),
                                          bg=blanco,
                                          fg=azul,
                                          anchor="e")
        self.label_fase_actual.place(x=200, y=25, width=150, height=25)

        label_grupos = tk.Label(frame_estado,
                                text="Grupos configurados:",
                                font=("Arial", 12),
                                bg=blanco,
                                anchor="w")
        label_grupos.place(x=25, y=70, width=190, height=25)

        self.label_grupos = tk.Label(frame_estado,
                                     text="0",
                                     font=("Arial", 12, "bold"),
                                     bg=blanco,
                                     fg=azul,
                                     anchor="e")
        self.label_grupos.place(x=240, y=70, width=110, height=25)

        label_partidos = tk.Label(frame_estado,
                                  text="Partidos jugados:",
                                  font=("Arial", 12),
                                  bg=blanco,
                                  anchor="w")
        label_partidos.place(x=25, y=115, width=190, height=25)

        self.label_partidos = tk.Label(frame_estado,
                                       text="0",
                                       font=("Arial", 12, "bold"),
                                       bg=blanco,
                                       fg=azul,
                                       anchor="e")
        self.label_partidos.place(x=240, y=115, width=110, height=25)

        label_clasificados = tk.Label(frame_estado,
                                      text="Equipos clasificados:",
                                      font=("Arial", 12),
                                      bg=blanco,
                                      anchor="w")
        label_clasificados.place(x=25, y=160, width=190, height=25)

        self.label_clasificados = tk.Label(frame_estado,
                                           text="0",
                                           font=("Arial", 12, "bold"),
                                           bg=blanco,
                                           fg=azul,
                                           anchor="e")
        self.label_clasificados.place(x=240, y=160, width=110, height=25)

    """
    Nombre: simular_mundial
    Entrada: no recibe parámetros
    Salida: crea los botones principales para jugar el mundial
    Restricciones: 
    """
    def simular_mundial(self):
        frame_acciones = tk.LabelFrame(self,
                                       text=" Acciones ",
                                       font=("Arial", 14, "bold"),
                                       fg=azul_oscuro,
                                       bg=blanco,
                                       bd=1,
                                       relief="solid")
        frame_acciones.place(x=750, y=120, width=330, height=205)

        boton_grupos = tk.Button(frame_acciones,
                                 text="Simular Fase de Grupos",
                                 font=("Arial", 12, "bold"),
                                 bg=verde,
                                 fg=blanco,
                                 bd=2,
                                 relief="raised")
        boton_grupos.place(x=25, y=25, width=280, height=38)

        boton_fase = tk.Button(frame_acciones,
                               text="Avanzar a Siguiente Fase",
                               font=("Arial", 12, "bold"),
                               bg=gris_claro,
                               fg=negro,
                               bd=2,
                               relief="raised")
        boton_fase.place(x=25, y=70, width=280, height=38)

        boton_campeon = tk.Button(frame_acciones,
                                  text="Ver Campeón",
                                  font=("Arial", 12, "bold"),
                                  bg=amarillo,
                                  fg=negro,
                                  bd=2,
                                  relief="raised")
        boton_campeon.place(x=25, y=115, width=280, height=38)

        boton_volver = tk.Button(frame_acciones,
                                 text="Volver al Inicio",
                                 font=("Arial", 12, "bold"),
                                 bg=celeste,
                                 fg=negro,
                                 bd=2,
                                 relief="raised")
        boton_volver.place(x=25, y=160, width=280, height=30)

    """
    Nombre: resultados_recientes
    Entrada: no recibe parámetros.
    Salida: crea una tabla vacía para mostrar los resultados recientes
    Restricciones: 
    """
    def resultados_recientes(self):
        frame_resultados = tk.LabelFrame(self,
                                         text=" Resultados Recientes ",
                                         font=("Arial", 14, "bold"),
                                         fg=azul_oscuro,
                                         bg=blanco,
                                         bd=1,
                                         relief="solid")
        frame_resultados.place(x=340, y=345, width=740, height=205)

        self.tabla_resultados = ttk.Treeview(frame_resultados,
                                             columns=("partido", "fase", "resultado", "ganador"),
                                             show="headings",
                                             height=6)

        self.tabla_resultados.heading("partido", text="Partido")
        self.tabla_resultados.heading("fase", text="Fase")
        self.tabla_resultados.heading("resultado", text="Resultado")
        self.tabla_resultados.heading("ganador", text="Ganador")

        self.tabla_resultados.column("partido", width=260)
        self.tabla_resultados.column("fase", width=130)
        self.tabla_resultados.column("resultado", width=130)
        self.tabla_resultados.column("ganador", width=180)

        self.tabla_resultados.place(x=20, y=25, width=700, height=140)

    """
    Nombre: tabla_grupo
    Entrada: no recibe parámetros
    Salida: crea una tabla vacía para mostrar posiciones de grupos
    Restricciones: 
    """
    def tabla_grupo(self):
        frame_tabla = tk.LabelFrame(self,
                                    text=" Tabla de Grupo ",
                                    font=("Arial", 14, "bold"),
                                    fg=azul_oscuro,
                                    bg=blanco,
                                    bd=1,
                                    relief="solid")
        frame_tabla.place(x=340, y=575, width=620, height=160)

        self.tabla_posiciones = ttk.Treeview(frame_tabla,
                                             columns=("equipo", "pts", "gf", "gc", "dg"),
                                             show="headings",
                                             height=4)

        self.tabla_posiciones.heading("equipo", text="Equipo")
        self.tabla_posiciones.heading("pts", text="Pts")
        self.tabla_posiciones.heading("gf", text="GF")
        self.tabla_posiciones.heading("gc", text="GC")
        self.tabla_posiciones.heading("dg", text="DG")


        self.tabla_posiciones.column("equipo", width=260)
        self.tabla_posiciones.column("pts", width=70)
        self.tabla_posiciones.column("gf", width=70)
        self.tabla_posiciones.column("gc", width=70)
        self.tabla_posiciones.column("dg", width=70)

        self.tabla_posiciones.place(x=20, y=25, width=570, height=95)
    

    """
    Nombre: campeon_actual
    Entrada: no recibe parámetros.
    Salida: crea el panel visual del campeón actual.
    Restricciones: al inicio el campeón aparece sin definir
    """
    def campeon_actual(self):
        frame_campeon = tk.LabelFrame(self,
                                      text=" Campeón Actual ",
                                      font=("Arial", 14, "bold"),
                                      fg=azul_oscuro,
                                      bg="#FFF4C2",
                                      bd=2,
                                      relief="solid")
        frame_campeon.place(x=980, y=575, width=520, height=160)
        imagen_trofeo = Image.open("trofeo.jpg")
        imagen_trofeo = imagen_trofeo.resize((100, 100))

        self.imagen_trofeo = ImageTk.PhotoImage(imagen_trofeo)

        label_trofeo = tk.Label(frame_campeon,
                                image=self.imagen_trofeo,
                                bg="#FFF4C2")
        label_trofeo.place(x=35, y=25, width=140, height=120)

        self.label_campeon = tk.Label(frame_campeon,
                                      text="Sin definir",
                                      
                                      font=("Arial", 27, "bold"),
                                      bg="#FFF4C2",
                                      fg=azul_oscuro)
        self.label_campeon.place(x=200, y=35, width=280, height=45)

        linea = tk.Label(frame_campeon,
                         bg=anaranjado)
        linea.place(x=225, y=87, width=220, height=2)

        self.label_estado_campeon = tk.Label(frame_campeon,
                                             text="Esperando final",
                                             font=("Arial", 14, "italic"),
                                             bg="#FFF4C2",
                                             fg=gris)
        self.label_estado_campeon.place(x=200, y=98, width=280, height=30)
    
    """
    Nombre: llave_eliminatoria
    Entrada: no recibe parámetros.
    Salida: dibuja una llave eliminatoria básica.
    Restricciones: 
    """
    def llave_eliminatoria(self):
        frame_llave = tk.LabelFrame(self,
                                    text=" Llave Eliminatoria ",
                                    font=("Arial", 14, "bold"),
                                    fg=azul_oscuro,
                                    bg=blanco,
                                    bd=1,
                                    relief="solid")
        frame_llave.place(x=1100, y=120, width=400, height=430)

        canvas_llave = tk.Canvas(frame_llave,
                                 bg=blanco,
                                 highlightthickness=0)
        canvas_llave.place(x=10, y=10, width=370, height=385)




    


class Estadisticas(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)

        self.geometry("1535x930+-7+-0")
        self.resizable(False, False)




if __name__ == "__main__":
    app = Pantalla_Principal()
    app.mainloop()

    
    



