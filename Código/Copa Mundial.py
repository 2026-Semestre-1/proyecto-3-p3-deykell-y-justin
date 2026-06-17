# ===  Copa Mundial  === #

# Librerías

import tkinter as tk
from PIL import ImageTk, Image




class Pais:

    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):

        if not (isinstance(codigo_fifa, str) and isinstance(nombre, str) and isinstance(continente, str)):
            return "Error: los parámetros deben ser str"
        elif not isinstance(ranking_fifa, int):
            return "Error: el parámetro debe ser int"

        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa

class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        if not (isinstance(nombre, str) and isinstance(apellido, str) and isinstance(fecha_nacimiento, str) and isinstance(nacionalidad, str)):
            return "Error: los parámetros deben ser str"

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad


class Entrenador(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)

        if not (isinstance(licencia, str) and isinstance(sistema_juego, str)):
            return "Error: los parámetros deben ser str"
        elif not isinstance(experiencia_anios, int):
            return "Error: el parámetro debe ser int"

        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego


class Futbolista(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_targetas_amarillas, total_targetas_rojas, goles, asistencias, puntaje_individual):
        Persona.__init__(nombre, apellido, fecha_nacimiento, nacionalidad)

        if not isinstance(posicion, int):
            return "Error: el parpametro debe ser str"
        elif not (isinstance(dorsal, int) and isinstance(total_targetas_amarillas, int) and isinstance(total_targetas_rojas, int) and isinstance(goles, int) and isinstance(asistencias, int) and isinstance(puntaje_individual, int)):
            return "Error: los parámetros deben ser int"

        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.goles = goles
        self.asistencias = asistencias
        self.puntaje_individual = puntaje_individual

class Seleccion:

    def __init__(self, codigo_equipo, pais, entrenador, jugadores, total_goles_favor, total_goles_contra, total_tarjetas_amarillas, total_tarjetas_rojas, fuerza_equipo):
        
        if not isinstance(codigo_equipo, str):
            return "Error: el parámetro debe ser str"
        if not (isinstance(total_goles_favor, int) and isinstance(total_goles_contra, int) and isinstance(total_tarjetas_amarillas) and isinstance(total_tarjetas_rojas) and isinstance(fuerza_equipo)):
            return "Error: los parámetros deben ser int"

        self.codigo_equipo = codigo_equipo
        self.pais = Pais()
        self.entrenador = entrenador()
        self.jugadores = []
        self.total_goles_favor = total_goles_favor
        self.total_goles_contra = total_goles_contra
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.fuerza_equipo = fuerza_equipo

class Partido:

    def __init__(self, id_partido, equipo_1, equipo_2, goles_equipo1, goles_equipo2, fase, fecha):
        if not (isinstance(fase, str) and isinstance(fecha, str)):
            return "Error: los parámetros deben ser str"
        elif not (isinstance(goles_equipo1, int) and isinstance(goles_equipo2, int)):
            return "Error: los parámetros deben ser int"
        
        equipo_1 = Seleccion()
        equipo_2 = Seleccion()
        

class Grupo:

    def __init__(self, nombre_grupo, equipos, partidos):

        if not isinstance(nombre_grupo, str):
            return "Error: el parámetro debe ser str"

        self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []

class Fase:

    def __init__(self, nombre_fase, partidos):

        if not isinstance(nombre_fase, str):
            return "Error: el parámetro debe ser str"

        self.nombre_fase = nombre_fase
        self.partidos = []


class Mundial:

    def __init__(self, nombre, anio, paises, selecciones, grupos, fases, campeon):
        
        if not isinstance(nombre, str):
            return "Error: el parámetro debe ser str"
        elif not isinstance(anio, int):
            return "Error: el parámetro debe ser int"

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

        admin_paises_selecciones = tk.Button(self,
                                             text= "Administrar Países \ny Selecciones",
                                             font=(30))
        admin_paises_selecciones.place(x=457, y=328, width=292, height=125)

        admin_entrenadores_jugadores = tk.Button(self,
                                             text= "Administrar Entrenadores \ny Jugadores",
                                             font=(30))
        admin_entrenadores_jugadores.place(x=774, y=328, width=292, height=125)
        
        config_mundial = tk.Button(self,
                                   text= "Configurar Mundial Países \n(Grupos)",
                                   font=(30))
        config_mundial.place(x=457, y=480, width=292, height=125)    

        estadisticas = tk.Button(self,
                                 text= "Estadísticas / Ranking",
                                 font=(30))
        estadisticas.place(x=774, y=480, width=292, height=125)

        jugar = tk.Button(self,
                          text= "Jugar Mundial",
                          font=(30))
        jugar.place(x=517, y=636, width=481, height=71)














if __name__ == "__main__":
    app = Pantalla_Principal()
    app.mainloop()

    
        


