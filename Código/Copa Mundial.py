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


        entry_codigo = tk.Entry(self,
                                fg=gris)
        entry_codigo.insert(0, "Ej: CRC")
        entry_codigo.place(x=500, y=170, width=200, height=30)

        entry_nombre = tk.Entry(self,
                                fg=gris)
        entry_nombre.insert(0, "Ej: Costa Rica")
        entry_nombre.place(x=500, y=210, width=300, height=30)

        continentes = ["América", "Europa", "África", "Oceanía"]
        conbobox_continente = ttk.Combobox(self,
                                          values=continentes,
                                          state="readonly")
        conbobox_continente.set("Seleccione un Continente")
        conbobox_continente.place(x=500, y=250, width=300, height=30)

        spinbox_ranking = tk.Spinbox(self,
                                     from_=1,
                                     to=100,
                                     width=300)
        spinbox_ranking.place(x=500, y=290, width=300, height=30)

        self.boton_limpiar = tk.Button(self,
                                  text="🧹Limpiar",
                                  font=("Arial", 14),
                                  bd=2,
                                  relief= "groove",
                                  fg=gris,
                                  bg=amarillo,
                                  anchor="w")
        self.boton_limpiar.place(x=680, y=350, width=100, height=40)

        self.boton_añadir_pais = tk.Button(self,
                                           text="➕ Añadir País",
                                           font=("Arial", 14),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="w")
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

class Jugar_Mundial(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("1535x930+-7+-0")
        self.resizable(False, False)

class Estadisticas(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("1535x930+-7+-0")
        self.resizable(False, False)












if __name__ == "__main__":
    app = Pantalla_Principal()
    app.mainloop()

    
        


