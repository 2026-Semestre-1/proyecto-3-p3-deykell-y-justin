# ===  Copa Mundial  === #

# Librerías

import tkinter as tk
from tkinter import ttk, messagebox
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
azul_seleccion = "#347083"


lista_paises = []
lista_selecciones = []
lista_jugadores = []
lista_entrenadores = []


def contar(elementos):
    cantidad = 0

    for elemento in elementos:
        cantidad = cantidad + 1

    return cantidad


def tiene_tres_caracteres(texto):
    cantidad = 0

    for caracter in texto:
        cantidad = cantidad + 1

    if cantidad == 3:
        return True
    else:
        return False


def buscar_pais(dato_pais):
    for pais in lista_paises:
        if pais.nombre == dato_pais or pais.codigo_fifa == dato_pais:
            return pais

    return 0


def buscar_entrenador(dato_entrenador):
    for entrenador in lista_entrenadores:
        nombre_completo = entrenador.nombre + " " + entrenador.apellido

        if entrenador.nombre == dato_entrenador or nombre_completo == dato_entrenador:
            return entrenador

    return 0


class Pais:

    """
    Nombre: Pais
    Entrada: codigo_fifa, nombre, continente, ranking_fifa
    Salida: crea un país
    Restricciones: codigo_fifa, nombre y continente deben ser texto; ranking_fifa debe ser entero
    """
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):

        if not (isinstance(codigo_fifa, str) and isinstance(nombre, str) and isinstance(continente, str)):
            print("Error: los parámetros deben ser texto")
            return 
        elif not isinstance(ranking_fifa, int):
            print("Error: el ranking fifa debe ser entero")
            return 
        elif not 1 <= ranking_fifa <= 100:
            print("Error: el ranking fifa debe estar entre 1 y 100")
            return
        elif nombre == "" or continente == "" or codigo_fifa == "":
            print("Error: los parámetros no pueden estar vacíos")
            return

        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa

    """
    Nombre: mostrar_datos
    Entrada: no recibe parámetros
    Salida: muestra los datos del país
    Restricciones: el país debe estar creado
    """
    def mostrar_datos(self):
        print("Código FIFA del País:", self.codigo_fifa)
        print("Nombre del País:", self.nombre)
        print("Continente:", self.continente)
        print("Ranking FIFA:", self.ranking_fifa)
        print("")

    """
    Nombre: actualizar_datos
    Entrada: codigo_fifa, nombre, continente, ranking_fifa
    Salida: actualiza los datos del país
    Restricciones: ranking_fifa debe ser entero
    """
    def actualizar_datos(self, codigo_fifa, nombre, continente, ranking_fifa):

        if not (isinstance(codigo_fifa, str) and isinstance(nombre, str) and isinstance(continente, str)):
            print("Error: los parámetros deben ser texto")
            return 
        elif not isinstance(ranking_fifa, int):
            print("Error: el ranking fifa debe ser entero")
            return
        
        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa


class Persona:

    """
    Nombre: Persona
    Entrada: nombre, apellido, fecha_nacimiento, nacionalidad
    Salida: crea una persona
    Restricciones: todos los datos deben ser texto
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        if not (isinstance(nombre, str) and isinstance(apellido, str) and isinstance(fecha_nacimiento, str) and isinstance(nacionalidad, str)):
            print("Error: los parámetros deben ser texto")
            return

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad

    """
    Nombre: mostrar_datos
    Entrada: no recibe parámetros
    Salida: muestra los datos de la persona
    Restricciones: la persona debe estar creada
    """
    def mostrar_datos(self):
        print("Nombre:", self.nombre, self.apellido)
        print("Fecha de Nacimiento:", self.fecha_nacimiento)
        print("Nacionalidad:", self.nacionalidad)
        print("")


class Entrenador(Persona):

    """
    Nombre: Entrenador
    Entrada: nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego
    Salida: crea un entrenador
    Restricciones: experiencia_anios debe ser entero
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)

        if not (isinstance(licencia, str) and isinstance(sistema_juego, str)):
            print("Error: los parámetros deben ser texto")
            return 
        elif not isinstance(experiencia_anios, int):
            print("Error: experiencia_anios debe ser entero")
            return 

        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego

    """
    Nombre: mostrar_datos
    Entrada: no recibe parámetros
    Salida: muestra los datos del entrenador
    Restricciones: el entrenador debe estar creado
    """
    def mostrar_datos(self):
        print("Nombre:", self.nombre, self.apellido)
        print("Fecha de Nacimiento:", self.fecha_nacimiento)
        print("Nacionalidad:", self.nacionalidad)
        print("Licencia:", self.licencia)
        print("Experiencia:", self.experiencia_anios)
        print("Sistema de Juego:", self.sistema_juego)
        print("")

    """
    Nombre: actualizar_datos
    Entrada: datos del entrenador
    Salida: actualiza los datos del entrenador
    Restricciones: experiencia_anios debe ser entero
    """
    def actualizar_datos(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego):
        if not (isinstance(nombre, str) and isinstance(apellido, str) and isinstance(fecha_nacimiento, str) and isinstance(nacionalidad, str)):
            print("Error: los parámetros deben ser texto")
            return
        if not (isinstance(licencia, str) and isinstance(sistema_juego, str)):
            print("Error: los parámetros deben ser texto")
            return 
        elif not isinstance(experiencia_anios, int):
            print("Error: experiencia_anios debe ser entero")
            return

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego


class Futbolista(Persona):

    """
    Nombre: Futbolista
    Entrada: datos personales y deportivos del jugador
    Salida: crea un futbolista
    Restricciones: los datos numéricos deben ser enteros
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)

        if not isinstance(posicion, str):
            print("Error: posicion debe ser texto")
            return
        elif not (isinstance(dorsal, int) and isinstance(total_tarjetas_amarillas, int) and isinstance(total_tarjetas_rojas, int) and isinstance(goles, int) and isinstance(asistencias, int) and isinstance(puntaje_individual, int)):
            print("Error: los parámetros deportivos deben ser enteros")
            return

        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.goles = goles
        self.asistencias = asistencias
        self.puntaje_individual = puntaje_individual

    """
    Nombre: mostrar_datos
    Entrada: no recibe parámetros
    Salida: muestra los datos del futbolista
    Restricciones: el futbolista debe estar creado
    """
    def mostrar_datos(self):
        print("Nombre:", self.nombre, self.apellido)
        print("Fecha de Nacimiento:", self.fecha_nacimiento)
        print("Nacionalidad:", self.nacionalidad)
        print("Dorsal:", self.dorsal)
        print("Posicion:", self.posicion)
        print("Tarjetas Amarillas:", self.total_tarjetas_amarillas)
        print("Tarjetas Rojas:", self.total_tarjetas_rojas)
        print("Goles:", self.goles)
        print("Asistencias:", self.asistencias)
        print("Puntaje Individual:", self.puntaje_individual)
        print("")

    """
    Nombre: actualizar_datos
    Entrada: datos personales y deportivos del futbolista
    Salida: actualiza los datos del futbolista
    Restricciones: los datos numéricos deben ser enteros
    """
    def actualizar_datos(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):
        if not (isinstance(nombre, str) and isinstance(apellido, str) and isinstance(fecha_nacimiento, str) and isinstance(nacionalidad, str)):
            print("Error: los parámetros deben ser texto")
            return
        if not isinstance(posicion, str):
            print("Error: posicion debe ser texto")
            return
        elif not (isinstance(dorsal, int) and isinstance(total_tarjetas_amarillas, int) and isinstance(total_tarjetas_rojas, int) and isinstance(goles, int) and isinstance(asistencias, int) and isinstance(puntaje_individual, int)):
            print("Error: los parámetros deportivos deben ser enteros")
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

    """
    Nombre: registrar_gol
    Entrada: no recibe parámetros
    Salida: suma un gol al jugador
    Restricciones: goles debe ser entero
    """
    def registrar_gol(self):
        self.goles = self.goles + 1

    """
    Nombre: registrar_asistencia
    Entrada: no recibe parámetros
    Salida: suma una asistencia al jugador
    Restricciones: asistencias debe ser entero
    """
    def registrar_asistencia(self):
        self.asistencias = self.asistencias + 1

    """
    Nombre: registrar_tarjetas
    Entrada: tipo
    Salida: suma tarjeta amarilla o roja
    Restricciones: tipo debe ser texto
    """
    def registrar_tarjetas(self, tipo):
        if not isinstance(tipo, str):
            print("Error: el parámetro debe ser texto")
            return 
        
        if tipo == "amarilla":
            self.total_tarjetas_amarillas = self.total_tarjetas_amarillas + 1
        elif tipo == "roja":
            self.total_tarjetas_rojas = self.total_tarjetas_rojas + 1
        else:
            return "Error: ingrese el tipo de tarjeta amarilla o roja"


class Seleccion:

    """
    Nombre: Seleccion
    Entrada: codigo_equipo, pais y entrenador
    Salida: crea una selección
    Restricciones: codigo_equipo debe ser texto
    """
    def __init__(self, codigo_equipo, pais, entrenador):
        
        if not isinstance(codigo_equipo, str):
            print("Error: el parámetro debe ser texto")
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

    """
    Nombre: mostrar_datos
    Entrada: no recibe parámetros
    Salida: muestra los datos de la selección
    Restricciones: la selección debe tener país y entrenador
    """
    def mostrar_datos(self):
        print("Código de la Selección:", self.codigo_equipo)

        if self.pais != 0:
            print("País:", self.pais.nombre)

        if self.entrenador != 0:
            print("Entrenador:", self.entrenador.nombre)

        print("Jugadores:")

        for futbolista in self.jugadores:
            print("Nombre:", futbolista.nombre, futbolista.apellido)
            print("Dorsal:", futbolista.dorsal)
            print("")

        print("Goles a Favor:", self.total_goles_a_favor)
        print("Goles en Contra:", self.total_goles_en_contra)
        print("Tarjetas Amarillas:", self.total_tarjetas_amarillas)
        print("Tarjetas Rojas:", self.total_tarjetas_rojas)
        print("Fuerza de equipo:", self.fuerza_equipo)
        print("")

    """
    Nombre: agregar_jugador
    Entrada: futbolista
    Salida: agrega un jugador a la selección
    Restricciones: máximo 23 jugadores
    """
    def agregar_jugador(self, futbolista):

        cantidad = contar(self.jugadores)

        if cantidad < 23:
            self.jugadores += [futbolista]
        else:
            return "Error: La plantilla ya cuenta con 23 jugadores"
        
    """
    Nombre: eliminar_jugador
    Entrada: dorsal
    Salida: elimina un jugador según dorsal
    Restricciones: dorsal debe ser entero
    """
    def eliminar_jugador(self, dorsal):
        lista_sin_jugador = []

        for jugador in self.jugadores:
            if jugador.dorsal != dorsal:
                lista_sin_jugador += [jugador]

        self.jugadores = lista_sin_jugador

    """
    Nombre: asignar_entrenador
    Entrada: entrenador
    Salida: asigna entrenador a la selección
    Restricciones: entrenador debe existir
    """
    def asignar_entrenador(self, entrenador):
        self.entrenador = entrenador

    """
    Nombre: registrar_resultado
    Entrada: goles_favor, goles_contra, amarillas, rojas
    Salida: actualiza estadísticas de la selección
    Restricciones: todos los datos deben ser enteros
    """
    def registrar_resultado(self, goles_favor, goles_contra, amarillas, rojas):
        if not (isinstance(goles_favor, int) and isinstance(goles_contra, int) and isinstance(amarillas, int) and isinstance(rojas, int)):
            print("Error: los datos deben ser enteros")
            return

        self.total_goles_a_favor = self.total_goles_a_favor + goles_favor
        self.total_goles_en_contra = self.total_goles_en_contra + goles_contra
        self.total_tarjetas_amarillas = self.total_tarjetas_amarillas + amarillas
        self.total_tarjetas_rojas = self.total_tarjetas_rojas + rojas

    """
    Nombre: calcular_fuerza_equipo
    Entrada: no recibe parámetros
    Salida: calcula la fuerza del equipo
    Restricciones: usa jugadores, entrenador y ranking
    """
    def calcular_fuerza_equipo(self):
        cantidad_jugadores = contar(self.jugadores)

        if cantidad_jugadores == 0:
            self.fuerza_equipo = 0
            return self.fuerza_equipo

        suma = 0

        for jugador in self.jugadores:
            suma = suma + jugador.puntaje_individual

        promedio = suma // cantidad_jugadores
        fuerza_entrenador = 0
        fuerza_ranking = 0

        if self.entrenador != 0:
            fuerza_entrenador = self.entrenador.experiencia_anios

        if self.pais != 0:
            fuerza_ranking = 101 - self.pais.ranking_fifa

        self.fuerza_equipo = promedio + fuerza_entrenador + fuerza_ranking

        return self.fuerza_equipo


class Partido:

    """
    Nombre: Partido
    Entrada: id_partido, equipo_1, equipo_2, goles_equipo1, goles_equipo2, fase, fecha
    Salida: crea un partido
    Restricciones: fase y fecha deben ser texto; goles deben ser enteros
    """
    def __init__(self, id_partido, equipo_1, equipo_2, goles_equipo1, goles_equipo2, fase, fecha):
        if not (isinstance(fase, str) and isinstance(fecha, str)):
            print("Error: los parámetros deben ser texto")
            return
        elif not (isinstance(goles_equipo1, int) and isinstance(goles_equipo2, int)):
            print("Error: los goles deben ser enteros")
            return
        
        self.id = id_partido
        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.goles_equipo1 = goles_equipo1
        self.goles_equipo2 = goles_equipo2
        self.fase = fase
        self.fecha = fecha
        self.ganador = 0
        

class Grupo:

    """
    Nombre: Grupo
    Entrada: nombre_grupo, equipos, partidos
    Salida: crea un grupo
    Restricciones: nombre_grupo debe ser texto
    """
    def __init__(self, nombre_grupo, equipos, partidos):

        if not isinstance(nombre_grupo, str):
            print("Error: el parámetro debe ser texto")
            return

        self.nombre_grupo = nombre_grupo
        self.equipos = equipos
        self.partidos = partidos


class Fase:

    """
    Nombre: Fase
    Entrada: nombre_fase, partidos
    Salida: crea una fase
    Restricciones: nombre_fase debe ser texto
    """
    def __init__(self, nombre_fase, partidos):

        if not isinstance(nombre_fase, str):
            print("Error: el parámetro debe ser texto")
            return 

        self.nombre_fase = nombre_fase
        self.partidos = partidos


class Mundial:

    """
    Nombre: Mundial
    Entrada: nombre, anio, paises, selecciones, grupos, fases, campeon
    Salida: crea un mundial
    Restricciones: nombre debe ser texto y anio entero
    """
    def __init__(self, nombre, anio, paises, selecciones, grupos, fases, campeon):
        
        if not isinstance(nombre, str):
            print("Error: el parámetro debe ser texto")
            return
        elif not isinstance(anio, int):
            print("Error: el año debe ser entero")
            return

        self.nombre = nombre
        self.anio = anio
        self.paises = paises
        self.selecciones = selecciones
        self.grupos = grupos
        self.fases = fases
        self.campeon = campeon


def cargar_paises_archivo():
    global lista_paises

    archivo_paises = open("paises.txt", "r")
    contenido_paises = archivo_paises.readlines()
    archivo_paises.close()

    for linea in contenido_paises:
        datos = linea.strip().split(";")

        if contar(datos) == 4:
            nuevo_pais = Pais(datos[0], datos[1], datos[2], int(datos[3]))
            lista_paises += [nuevo_pais]


def cargar_entrenadores_archivo():
    global lista_entrenadores

    archivo_entrenadores = open("entrenadores.txt", "r")
    contenido_entrenadores = archivo_entrenadores.readlines()
    archivo_entrenadores.close()

    for linea in contenido_entrenadores:
        datos = linea.strip().split(";")

        if contar(datos) == 7:
            nuevo_entrenador = Entrenador(datos[0], datos[1], datos[2], datos[3], datos[4], int(datos[5]), datos[6])
            lista_entrenadores += [nuevo_entrenador]


def cargar_jugadores_archivo():
    global lista_jugadores

    archivo_jugadores = open("jugadores.txt", "r")
    contenido_jugadores = archivo_jugadores.readlines()
    archivo_jugadores.close()

    for linea in contenido_jugadores:
        datos = linea.strip().split(";")

        if contar(datos) == 11:
            nuevo_jugador = Futbolista(datos[0], datos[1], datos[2], datos[3], int(datos[4]), datos[5], int(datos[6]), int(datos[7]), int(datos[8]), int(datos[9]), int(datos[10]))
            lista_jugadores += [nuevo_jugador]


def cargar_selecciones_archivo():
    global lista_selecciones

    archivo_selecciones = open("selecciones.txt", "r")
    contenido_selecciones = archivo_selecciones.readlines()
    archivo_selecciones.close()

    for linea in contenido_selecciones:
        datos = linea.strip().split(";")

        if contar(datos) >= 3:
            pais = buscar_pais(datos[1])
            entrenador = buscar_entrenador(datos[2])
            nueva_seleccion = Seleccion(datos[0], pais, entrenador)
            lista_selecciones += [nueva_seleccion]


cargar_paises_archivo()
cargar_entrenadores_archivo()
cargar_jugadores_archivo()
cargar_selecciones_archivo()


#===== Interfas Gráfica =====#


class Pantalla_Principal(tk.Tk):

    """
    Nombre: Pantalla_Principal
    Entrada: no recibe parámetros
    Salida: crea la pantalla principal
    Restricciones: deben existir las imágenes usadas
    """
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("1535x930+-7+-0")
        self.title("Ventana")
        self.resizable(False, False)

        self.fondo()
        self.botones()

    """
    Nombre: fondo
    Entrada: no recibe parámetros
    Salida: coloca imagen de fondo
    Restricciones: debe existir pantalla_principal.png
    """
    def fondo(self):

        imagen_fondo = Image.open("pantalla_principal.png")
        imagen_fondo = imagen_fondo.resize((1535, 930))

        self.fondo = ImageTk.PhotoImage(imagen_fondo)
        label_fondo = tk.Label(self, image=self.fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    """
    Nombre: botones
    Entrada: no recibe parámetros
    Salida: crea botones principales
    Restricciones: las clases de ventanas deben existir
    """
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
                                   cursor="hand2")
        self.registrar.place(x=40, y=80, width=400, height=60)

    """
    Nombre: paises_selecciones
    Entrada: no recibe parámetros
    Salida: abre administración de países y selecciones
    Restricciones: debe existir la ventana correspondiente
    """
    def paises_selecciones(self):

        self.withdraw()
        Administrar_Paises_Selecciones(self)

    """
    Nombre: entrenadores_jugadores
    Entrada: no recibe parámetros
    Salida: abre administración de entrenadores y jugadores
    Restricciones: debe existir la ventana correspondiente
    """
    def entrenadores_jugadores(self):

        self.withdraw()
        Administrar_Entrenadores_Jugadores(self)

    """
    Nombre: configurar_mundial
    Entrada: no recibe parámetros
    Salida: abre configuración del mundial
    Restricciones: debe existir la ventana correspondiente
    """
    def configurar_mundial(self):

        self.withdraw()
        Configuracion_Mundial(self)

    """
    Nombre: jugar_mundial
    Entrada: no recibe parámetros
    Salida: abre jugar mundial
    Restricciones: debe existir la ventana correspondiente
    """
    def jugar_mundial(self):

        self.withdraw()
        Jugar_Mundial(self)

    """
    Nombre: estadísticas
    Entrada: no recibe parámetros
    Salida: abre estadísticas
    Restricciones: debe existir la clase Estadisticas
    """
    def estadísticas(self):

        self.withdraw()
        Estadisticas(self)


class Administrar_Paises_Selecciones(tk.Toplevel):

    """
    Nombre: Administrar_Paises_Selecciones
    Entrada: principal
    Salida: crea ventana para administrar países y selecciones
    Restricciones: principal debe existir
    """
    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)

        self.principal = principal
        
        self.geometry("1535x930+-7+-0")
        self.title("Administrar Países y Selecciones")
        self.resizable(False, False)

        self.labels()
        self.frames()

    """
    Nombre: labels
    Entrada: no recibe parámetros
    Salida: crea títulos
    Restricciones: usa colores globales
    """
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
        
    """
    Nombre: frames
    Entrada: no recibe parámetros
    Salida: crea la interfaz de países y selecciones
    Restricciones: usa listas globales
    """
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

        self.boton_anadir_pais = tk.Button(self,
                                           text="➕ Añadir País",
                                           font=("Arial", 14),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w",
                                           command=self.anadir)
        self.boton_anadir_pais.place(x=300, y=350, width=160, height=40)

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

        frame_paises_registrados = tk.LabelFrame(self,
                                          text="Lista de Países Registrados",
                                          font=("Arial", 14),
                                          fg=azul,
                                          bd=1,
                                          relief="solid")
        frame_paises_registrados.place(x=270, y=460, width=560, height=400)

        label_total_paises = tk.Label(self,
                                      text="Total de países registrados:",
                                      font=("Arial", 10, "bold"))
        label_total_paises.place(x=610, y=480, width=180, height=30)

        self.label_numero_paises = tk.Label(self,
                                            text=contar(lista_paises),
                                            font=("Arial", 10, "bold"))
        self.label_numero_paises.place(x=790, y=480, width=30, height=30)

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
    
        frame_registrar_selecciones = tk.Frame(self,
                                          bd=1,
                                          relief="solid")
        frame_registrar_selecciones.place(x=920, y=120, width=560, height=300)

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

        self.boton_anadir_seleccion = tk.Button(self,
                                           text="➕ Añadir Selección",
                                           font=("Arial", 14),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w")
        self.boton_anadir_seleccion.place(x=940, y=350, width=190, height=40)

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

        frame_selecciones_registradas = tk.LabelFrame(self,
                                          text="Lista de Selecciones Registradas",
                                          font=("Arial", 14),
                                          fg=azul,
                                          bd=1,
                                          relief="solid")
        frame_selecciones_registradas.place(x=920, y=460, width=560, height=400)

        label_total_selecciones = tk.Label(self,
                                      text="Total de selecciones registradas:",
                                      font=("Arial", 10, "bold"))
        label_total_selecciones.place(x=1230, y=480, width=220, height=30)

        self.label_numero_selecciones = tk.Label(self,
                                                 text=contar(lista_selecciones),
                                                 font=("Arial", 10, "bold"))
        self.label_numero_selecciones.place(x=1450, y=480, width=30, height=30)

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
            numero = numero + 1

        self.tree_view.bind("<ButtonRelease-1>", self.pais_seleccionado)

    """
    Nombre: volver
    Entrada: no recibe parámetros
    Salida: vuelve al menú principal
    Restricciones: principal debe existir
    """
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

    """
    Nombre: anadir
    Entrada: datos de los entry y spinbox
    Salida: registra un país
    Restricciones: el código FIFA debe tener tres letras
    """
    def anadir(self):

        global lista_paises

        codigo_fifa = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        continente = self.seleccion.get().strip()
        ranking_fifa_texto = self.spinbox_ranking.get().strip()

        if codigo_fifa == "Ej: CRC":
            messagebox.showerror("¡Error!", "Ingrese el código FIFA del país")
            return 
        elif nombre == "Ej: Costa Rica":
            messagebox.showerror("¡Error!", "Ingrese el nombre del país")
            return 
        elif continente == "Seleccione un Continente":
            messagebox.showerror("¡Error!", "Debe seleccionar un continente para el país")
            return 
        elif ranking_fifa_texto == "":
            messagebox.showerror("¡Error!", "Debe ingresar el ranking FIFA del país")
            return 
        elif tiene_tres_caracteres(codigo_fifa) == False:
            messagebox.showerror("!Error¡", "El código FIFA debe contener 3 letras")
            return 
        
        codigo_fifa = codigo_fifa.upper()
        continente = continente.title()
        nombre = nombre.title()  
        ranking_fifa = int(ranking_fifa_texto)

        for pais in lista_paises:
            if pais.nombre == nombre:
                messagebox.showerror("Error", "El nombre del país ingresado ya ha sido registrado")
                return 
            elif pais.codigo_fifa == codigo_fifa:
                messagebox.showerror("Error", "El código FIFA ingresado ya le ha sido asignado a un país")
                return 
            elif pais.ranking_fifa == ranking_fifa:
                messagebox.showerror("Error", "El ranking FIFA ingresado ya le ha sido asignado a un país")
                return

        if lista_paises == []:
            archivo = open("paises.txt", "a")
            linea = codigo_fifa + ";" + nombre + ";" + continente + ";" + ranking_fifa_texto
            archivo.write(linea)
            archivo.close()
        else:
            archivo = open("paises.txt", "a")
            linea = "\n" + codigo_fifa + ";" + nombre + ";" + continente + ";" + ranking_fifa_texto
            archivo.write(linea)
            archivo.close()

        nuevo_pais = Pais(codigo_fifa, nombre, continente, ranking_fifa)
        lista_paises += [nuevo_pais]

        numero = contar(lista_paises) - 1

        if numero % 2 == 0:
            self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("evenrow",))
        else:
            self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("oddrow",))

        self.label_numero_paises.config(text=contar(lista_paises))
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

    """
    Nombre: actualizar
    Entrada: datos de los entry y spinbox
    Salida: actualiza país seleccionado
    Restricciones: primero se debe seleccionar un país
    """
    def actualizar(self):
       
        global lista_paises

        codigo_fifa = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        continente = self.seleccion.get().strip()
        ranking_fifa_texto = self.spinbox_ranking.get().strip()

        if codigo_fifa == "Ej: CRC":
            messagebox.showerror("¡Error!", "Ingrese el código FIFA del país")
            return 
        elif nombre == "Ej: Costa Rica":
            messagebox.showerror("¡Error!", "Ingrese el nombre del país")
            return 
        elif continente == "Seleccione un Continente":
            messagebox.showerror("¡Error!", "Debe seleccionar un continente para el país")
            return 
        elif ranking_fifa_texto == "":
            messagebox.showerror("¡Error!", "Debe ingresar el ranking FIFA del país")
            return 
        elif tiene_tres_caracteres(codigo_fifa) == False:
            messagebox.showerror("!Error¡", "El código FIFA debe contener 3 letras")
            return 
        
        codigo_fifa = codigo_fifa.upper()
        continente = continente.title()
        nombre = nombre.title()  
        ranking_fifa = int(ranking_fifa_texto)

        archivo_paises = open("paises.txt", "r")
        contenido_paises = archivo_paises.readlines()
        archivo_paises.close()

        contenido_paises_dividido = []

        for linea in contenido_paises:
            contenido_paises_dividido += [linea.strip().split(";")]

        for pais in lista_paises:
            if pais.codigo_fifa == codigo_fifa:
                pais.actualizar_datos(codigo_fifa, nombre, continente, ranking_fifa)
                break
        
        for pais in contenido_paises_dividido:
            if pais[0] == codigo_fifa:
                pais[1] = nombre
                pais[2] = continente
                pais[3] = ranking_fifa_texto
                break

        archivo_paises_modificar = open("paises.txt", "w")

        contador = 0
        cantidad = contar(contenido_paises_dividido)

        for pais in contenido_paises_dividido:
            linea = pais[0] + ";" + pais[1] + ";" + pais[2] + ";" + pais[3]

            if contador < cantidad - 1:
                linea = linea + "\n"

            archivo_paises_modificar.write(linea)
            contador = contador + 1

        archivo_paises_modificar.close()

        selected = self.tree_view.focus()

        self.tree_view.item(selected, text="", values=(codigo_fifa, nombre, continente, ranking_fifa))

        messagebox.showinfo(None, "País actualizado correctamente")
        self.limpiar_selecciones()
    
    """
    Nombre: limpiar_selecciones
    Entrada: no recibe parámetros
    Salida: limpia campos de país
    Restricciones: los entry deben existir
    """
    def limpiar_selecciones(self):
            
        self.entry_codigo.config(state="normal")
        self.entry_nombre.config(state="normal")
        self.boton_guardar.config(state="disabled")
        self.boton_anadir_pais.config(state="normal")
        self.combobox_continente.config(state="readonly")
            
        self.entry_codigo.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.combobox_continente.delete(0, "end")
        self.spinbox_ranking.delete(0, "end")
            
        self.entry_codigo.insert(0, "Ej: CRC")
        self.entry_nombre.insert(0, "Ej: Costa Rica")
        self.combobox_continente.set("Seleccione un Continente")

    """
    Nombre: pais_seleccionado
    Entrada: evento
    Salida: coloca los datos seleccionados en los entry
    Restricciones: debe seleccionarse una fila de la tabla
    """
    def pais_seleccionado(self, e=None):  

        self.entry_codigo.config(state="normal")
        self.entry_nombre.config(state="normal")  
            
        self.entry_codigo.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.combobox_continente.delete(0, "end")
        self.spinbox_ranking.delete(0, "end")
    
        selected = self.tree_view.focus()
    
        values = self.tree_view.item(selected, "values")
        cantidad_valores = contar(values)

        if cantidad_valores < 4:
            return 
    
        self.entry_codigo.insert(0, values[0])
        self.entry_nombre.insert(0, values[1])
        self.combobox_continente.set(values[2])
        self.spinbox_ranking.insert(0, values[3])

        self.entry_codigo.config(state="disabled")
        self.entry_nombre.config(state="disabled")
        self.boton_guardar.config(state="active")
        self.boton_anadir_pais.config(state="disabled")
        self.combobox_continente.config(state="disabled")


class Administrar_Entrenadores_Jugadores(tk.Toplevel):

    """
    Nombre: Administrar_Entrenadores_Jugadores
    Entrada: principal
    Salida: crea ventana de entrenadores y jugadores
    Restricciones: principal debe existir
    """
    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)

        self.principal = principal

        self.geometry("1535x930+-7+-0")
        self.resizable(False, False)
        self.title("Administración de Entrenadores y Jugadores")

        self.frames()

    """
    Nombre: frames
    Entrada: no recibe parámetros
    Salida: crea marcos de la ventana
    Restricciones: usa tkinter
    """
    def frames(self):

        self.frame_grande = tk.Frame(self,
                                     bd=1,
                                     relief="solid")
        self.frame_grande.place(x=10, y=10, width=1515, height=830)

        self.frame_registrar_entrenadores = tk.Frame(self, 
                                                     bd=1, 
                                                     relief="solid")
        self.frame_registrar_entrenadores.place(x=30, y=20, width=550, height=400)

        label_titulo_registrar = tk.Label(self, 
                                          text="📋 Registrar / Editar Entrenador",
                                          font=("arial", 12, "bold"),
                                          anchor="w")
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
        label_nombre_entrenador.place(x=50, y=120, width=150, height=30)

        label_apellidos_entrenador = tk.Label(self, 
                                              text="Apellidos:",
                                              font=("arial", 10, "bold"),
                                              anchor="w")
        label_apellidos_entrenador.place(x=50, y=160, width=150, height=30)

        label_nacionalidad_entrenador = tk.Label(self,
                                                 text="Nacionalidad:",
                                                 font=("arial", 10, "bold"),
                                                 anchor="w")
        label_nacionalidad_entrenador.place(x=50, y=200, width=150, height=30)

        label_fecha_entrenador = tk.Label(self,
                                          text="Fecha de Nacimiento:",
                                          font=("arial", 10, "bold"),
                                          anchor="w")
        label_fecha_entrenador.place(x=50, y=240, width=200, height=30)

        self.frame_asignar_seleccion = tk.Frame(self,
                                                bd=1,
                                                relief="solid")
        self.frame_asignar_seleccion.place(x=590, y=20, width=350, height=400)

        self.frame_entrenadores = tk.Frame(self,
                                           bd=1,
                                           relief="solid")
        self.frame_entrenadores.place(x=950, y=20, width=560, height=400)

        self.frame_registrar_jugadores = tk.Frame(self,
                                                  bd=1,
                                                  relief="solid")
        self.frame_registrar_jugadores.place(x=30, y=430, width=750, height=400)

        self.frame_seleccion = tk.Frame(self,
                                        bd=1,
                                        relief="solid")
        self.frame_seleccion.place(x=790, y=430, width=200, height=400)

        self.frame_jugadores = tk.Frame(self,
                                        bd=1,
                                        relief="solid")
        self.frame_jugadores.place(x=1000, y=430, width=510, height=400)

        boton_volver = tk.Button(self,
                                 text="Regresar al menú principal",
                                 font=("Arial", 14, "bold"),
                                 bg=gris_claro,
                                 fg=negro,
                                 command=self.volver)
        boton_volver.place(x=1200, y=860, width=300, height=45)

    """
    Nombre: volver
    Entrada: no recibe parámetros
    Salida: vuelve al menú principal
    Restricciones: principal debe existir
    """
    def volver(self):
        self.destroy()
        self.principal.deiconify()


class Configuracion_Mundial(tk.Toplevel):

    """
    Nombre: Configuracion_Mundial
    Entrada: principal
    Salida: crea ventana de configuración
    Restricciones: principal debe existir
    """
    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)

        self.principal = principal

        self.geometry("1535x930+-7+-0")
        self.resizable(False, False)

        boton_volver = tk.Button(self,
                                 text="Regresar al menú principal",
                                 font=("Arial", 14, "bold"),
                                 bg=gris_claro,
                                 fg=negro,
                                 command=self.volver)
        boton_volver.place(x=1200, y=860, width=300, height=45)

    """
    Nombre: volver
    Entrada: no recibe parámetros
    Salida: vuelve al menú principal
    Restricciones: principal debe existir
    """
    def volver(self):
        self.destroy()
        self.principal.deiconify()


###JuSTIN
"""
Nombre: Jugar_Mundial
Entrada: principal
Salida: crea una ventana gráfica para jugar el mundial
Restricciones: se debe llamar desde la pantalla principal
"""
class Jugar_Mundial(tk.Toplevel):

    """
    Nombre: Jugar_Mundial
    Entrada: principal
    Salida: inicializa la ventana Jugar Mundial
    Restricciones: principal debe existir
    """
    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)

        self.principal = principal

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
    Salida: crea el menú lateral izquierdo
    Restricciones: usa colores globales
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
                                 anchor="w",
                                 command=self.volver_inicio)
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
    Salida: muestra el título
    Restricciones: debe existir la ventana
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
    Salida: crea el panel de estado
    Restricciones: no aplica
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
    Salida: crea botones principales
    Restricciones: los comandos de simulación quedan pendientes
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
                                 relief="raised",
                                 command=self.volver_inicio)
        boton_volver.place(x=25, y=160, width=280, height=30)

    """
    Nombre: resultados_recientes
    Entrada: no recibe parámetros
    Salida: crea tabla de resultados
    Restricciones: no aplica
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
    Salida: crea tabla de grupo
    Restricciones: no aplica
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
    Entrada: no recibe parámetros
    Salida: crea panel del campeón
    Restricciones: debe existir trofeo.jpg
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
    Entrada: no recibe parámetros
    Salida: dibuja llave eliminatoria
    Restricciones: no aplica
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

    """
    Nombre: volver_inicio
    Entrada: no recibe parámetros
    Salida: vuelve al menú principal
    Restricciones: principal debe existir
    """
    def volver_inicio(self):
        self.destroy()
        self.principal.deiconify()


"""
Nombre: Estadisticas
Entrada: principal
Salida: crea la ventana de estadísticas y ranking
Restricciones: usa las listas globales del programa
"""
class Estadisticas(tk.Toplevel):

    """
    Nombre: Estadisticas
    Entrada: principal
    Salida: inicializa la ventana de estadísticas
    Restricciones: principal debe existir
    """
    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)

        self.principal = principal

        self.geometry("1535x930+-7+-0")
        self.title("Estadísticas / Ranking")
        self.resizable(False, False)
        self.config(bg=blanco)

        self.encabezado()
        self.tarjetas_resumen()
        self.tabla_ranking_paises()
        self.tabla_ranking_jugadores()
        self.tabla_estadisticas_selecciones()
        self.botones()
        self.actualizar_estadisticas()

    """
    Nombre: encabezado
    Entrada: no recibe parámetros
    Salida: crea encabezado
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
        label_titulo.place(x=40, y=18, width=600, height=50)

        label_subtitulo = tk.Label(frame_titulo,
                                   text="Resumen general de países, selecciones, jugadores y rendimiento",
                                   font=("Arial", 13, "bold"),
                                   bg=azul_oscuro,
                                   fg=celeste,
                                   anchor="w")
        label_subtitulo.place(x=45, y=60, width=800, height=25)

    """
    Nombre: tarjetas_resumen
    Entrada: no recibe parámetros
    Salida: crea tarjetas con totales
    Restricciones: usa listas globales
    """
    def tarjetas_resumen(self):
        self.frame_total_paises = tk.LabelFrame(self,
                                                text=" Países ",
                                                font=("Arial", 13, "bold"),
                                                fg=azul_oscuro,
                                                bg=blanco,
                                                bd=2,
                                                relief="solid")
        self.frame_total_paises.place(x=40, y=120, width=320, height=120)

        self.label_total_paises = tk.Label(self.frame_total_paises,
                                           text=0,
                                           font=("Arial", 35, "bold"),
                                           bg=blanco,
                                           fg=azul)
        self.label_total_paises.place(x=20, y=25, width=260, height=55)

        label_paises = tk.Label(self.frame_total_paises,
                                text="registrados",
                                font=("Arial", 13),
                                bg=blanco,
                                fg=gris)
        label_paises.place(x=20, y=78, width=260, height=25)

        self.frame_total_selecciones = tk.LabelFrame(self,
                                                     text=" Selecciones ",
                                                     font=("Arial", 13, "bold"),
                                                     fg=azul_oscuro,
                                                     bg=blanco,
                                                     bd=2,
                                                     relief="solid")
        self.frame_total_selecciones.place(x=400, y=120, width=320, height=120)

        self.label_total_selecciones = tk.Label(self.frame_total_selecciones,
                                                text=0,
                                                font=("Arial", 35, "bold"),
                                                bg=blanco,
                                                fg=verde)
        self.label_total_selecciones.place(x=20, y=25, width=260, height=55)

        label_selecciones = tk.Label(self.frame_total_selecciones,
                                     text="registradas",
                                     font=("Arial", 13),
                                     bg=blanco,
                                     fg=gris)
        label_selecciones.place(x=20, y=78, width=260, height=25)

        self.frame_total_entrenadores = tk.LabelFrame(self,
                                                      text=" Entrenadores ",
                                                      font=("Arial", 13, "bold"),
                                                      fg=azul_oscuro,
                                                      bg=blanco,
                                                      bd=2,
                                                      relief="solid")
        self.frame_total_entrenadores.place(x=760, y=120, width=320, height=120)

        self.label_total_entrenadores = tk.Label(self.frame_total_entrenadores,
                                                 text=0,
                                                 font=("Arial", 35, "bold"),
                                                 bg=blanco,
                                                 fg=anaranjado)
        self.label_total_entrenadores.place(x=20, y=25, width=260, height=55)

        label_entrenadores = tk.Label(self.frame_total_entrenadores,
                                      text="registrados",
                                      font=("Arial", 13),
                                      bg=blanco,
                                      fg=gris)
        label_entrenadores.place(x=20, y=78, width=260, height=25)

        self.frame_total_jugadores = tk.LabelFrame(self,
                                                   text=" Jugadores ",
                                                   font=("Arial", 13, "bold"),
                                                   fg=azul_oscuro,
                                                   bg=blanco,
                                                   bd=2,
                                                   relief="solid")
        self.frame_total_jugadores.place(x=1120, y=120, width=320, height=120)

        self.label_total_jugadores = tk.Label(self.frame_total_jugadores,
                                              text=0,
                                              font=("Arial", 35, "bold"),
                                              bg=blanco,
                                              fg=rojo)
        self.label_total_jugadores.place(x=20, y=25, width=260, height=55)

        label_jugadores = tk.Label(self.frame_total_jugadores,
                                   text="registrados",
                                   font=("Arial", 13),
                                   bg=blanco,
                                   fg=gris)
        label_jugadores.place(x=20, y=78, width=260, height=25)
    """
    Nombre: tabla_ranking_paises
    Entrada: no recibe parámetros
    Salida: crea tabla para países
    Restricciones: usa lista_paises
    """
    def tabla_ranking_paises(self):
        frame_paises = tk.LabelFrame(self,
                                     text=" Ranking FIFA de Países ",
                                     font=("Arial", 14, "bold"),
                                     fg=azul_oscuro,
                                     bg=blanco,
                                     bd=1,
                                     relief="solid")
        frame_paises.place(x=40, y=270, width=700, height=280)

        self.tabla_paises = ttk.Treeview(frame_paises,
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
    

if __name__ == "__main__":
    app = Pantalla_Principal()
    app.mainloop()