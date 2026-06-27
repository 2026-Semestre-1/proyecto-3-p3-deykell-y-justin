# ===  Copa Mundial  === #

# Librerías

import tkinter as tk
from tkinter import ttk, messagebox

from PIL import ImageTk, Image

import random

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
azul_seleccion = "#347083"


lista_paises = []
lista_selecciones = []
lista_jugadores = []
lista_entrenadores = []


# Función para contar elementos manualmente
def contar(elementos):
    cantidad = 0

    for elemento in elementos:
        cantidad = cantidad + 1

    return cantidad


# Convierte números a texto manualmente
def numero_a_texto(numero):
    resultado = ""

    if numero == 0:
        resultado = "0"

    while numero > 0:
        digito = numero % 10

        if digito == 0:
            resultado = "0" + resultado
        elif digito == 1:
            resultado = "1" + resultado
        elif digito == 2:
            resultado = "2" + resultado
        elif digito == 3:
            resultado = "3" + resultado
        elif digito == 4:
            resultado = "4" + resultado
        elif digito == 5:
            resultado = "5" + resultado
        elif digito == 6:
            resultado = "6" + resultado
        elif digito == 7:
            resultado = "7" + resultado
        elif digito == 8:
            resultado = "8" + resultado
        elif digito == 9:
            resultado = "9" + resultado

        numero = numero // 10

    return resultado




class Pais:

    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):

        if not (isinstance(codigo_fifa, str) and isinstance(nombre, str) and isinstance(continente, str)):
            print("Error: los parámetros deben ser str")
            return 
        elif not isinstance(ranking_fifa, int):
            print( "Error: el parámetro debe ser int")
            return 
        elif not 1 <= ranking_fifa <= 100:
            print("Error: el ranking fifa debe estar entre 1 y 100")
            return
        elif nombre == "" or continente == "" or codigo_fifa == "":
            print("Error: los parámetros no pueden estar vacíos")

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
        

archivo_paises = open("paises.txt", "r")
contenido_paises = archivo_paises.readlines()
archivo_paises.close()

archivo_selecciones = open("selecciones.txt", "r")
contenido_selecciones = archivo_selecciones.readlines()
archivo_selecciones.close()

archivo_entrenadores = open("entrenadores.txt", "r")
contenido_entrenadores = archivo_entrenadores.readlines()
archivo_entrenadores.close()

archivo_jugadores = open("jugadores.txt", "r")
contenido_jugadores = archivo_jugadores.readlines()
archivo_jugadores.close()

contenido_paises_dividido = [linea.strip().split(";") for linea in contenido_paises]

for linea in contenido_paises_dividido:
    nuevo_pais = Pais(linea[0], linea[1], linea[2], int(linea[3]))
    lista_paises += [nuevo_pais]

contenido_selecciones_dividido = [linea.strip().split(";") for linea in contenido_selecciones]

contenido_entrenadores_dividido = [linea.strip().split(";") for linea in contenido_entrenadores]


# Carga los jugadores guardados en jugadores.txt
def cargar_jugadores_archivo():

    global lista_jugadores

    for linea in contenido_jugadores:
        if linea.strip() != "":
            datos = linea.strip().split(";")

            if contar(datos) == 11:
                nombre = datos[0]
                apellido = datos[1]
                fecha_nacimiento = datos[2]
                nacionalidad = datos[3]
                dorsal = int(datos[4])
                posicion = datos[5]
                total_tarjetas_amarillas = int(datos[6])
                total_tarjetas_rojas = int(datos[7])
                goles = int(datos[8])
                asistencias = int(datos[9])
                puntaje_individual = int(datos[10])

                nuevo_jugador = Futbolista(nombre,
                                           apellido,
                                           fecha_nacimiento,
                                           nacionalidad,
                                           dorsal,
                                           posicion,
                                           total_tarjetas_amarillas,
                                           total_tarjetas_rojas,
                                           goles,
                                           asistencias,
                                           puntaje_individual)

                lista_jugadores += [nuevo_jugador]
            else:
                print("Error: una línea de jugadores.txt no tiene 11 datos")


cargar_jugadores_archivo()


#===== Interfas Gráfica =====#


class Pantalla_Principal(tk.Tk):

    def __init__(self):
        super().__init__()

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
        Administrar_Paises_Selecciones(self)

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

    def __init__(self, principal):
        super().__init__(principal)

        self.principal = principal
        
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

#Frame de la Izquierda

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

#Frame registrar países

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
        self.combobox_continente = ttk.Combobox(self,
                                          values=continentes,
                                          state="readonly",
                                          textvariable=self.seleccion)
        self.combobox_continente.set("Seleccione un Continente")
        self.combobox_continente.place(x=500, y=250, width=300, height=30)

        self.spinbox_ranking = tk.Spinbox(self,
                                     from_=1,
                                     to=100,
                                     width=300)

        self.spinbox_ranking.place(x=500, y=290, width=300, height=30)
        self.spinbox_ranking.delete(0, "end")

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
                                           anchor="w",
                                           command=self.actualizar,
                                           state="disabled")
        self.boton_guardar.place(x=480, y=350, width=170, height=40)

        self.boton_limpiar = tk.Button(self,
                                  text="🧹Limpiar",
                                  font=("Arial", 14),
                                  bd=2,
                                  relief= "groove",
                                  fg=gris,
                                  bg=amarillo,
                                  anchor="w",
                                  command=self.limpiar_selecciones)
        self.boton_limpiar.place(x=680, y=350, width=100, height=40)





#Frame de los países registrados

        frame_paises_registrados = tk.LabelFrame(self,
                                          text="Lista de Países Registrados",
                                          font=("Arial", 14),
                                          fg=azul,
                                          bd=1,
                                          relief="solid")
        frame_paises_registrados.place(x=270, y=460, width=560, height=400)

        label_total_paises = tk.Label(self,
                                      text=f"Total: {len(lista_paises)} paises",
                                      font=("Arial", 10, "bold"))
        label_total_paises.place(x=680, y=480, width=100, height=30)

        







#Frame de la derecha

        label_paises = tk.Label(self,
                                text="🌐 Selecciones",
                                font=("Arial", 16),
                                fg=azul,
                                anchor="w")
        label_paises.place(x=910, y=84, width=200, height=30)


        frame_principal2 = tk.Frame(self,
                                    bd=1,
                                    relief="solid")
        frame_principal2.place(x=900, y=80, width=600, height=800)
    
        frame_registrar_paises = tk.Frame(self,
                                          bd=1,
                                          relief="solid")
        frame_registrar_paises.place(x=920, y=120, width=560, height=300)

        label_registrar_seleccion = tk.Label(self,
                                   text= "Registrar / Editar Selección",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_registrar_seleccion.place(x=930, y=130, width=300, height=30)

        label_codigo = tk.Label(self,
                                   text= "Código Seleccción:",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_codigo.place(x=930, y=170, width=300, height=30)

        label_pais = tk.Label(self,
                                   text= "País:",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_pais.place(x=930, y=210, width=300, height=30)

        label_entrenador = tk.Label(self,
                                   text= "Entrenador:",
                                   font=("Arial", 10, "bold"),
                                   anchor="w")
        label_entrenador.place(x=930, y=250, width=300, height=30)

        self.entry_codigo_seleccion = tk.Entry(self,
                                fg=gris,
                                insertwidth=1,
                                bd=1,
                                highlightcolor=azul,
                                highlightthickness=1)
        self.entry_codigo_seleccion.insert(0, "Ej: CRC")
        self.entry_codigo_seleccion.place(x=1180, y=170, width=200, height=30)

        self.entry_codigo_seleccion.bind("<FocusIn>", self.borrar_codigo_seleccion)
        self.entry_codigo_seleccion.bind("<FocusOut>", self.restaurar_codigo_seleccion)

        self.pais_seleccion = tk.StringVar()
        paises = []

        for pais in lista_paises:
            paises += [pais.nombre]

        self.combobox_pais = ttk.Combobox(self,
                                          values=paises,
                                          state="readonly",
                                          textvariable=self.pais_seleccion)
        self.combobox_pais.set("Seleccione un pais")
        self.combobox_pais.place(x=1180, y=210, width=200, height=30)

        self.entrenador_seleccion = tk.StringVar()
        entrenadores = []

        for entrenador in lista_entrenadores:
            entrenadores += [entrenador.nombre]

        self.combobox_entrenador = ttk.Combobox(self,
                                          values=entrenadores,
                                          state="readonly",
                                          textvariable=self.entrenador_seleccion)
        self.combobox_entrenador.set("Seleccione un entrenador")
        self.combobox_entrenador.place(x=1180, y=250, width=200, height=30)



        self.boton_añadir_seleccion = tk.Button(self,
                                           text="➕ Añadir Selección",
                                           font=("Arial", 14),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w")
        self.boton_añadir_seleccion.place(x=940, y=350, width=190, height=40)

        self.boton_guardar_seleccion = tk.Button(self,
                                           text="💾 Guardar Cambios",
                                           font=("Arial", 14),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=azul,
                                           anchor="w")
        self.boton_guardar_seleccion.place(x=1150, y=350, width=170, height=40)

        self.boton_limpiar_seleccion = tk.Button(self,
                                  text="🧹Limpiar",
                                  font=("Arial", 14),
                                  bd=2,
                                  relief= "groove",
                                  fg=gris,
                                  bg=amarillo,
                                  anchor="w")
        self.boton_limpiar_seleccion.place(x=1350, y=350, width=100, height=40)


#Frame de los selecciones registrados

        frame_selecciones_registradas = tk.LabelFrame(self,
                                          text="Lista de Selecciones Registradas",
                                          font=("Arial", 14),
                                          fg=azul,
                                          bd=1,
                                          relief="solid")
        frame_selecciones_registradas.place(x=920, y=460, width=560, height=400)

        label_total_selecciones = tk.Label(self,
                                      text=f"Total: {len(lista_selecciones)} selecciones",
                                      font=("Arial", 10, "bold"))
        label_total_selecciones.place(x=1320, y=480, width=130, height=30)

        self.boton_volver = tk.Button(self, 
                                     text= "Regresar al menú principal",
                                     font= ("Arial Balck", 15, "bold"),
                                     fg=blanco,
                                     bg=gris_claro,
                                     activeforeground=negro,
                                     activebackground=gris,
                                     relief="flat",
                                     bd=5,
                                     cursor="hand2",
                                     command=self.volver)
        self.boton_volver.place(x=1200, y=20, width=300, height=40)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background= "#D3D3D3",
                        foreground= negro,
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        
        style.map("Treeview",
                   background= [("selected", azul_seleccion)])
        
        self.tree_frame = tk.Frame(self,
                                   bd=1,
                                   relief="flat")
        self.tree_frame.place(x=280, y=510, width=530, height=330) 

        tree_scroll = tk.Scrollbar(self.tree_frame)
        tree_scroll.pack(side="right", fill="y")
        
        self.tree_view = ttk.Treeview(self.tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        self.tree_view.pack()

        tree_scroll.config(command=self.tree_view.yview)

        self.tree_view["columns"] = ("codigo", "nombre", "continente", "ranking")

        self.tree_view.column("#0", width=0, stretch=False)
        self.tree_view.column("codigo", anchor="center", width=80)
        self.tree_view.column("nombre", anchor="w", width=180)
        self.tree_view.column("continente", anchor="w", width=160)
        self.tree_view.column("ranking", anchor="center", width=100)

        self.tree_view.heading("#0", text="", anchor="w")
        self.tree_view.heading("codigo", text="Código FIFA", anchor="center")
        self.tree_view.heading("nombre", text="Nombre", anchor="center")
        self.tree_view.heading("continente", text="Continente", anchor="center")
        self.tree_view.heading("ranking", text="Ranking fifa", anchor="center")

        self.tree_view.tag_configure("oddrow", background=blanco)
        self.tree_view.tag_configure("evenrow", background=celeste)


        numero = 0

        for pais in lista_paises:
            if numero % 2 == 0:
                self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(pais.codigo_fifa, pais.nombre, pais.continente, pais.ranking_fifa), tags=("evenrow",))
            else:
                self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(pais.codigo_fifa, pais.nombre, pais.continente, pais.ranking_fifa), tags=("oddrow",))
            numero += 1

        self.tree_view.bind("<ButtonRelease-1>", self.pais_seleccionado)

        











    def volver(self):
        self.destroy()
        self.principal.deiconify()


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

    def borrar_codigo_seleccion(self, event):
        if self.entry_codigo_seleccion.get() == "Ej: CRC":
            self.entry_codigo_seleccion.delete(0, "end")

    def restaurar_codigo_seleccion(self, event):
        if self.entry_codigo_seleccion.get() == "":
            self.entry_codigo_seleccion.insert(0, "Ej: CRC")

    def añadir(self):

        global lista_paises

        codigo_fifa = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        continente = self.seleccion.get().strip()
        ranking_fifa = self.spinbox_ranking.get().strip()



        if codigo_fifa == "Ej: CRC":
            messagebox.showerror("¡Error!", "Ingrese el código FIFA del país")
            return 
        elif nombre == "Ej: Costa Rica":
            messagebox.showerror("¡Error!", "Ingrese el nombre del país")
            return 
        elif continente == "Seleccione un Continente":
            messagebox.showerror("¡Error!", "Debe seleccionar un continente para el país")
            return 
        elif ranking_fifa == "":
            messagebox.showerror("¡Error!", "Debe ingresar el ranking FIFA del país")
            return 
        elif not len(codigo_fifa) == 3:
            messagebox.showerror("!Error¡", "El códifo FIFA debe contener 3 letras")
            return 
        

        codigo_fifa = codigo_fifa.upper()
        continente = continente.title()
        nombre = nombre.title()  
        ranking_fifa = int(ranking_fifa)

        for pais in lista_paises:
            if pais.nombre == nombre:
                messagebox.showerror("Error", "El el nombre del páis ingresado ya ha sido registrado")
                return 
            elif pais.codigo_fifa == codigo_fifa:
                messagebox.showerror("Error", "El código FIFA ingresado ya le ha sido asignado a un país")
                return 
            elif pais.ranking_fifa == ranking_fifa:
                messagebox.showerror("Error", "El ranking FIFA ingresado ya le ha sido asignado a un país")
                return


        if lista_paises == []:

            archivo = open("paises.txt", "a")
            linea = (f"{codigo_fifa};{nombre};{continente};{ranking_fifa}")
            archivo.write(linea)
            archivo.close()

            nuevo_pais = Pais(codigo_fifa, nombre, continente, ranking_fifa)
            lista_paises += [nuevo_pais]


            numero = len(lista_paises)

            if numero % 2 == 0:
                self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("evenrow",))
            else:
                self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("oddrow",))

            
            messagebox.showinfo(None, "País registrado correctamente")

            self.entry_codigo.delete(0, "end")
            self.entry_nombre.delete(0, "end")
            self.combobox_continente.delete(0, "end")
            self.spinbox_ranking.delete(0, "end")
            
            self.entry_codigo.insert(0, "Ej: CRC")
            self.entry_nombre.insert(0, "Ej: Costa Rica")
            self.combobox_continente.set("Seleccione un Continente")
            return

            
        archivo = open("paises.txt", "a")
        linea = (f"\n{codigo_fifa};{nombre};{continente};{ranking_fifa}")
        archivo.write(linea)
        archivo.close()

        nuevo_pais = Pais(codigo_fifa, nombre, continente, ranking_fifa)
        lista_paises += [nuevo_pais]


        numero = len(lista_paises) - 1

        if numero % 2 == 0:
            self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("evenrow",))
        else:
            self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("oddrow",))

        messagebox.showinfo(None, "País registrado correctamente")
        

        self.entry_codigo.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.combobox_continente.delete(0, "end")
        self.spinbox_ranking.delete(0, "end")
            
        self.entry_codigo.insert(0, "Ej: CRC")
        self.entry_nombre.insert(0, "Ej: Costa Rica")
        self.combobox_continente.set("Seleccione un Continente")
        
        for pais in lista_paises:
            pais.mostrar_datos()

    def actualizar(self):
       
        global lista_paises

        codigo_fifa = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        continente = self.seleccion.get().strip()
        ranking_fifa = self.spinbox_ranking.get().strip()


        if codigo_fifa == "Ej: CRC":
            messagebox.showerror("¡Error!", "Ingrese el código FIFA del país")
            return 
        elif nombre == "Ej: Costa Rica":
            messagebox.showerror("¡Error!", "Ingrese el nombre del país")
            return 
        elif continente == "Seleccione un Continente":
            messagebox.showerror("¡Error!", "Debe seleccionar un continente para el país")
            return 
        elif ranking_fifa == "":
            messagebox.showerror("¡Error!", "Debe ingresar el ranking FIFA del país")
            return 
        elif not len(codigo_fifa) == 3:
            messagebox.showerror("!Error¡", "El códifo FIFA debe contener 3 letras")
            return 
        

        codigo_fifa = codigo_fifa.upper()
        continente = continente.title()
        nombre = nombre.title()  
        ranking_fifa = int(ranking_fifa)

        archivo_paises = open("paises.txt", "r")
        contenido_paises = archivo_paises.readlines()
        archivo_paises.close()

        contenido_paises_dividido = [linea.strip().split(";") for linea in contenido_paises]

        for pais in lista_paises:
            if pais.nombre == nombre and pais.codigo_fifa == codigo_fifa:
                pais.actualizar_datos(codigo_fifa, nombre, continente, ranking_fifa)
                break
        

        for pais in contenido_paises_dividido:
            if  pais[0] == codigo_fifa:
                pais[3] = str(ranking_fifa)
                break

        archivo_paises_modificar = open("paises.txt", "w")

        for pais in contenido_paises_dividido:
            linea = f"{pais[0]};{pais[1]};{pais[2]};{pais[3]}\n"
            archivo_paises_modificar.write(linea)

        archivo_paises_modificar.close()

        selected = self.tree_view.focus()

        self.tree_view.item(selected, text="", values=(codigo_fifa, nombre, continente, ranking_fifa))

        messagebox.showinfo(None, "País actualizado correctamente")
        self.limpiar_selecciones()

    



    
    def limpiar_selecciones(self):
            
            self.entry_codigo.config(state="normal")
            self.entry_nombre.config(state="normal")
            self.boton_guardar.config(state="disabled")
            self.boton_añadir_pais.config(state="normal")
            self.combobox_continente.config(state="readonly")
            
            self.entry_codigo.delete(0, "end")
            self.entry_nombre.delete(0, "end")
            self.combobox_continente.delete(0, "end")
            self.spinbox_ranking.delete(0, "end")
            
            self.entry_codigo.insert(0, "Ej: CRC")
            self.entry_nombre.insert(0, "Ej: Costa Rica")
            self.combobox_continente.set("Seleccione un Continente")



    def pais_seleccionado(self, e=None):  

        self.entry_codigo.config(state="normal")
        self.entry_nombre.config(state="normal")  
            
        self.entry_codigo.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.combobox_continente.delete(0, "end")
        self.spinbox_ranking.delete(0, "end")
    
        selected = self.tree_view.focus()
    
        values = self.tree_view.item(selected, "values")
        if not values or len(values) < 4:
            return 
    
        self.entry_codigo.insert(0, values[0])
        self.entry_nombre.insert(0, values[1])
        self.combobox_continente.set(values[2])
        self.spinbox_ranking.insert(0, values[3])

        self.entry_codigo.config(state="disabled")
        self.entry_nombre.config(state="disabled")
        self.boton_guardar.config(state="active")
        self.boton_añadir_pais.config(state="disabled")
        self.combobox_continente.config(state="disabled")




    


class Administrar_Entrenadores_Jugadores(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("1535x930+-7+-0")
        self.resizable(False, False)
        self.title("Administración de Entrenadores y Jugadores")

        self.frames()


    def frames(self):

        global lista_paises
        global lista_entrenadores
        global lista_jugadores

        self.frame_grande = tk.Frame(self,
                                     bd=1,
                                     relief="solid",
                                     bg=gris_claro)
        self.frame_grande.place(x=10, y=10, width=1515, height=830)

#Frame arriba izquierda

        self.frame_registrar_entrenadores = tk.Frame(self, 
                                                     bd=1, 
                                                     relief="solid")
        self.frame_registrar_entrenadores.place(x=30, y=20, width=550, height=400)

        label_titulo_registrar = tk.Label(self, 
                                          text="📋 Registrar / Editar Entrenador",
                                          font=("arial", 12, "bold"),
                                          anchor="w",
                                          fg=azul)
        label_titulo_registrar.place(x=35, y=40, width=400, height=30)

        label_personales_entrenador = tk.Label(self,
                                               text="Datos Personales del Entrenador",
                                               font=("arial", 10, "bold"),
                                               anchor="w")
        label_personales_entrenador.place(x=40, y=80, width=300, height=30)

        label_nombre_entrenador = tk.Label(self,
                                           text="Nombre:",
                                           font=("arial", 10, "bold"),
                                           anchor="w")
        label_nombre_entrenador.place(x=35, y=120, width=150, height=30)

        label_apellidos_entrenador = tk.Label(self, 
                                              text="Apellidos:",
                                              font=("arial", 10, "bold"),
                                              anchor="w")
        label_apellidos_entrenador.place(x=35, y=160, width=150, height=30)

        label_nacionalidad_entrenador = tk.Label(self,
                                                 text="Nacionalidad:",
                                                 font=("arial", 10, "bold"),
                                                 anchor="w")
        label_nacionalidad_entrenador.place(x=35, y=200, width=150, height=30)

        label_fecha_entrenador = tk.Label(self,
                                          text="Fecha de Nacimiento:",
                                          font=("arial", 10, "bold"),
                                          anchor="w")
        label_fecha_entrenador.place(x=35, y=240, width=200, height=30)

        self.entry_nombre_entrenador = tk.Entry(self, 
                                                fg=gris,
                                                insertwidth=1,
                                                bd=1,
                                                highlightcolor=azul,
                                                highlightthickness=1)
        self.entry_nombre_entrenador.insert(0, "Ej: Carlo")
        self.entry_nombre_entrenador.place(x=145, y=120, width=155, height=30)

        self.entry_apellidos_entrenador = tk.Entry(self,
                                fg=gris,
                                insertwidth=1,
                                bd=1,
                                highlightcolor=azul,
                                highlightthickness=1)
        self.entry_apellidos_entrenador.insert(0, "Ej: Ancelotti")
        self.entry_apellidos_entrenador.place(x=145, y=160, width=155, height=30)                                          


        self.seleccion_nacionalidad_entrenador = tk.StringVar()

        paises = []

        for pais in lista_paises:
            paises += [pais.nombre]

        self.combobox_nacionalidad_entrenador = ttk.Combobox(self,
                                          values=paises,
                                          state="readonly",
                                          textvariable=self.seleccion_nacionalidad_entrenador)
        self.combobox_nacionalidad_entrenador.set("Seleccione Nacionalidad")
        self.combobox_nacionalidad_entrenador.place(x=145, y=200, width=155, height=30)

        lista_dias = []

        for i in range(1, 32):
            lista_dias += [i]

        self.dia_seleccionado = tk.StringVar()

        self.combobox_dias = ttk.Combobox(self, 
                                          values=lista_dias,
                                          state="readonly",
                                          textvariable=self.dia_seleccionado)
        self.combobox_dias.set("Día")
        self.combobox_dias.place(x=50, y=270, width=60, height=30)

        meses = []

        for i in range(1, 13):
            meses += [i]
        
        self.mes_seleccionado = tk.StringVar()
        self.combobox_meses = ttk.Combobox(self,
                                           values=meses,
                                           state="readonly",
                                           textvariable=self.mes_seleccionado)
        self.combobox_meses.set("Mes")
        self.combobox_meses.place(x=110, y=270, width=100, height=30)

        años = []

        for i in range(1950, 2027):
            años += [i]

        self.año_seleccionado = tk.StringVar()

        self.combobox_año = ttk.Combobox(self,
                                         values=años,
                                         state="readonly",
                                         textvariable=self.año_seleccionado)
        self.combobox_año.set("Año")
        self.combobox_año.place(x=210, y=270, width=90, height=30)

        self.boton_añadir_entrenador = tk.Button(self,
                                           text="➕ Añadir Entrenador",
                                           font=("Arial", 13),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w",
                                           command=self.agregar_entrenador)
        self.boton_añadir_entrenador.place(x=50, y=350, width=170, height=40)

        self.boton_modificar_entrenador = tk.Button(self,
                                           text="💾 Guardar Cambios",
                                           font=("Arial", 13),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=azul,
                                           anchor="w")
        self.boton_modificar_entrenador.place(x=240, y=350, width=170, height=40)

        self.boton_limpiar_seleccion_entrenador = tk.Button(self,
                                  text="🧹Limpiar",
                                  font=("Arial", 13),
                                  bd=2,
                                  relief= "groove",
                                  fg=gris,
                                  bg=amarillo,
                                  anchor="w")
        self.boton_limpiar_seleccion_entrenador.place(x=430, y=350, width=100, height=40)

        label_datos_entrenador = tk.Label(self,
                                               text="Datos del Entrenador",
                                               font=("arial", 10, "bold"),
                                               anchor="w")
        label_datos_entrenador.place(x=320, y=80, width=230, height=30)

        label_licencia = tk.Label(self,
                                               text="Licencia:",
                                               font=("arial", 10, "bold"),
                                               anchor="w")
        label_licencia.place(x=320, y=120, width=150, height=30)

        label_experiencia = tk.Label(self,
                                           text="Experiencia:",
                                           font=("arial", 10, "bold"),
                                           anchor="w")
        label_experiencia.place(x=320, y=180, width=150, height=30)

        label_sistema_juego = tk.Label(self, 
                                              text="Sistema de Juego:",
                                              font=("arial", 10, "bold"),
                                              anchor="w")
        label_sistema_juego.place(x=320, y=240, width=150, height=30)

        self.seleccion_licencia = tk.StringVar()
        licencias = ["UEFA PRO", "UEFA A", "UEFA B", "UEFA C"]
        self.combobox_licencia = ttk.Combobox(self,
                                              values=licencias,
                                              state="readonly",
                                              textvariable=self.seleccion_licencia)
        self.combobox_licencia.set("Seleccione Licencia")
        self.combobox_licencia.place(x=420, y=120, width=150, height=30)

        self.spinbox_experiencia = tk.Spinbox(self,
                                              from_=1,
                                              to=50)
        self.spinbox_experiencia.delete(0, "end")
        self.spinbox_experiencia.place(x=420, y=180, width=150, height=30)

        self.seleccion_sistema_juego = tk.StringVar()
        sistemas_juego = ["4-3-3", "4-4-2", "4-2-3-1","3-5-2", "5-3-2", "3-4-3", "4-1-4-1", "3-2-5"]
        self.combobox_sistema_juego = ttk.Combobox(self,
                                                   values=sistemas_juego,
                                                   state="readonly",
                                                   textvariable=self.seleccion_sistema_juego)
        self.combobox_sistema_juego.set("Seleccione Sistema")
        self.combobox_sistema_juego.place(x=447, y=240, width=123, height=30)






#Frame linea vertical

        frame_linea_vertical = tk.Frame(self,
                                        bd=1,
                                        relief="solid")
        frame_linea_vertical.place(x=310, y=90, width=2, height=210)


#Frame arriba centro


        self.frame_asignar_seleccion = tk.Frame(self,
                                                bd=1,
                                                relief="solid")
        self.frame_asignar_seleccion.place(x=590, y=20, width=350, height=400)

        label_asignar_pais = tk.Label(self,
                                      text="👤 Asignar Entrenador a Selección",
                                      fg=azul,
                                      font=("arial", 12, "bold"),
                                      anchor="w")
        label_asignar_pais.place(x=620, y=60, width=290, height=30)

        label_seleccion = tk.Label(self,
                                   text="Selección:",
                                   font=("arial", 10, "bold"),
                                   anchor="w")
        label_seleccion.place(x=620, y=140, width=100, height=30)

        label_entrenador = tk.Label(self,
                                   text="Entrenador:",
                                   font=("arial", 10, "bold"),
                                   anchor="w")
        label_entrenador.place(x=620, y=200, width=100, height=30)

        self.obtener_entrenador_para_seleccion = tk.StringVar()

        self.combobox_seleccion_entrenador = ttk.Combobox(self,
                                          values=paises,
                                          state="readonly",
                                          textvariable=self.obtener_entrenador_para_seleccion)
        self.combobox_seleccion_entrenador.set("Seleccione Selección")
        self.combobox_seleccion_entrenador.place(x=720, y=140, width=150, height=30)

        self.obtener_seleccion_para_entrenador = tk.StringVar()
        entrenadores = []
        for entrenador in lista_entrenadores:
            entrenadores += [entrenador.nombre]


        self.seleccion_entrenador_seleccion = ttk.Combobox(self,
                                          values=entrenadores,
                                          state="readonly",
                                          textvariable=self.obtener_seleccion_para_entrenador)

        self.seleccion_entrenador_seleccion.set("Seleccione Entrenador")
        self.seleccion_entrenador_seleccion.place(x=720, y=200, width=150, height=30)

        self.boton_asignar_entrenador_seleccion = tk.Button(self,
                                           text="➕ Asignar Entrenador a Selección",
                                           font=("Arial", 13),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w")
        self.boton_asignar_entrenador_seleccion.place(x=620, y=350, width=290, height=40)

#Frame arriba derecha


        self.frame_entrenadores = tk.Frame(self,
                                           bd=1,
                                           relief="solid")
        self.frame_entrenadores.place(x=950, y=20, width=560, height=400)


#Frame abajo izquierda

        self.frame_registrar_jugadores = tk.Frame(self,
                                                  bd=1,
                                                  relief="solid")
        self.frame_registrar_jugadores.place(x=30, y=430, width=600, height=400)

        label_titulo_registrar_jugador = tk.Label(self, 
                                          text="📋 Registrar / Editar Jugador",
                                          font=("arial", 12, "bold"),
                                          anchor="w",
                                          fg=azul)
        label_titulo_registrar_jugador.place(x=35, y=460, width=400, height=30)

        label_personales_jugadores = tk.Label(self,
                                               text="Datos Personales del Jugador",
                                               font=("arial", 10, "bold"),
                                               anchor="w")
        label_personales_jugadores.place(x=40, y=500, width=300, height=30)

        label_nombre_jugador = tk.Label(self,
                                           text="Nombre:",
                                           font=("arial", 10, "bold"),
                                           anchor="w")
        label_nombre_jugador.place(x=35, y=540, width=150, height=30)

        label_apellidos_jugador = tk.Label(self, 
                                              text="Apellidos:",
                                              font=("arial", 10, "bold"),
                                              anchor="w")
        label_apellidos_jugador.place(x=35, y=580, width=150, height=30)

        label_nacionalidad_jugador = tk.Label(self,
                                                 text="Nacionalidad:",
                                                 font=("arial", 10, "bold"),
                                                 anchor="w")
        label_nacionalidad_jugador.place(x=35, y=620, width=150, height=30)

        label_fecha_jugador = tk.Label(self,
                                          text="Fecha de Nacimiento:",
                                          font=("arial", 10, "bold"),
                                          anchor="w")
        label_fecha_jugador.place(x=35, y=660, width=200, height=30)


        self.entry_nombre_jugador = tk.Entry(self, 
                                                fg=gris,
                                                insertwidth=1,
                                                bd=1,
                                                highlightcolor=azul,
                                                highlightthickness=1)
        self.entry_nombre_jugador.insert(0, "Ej: Lionel")
        self.entry_nombre_jugador.place(x=145, y=540, width=155, height=30)

        self.entry_apellidos_jugador = tk.Entry(self,
                                fg=gris,
                                insertwidth=1,
                                bd=1,
                                highlightcolor=azul,
                                highlightthickness=1)
        self.entry_apellidos_jugador.insert(0, "Ej: Messi")
        self.entry_apellidos_jugador.place(x=145, y=580, width=155, height=30)

        self.combobox_nacionalidad_jugador= ttk.Combobox()
                                          


        self.seleccion_nacionalidad_jugador = tk.StringVar()

        self.combobox_nacionalidad_jugador = ttk.Combobox(self,
                                          values=paises,
                                          state="readonly",
                                          textvariable=self.seleccion_nacionalidad_jugador)
        self.combobox_nacionalidad_jugador.set("Seleccione Nacionalidad")
        self.combobox_nacionalidad_jugador.place(x=145, y=620, width=155, height=30)



        self.dia_seleccionado_jugador = tk.StringVar()

        self.combobox_dias_jugador = ttk.Combobox(self, 
                                          values=lista_dias,
                                          state="readonly",
                                          textvariable=self.dia_seleccionado_jugador)
        self.combobox_dias_jugador.set("Día")
        self.combobox_dias_jugador.place(x=50, y=690, width=60, height=30)

        self.mes_seleccionado_jugador = tk.StringVar()
        self.combobox_meses_jugador = ttk.Combobox(self,
                                           values=meses,
                                           state="readonly",
                                           textvariable=self.mes_seleccionado_jugador)
        self.combobox_meses_jugador.set("Mes")
        self.combobox_meses_jugador.place(x=110, y=690, width=100, height=30)


        self.año_seleccionado_jugador = tk.StringVar()

        self.combobox_año_jugador = ttk.Combobox(self,
                                         values=años,
                                         state="readonly",
                                         textvariable=self.año_seleccionado_jugador)
        self.combobox_año_jugador.set("Año")
        self.combobox_año_jugador.place(x=210, y=690, width=90, height=30)

#Frame linea vertical

        frame_linea_vertical_jugadores = tk.Frame(self,
                                        bd=1,
                                        relief="solid")
        frame_linea_vertical_jugadores.place(x=310, y=440, width=2, height=270)

        label_datos_jugador = tk.Label(self,
                                               text="Datos del Jugador",
                                               font=("arial", 10, "bold"),
                                               anchor="w")
        label_datos_jugador.place(x=320, y=440, width=230, height=30)

        label_dorsal = tk.Label(self,
                                text="Dorsal:",
                                font=("arial", 10, "bold"),
                                anchor="w")
        label_dorsal.place(x=320, y=470, width=150, height=30)

        self.spinbox_dorsal = tk.Spinbox(self,
                                         from_=1,
                                         to=99)
        self.spinbox_dorsal.delete(0, "end")
        self.spinbox_dorsal.place(x=400, y=470, width=120, height=30)

        label_posicion = tk.Label(self,
                                text="Posicion:",
                                font=("arial", 10, "bold"),
                                anchor="w")
        label_posicion.place(x=320, y=510, width=150, height=30)

        posiciones = ["Portero", "Defensa Central", "Lateral Izquierdo", "Lateral Derecho", "Interior Izquierdo", "Interior Derecho", "Extremo Izquierdo", "Extremo Derecho", "Mediocentro", "Delantero Derecho", "Delantero Izquierdo", "Delantero Centro"]
        self.obtener_posicion = tk.StringVar()

        self.combobox_posiciones = ttk.Combobox(self,
                                                values=posiciones,
                                                state="readonly",
                                                textvariable=self.obtener_posicion)
        self.combobox_posiciones.set("Seleccione Posicion")
        self.combobox_posiciones.place(x=400, y=510, width=130, height=30)

#Frame linea horizontal

        frame_linea_horizontal_jugadores = tk.Frame(self,
                                        bd=1,
                                        relief="solid")
        frame_linea_horizontal_jugadores.place(x=320, y=550, width=250, height=2)    

        label_velocidad = tk.Label(self,
                                text="Velocidad:",
                                font=("arial", 10, "bold"),
                                anchor="w")
        label_velocidad.place(x=320, y=570, width=150, height=30)

        self.spinbox_velocidad = tk.Spinbox(self,
                                         from_=1,
                                         to=25)
        self.spinbox_velocidad.delete(0, "end")
        self.spinbox_velocidad.place(x=460, y=570, width=100, height=30)

        label_estratega = tk.Label(self,
                                text="Estratega:",
                                font=("arial", 10, "bold"),
                                anchor="w")
        label_estratega.place(x=320, y=610, width=150, height=30)

        self.spinbox_estratega = tk.Spinbox(self,
                                         from_=1,
                                         to=25)
        self.spinbox_estratega.delete(0, "end")
        self.spinbox_estratega.place(x=460, y=610, width=100, height=30)

        label_dominio = tk.Label(self,
                                text="Dominio del Balón:",
                                font=("arial", 10, "bold"),
                                anchor="w")
        label_dominio.place(x=320, y=650, width=150, height=30)

        self.spinbox_dominio = tk.Spinbox(self,
                                         from_=1,
                                         to=25)
        self.spinbox_dominio.delete(0, "end")
        self.spinbox_dominio.place(x=460, y=650, width=100, height=30)

        label_fuerza = tk.Label(self,
                                text="Fuerza:",
                                font=("arial", 10, "bold"),
                                anchor="w")
        label_fuerza.place(x=320, y=690, width=150, height=30)

        self.spinbox_fuerza = tk.Spinbox(self,
                                         from_=1,
                                         to=25)
        self.spinbox_fuerza.delete(0, "end")
        self.spinbox_fuerza.place(x=460, y=690, width=100, height=30)

        self.boton_añadir_jugador = tk.Button(self,
                                           text="➕ Añadir Jugador",
                                           font=("Arial", 13),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w",
                                           command=self.añadir_jugador)
        self.boton_añadir_jugador.place(x=50, y=770, width=170, height=40)

        self.boton_modificar_jugador = tk.Button(self,
                                           text="💾 Guardar Cambios",
                                           font=("Arial", 13),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=azul,
                                           anchor="w")
        self.boton_modificar_jugador.place(x=240, y=770, width=170, height=40)

        self.boton_limpiar_seleccion_jugador = tk.Button(self,
                                  text="🧹Limpiar",
                                  font=("Arial", 13),
                                  bd=2,
                                  relief= "groove",
                                  fg=gris,
                                  bg=amarillo,
                                  anchor="w",
                                  command=self.limpiar_jugador)
        self.boton_limpiar_seleccion_jugador.place(x=430, y=770, width=100, height=40)


#Frame abajo centro

        self.frame_seleccion = tk.Frame(self,
                                        bd=1,
                                        relief="solid")
        self.frame_seleccion.place(x=640, y=430, width=300, height=400)

        label_asignar_seleccion = tk.Label(self, 
                                          text="👤 Asignar Entrenador a Selección",
                                          font=("arial", 12, "bold"),
                                          anchor="w",
                                          fg=azul)
        label_asignar_seleccion.place(x=660, y=435, width=270, height=40)

        label_jugador = tk.Label(self, 
                                          text="Jugador:",
                                          font=("arial", 10, "bold"),
                                          anchor="w")
        label_jugador.place(x=660, y=490, width=270, height=40)

        self.obtener_jugador = tk.StringVar()
        jugadores = []
        for jugador in lista_jugadores:
            jugadores += [f"{jugador.nombre} {jugador.apellido}"]

        self.combobox_jugadores = ttk.Combobox(self,
                                               values=jugadores,
                                               state="readonly",
                                               textvariable=self.obtener_jugador)
        self.combobox_jugadores.set("Seleccione Jugador")
        self.combobox_jugadores.place(x=760, y=490, width=150, height=30)

        self.obtener_pais_de_jugador = tk.StringVar()

        label_pais = tk.Label(self, 
                                          text="Selección:",
                                          font=("arial", 10, "bold"),
                                          anchor="w")
        label_pais.place(x=660, y=530, width=270, height=40)

        self.combobox_paises = ttk.Combobox(self,
                                               values=paises,
                                               state="readonly",
                                               textvariable=self.obtener_pais_de_jugador)
        self.combobox_paises.set("Seleccione Selección")
        self.combobox_paises.place(x=760, y=530, width=150, height=30)

        self.boton_asignar_jugador_a_seleccion = tk.Button(self,
                                           text="➕ Asignar Jugador a Selección",
                                           font=("Arial", 13),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w")
        self.boton_asignar_jugador_a_seleccion.place(x=655, y=580, width=270, height=40)

#Frame linea horizontal

        frame_linea_horizontal_jugadores_selecciones = tk.Frame(self,
                                                                bd=1,
                                                                relief="solid")
        frame_linea_horizontal_jugadores_selecciones.place(x=650, y=640, width=280, height=2)

        label_ver_jugadores = tk.Label(self, 
                                          text="Ver Jugadores por Selección",
                                          font=("arial", 12, "bold"),
                                          anchor="w",
                                          fg=azul)
        label_ver_jugadores.place(x=670, y=650, width=250, height=40)

        self.combobox_selecciones = ttk.Combobox(self,
                                               values=paises,
                                               state="readonly",
                                               textvariable=self.obtener_pais_de_jugador)
        self.combobox_selecciones.set("Seleccione Selección")
        self.combobox_selecciones.place(x=710, y=690, width=150, height=30)

        self.boton_ver_jugadoress = tk.Button(self,
                                           text="Ver Jugadores",
                                           font=("Arial", 13),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="center")
        self.boton_ver_jugadoress.place(x=655, y=760, width=270, height=40)
        self.frame_jugadores = tk.Frame(self,
                                        bd=1,
                                        relief="solid")
        self.frame_jugadores.place(x=950, y=430, width=560, height=400)

        self.crear_tabla_jugadores_registrados()


    def agregar_entrenador(self):

        global lista_entrenadores
        
        nombre = self.entry_nombre_entrenador.get().strip()
        apellido = self.entry_apellidos_entrenador.get().strip()
        nacionalidad = self.seleccion_nacionalidad_entrenador.get().strip()
        dia = self.dia_seleccionado.get().strip()
        mes = self.mes_seleccionado.get().strip()
        año = self.año_seleccionado.get().strip()
        licencia = self.seleccion_licencia.get().strip()
        experiencia = self.spinbox_experiencia.get().strip()
        sistema_juego = self.seleccion_sistema_juego.get().strip()


        if nombre == "Ej: Carlo":
            messagebox.showerror("¡Error!", "Ingrese el nombre del entrenador")
            return
        elif apellido == "Ej: Ancelotti":
            messagebox.showerror("¡Error!", "Ingrese el apellido del entrenador")
            return 
        elif nacionalidad == "Seleccione Nacionalidad":
            messagebox.showerror("¡Error!", "Seleccione la nacionalidad del entrenador")
            return
        elif dia == "Día":
            messagebox.showerror("¡Error!", "Seleccione el día de nacimiento del entrenador")
            return 
        elif mes == "Mes":
            messagebox.showerror("¡Error!", "Seleccione el mes de nacimiento del entrenador")
            return 
        elif año == "Año":
            messagebox.showerror("¡Error!", "Seleccione el año de nacimiento del entrenador")
            return 
        elif licencia == "Seleccione Licencia":
            messagebox.showerror("¡Error!", "Seleccione el tipo de licencia del entrenador")
            return 
        elif experiencia == "":
            messagebox.showerror("¡Error!", "Ingrese los años de experiencia del entrenador")
            return 
        elif sistema_juego == "Seleccione Sistema":
            messagebox.showerror("¡Error!", "Seleccione el sistema de juego del entrenador")
            return 
        
        nombre = nombre.title()
        apellido = apellido.title()
        nacionalidad = nacionalidad.title()
        dia = int(dia)
        mes = int(mes)
        año = int(año)
        experiencia = int(experiencia)

        fecha = (f"{dia:02}/{mes:02}/{año}")


        if not 1 <= experiencia  <= 50:
            messagebox.showerror("¡Error!", "La experiencia del entrenador ")
            return 
        

        if lista_entrenadores == []:

            archivo = open("entrenadores.txt", "a")
            linea = (f"{nombre};{apellido};{nacionalidad};{fecha};{licencia};{experiencia};{sistema_juego}")
            archivo.write(linea)
            archivo.close()

            nuevo_entrenador = Entrenador(nombre, apellido, nacionalidad, fecha, licencia, experiencia, sistema_juego)
            lista_entrenadores += [nuevo_entrenador]

            messagebox.showinfo(None, "Entrenador registrado correctamente")

            self.entry_nombre_entrenador.delete(0, "end")
            self.entry_apellidos_entrenador.delete(0, "end")
            self.combobox_nacionalidad_entrenador.delete(0, "end")
            self.combobox_dias.delete(0, "end")
            self.combobox_meses.delete(0, "end")
            self.combobox_año.delete(0, "end")
            self.combobox_licencia.delete(0, "end")
            self.spinbox_experiencia.delete(0, "end")
            self.combobox_sistema_juego.delete(0, "end") 

            self.entry_nombre_entrenador.insert(0, "Ej: Carlo")
            self.entry_apellidos_entrenador.insert(0, "Ej: Ancelotti")
            self.combobox_nacionalidad_entrenador.set("Seleccione Nacionalidad")
            self.combobox_dias.set("Día")
            self.combobox_meses.set("Mes")
            self.combobox_año.set("Año")
            self.combobox_licencia.set("Seleccione Licencia")
            self.combobox_sistema_juego.set("Seleccione Sistema") 
            return  
        
        archivo = open("entrenadores.txt", "a")
        linea = (f"\n{nombre};{apellido};{nacionalidad};{fecha};{licencia};{experiencia};{sistema_juego}")
        archivo.write(linea)
        archivo.close()

        nuevo_entrenador = Entrenador(nombre, apellido, nacionalidad, fecha, licencia, experiencia, sistema_juego)
        lista_entrenadores += [nuevo_entrenador]

        messagebox.showinfo(None, "Entrenador registrado correctamente")

        self.entry_nombre_entrenador.delete(0, "end")
        self.entry_apellidos_entrenador.delete(0, "end")
        self.combobox_nacionalidad_entrenador.delete(0, "end")
        self.combobox_dias.delete(0, "end")
        self.combobox_meses.delete(0, "end")
        self.combobox_año.delete(0, "end")
        self.combobox_licencia.delete(0, "end")
        self.spinbox_experiencia.delete(0, "end")
        self.combobox_sistema_juego.delete(0, "end") 

        self.entry_nombre_entrenador.insert(0, "Ej: Carlo")
        self.entry_apellidos_entrenador.insert(0, "Ej: Ancelotti")
        self.combobox_nacionalidad_entrenador.set("Seleccione Nacionalidad")
        self.combobox_dias.set("Día")
        self.combobox_meses.set("Mes")
        self.combobox_año.set("Año")
        self.combobox_licencia.set("Seleccione Licencia")
        self.combobox_sistema_juego.set("Seleccione Sistema")












    """
    Nombre: crear_tabla_jugadores_registrados
    Entrada: no recibe parámetros
    Salida: crea la tabla para mostrar jugadores registrados
    Restricciones: usa lista_jugadores
    """
    def crear_tabla_jugadores_registrados(self):

        label_jugadores_registrados = tk.Label(self,
                                               text="Jugadores Registrados",
                                               font=("Arial", 12, "bold"),
                                               fg=azul,
                                               anchor="w")
        label_jugadores_registrados.place(x=970, y=440, width=300, height=30)

        self.tree_jugadores = ttk.Treeview(self,
                                           columns=("nombre", "nacionalidad", "dorsal", "posicion", "puntaje"),
                                           show="headings")

        self.tree_jugadores.heading("nombre", text="Jugador")
        self.tree_jugadores.heading("nacionalidad", text="Nacionalidad")
        self.tree_jugadores.heading("dorsal", text="Dorsal")
        self.tree_jugadores.heading("posicion", text="Posición")
        self.tree_jugadores.heading("puntaje", text="Puntaje")

        self.tree_jugadores.column("nombre", width=130, anchor="w")
        self.tree_jugadores.column("nacionalidad", width=105, anchor="center")
        self.tree_jugadores.column("dorsal", width=60, anchor="center")
        self.tree_jugadores.column("posicion", width=130, anchor="center")
        self.tree_jugadores.column("puntaje", width=70, anchor="center")

        self.tree_jugadores.place(x=970, y=480, width=515, height=310)

        self.cargar_tabla_jugadores()


    """
    Nombre: cargar_tabla_jugadores
    Entrada: no recibe parámetros
    Salida: carga los jugadores de lista_jugadores en la tabla
    Restricciones: la tabla debe existir
    """
    def cargar_tabla_jugadores(self):

        filas = self.tree_jugadores.get_children()

        for fila in filas:
            self.tree_jugadores.delete(fila)

        for jugador in lista_jugadores:
            nombre_completo = jugador.nombre + " " + jugador.apellido

            self.tree_jugadores.insert("",
                                       "end",
                                       values=(nombre_completo,
                                               jugador.nacionalidad,
                                               jugador.dorsal,
                                               jugador.posicion,
                                               jugador.puntaje_individual))


    """
    Nombre: actualizar_combobox_jugadores
    Entrada: no recibe parámetros
    Salida: actualiza el combobox de jugadores
    Restricciones: usa lista_jugadores
    """
    def actualizar_combobox_jugadores(self):

        jugadores = []

        for jugador in lista_jugadores:
            jugadores += [jugador.nombre + " " + jugador.apellido]

        self.combobox_jugadores.config(values=jugadores)


    """
    Nombre: añadir_jugador
    Entrada: datos ingresados en la interfaz
    Salida: registra un jugador en lista_jugadores y jugadores.txt
    Restricciones: int() solo se usa con datos de Entry, Spinbox o Combobox
    """
    def añadir_jugador(self):

        global lista_jugadores

        nombre = self.entry_nombre_jugador.get().strip()
        apellido = self.entry_apellidos_jugador.get().strip()
        nacionalidad = self.seleccion_nacionalidad_jugador.get().strip()
        dia = self.dia_seleccionado_jugador.get().strip()
        mes = self.mes_seleccionado_jugador.get().strip()
        año = self.año_seleccionado_jugador.get().strip()
        dorsal_texto = self.spinbox_dorsal.get().strip()
        posicion = self.obtener_posicion.get().strip()
        velocidad_texto = self.spinbox_velocidad.get().strip()
        estratega_texto = self.spinbox_estratega.get().strip()
        dominio_texto = self.spinbox_dominio.get().strip()
        fuerza_texto = self.spinbox_fuerza.get().strip()

        if nombre == "" or nombre == "Ej: Lionel":
            messagebox.showerror("Error", "Ingrese el nombre del jugador")
            return
        elif apellido == "" or apellido == "Ej: Messi":
            messagebox.showerror("Error", "Ingrese el apellido del jugador")
            return
        elif nacionalidad == "" or nacionalidad == "Seleccione Nacionalidad":
            messagebox.showerror("Error", "Seleccione la nacionalidad del jugador")
            return
        elif dia == "Día":
            messagebox.showerror("Error", "Seleccione el día de nacimiento")
            return
        elif mes == "Mes":
            messagebox.showerror("Error", "Seleccione el mes de nacimiento")
            return
        elif año == "Año":
            messagebox.showerror("Error", "Seleccione el año de nacimiento")
            return
        elif dorsal_texto == "":
            messagebox.showerror("Error", "Ingrese el dorsal del jugador")
            return
        elif posicion == "Seleccione Posicion":
            messagebox.showerror("Error", "Seleccione la posición del jugador")
            return
        elif velocidad_texto == "":
            messagebox.showerror("Error", "Ingrese la velocidad del jugador")
            return
        elif estratega_texto == "":
            messagebox.showerror("Error", "Ingrese el puntaje de estratega")
            return
        elif dominio_texto == "":
            messagebox.showerror("Error", "Ingrese el dominio del balón")
            return
        elif fuerza_texto == "":
            messagebox.showerror("Error", "Ingrese la fuerza del jugador")
            return

        nombre = nombre.title()
        apellido = apellido.title()

        dorsal = int(dorsal_texto)
        velocidad = int(velocidad_texto)
        estratega = int(estratega_texto)
        dominio = int(dominio_texto)
        fuerza = int(fuerza_texto)

        puntaje_individual = velocidad + estratega + dominio + fuerza
        fecha_nacimiento = dia + "/" + mes + "/" + año

        for jugador in lista_jugadores:
            if jugador.nombre == nombre and jugador.apellido == apellido and jugador.nacionalidad == nacionalidad:
                messagebox.showerror("Error", "Ese jugador ya está registrado")
                return

        nuevo_jugador = Futbolista(nombre,
                                   apellido,
                                   fecha_nacimiento,
                                   nacionalidad,
                                   dorsal,
                                   posicion,
                                   0,
                                   0,
                                   0,
                                   0,
                                   puntaje_individual)

        lista_jugadores += [nuevo_jugador]

        puntaje_texto = numero_a_texto(puntaje_individual)

        archivo = open("jugadores.txt", "a")

        if contar(lista_jugadores) == 1:
            linea = nombre + ";" + apellido + ";" + fecha_nacimiento + ";" + nacionalidad + ";" + dorsal_texto + ";" + posicion + ";0;0;0;0;" + puntaje_texto
        else:
            linea = "\n" + nombre + ";" + apellido + ";" + fecha_nacimiento + ";" + nacionalidad + ";" + dorsal_texto + ";" + posicion + ";0;0;0;0;" + puntaje_texto

        archivo.write(linea)
        archivo.close()

        self.cargar_tabla_jugadores()
        self.actualizar_combobox_jugadores()
        self.limpiar_jugador()

        messagebox.showinfo("Correcto", "Jugador registrado correctamente")


    """
    Nombre: limpiar_jugador
    Entrada: no recibe parámetros
    Salida: limpia los campos de jugador
    Restricciones: los entry y combobox deben existir
    """
    def limpiar_jugador(self):

        self.entry_nombre_jugador.delete(0, "end")
        self.entry_apellidos_jugador.delete(0, "end")
        self.spinbox_dorsal.delete(0, "end")
        self.spinbox_velocidad.delete(0, "end")
        self.spinbox_estratega.delete(0, "end")
        self.spinbox_dominio.delete(0, "end")
        self.spinbox_fuerza.delete(0, "end")

        self.entry_nombre_jugador.insert(0, "Ej: Lionel")
        self.entry_apellidos_jugador.insert(0, "Ej: Messi")
        self.combobox_nacionalidad_jugador.set("Seleccione Nacionalidad")
        self.combobox_dias_jugador.set("Día")
        self.combobox_meses_jugador.set("Mes")
        self.combobox_año_jugador.set("Año")
        self.combobox_posiciones.set("Seleccione Posicion")
        





        





























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
        canvas_llave.create_text(50, 20, text="Octavos", font=("Arial", 10, "bold"))
        canvas_llave.create_text(145, 20, text="Cuartos", font=("Arial", 10, "bold"))
        canvas_llave.create_text(240, 20, text="Semifinal", font=("Arial", 10, "bold"))
        canvas_llave.create_text(345, 20, text="Final", font=("Arial", 10, "bold"))

        y = 50
        contador = 0

        while contador < 8:
            canvas_llave.create_rectangle(15, y, 85, y + 22, outline=azul)
            canvas_llave.create_text(50, y + 11, text="Equipo", font=("Arial", 8))

            y = y + 38
            contador = contador + 1

        y = 61
        contador = 0

        while contador < 4:
            canvas_llave.create_line(85, y, 105, y, fill=azul)
            canvas_llave.create_line(85, y + 38, 105, y + 38, fill=azul)
            canvas_llave.create_line(105, y, 105, y + 38, fill=azul)
            canvas_llave.create_line(105, y + 19, 125, y + 19, fill=azul)

            canvas_llave.create_rectangle(125, y + 8, 190, y + 30, outline=azul)

            y = y + 76
            contador = contador + 1

        y = 80
        contador = 0

        while contador < 2:
            canvas_llave.create_line(190, y, 210, y, fill=azul)
            canvas_llave.create_line(190, y + 76, 210, y + 76, fill=azul)
            canvas_llave.create_line(210, y, 210, y + 76, fill=azul)
            canvas_llave.create_line(210, y + 38, 230, y + 38, fill=azul)

            canvas_llave.create_rectangle(230, y + 27, 295, y + 49, outline=azul)

            y = y + 152
            contador = contador + 1





    


class Estadisticas(tk.Toplevel):

    """
    Nombre: Estadisticas
    Entrada: principal
    Salida: crea la ventana de estadísticas y ranking
    Restricciones: principal debe ser la pantalla principal
    """
    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)

        self.principal = principal

        self.geometry("1535x930+-7+-0")
        self.title("Estadísticas / Ranking")
        self.resizable(False, False)
        self.config(bg=blanco)

        self.encabezado()
        self.resumen_general()
        self.ranking_paises()
        self.ranking_jugadores()
        self.estadisticas_selecciones()
        self.botones()
        self.actualizar_estadisticas()


    """
    Nombre: contar_lista
    Entrada: lista
    Salida: cantidad de elementos de la lista
    Restricciones:
    """
    def contar_lista(self, lista):
        cantidad = 0

        for elemento in lista:
            cantidad = cantidad + 1

        return cantidad


    """
    Nombre: encabezado
    Entrada: no recibe parámetros
    Salida: crea el título de la ventana
    Restricciones: usa colores globales
    """
    def encabezado(self):
        frame_titulo = tk.Frame(self,
                                bg=azul_oscuro)
        frame_titulo.place(x=0, y=0, width=1535, height=90)

        label_titulo = tk.Label(frame_titulo,
                                text="Estadísticas / Ranking",
                                font=("Arial", 30, "bold"),
                                bg=azul_oscuro,
                                fg=blanco,
                                anchor="w")
        label_titulo.place(x=40, y=15, width=600, height=45)

        label_subtitulo = tk.Label(frame_titulo,
                                   text="Resumen general de países, selecciones, entrenadores y jugadores",
                                   font=("Arial", 13, "bold"),
                                   bg=azul_oscuro,
                                   fg=celeste,
                                   anchor="w")
        label_subtitulo.place(x=45, y=58, width=800, height=25)


    """
    Nombre: resumen_general
    Entrada: no recibe parámetros
    Salida: crea tarjetas de resumen
    Restricciones: usa listas globales
    """
    def resumen_general(self):
        frame_paises = tk.LabelFrame(self,
                                     text=" Países ",
                                     font=("Arial", 13, "bold"),
                                     fg=azul_oscuro,
                                     bg=blanco,
                                     bd=2,
                                     relief="solid")
        frame_paises.place(x=40, y=120, width=320, height=120)

        self.label_total_paises = tk.Label(frame_paises,
                                           text=0,
                                           font=("Arial", 35, "bold"),
                                           bg=blanco,
                                           fg=azul)
        self.label_total_paises.place(x=20, y=25, width=260, height=55)

        label_paises = tk.Label(frame_paises,
                                text="registrados",
                                font=("Arial", 13),
                                bg=blanco,
                                fg=gris)
        label_paises.place(x=20, y=78, width=260, height=25)


        frame_selecciones = tk.LabelFrame(self,
                                          text=" Selecciones ",
                                          font=("Arial", 13, "bold"),
                                          fg=azul_oscuro,
                                          bg=blanco,
                                          bd=2,
                                          relief="solid")
        frame_selecciones.place(x=400, y=120, width=320, height=120)

        self.label_total_selecciones = tk.Label(frame_selecciones,
                                                text=0,
                                                font=("Arial", 35, "bold"),
                                                bg=blanco,
                                                fg=verde)
        self.label_total_selecciones.place(x=20, y=25, width=260, height=55)

        label_selecciones = tk.Label(frame_selecciones,
                                     text="registradas",
                                     font=("Arial", 13),
                                     bg=blanco,
                                     fg=gris)
        label_selecciones.place(x=20, y=78, width=260, height=25)


        frame_entrenadores = tk.LabelFrame(self,
                                           text=" Entrenadores ",
                                           font=("Arial", 13, "bold"),
                                           fg=azul_oscuro,
                                           bg=blanco,
                                           bd=2,
                                           relief="solid")
        frame_entrenadores.place(x=760, y=120, width=320, height=120)

        self.label_total_entrenadores = tk.Label(frame_entrenadores,
                                                 text=0,
                                                 font=("Arial", 35, "bold"),
                                                 bg=blanco,
                                                 fg=anaranjado)
        self.label_total_entrenadores.place(x=20, y=25, width=260, height=55)

        label_entrenadores = tk.Label(frame_entrenadores,
                                      text="registrados",
                                      font=("Arial", 13),
                                      bg=blanco,
                                      fg=gris)
        label_entrenadores.place(x=20, y=78, width=260, height=25)


        frame_jugadores = tk.LabelFrame(self,
                                        text=" Jugadores ",
                                        font=("Arial", 13, "bold"),
                                        fg=azul_oscuro,
                                        bg=blanco,
                                        bd=2,
                                        relief="solid")
        frame_jugadores.place(x=1120, y=120, width=320, height=120)

        self.label_total_jugadores = tk.Label(frame_jugadores,
                                              text=0,
                                              font=("Arial", 35, "bold"),
                                              bg=blanco,
                                              fg=rojo)
        self.label_total_jugadores.place(x=20, y=25, width=260, height=55)

        label_jugadores = tk.Label(frame_jugadores,
                                   text="registrados",
                                   font=("Arial", 13),
                                   bg=blanco,
                                   fg=gris)
        label_jugadores.place(x=20, y=78, width=260, height=25)


    """
    Nombre: ranking_paises
    Entrada: no recibe parámetros
    Salida: crea tabla del ranking FIFA de países
    Restricciones: usa lista_paises
    """
    def ranking_paises(self):
        frame_ranking_paises = tk.LabelFrame(self,
                                             text=" Ranking FIFA de Países ",
                                             font=("Arial", 14, "bold"),
                                             fg=azul_oscuro,
                                             bg=blanco,
                                             bd=1,
                                             relief="solid")
        frame_ranking_paises.place(x=40, y=270, width=700, height=280)

        self.tabla_paises = ttk.Treeview(frame_ranking_paises,
                                         columns=("posicion", "codigo", "pais", "continente", "ranking"),
                                         show="headings",
                                         height=8)

        self.tabla_paises.heading("posicion", text="#")
        self.tabla_paises.heading("codigo", text="Código")
        self.tabla_paises.heading("pais", text="País")
        self.tabla_paises.heading("continente", text="Continente")
        self.tabla_paises.heading("ranking", text="Ranking")

        self.tabla_paises.column("posicion", width=50, anchor="center")
        self.tabla_paises.column("codigo", width=90, anchor="center")
        self.tabla_paises.column("pais", width=220, anchor="w")
        self.tabla_paises.column("continente", width=180, anchor="w")
        self.tabla_paises.column("ranking", width=100, anchor="center")

        self.tabla_paises.place(x=20, y=25, width=650, height=220)


    """
    Nombre: ranking_jugadores
    Entrada: no recibe parámetros
    Salida: crea tabla del ranking de jugadores
    Restricciones: usa lista_jugadores
    """
    def ranking_jugadores(self):
        frame_ranking_jugadores = tk.LabelFrame(self,
                                                text=" Ranking de Jugadores ",
                                                font=("Arial", 14, "bold"),
                                                fg=azul_oscuro,
                                                bg=blanco,
                                                bd=1,
                                                relief="solid")
        frame_ranking_jugadores.place(x=780, y=270, width=700, height=280)

        self.tabla_jugadores = ttk.Treeview(frame_ranking_jugadores,
                                            columns=("posicion", "jugador", "posicion_juego", "goles", "asistencias", "puntaje"),
                                            show="headings",
                                            height=8)

        self.tabla_jugadores.heading("posicion", text="#")
        self.tabla_jugadores.heading("jugador", text="Jugador")
        self.tabla_jugadores.heading("posicion_juego", text="Posición")
        self.tabla_jugadores.heading("goles", text="Goles")
        self.tabla_jugadores.heading("asistencias", text="Asist.")
        self.tabla_jugadores.heading("puntaje", text="Puntaje")

        self.tabla_jugadores.column("posicion", width=50, anchor="center")
        self.tabla_jugadores.column("jugador", width=230, anchor="w")
        self.tabla_jugadores.column("posicion_juego", width=130, anchor="center")
        self.tabla_jugadores.column("goles", width=80, anchor="center")
        self.tabla_jugadores.column("asistencias", width=80, anchor="center")
        self.tabla_jugadores.column("puntaje", width=90, anchor="center")

        self.tabla_jugadores.place(x=20, y=25, width=650, height=220)


    """
    Nombre: estadisticas_selecciones
    Entrada: no recibe parámetros
    Salida: crea tabla de estadísticas de selecciones
    Restricciones: usa lista_selecciones
    """
    def estadisticas_selecciones(self):
        frame_selecciones = tk.LabelFrame(self,
                                          text=" Estadísticas de Selecciones ",
                                          font=("Arial", 14, "bold"),
                                          fg=azul_oscuro,
                                          bg=blanco,
                                          bd=1,
                                          relief="solid")
        frame_selecciones.place(x=40, y=580, width=1440, height=250)

        self.tabla_selecciones = ttk.Treeview(frame_selecciones,
                                              columns=("codigo", "pais", "gf", "gc", "amarillas", "rojas", "fuerza"),
                                              show="headings",
                                              height=7)

        self.tabla_selecciones.heading("codigo", text="Código")
        self.tabla_selecciones.heading("pais", text="País")
        self.tabla_selecciones.heading("gf", text="Goles Favor")
        self.tabla_selecciones.heading("gc", text="Goles Contra")
        self.tabla_selecciones.heading("amarillas", text="Amarillas")
        self.tabla_selecciones.heading("rojas", text="Rojas")
        self.tabla_selecciones.heading("fuerza", text="Fuerza")

        self.tabla_selecciones.column("codigo", width=100, anchor="center")
        self.tabla_selecciones.column("pais", width=300, anchor="w")
        self.tabla_selecciones.column("gf", width=140, anchor="center")
        self.tabla_selecciones.column("gc", width=140, anchor="center")
        self.tabla_selecciones.column("amarillas", width=140, anchor="center")
        self.tabla_selecciones.column("rojas", width=140, anchor="center")
        self.tabla_selecciones.column("fuerza", width=140, anchor="center")

        self.tabla_selecciones.place(x=20, y=25, width=1390, height=180)


    """
    Nombre: botones
    Entrada: no recibe parámetros
    Salida: crea botones de actualizar y volver
    Restricciones: principal debe existir
    """
    def botones(self):
        boton_actualizar = tk.Button(self,
                                     text="Actualizar Estadísticas",
                                     font=("Arial", 14, "bold"),
                                     bg=verde,
                                     fg=blanco,
                                     bd=2,
                                     relief="raised",
                                     command=self.actualizar_estadisticas)
        boton_actualizar.place(x=990, y=855, width=250, height=45)

        boton_volver = tk.Button(self,
                                 text="Regresar al menú principal",
                                 font=("Arial", 14, "bold"),
                                 bg=gris_claro,
                                 fg=negro,
                                 bd=2,
                                 relief="raised",
                                 command=self.volver)
        boton_volver.place(x=1260, y=855, width=250, height=45)


    """
    Nombre: limpiar_tabla
    Entrada: tabla
    Salida: elimina todas las filas de una tabla
    Restricciones: tabla debe ser Treeview
    """
    def limpiar_tabla(self, tabla):
        filas = tabla.get_children()

        for fila in filas:
            tabla.delete(fila)


    """
    Nombre: ordenar_paises
    Entrada: no recibe parámetros
    Salida: retorna países ordenados por ranking FIFA
    Restricciones: menor ranking significa mejor posición
    """
    def ordenar_paises(self):
        paises_ordenados = []

        for pais in lista_paises:
            paises_ordenados += [pais]

        cantidad = self.contar_lista(paises_ordenados)

        i = 0

        while i < cantidad - 1:
            j = i + 1

            while j < cantidad:
                if paises_ordenados[j].ranking_fifa < paises_ordenados[i].ranking_fifa:
                    temporal = paises_ordenados[i]
                    paises_ordenados[i] = paises_ordenados[j]
                    paises_ordenados[j] = temporal

                j = j + 1

            i = i + 1

        return paises_ordenados


    """
    Nombre: ordenar_jugadores
    Entrada: no recibe parámetros
    Salida: retorna jugadores ordenados por goles, asistencias y puntaje
    Restricciones: mayor cantidad queda primero
    """
    def ordenar_jugadores(self):
        jugadores_ordenados = []

        for jugador in lista_jugadores:
            jugadores_ordenados += [jugador]

        cantidad = self.contar_lista(jugadores_ordenados)

        i = 0

        while i < cantidad - 1:
            j = i + 1

            while j < cantidad:
                cambiar = False

                if jugadores_ordenados[j].goles > jugadores_ordenados[i].goles:
                    cambiar = True

                elif jugadores_ordenados[j].goles == jugadores_ordenados[i].goles and jugadores_ordenados[j].asistencias > jugadores_ordenados[i].asistencias:
                    cambiar = True

                elif jugadores_ordenados[j].goles == jugadores_ordenados[i].goles and jugadores_ordenados[j].asistencias == jugadores_ordenados[i].asistencias and jugadores_ordenados[j].puntaje_individual > jugadores_ordenados[i].puntaje_individual:
                    cambiar = True

                if cambiar == True:
                    temporal = jugadores_ordenados[i]
                    jugadores_ordenados[i] = jugadores_ordenados[j]
                    jugadores_ordenados[j] = temporal

                j = j + 1

            i = i + 1

        return jugadores_ordenados


    """
    Nombre: ordenar_selecciones
    Entrada: no recibe parámetros
    Salida: retorna selecciones ordenadas por goles a favor
    Restricciones: mayor cantidad queda primero
    """
    def ordenar_selecciones(self):
        selecciones_ordenadas = []

        for seleccion in lista_selecciones:
            selecciones_ordenadas += [seleccion]

        cantidad = self.contar_lista(selecciones_ordenadas)

        i = 0

        while i < cantidad - 1:
            j = i + 1

            while j < cantidad:
                if selecciones_ordenadas[j].total_goles_a_favor > selecciones_ordenadas[i].total_goles_a_favor:
                    temporal = selecciones_ordenadas[i]
                    selecciones_ordenadas[i] = selecciones_ordenadas[j]
                    selecciones_ordenadas[j] = temporal

                j = j + 1

            i = i + 1

        return selecciones_ordenadas


    """
    Nombre: cargar_paises
    Entrada: no recibe parámetros
    Salida: carga países en la tabla de ranking
    Restricciones: usa lista_paises
    """
    def cargar_paises(self):
        paises_ordenados = self.ordenar_paises()

        contador = 0

        for pais in paises_ordenados:
            self.tabla_paises.insert("",
                                     "end",
                                     values=(contador + 1,
                                             pais.codigo_fifa,
                                             pais.nombre,
                                             pais.continente,
                                             pais.ranking_fifa))

            contador = contador + 1


    """
    Nombre: cargar_jugadores
    Entrada: no recibe parámetros
    Salida: carga jugadores en la tabla de ranking
    Restricciones: usa lista_jugadores
    """
    def cargar_jugadores(self):
        jugadores_ordenados = self.ordenar_jugadores()

        contador = 0

        for jugador in jugadores_ordenados:
            nombre_completo = jugador.nombre + " " + jugador.apellido

            self.tabla_jugadores.insert("",
                                        "end",
                                        values=(contador + 1,
                                                nombre_completo,
                                                jugador.posicion,
                                                jugador.goles,
                                                jugador.asistencias,
                                                jugador.puntaje_individual))

            contador = contador + 1


    """
    Nombre: cargar_selecciones
    Entrada: no recibe parámetros
    Salida: carga selecciones en la tabla de estadísticas
    Restricciones: usa lista_selecciones
    """
    def cargar_selecciones(self):
        selecciones_ordenadas = self.ordenar_selecciones()

        for seleccion in selecciones_ordenadas:
            self.tabla_selecciones.insert("",
                                          "end",
                                          values=(seleccion.codigo_equipo,
                                                  seleccion.pais.nombre,
                                                  seleccion.total_goles_a_favor,
                                                  seleccion.total_goles_en_contra,
                                                  seleccion.total_tarjetas_amarillas,
                                                  seleccion.total_tarjetas_rojas,
                                                  seleccion.fuerza_equipo))


    """
    Nombre: actualizar_estadisticas
    Entrada: no recibe parámetros
    Salida: actualiza totales y tablas
    Restricciones: las listas globales deben existir
    """
    def actualizar_estadisticas(self):
        self.label_total_paises.config(text=self.contar_lista(lista_paises))
        self.label_total_selecciones.config(text=self.contar_lista(lista_selecciones))
        self.label_total_entrenadores.config(text=self.contar_lista(lista_entrenadores))
        self.label_total_jugadores.config(text=self.contar_lista(lista_jugadores))

        self.limpiar_tabla(self.tabla_paises)
        self.limpiar_tabla(self.tabla_jugadores)
        self.limpiar_tabla(self.tabla_selecciones)

        self.cargar_paises()
        self.cargar_jugadores()
        self.cargar_selecciones()


    """
    Nombre: volver
    Entrada: no recibe parámetros
    Salida: cierra estadísticas y vuelve al menú principal
    Restricciones: principal debe existir
    """
    def volver(self):
        self.destroy()
        self.principal.deiconify()



if __name__ == "__main__":
    app = Pantalla_Principal()
    app.mainloop()

    
    








