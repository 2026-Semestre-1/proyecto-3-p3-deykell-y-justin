# ===  Copa Mundial  === #

# Librerías

import tkinter as tk
from tkinter import ttk, messagebox

from PIL import ImageTk, Image

import random

# Colores principales de la interfaz
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
mundial_actual = None

"""
Nombre: contar
Descripción: Cuenta elementos de forma manual
Entrada: Lista o grupo de datos que se quiere contar
Salida: Cantidad de elementos encontrados
Restricción: El dato recibido debe poder recorrerse con for

"""
def contar(elementos):
    cantidad = 0

    for elemento in elementos:
        cantidad = cantidad + 1

    return cantidad

"""
Nombre: numero_a_texto
Descripción: Pasa un número a texto sin usar conversión directa
Entrada: Número entero que se necesita mostrar
Salida: Texto con el número escrito
Restricción: El número debe ser mayor o igual a cero
"""
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

"""
Nombre: texto_es_entero
Descripción: Revisa si un texto está formado solo por números
Entrada: Texto leído desde Entry, Spinbox o archivo
Salida: True si el texto es válido y False si no lo es
Restricción: No acepta letras, espacios ni símbolos
"""
def texto_es_entero(texto):
    if texto == "":
        return False

    for caracter in texto:
        if caracter != "0" and caracter != "1" and caracter != "2" and caracter != "3" and caracter != "4" and caracter != "5" and caracter != "6" and caracter != "7" and caracter != "8" and caracter != "9":
            return False

    return True

"""
Nombre: texto_es_nombre
Descripción: Revisa que un nombre tenga letras válidas
Entrada: Texto escrito por el usuario
Salida: True si puede usarse como nombre y False si no
Restricción: No acepta números ni símbolos extraños
"""
def texto_es_nombre(texto):
    if not isinstance(texto, str):
        return False

    if texto == "":
        return False

    letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚüÜ"
    tiene_letra = False

    for caracter in texto:
        if caracter in letras:
            tiene_letra = True
        elif caracter == " " or caracter == "-" or caracter == "'":
            tiene_letra = tiene_letra
        else:
            return False

    if tiene_letra == False:
        return False

    return True

"""
Nombre: texto_es_codigo
Descripción: Revisa que el código FIFA esté formado por letras
Entrada: Código escrito por el usuario
Salida: True si el código es válido y False si no
Restricción: Debe tener letras y respetar el tamaño solicitado
"""
def texto_es_codigo(texto):
    if not isinstance(texto, str):
        return False

    if texto == "":
        return False

    letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    for caracter in texto:
        if caracter not in letras:
            return False

    return True

"""
Nombre: Pais
Descripción: Guarda los datos de un país que puede participar en el Mundial
Entrada: Código FIFA, nombre, continente y ranking FIFA
Salida: Un país con sus datos principales listos para usarse
Restricción: El ranking FIFA debe estar entre 1 y 100
"""
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
        print("Ranking FIFA: " + numero_a_texto(self.ranking_fifa))
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

"""
Nombre: Persona
Descripción: Reúne los datos personales que se repiten en entrenadores y jugadores
Entrada: Nombre, apellido, fecha de nacimiento y nacionalidad
Salida: Una persona con la información básica guardada
Restricción: Los datos personales se trabajan como texto
"""
class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        if not (isinstance(nombre, str) and isinstance(apellido, str) and isinstance(fecha_nacimiento, str) and isinstance(nacionalidad, str)):
            print("Error: los parámetros deben ser str")
            return
        elif not texto_es_nombre(nombre) or not texto_es_nombre(apellido):
            print("Error: nombre y apellido solo deben contener letras")

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad

    def mostrar_datos(self):
        print("Nombre: " + self.nombre + " " + self.apellido)
        print("Fecha de Nacimiento: " + self.fecha_nacimiento)
        print("Nacionalidad: " + self.nacionalidad)
        print("")

"""
Nombre: Entrenador
Descripción: Guarda la información deportiva del entrenador de una selección
Entrada: Datos personales, licencia, años de experiencia y sistema de juego
Salida: Un entrenador que puede asignarse a una selección
Restricción: La experiencia se maneja como número entero
"""
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
        self.seleccion = ""

    def mostrar_datos(self):
        print("Nombre: " + self.nombre + " " + self.apellido)
        print("Fecha de Nacimiento: " + self.fecha_nacimiento)
        print("Nacionalidad: " + self.nacionalidad)
        print("Licencia: " + self.licencia)
        print("Experiencia: " + numero_a_texto(self.experiencia_anios))
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

"""
Nombre: Futbolista
Descripción: Representa a un jugador con sus datos y estadísticas del torneo
Entrada: Datos personales, dorsal, posición, tarjetas, goles, asistencias y puntaje
Salida: Un jugador registrado con sus acumulados
Restricción: Dorsal, tarjetas, goles, asistencias y puntaje deben ser enteros
"""
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
        self.seleccion = ""

    def mostrar_datos(self):
        print("Nombre: " + self.nombre + " " + self.apellido)
        print("Fecha de Nacimiento: " + self.fecha_nacimiento)
        print("Nacionalidad: " + self.nacionalidad)
        print("Dorsal: " + numero_a_texto(self.dorsal))
        print("Posicion: " + self.posicion)
        print("Tarjetas Amarillas: " + numero_a_texto(self.total_tarjetas_amarillas))
        print("Tarjetas Rojas: " + numero_a_texto(self.total_tarjetas_rojas))
        print("Goles: " + numero_a_texto(self.goles))
        print("Asistencias: " + numero_a_texto(self.asistencias))
        print("Puntaje Individual: " + numero_a_texto(self.puntaje_individual))
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


    def registrar_tarjeta(self, tipo):
        if not isinstance(tipo, str):
            print("Error: el parámetro debe ser de tipo str")
            return

        if tipo == "amarilla":
            self.total_tarjetas_amarillas += 1
        elif tipo == "roja":
            self.total_tarjetas_rojas += 1
        else:
            return "Error: ingrese el tipo de tarjeta amarilla o roja"
        
"""
Nombre: Seleccion
Descripción: Une el país, el entrenador, los jugadores y los datos deportivos del equipo
Entrada: Código del equipo, país y entrenador
Salida: Una selección lista para formar grupos y jugar partidos
Restricción: Debe tener país y entrenador asignados
"""
class Seleccion:

    def __init__(self, codigo_equipo, pais, entrenador):
        if not isinstance(codigo_equipo, str):
            print("Error: el parámetro debe ser str")
            return

        self.codigo_equipo = codigo_equipo
        self.pais = pais
        self.entrenador = entrenador
        self.jugadores = []
        self.total_goles_a_favor = 0
        self.total_goles_en_contra = 0
        self.total_tarjetas_amarillas = 0
        self.total_tarjetas_rojas = 0
        self.goles_torneo_favor = 0
        self.goles_torneo_contra = 0
        self.tarjetas_amarillas_torneo = 0
        self.tarjetas_rojas_torneo = 0
        self.fuerza_equipo = 0
        self.puntos = 0
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.diferencia_goles = 0
        self.fase_alcanzada = "Fase de grupos"

    def mostrar_datos(self):
        print("Código de la Selección: " + self.codigo_equipo)
        print("País: " + self.pais.nombre)
        if self.entrenador is not None and self.entrenador != "":
            print("Entrenador: " + self.entrenador.nombre + " " + self.entrenador.apellido)
        print("Jugadores:")
        for futbolista in self.jugadores:
            print(futbolista.nombre + " " + futbolista.apellido + " Dorsal: " + numero_a_texto(futbolista.dorsal))
        print("Goles a Favor: " + numero_a_texto(self.total_goles_a_favor))
        print("Goles en Contra: " + numero_a_texto(self.total_goles_en_contra))
        print("Fuerza de equipo: " + numero_a_texto(self.fuerza_equipo))
        print("")

    def agregar_jugador(self, futbolista):
        if contar(self.jugadores) < 23:
            self.jugadores += [futbolista]
        else:
            return "Error: La plantilla ya cuenta con 23 jugadores"

    def eliminar_jugador(self, dorsal):
        nueva_lista = []
        for jugador in self.jugadores:
            if jugador.dorsal != dorsal:
                nueva_lista += [jugador]
        self.jugadores = nueva_lista

    def asignar_entrenador(self, entrenador):
        self.entrenador = entrenador

    def reiniciar_estadisticas(self):
        self.total_goles_a_favor = 0
        self.total_goles_en_contra = 0
        self.total_tarjetas_amarillas = 0
        self.total_tarjetas_rojas = 0
        self.goles_torneo_favor = 0
        self.goles_torneo_contra = 0
        self.tarjetas_amarillas_torneo = 0
        self.tarjetas_rojas_torneo = 0
        self.puntos = 0
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.diferencia_goles = 0
        self.fase_alcanzada = "Fase de grupos"

        for jugador in self.jugadores:
            jugador.total_tarjetas_amarillas = 0
            jugador.total_tarjetas_rojas = 0
            jugador.goles = 0
            jugador.asistencias = 0

    def registrar_estadisticas_torneo(self, goles_favor, goles_contra, tarjetas_am, tarjetas_roj):
        self.goles_torneo_favor += goles_favor
        self.goles_torneo_contra += goles_contra
        self.tarjetas_amarillas_torneo += tarjetas_am
        self.tarjetas_rojas_torneo += tarjetas_roj

    """
    Nombre: registrar_resultado
    Descripción: Suma puntos y estadísticas de grupo después de un partido
    Entrada: Goles a favor y goles en contra
    Salida: Puntos, partidos jugados, goles y diferencia actualizados
    Restricción: Se usa para resultados de fase de grupos
    """
    def registrar_resultado(self, goles_favor, goles_contra, tarjetas_am, tarjetas_roj):
        self.total_goles_a_favor += goles_favor
        self.total_goles_en_contra += goles_contra
        self.total_tarjetas_amarillas += tarjetas_am
        self.total_tarjetas_rojas += tarjetas_roj
        self.partidos_jugados += 1
        self.diferencia_goles = self.total_goles_a_favor - self.total_goles_en_contra

        if goles_favor > goles_contra:
            self.puntos += 3
            self.partidos_ganados += 1
        elif goles_favor == goles_contra:
            self.puntos += 1
            self.partidos_empatados += 1
        else:
            self.partidos_perdidos += 1
    """
    Nombre: ordenar_jugadores_por_puntaje
    Descripción: ordena los jugadores de la selección desde el puntaje más alto hasta el más bajo
    Entrada: usa la lista de jugadores guardada en la selección
    Salida: lista de jugadores ordenada por puntaje individual
    Restricción: cada jugador debe tener un puntaje individual registrado
    """

    def ordenar_jugadores_por_puntaje(self):
        jugadores_ordenados = []
        for jugador in self.jugadores:
            jugadores_ordenados += [jugador]

        cantidad = contar(jugadores_ordenados)
        i = 0
        while i < cantidad - 1:
            j = i + 1
            while j < cantidad:
                if jugadores_ordenados[j].puntaje_individual > jugadores_ordenados[i].puntaje_individual:
                    jugadores_ordenados[i], jugadores_ordenados[j] = jugadores_ordenados[j], jugadores_ordenados[i]
                j += 1
            i += 1
        return jugadores_ordenados


    """
    Nombre: promedio_11_mejores
    Descripción: calcula el promedio de puntaje de los 11 mejores jugadores de la selección
    Entrada: usa los jugadores ordenados por puntaje individual
    Salida: promedio entero de los mejores 11 jugadores
    Restricción: la selección debe tener jugadores registrados
    """

    def promedio_11_mejores(self):
        suma = 0
        cantidad = 0
        for jugador in self.ordenar_jugadores_por_puntaje():
            if cantidad < 11:
                suma += jugador.puntaje_individual
                cantidad += 1
        if cantidad == 0:
            return 0
        return suma // cantidad

    """
    Nombre: calcular_fuerza_equipo
    Descripción: Calcula la fuerza del equipo usando jugadores, entrenador y ranking
    Entrada: Datos de jugadores, entrenador y ranking FIFA
    Salida: Fuerza del equipo actualizada
    Restricción: La selección debe tener jugadores y entrenador
    """
    def calcular_fuerza_equipo(self):
        promedio_jugadores = self.promedio_11_mejores()
        factor_entrenador = 0

        if self.entrenador is not None and self.entrenador != "":
            factor_entrenador = self.entrenador.experiencia_anios * 4
            if factor_entrenador > 100:
                factor_entrenador = 100

        factor_ranking = 100 - self.pais.ranking_fifa
        self.fuerza_equipo = (promedio_jugadores * 60 + factor_entrenador * 25 + factor_ranking * 15) // 100
        return self.fuerza_equipo

"""
Nombre: Partido
Descripción: Se encarga de guardar y simular un partido entre dos selecciones
Entrada: Identificador, equipos, goles, fase y fecha
Salida: Resultado del partido con ganador cuando corresponde
Restricción: Los equipos deben estar creados antes de simular
"""
class Partido:

    def __init__(self, id_partido, equipo_1, equipo_2, goles_equipo1, goles_equipo2, fase, fecha):
        if not (isinstance(fase, str) and isinstance(fecha, str)):
            print("Error: los parámetros deben ser str")
            return
        elif not (isinstance(goles_equipo1, int) and isinstance(goles_equipo2, int)):
            print("Error: los parámetros deben ser int")
            return

        self.id = id_partido
        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.goles_equipo1 = goles_equipo1
        self.goles_equipo2 = goles_equipo2
        self.fase = fase
        self.fecha = fecha
        self.penales_equipo1 = 0
        self.penales_equipo2 = 0
        self.jugado = False



    """
    Nombre: buscar_jugador_indice
    Descripción: busca un jugador dentro de una lista usando la posición indicada
    Entrada: lista de jugadores y el índice que se quiere buscar
    Salida: jugador encontrado o None si el índice no existe
    Restricción: el índice debe estar dentro del rango de la lista de jugadores
    """

    def buscar_jugador_indice(self, jugadores, indice_buscado):
        indice = 0
        for jugador in jugadores:
            if indice == indice_buscado:
                return jugador
            indice += 1
        return None



    """
    Nombre: registrar_goles_jugadores
    Descripción: asigna los goles y asistencias a jugadores de una selección después de simular un partido
    Entrada: selección que anotó y cantidad de goles realizados
    Salida: jugadores actualizados con goles y asistencias
    Restricción: la selección debe tener jugadores registrados para poder asignar estadísticas
    """

    def registrar_goles_jugadores(self, seleccion, cantidad_goles):
        cantidad_jugadores = contar(seleccion.jugadores)
        contador = 0

        while contador < cantidad_goles and cantidad_jugadores > 0:
            indice_goleador = random.randint(0, cantidad_jugadores - 1)
            goleador = self.buscar_jugador_indice(seleccion.jugadores, indice_goleador)

            if goleador is not None:
                goleador.registrar_gol()

            if cantidad_jugadores > 1:
                indice_asistente = random.randint(0, cantidad_jugadores - 1)

                while indice_asistente == indice_goleador:
                    indice_asistente = random.randint(0, cantidad_jugadores - 1)

                asistente = self.buscar_jugador_indice(seleccion.jugadores, indice_asistente)

                if asistente is not None:
                    asistente.registrar_asistencia()

            contador += 1

    """
    Nombre: calcular_tarjetas_equipo
    Descripción: calcula cuántas tarjetas puede recibir una selección según la fuerza del rival
    Entrada: selección que se evalúa y selección rival
    Salida: lista con cantidad de tarjetas amarillas y tarjetas rojas
    Restricción: ambas selecciones deben tener fuerza de equipo calculada
    """

    def calcular_tarjetas_equipo(self, seleccion, rival):
        diferencia = rival.fuerza_equipo - seleccion.fuerza_equipo
        maximo_amarillas = 3
        probabilidad_roja = 5

        if diferencia > 25:
            maximo_amarillas = 5
            probabilidad_roja = 18
        elif diferencia > 10:
            maximo_amarillas = 4
            probabilidad_roja = 10
        elif diferencia < -25:
            maximo_amarillas = 2
            probabilidad_roja = 3

        amarillas = random.randint(0, maximo_amarillas)
        rojas = 0

        if random.randint(1, 100) <= probabilidad_roja:
            rojas = 1

        return [amarillas, rojas]
    """
    Nombre: registrar_tarjetas_jugadores
    Descripción: reparte las tarjetas amarillas y rojas entre jugadores de una selección
    Entrada: selección, cantidad de tarjetas amarillas y cantidad de tarjetas rojas
    Salida: jugadores actualizados con sus tarjetas registradas
    Restricción: la selección debe tener jugadores para poder asignar las tarjetas
    """

    def registrar_tarjetas_jugadores(self, seleccion, amarillas, rojas):
        cantidad_jugadores = contar(seleccion.jugadores)
        contador = 0

        while contador < amarillas and cantidad_jugadores > 0:
            jugador = self.buscar_jugador_indice(seleccion.jugadores, random.randint(0, cantidad_jugadores - 1))
            if jugador is not None:
                jugador.registrar_tarjeta("amarilla")
            contador += 1

        contador = 0
        while contador < rojas and cantidad_jugadores > 0:
            jugador = self.buscar_jugador_indice(seleccion.jugadores, random.randint(0, cantidad_jugadores - 1))
            if jugador is not None:
                jugador.registrar_tarjeta("roja")
            contador += 1

    """
    Nombre: simular
    Descripción: Genera el marcador usando la fuerza de ambas selecciones
    Entrada: Dos selecciones y el nombre de la fase
    Salida: Goles, tarjetas, ganador y estadísticas actualizadas
    Restricción: Los equipos deben estar completos antes de jugar
    """
    def simular(self):
        fuerza1 = self.equipo_1.calcular_fuerza_equipo()
        fuerza2 = self.equipo_2.calcular_fuerza_equipo()
        diferencia = fuerza1 - fuerza2

        if diferencia > 30:
            self.goles_equipo1 = random.randint(2, 7)
            self.goles_equipo2 = random.randint(0, 3)
        elif diferencia > 15:
            self.goles_equipo1 = random.randint(1, 5)
            self.goles_equipo2 = random.randint(0, 4)
        elif diferencia < -30:
            self.goles_equipo1 = random.randint(0, 3)
            self.goles_equipo2 = random.randint(2, 7)
        elif diferencia < -15:
            self.goles_equipo1 = random.randint(0, 4)
            self.goles_equipo2 = random.randint(1, 5)
        else:
            self.goles_equipo1 = random.randint(0, 4)
            self.goles_equipo2 = random.randint(0, 4)

        tarjetas_equipo1 = self.calcular_tarjetas_equipo(self.equipo_1, self.equipo_2)
        tarjetas_equipo2 = self.calcular_tarjetas_equipo(self.equipo_2, self.equipo_1)

        self.registrar_goles_jugadores(self.equipo_1, self.goles_equipo1)
        self.registrar_goles_jugadores(self.equipo_2, self.goles_equipo2)

        self.registrar_tarjetas_jugadores(self.equipo_1, tarjetas_equipo1[0], tarjetas_equipo1[1])
        self.registrar_tarjetas_jugadores(self.equipo_2, tarjetas_equipo2[0], tarjetas_equipo2[1])

        self.equipo_1.registrar_estadisticas_torneo(self.goles_equipo1, self.goles_equipo2, tarjetas_equipo1[0], tarjetas_equipo1[1])
        self.equipo_2.registrar_estadisticas_torneo(self.goles_equipo2, self.goles_equipo1, tarjetas_equipo2[0], tarjetas_equipo2[1])

        if self.fase[0:5] == "Grupo":
            self.equipo_1.registrar_resultado(self.goles_equipo1, self.goles_equipo2, tarjetas_equipo1[0], tarjetas_equipo1[1])
            self.equipo_2.registrar_resultado(self.goles_equipo2, self.goles_equipo1, tarjetas_equipo2[0], tarjetas_equipo2[1])

        self.jugado = True

    def generar_ganador(self):
        if self.goles_equipo1 > self.goles_equipo2:
            return self.equipo_1
        elif self.goles_equipo2 > self.goles_equipo1:
            return self.equipo_2
        return None

    """
    Nombre: simular_penales
    Descripción: Define un ganador por penales si la eliminatoria queda empatada
    Entrada: Equipos que terminaron empatados
    Salida: Ganador del partido y marcador de penales
    Restricción: Solo se usa en fases eliminatorias
    """
    def simular_penales(self):
        self.penales_equipo1 = random.randint(2, 5)
        self.penales_equipo2 = random.randint(2, 5)
        while self.penales_equipo1 == self.penales_equipo2:
            self.penales_equipo1 = random.randint(2, 5)
            self.penales_equipo2 = random.randint(2, 5)

    def ganador_eliminatoria(self):
        ganador = self.generar_ganador()
        if ganador is not None:
            return ganador
        self.simular_penales()
        if self.penales_equipo1 > self.penales_equipo2:
            return self.equipo_1
        return self.equipo_2

    def mostrar_resultado(self):
        texto = self.equipo_1.pais.nombre + " " + numero_a_texto(self.goles_equipo1) + " - " + numero_a_texto(self.goles_equipo2) + " " + self.equipo_2.pais.nombre
        if self.penales_equipo1 != 0 or self.penales_equipo2 != 0:
            texto += " Penales: " + numero_a_texto(self.penales_equipo1) + " - " + numero_a_texto(self.penales_equipo2)
        return texto

"""
Nombre: Grupo
Descripción: Maneja los equipos de un grupo y su tabla de posiciones
Entrada: Nombre del grupo, equipos y partidos
Salida: Partidos jugados, tabla ordenada y clasificados
Restricción: El grupo necesita selecciones válidas
"""
class Grupo:

    def __init__(self, nombre_grupo, equipos, partidos):
        if not isinstance(nombre_grupo, str):
            print("Error: el parámetro debe ser str")
            return
        self.nombre_grupo = nombre_grupo
        self.equipos = equipos
        self.partidos = partidos

    def agregar_equipo(self, seleccion):
        if contar(self.equipos) < 4:
            self.equipos += [seleccion]
        else:
            return "Error: el grupo ya tiene 4 selecciones"

    """
    Nombre: jugar_partidos
    Descripción: Simula los partidos que corresponden dentro del grupo
    Entrada: Selecciones guardadas en el grupo
    Salida: Partidos creados con sus resultados
    Restricción: El grupo debe tener equipos suficientes
    """
    def jugar_partidos(self):
        cantidad = contar(self.equipos)
        i = 0
        while i < cantidad - 1:
            j = i + 1
            while j < cantidad:
                partido = Partido(contar(self.partidos) + 1, self.equipos[i], self.equipos[j], 0, 0, self.nombre_grupo, "Sin fecha")
                partido.simular()
                self.partidos += [partido]
                j += 1
            i += 1

    def seleccion_va_antes(self, seleccion1, seleccion2):
        if seleccion1.puntos != seleccion2.puntos:
            return seleccion1.puntos > seleccion2.puntos
        if seleccion1.diferencia_goles != seleccion2.diferencia_goles:
            return seleccion1.diferencia_goles > seleccion2.diferencia_goles
        return seleccion1.total_goles_a_favor > seleccion2.total_goles_a_favor

    """
    Nombre: calcular_tabla
    Descripción: Ordena la tabla con puntos y criterios de desempate
    Entrada: Equipos del grupo con sus estadísticas
    Salida: Tabla de posiciones ordenada
    Restricción: Los equipos deben tener datos de grupo
    """
    def calcular_tabla(self):
        tabla = []
        for seleccion in self.equipos:
            tabla += [seleccion]

        cantidad = contar(tabla)
        i = 0
        while i < cantidad - 1:
            j = i + 1
            while j < cantidad:
                if self.seleccion_va_antes(tabla[j], tabla[i]):
                    tabla[i], tabla[j] = tabla[j], tabla[i]
                j += 1
            i += 1
        return tabla

    def obtener_clasificados(self):
        clasificados = []
        contador = 0
        for seleccion in self.calcular_tabla():
            if contador < 2:
                clasificados += [seleccion]
            contador += 1
        return clasificados

    def mostrar_tabla(self):
        print(self.nombre_grupo)
        for seleccion in self.calcular_tabla():
            print(seleccion.pais.nombre + " Pts: " + numero_a_texto(seleccion.puntos))

"""
Nombre: Fase
Descripción: Representa una ronda eliminatoria del Mundial
Entrada: Nombre de la fase y partidos de esa ronda
Salida: Ganadores que pasan a la siguiente fase
Restricción: Cada partido debe terminar con un ganador
"""
class Fase:

    def __init__(self, nombre_fase, partidos):
        if not isinstance(nombre_fase, str):
            print("Error: el parámetro debe ser str")
            return
        self.nombre_fase = nombre_fase
        self.partidos = partidos
        self.clasificados = []

    def registrar_juego(self, equipo1, equipo2):
        self.partidos += [Partido(contar(self.partidos) + 1, equipo1, equipo2, 0, 0, self.nombre_fase, "Sin fecha")]

    def jugar_fase(self):
        self.clasificados = []
        for partido in self.partidos:
            partido.simular()
            ganador = partido.ganador_eliminatoria()
            ganador.fase_alcanzada = self.nombre_fase
            self.clasificados += [ganador]

    def mostrar_juegos(self):
        for partido in self.partidos:
            print(partido.mostrar_resultado())

    def obtener_clasificados(self):
        return self.clasificados

# Clase que controla la creación de grupos y la simulación completa
"""
Nombre: Mundial
Descripción: Controla el torneo completo desde los grupos hasta el campeón
Entrada: Nombre, año, países y selecciones cargadas
Salida: Grupos, fases, resultados, rankings y campeón del torneo
Restricción: Para 48 selecciones se forman 12 grupos de 4 equipos
"""
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
        self.paises = paises
        self.selecciones = selecciones
        self.grupos = grupos
        self.fases = fases
        self.campeon = campeon
        self.clasificados_actuales = []
        self.fase_actual = "Sin iniciar"
        self.partidos_jugados = []

    def registrar_pais(self, pais):
        self.paises += [pais]

    def registrar_seleccion(self, seleccion):
        self.selecciones += [seleccion]

    def seleccion_es_valida(self, seleccion):
        cantidad_jugadores = contar(seleccion.jugadores)
        return seleccion.entrenador is not None and seleccion.entrenador != "" and cantidad_jugadores >= 11 and cantidad_jugadores <= 23

    def obtener_selecciones_validas(self):
        validas = []
        for seleccion in self.selecciones:
            if self.seleccion_es_valida(seleccion):
                validas += [seleccion]
        return validas

    def reiniciar_torneo(self):
        self.fases = []
        self.campeon = None
        self.clasificados_actuales = []
        self.partidos_jugados = []
        for seleccion in self.selecciones:
            seleccion.reiniciar_estadisticas()
            seleccion.calcular_fuerza_equipo()

    def nombre_grupo_por_indice(self, indice):
        nombres = ["Grupo A", "Grupo B", "Grupo C", "Grupo D", "Grupo E", "Grupo F", "Grupo G", "Grupo H", "Grupo I", "Grupo J", "Grupo K", "Grupo L"]
        contador = 0
        for nombre in nombres:
            if contador == indice:
                return nombre
            contador += 1
        return "Grupo " + numero_a_texto(indice + 1)

    """
    Nombre: crear_grupos
    Descripción: Reparte las selecciones válidas en los grupos del Mundial
    Entrada: Cantidad de grupos indicada
    Salida: Lista de grupos creada
    Restricción: Debe haber suficientes selecciones para llenar los grupos
    """
    def crear_grupos(self, cantidad_grupos):
        self.reiniciar_torneo()
        validas = self.obtener_selecciones_validas()
        necesarias = cantidad_grupos * 4
        if contar(validas) < necesarias:
            return "Error: no hay suficientes selecciones válidas. Cada grupo ocupa 4 selecciones con entrenador y de 11 a 23 jugadores."

        self.grupos = []
        contador = 0
        while contador < cantidad_grupos:
            self.grupos += [Grupo(self.nombre_grupo_por_indice(contador), [], [])]
            contador += 1

        indice = 0
        for seleccion in validas:
            if indice < necesarias:
                self.grupos[indice % cantidad_grupos].agregar_equipo(seleccion)
            indice += 1

        self.fase_actual = "Grupos configurados"
        return "Grupos creados correctamente"

    """
    Nombre: jugar_fase_grupos
    Descripción: Juega todos los partidos de los grupos
    Entrada: Grupos creados previamente
    Salida: Resultados y clasificados de grupos actualizados
    Restricción: No debe ejecutarse dos veces sobre el mismo torneo
    """
    def jugar_fase_grupos(self):
        if contar(self.grupos) == 0:
            return "Error: primero debe configurar los grupos."

        if self.fase_actual != "Grupos configurados":
            return "Aviso: la fase de grupos ya fue simulada. Si desea empezar de nuevo, vuelva a Configurar Mundial y cree los grupos otra vez."

        self.partidos_jugados = []
        for grupo in self.grupos:
            grupo.partidos = []
            grupo.jugar_partidos()
            for partido in grupo.partidos:
                self.partidos_jugados += [partido]
        self.clasificados_actuales = self.obtener_clasificados_grupos()
        self.fase_actual = "Fase de grupos finalizada"
        return "Fase de grupos simulada correctamente"

    """
    Nombre: obtener_tercero_grupo
    Descripción: busca la selección que quedó en tercer lugar dentro de un grupo
    Entrada: grupo del cual se quiere obtener el tercer lugar
    Salida: selección que está en la tercera posición o None si no existe
    Restricción: el grupo debe tener una tabla calculada con suficientes selecciones
    """

    def obtener_tercero_grupo(self, grupo):
        tabla = grupo.calcular_tabla()
        contador = 0
        for seleccion in tabla:
            if contador == 2:
                return seleccion
            contador += 1
        return None

    """
    Nombre: ordenar_terceros
    Descripción: ordena las selecciones que quedaron terceras para escoger las mejores
    Entrada: lista de selecciones que quedaron en tercer lugar
    Salida: lista de terceros ordenada según puntos, diferencia de goles y goles a favor
    Restricción: las selecciones deben tener sus estadísticas de grupo actualizadas
    """

    def ordenar_terceros(self, terceros):
        terceros_ordenados = []
        for seleccion in terceros:
            terceros_ordenados += [seleccion]

        cantidad = contar(terceros_ordenados)
        comparador = Grupo("Comparador", [], [])

        i = 0
        while i < cantidad - 1:
            j = i + 1
            while j < cantidad:
                if comparador.seleccion_va_antes(terceros_ordenados[j], terceros_ordenados[i]):
                    terceros_ordenados[i], terceros_ordenados[j] = terceros_ordenados[j], terceros_ordenados[i]
                j += 1
            i += 1

        return terceros_ordenados

    """
    Nombre: obtener_mejores_terceros
    Descripción: Escoge los terceros lugares con mejor rendimiento
    Entrada: Terceros lugares de todos los grupos
    Salida: Ocho mejores terceros para completar dieciseisavos
    Restricción: Se usa con 12 grupos y 48 selecciones
    """
    def obtener_mejores_terceros(self):
        terceros = []
        for grupo in self.grupos:
            tercero = self.obtener_tercero_grupo(grupo)
            if tercero is not None:
                terceros += [tercero]

        terceros_ordenados = self.ordenar_terceros(terceros)
        mejores_terceros = []
        contador = 0

        for seleccion in terceros_ordenados:
            if contador < 8:
                mejores_terceros += [seleccion]
            contador += 1

        return mejores_terceros


    """
    Nombre: obtener_clasificados_grupos
    Descripción: obtiene las selecciones clasificadas después de la fase de grupos
    Entrada: usa los grupos creados dentro del Mundial
    Salida: lista de selecciones clasificadas a la fase eliminatoria
    Restricción: los grupos deben estar creados y jugados antes de buscar clasificados
    """

    def obtener_clasificados_grupos(self):
        clasificados = []
        for grupo in self.grupos:
            for seleccion in grupo.obtener_clasificados():
                clasificados += [seleccion]

        if contar(self.grupos) == 12:
            for seleccion in self.obtener_mejores_terceros():
                clasificados += [seleccion]

        return clasificados

    def nombre_fase_por_cantidad(self, cantidad):
        if cantidad == 32:
            return "Dieciseisavos de Final"
        if cantidad == 16:
            return "Octavos de Final"
        if cantidad == 8:
            return "Cuartos de Final"
        if cantidad == 4:
            return "Semifinales"
        if cantidad == 2:
            return "Final"
        return "Fase Eliminatoria"
    """
    Nombre: cantidad_es_valida_eliminatoria
    Descripción: revisa si la cantidad de equipos sirve para armar una fase eliminatoria
    Entrada: cantidad de selecciones clasificadas
    Salida: True si la cantidad es válida o False si no sirve
    Restricción: la cantidad debe ser 2, 4, 8, 16 o 32
    """

    def cantidad_es_valida_eliminatoria(self, cantidad):
        return cantidad == 2 or cantidad == 4 or cantidad == 8 or cantidad == 16 or cantidad == 32

    """
    Nombre: armar_fase_eliminatoria
    Descripción: crea los partidos de una fase eliminatoria usando las selecciones clasificadas
    Entrada: nombre de la fase y lista de selecciones clasificadas
    Salida: fase eliminatoria con sus partidos registrados
    Restricción: la cantidad de clasificados debe ser válida para poder emparejar equipos
    """

    def armar_fase_eliminatoria(self, nombre_fase, clasificados):
        fase = Fase(nombre_fase, [])
        cantidad = contar(clasificados)
        if self.cantidad_es_valida_eliminatoria(cantidad):
            i = 0
            j = cantidad - 1
            while i < j:
                fase.registrar_juego(clasificados[i], clasificados[j])
                i += 1
                j -= 1
        return fase

    """
    Nombre: jugar_siguiente_fase
    Descripción: Avanza el torneo a la siguiente ronda eliminatoria
    Entrada: Clasificados de la ronda anterior
    Salida: Nueva fase jugada o campeón definido
    Restricción: La fase anterior debe estar lista
    """
    def jugar_siguiente_fase(self):
        cantidad = contar(self.clasificados_actuales)
        if cantidad == 0:
            return "Error: primero debe simular la fase de grupos."
        if not self.cantidad_es_valida_eliminatoria(cantidad):
            return "Error: la cantidad de clasificados no sirve para una llave eliminatoria. Use una cantidad de grupos que deje 4, 8, 16 o 32 clasificados."

        nombre_fase = self.nombre_fase_por_cantidad(cantidad)
        fase = self.armar_fase_eliminatoria(nombre_fase, self.clasificados_actuales)
        fase.jugar_fase()
        self.fases += [fase]
        for partido in fase.partidos:
            self.partidos_jugados += [partido]
        self.clasificados_actuales = fase.obtener_clasificados()
        self.fase_actual = nombre_fase

        if contar(self.clasificados_actuales) == 1:
            self.campeon = self.clasificados_actuales[0]
            self.campeon.fase_alcanzada = "Campeón"
            self.fase_actual = "Finalizada"
        return nombre_fase + " simulada correctamente"

    def jugar_fase_eliminatoria(self, fase):
        return self.jugar_siguiente_fase()

    def determinar_campeon(self):
        while contar(self.clasificados_actuales) > 1:
            self.jugar_siguiente_fase()
        return self.campeon

    def mostrar_tabla_general(self):
        for grupo in self.grupos:
            grupo.mostrar_tabla()

    def generar_reporte(self):
        self.guardar_ranking_selecciones()
        self.guardar_ranking_goleadores()
        self.guardar_partidos()

    def guardar_ranking_selecciones(self):
        archivo = open("ranking_selecciones.txt", "w", encoding="utf-8")
        primera = True
        selecciones_ordenadas = []
        for seleccion in self.selecciones:
            selecciones_ordenadas += [seleccion]

        cantidad = contar(selecciones_ordenadas)
        i = 0
        while i < cantidad - 1:
            j = i + 1
            while j < cantidad:
                if Grupo("", [], []).seleccion_va_antes(selecciones_ordenadas[j], selecciones_ordenadas[i]):
                    selecciones_ordenadas[i], selecciones_ordenadas[j] = selecciones_ordenadas[j], selecciones_ordenadas[i]
                j += 1
            i += 1

        for seleccion in selecciones_ordenadas:
            linea = seleccion.pais.nombre + ";" + numero_a_texto(seleccion.puntos) + ";" + numero_a_texto(seleccion.diferencia_goles) + ";" + numero_a_texto(seleccion.goles_torneo_favor) + ";" + numero_a_texto(seleccion.tarjetas_amarillas_torneo) + ";" + numero_a_texto(seleccion.tarjetas_rojas_torneo) + ";" + seleccion.fase_alcanzada
            if primera:
                archivo.write(linea)
                primera = False
            else:
                archivo.write("\n" + linea)
        archivo.close()

    def jugador_va_antes_reporte(self, jugador1, jugador2):
        if jugador1.goles != jugador2.goles:
            return jugador1.goles > jugador2.goles
        if jugador1.asistencias != jugador2.asistencias:
            return jugador1.asistencias > jugador2.asistencias
        return jugador1.puntaje_individual > jugador2.puntaje_individual

    def ordenar_jugadores_reporte(self):
        jugadores_ordenados = []
        for jugador in lista_jugadores:
            jugadores_ordenados += [jugador]

        cantidad = contar(jugadores_ordenados)
        i = 0
        while i < cantidad - 1:
            j = i + 1
            while j < cantidad:
                if self.jugador_va_antes_reporte(jugadores_ordenados[j], jugadores_ordenados[i]):
                    jugadores_ordenados[i], jugadores_ordenados[j] = jugadores_ordenados[j], jugadores_ordenados[i]
                j += 1
            i += 1

        return jugadores_ordenados

    def guardar_ranking_goleadores(self):
        archivo = open("ranking_goleadores.txt", "w", encoding="utf-8")
        primera = True
        for jugador in self.ordenar_jugadores_reporte():
            linea = jugador.nombre + " " + jugador.apellido + ";" + jugador.seleccion + ";" + numero_a_texto(jugador.goles) + ";" + numero_a_texto(jugador.asistencias) + ";" + numero_a_texto(jugador.puntaje_individual)
            if primera:
                archivo.write(linea)
                primera = False
            else:
                archivo.write("\n" + linea)
        archivo.close()

    def texto_ganador_partido(self, partido):
        if partido.fase[0:5] == "Grupo" and partido.goles_equipo1 == partido.goles_equipo2:
            return "Empate"

        if partido.goles_equipo1 > partido.goles_equipo2:
            return partido.equipo_1.pais.nombre
        elif partido.goles_equipo2 > partido.goles_equipo1:
            return partido.equipo_2.pais.nombre
        elif partido.penales_equipo1 > partido.penales_equipo2:
            return partido.equipo_1.pais.nombre
        elif partido.penales_equipo2 > partido.penales_equipo1:
            return partido.equipo_2.pais.nombre

        return "Empate"

    """
    Nombre: guardar_partidos
    Descripción: Guarda en archivo los partidos que ya se jugaron
    Entrada: Partidos de grupos y fases eliminatorias
    Salida: Archivo partidos.txt actualizado
    Restricción: Deben existir partidos creados
    """
    def guardar_partidos(self):
        archivo = open("partidos.txt", "w", encoding="utf-8")
        primera = True
        numero_partido = 1
        for partido in self.partidos_jugados:
            ganador = self.texto_ganador_partido(partido)
            linea = numero_a_texto(numero_partido) + ";" + partido.fase + ";" + partido.equipo_1.pais.nombre + ";" + partido.equipo_2.pais.nombre + ";" + numero_a_texto(partido.goles_equipo1) + ";" + numero_a_texto(partido.goles_equipo2) + ";" + numero_a_texto(partido.penales_equipo1) + ";" + numero_a_texto(partido.penales_equipo2) + ";" + ganador
            numero_partido += 1
            if primera:
                archivo.write(linea)
                primera = False
            else:
                archivo.write("\n" + linea)
        archivo.close()

# Lee un archivo y lo crea si todavía no existe
"""
Nombre: leer_archivo
Descripción: Abre un archivo de texto y lo crea si todavía no existe
Entrada: Nombre del archivo que se quiere leer
Salida: Lista con las líneas del archivo
Restricción: El archivo se busca en la carpeta del programa
"""
def leer_archivo(nombre):
    try:
        archivo = open(nombre, "r", encoding="utf-8")
        contenido = archivo.readlines()
        archivo.close()
        return contenido
    except UnicodeDecodeError:
        archivo = open(nombre, "r", encoding="cp1252")
        contenido = archivo.readlines()
        archivo.close()
        return contenido
    except:
        archivo = open(nombre, "w", encoding="utf-8")
        archivo.close()
        return []

contenido_paises = leer_archivo("paises.txt")
contenido_selecciones = leer_archivo("selecciones.txt")
contenido_entrenadores = leer_archivo("entrenadores.txt")
contenido_jugadores = leer_archivo("jugadores.txt")

for linea in contenido_paises:
    if linea.strip() != "":
        datos = linea.strip().split(";")
        if contar(datos) >= 4:
            lista_paises += [Pais(datos[0], datos[1], datos[2], int(datos[3]))]

def ordenar_lista_paises_por_ranking(lista):
    lista_ordenada = []

    for pais in lista:
        lista_ordenada += [pais]

    cantidad = contar(lista_ordenada)
    i = 0

    while i < cantidad - 1:
        j = i + 1

        while j < cantidad:
            if lista_ordenada[j].ranking_fifa < lista_ordenada[i].ranking_fifa:
                temporal = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[j]
                lista_ordenada[j] = temporal

            j = j + 1

        i = i + 1

    return lista_ordenada

def guardar_paises_archivo():
    archivo = open("paises.txt", "w", encoding="utf-8")
    primera_linea = True

    for pais in lista_paises:
        linea = pais.codigo_fifa + ";" + pais.nombre + ";" + pais.continente + ";" + numero_a_texto(pais.ranking_fifa)

        if primera_linea:
            archivo.write(linea)
            primera_linea = False
        else:
            archivo.write("\n" + linea)

    archivo.close()

def normalizar_rankings_paises():
    global lista_paises

    lista_paises = ordenar_lista_paises_por_ranking(lista_paises)
    posicion = 1

    for pais in lista_paises:
        pais.ranking_fifa = posicion
        posicion = posicion + 1

    guardar_paises_archivo()

"""
Nombre: mover_pais_a_ranking
Descripción: Acomoda los rankings cuando un país cambia de posición
Entrada: País seleccionado y nuevo ranking
Salida: Lista de países sin rankings repetidos
Restricción: El nuevo ranking debe estar dentro del rango permitido
"""
def mover_pais_a_ranking(pais_movido, ranking_nuevo):
    global lista_paises

    lista_sin_pais = []

    for pais in lista_paises:
        if pais is not pais_movido:
            lista_sin_pais += [pais]

    lista_sin_pais = ordenar_lista_paises_por_ranking(lista_sin_pais)
    lista_final = []
    posicion = 1
    agregado = False

    for pais in lista_sin_pais:
        if posicion == ranking_nuevo and not agregado:
            lista_final += [pais_movido]
            agregado = True
            posicion = posicion + 1

        lista_final += [pais]
        posicion = posicion + 1

    if not agregado:
        lista_final += [pais_movido]

    lista_paises = lista_final
    posicion = 1

    for pais in lista_paises:
        pais.ranking_fifa = posicion
        posicion = posicion + 1

    guardar_paises_archivo()

    for seleccion in lista_selecciones:
        seleccion.calcular_fuerza_equipo()

    if lista_selecciones != []:
        guardar_selecciones_archivo()

normalizar_rankings_paises()

def cargar_entrenadores_archivo():
    global lista_entrenadores
    for linea in contenido_entrenadores:
        if linea.strip() != "":
            datos = linea.strip().split(";")
            if contar(datos) == 7 or contar(datos) == 8:
                nuevo = Entrenador(datos[0], datos[1], datos[3], datos[2], datos[4], int(datos[5]), datos[6])
                if contar(datos) == 8:
                    nuevo.seleccion = datos[7]
                lista_entrenadores += [nuevo]

def cargar_jugadores_archivo():
    global lista_jugadores
    for linea in contenido_jugadores:
        if linea.strip() != "":
            datos = linea.strip().split(";")
            if contar(datos) == 11 or contar(datos) == 12:
                nuevo = Futbolista(datos[0], datos[1], datos[2], datos[3], int(datos[4]), datos[5], int(datos[6]), int(datos[7]), int(datos[8]), int(datos[9]), int(datos[10]))
                if contar(datos) == 12:
                    nuevo.seleccion = datos[11]
                lista_jugadores += [nuevo]

def buscar_pais_por_nombre(nombre_pais):
    for pais in lista_paises:
        if pais.nombre == nombre_pais:
            return pais
    return None

def buscar_entrenador_asignado(nombre_seleccion):
    for entrenador in lista_entrenadores:
        if entrenador.seleccion == nombre_seleccion:
            return entrenador
    return None

def buscar_entrenador_por_nombre_completo(nombre_completo):
    for entrenador in lista_entrenadores:
        if entrenador.nombre + " " + entrenador.apellido == nombre_completo:
            return entrenador
    return None

def completar_jugadores_seleccion(seleccion):
    seleccion.jugadores = []
    for jugador in lista_jugadores:
        if jugador.seleccion == seleccion.pais.nombre:
            seleccion.agregar_jugador(jugador)

def seleccion_existe(nombre_pais):
    for seleccion in lista_selecciones:
        if seleccion.pais.nombre == nombre_pais:
            return True
    return False

def crear_seleccion_desde_datos(codigo, nombre_pais, nombre_entrenador, fuerza_texto):
    pais = buscar_pais_por_nombre(nombre_pais)
    if pais is None:
        return None
    entrenador = buscar_entrenador_por_nombre_completo(nombre_entrenador)
    if entrenador is None:
        entrenador = buscar_entrenador_asignado(nombre_pais)
    nueva = Seleccion(codigo, pais, entrenador)
    completar_jugadores_seleccion(nueva)
    if fuerza_texto != "":
        nueva.fuerza_equipo = int(fuerza_texto)
    else:
        nueva.calcular_fuerza_equipo()
    return nueva
"""
Nombre: cargar_selecciones_archivo
Descripción: carga las selecciones guardadas en el archivo de texto
Entrada: usa las líneas leídas desde selecciones.txt
Salida: lista de selecciones actualizada con los datos del archivo
Restricción: cada línea debe tener 3 o 4 datos separados por punto y coma
"""

def cargar_selecciones_archivo():
    global lista_selecciones
    for linea in contenido_selecciones:
        if linea.strip() != "":
            datos = linea.strip().split(";")
            if contar(datos) == 3 or contar(datos) == 4:
                fuerza = ""
                if contar(datos) == 4:
                    fuerza = datos[3]
                nueva = crear_seleccion_desde_datos(datos[0], datos[1], datos[2], fuerza)
                if nueva is not None:
                    lista_selecciones += [nueva]



"""
Nombre: preparar_selecciones_desde_asignaciones
Descripción: completa las selecciones usando los países, entrenadores y jugadores ya cargados
Entrada: usa las listas globales de países, entrenadores, jugadores y selecciones
Salida: selecciones creadas o actualizadas con entrenador, jugadores y fuerza de equipo
Restricción: cada país debe tener un entrenador asignado para poder crear su selección
"""

def preparar_selecciones_desde_asignaciones():
    global lista_selecciones
    for pais in lista_paises:
        if not seleccion_existe(pais.nombre):
            entrenador = buscar_entrenador_asignado(pais.nombre)
            if entrenador is not None:
                nueva = Seleccion(pais.codigo_fifa, pais, entrenador)
                completar_jugadores_seleccion(nueva)
                nueva.calcular_fuerza_equipo()
                lista_selecciones += [nueva]

    for seleccion in lista_selecciones:
        if seleccion.entrenador is None or seleccion.entrenador == "":
            seleccion.entrenador = buscar_entrenador_asignado(seleccion.pais.nombre)
        completar_jugadores_seleccion(seleccion)
        seleccion.calcular_fuerza_equipo()

"""
Nombre: guardar_selecciones_archivo
Descripción: guarda en selecciones.txt las selecciones que están registradas en el sistema
Entrada: usa la lista global de selecciones
Salida: archivo selecciones.txt actualizado
Restricción: cada selección debe tener país, código de equipo y fuerza calculada
"""
def guardar_selecciones_archivo():
    archivo = open("selecciones.txt", "w", encoding="utf-8")
    primero = True
    for seleccion in lista_selecciones:
        entrenador = ""
        if seleccion.entrenador is not None and seleccion.entrenador != "":
            entrenador = seleccion.entrenador.nombre + " " + seleccion.entrenador.apellido
        linea = seleccion.codigo_equipo + ";" + seleccion.pais.nombre + ";" + entrenador + ";" + numero_a_texto(seleccion.fuerza_equipo)
        if primero:
            archivo.write(linea)
            primero = False
        else:
            archivo.write("\n" + linea)
    archivo.close()


"""
Nombre: guardar_entrenadores_archivo_general
Descripción: guarda en entrenadores.txt todos los entrenadores registrados
Entrada: usa la lista global de entrenadores
Salida: archivo entrenadores.txt actualizado con los datos de cada entrenador
Restricción: cada entrenador debe tener sus datos completos antes de guardar
"""
def guardar_entrenadores_archivo_general():
    archivo = open("entrenadores.txt", "w", encoding="utf-8")
    primero = True
    for entrenador in lista_entrenadores:
        linea = entrenador.nombre + ";" + entrenador.apellido + ";" + entrenador.nacionalidad + ";" + entrenador.fecha_nacimiento + ";" + entrenador.licencia + ";" + numero_a_texto(entrenador.experiencia_anios) + ";" + entrenador.sistema_juego + ";" + entrenador.seleccion
        if primero:
            archivo.write(linea)
            primero = False
        else:
            archivo.write("\n" + linea)
    archivo.close()


"""
Nombre: guardar_jugadores_archivo_general
Descripción: guarda en jugadores.txt todos los jugadores registrados con sus estadísticas
Entrada: usa la lista global de jugadores
Salida: archivo jugadores.txt actualizado con los datos de cada jugador
Restricción: cada jugador debe tener nombre, dorsal, posición, puntaje y selección registrados
"""
def guardar_jugadores_archivo_general():
    archivo = open("jugadores.txt", "w", encoding="utf-8")
    primero = True
    for jugador in lista_jugadores:
        linea = jugador.nombre + ";" + jugador.apellido + ";" + jugador.fecha_nacimiento + ";" + jugador.nacionalidad + ";" + numero_a_texto(jugador.dorsal) + ";" + jugador.posicion + ";" + numero_a_texto(jugador.total_tarjetas_amarillas) + ";" + numero_a_texto(jugador.total_tarjetas_rojas) + ";" + numero_a_texto(jugador.goles) + ";" + numero_a_texto(jugador.asistencias) + ";" + numero_a_texto(jugador.puntaje_individual) + ";" + jugador.seleccion
        if primero:
            archivo.write(linea)
            primero = False
        else:
            archivo.write("\n" + linea)
    archivo.close()

"""
Nombre: crear_mundial_actual
Descripción: Crea el objeto que guarda el estado general del torneo
Entrada: Países y selecciones que ya fueron cargados
Salida: Mundial actual listo para crear grupos
Restricción: Debe existir al menos una lista de selecciones válida
"""
def crear_mundial_actual():
    global mundial_actual
    preparar_selecciones_desde_asignaciones()
    if mundial_actual is None:
        mundial_actual = Mundial("Mundial FIFA 2026", 2026, lista_paises, lista_selecciones, [], [], None)
    else:
        mundial_actual.paises = lista_paises
        mundial_actual.selecciones = lista_selecciones
    return mundial_actual

cargar_entrenadores_archivo()
cargar_jugadores_archivo()
cargar_selecciones_archivo()

#===== Interfas Gráfica =====#

# Ventana inicial del programa
"""
Nombre: Pantalla_Principal
Descripción: Muestra el menú inicial del programa
Entrada: No recibe datos directos del usuario
Salida: Ventana principal con botones para abrir las secciones
Restricción: La imagen de fondo debe estar en la carpeta del proyecto
"""
class Pantalla_Principal(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("1535x930+-7+-0")
        self.title("Ventana Principal")
        self.resizable(False, False)

        self.fondo()
        self.botones()

    def fondo(self):

        imagen_fondo = Image.open("pantalla_principal.JPEG")
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


    def paises_selecciones(self):

        self.withdraw()
        Administrar_Paises_Selecciones(self)

    def entrenadores_jugadores(self):

        self.withdraw()
        Administrar_Entrenadores_Jugadores(self)

    def configurar_mundial(self):

        self.withdraw()
        Configuracion_Mundial(self)

    def jugar_mundial(self):
        self.withdraw()
        Jugar_Mundial(self)

    def estadísticas(self):

        self.withdraw()
        Estadisticas(self)

"""
Nombre: Administrar_Paises_Selecciones
Descripción: Permite trabajar con países y selecciones desde la interfaz
Entrada: Datos escritos o elegidos en los formularios
Salida: Países, selecciones, tablas y archivos actualizados
Restricción: No deben quedar campos obligatorios vacíos
"""
class Administrar_Paises_Selecciones(tk.Toplevel):

    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)

        self.principal = principal
        
        self.geometry("1535x930+-7+-0")
        self.title("Administrar Países y Selecciones")
        self.resizable(False, False)


        self.labels()
        self.frames()


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
                                      text="Total: " + numero_a_texto(contar(lista_paises)) + " paises",
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
            entrenadores += [entrenador.nombre + " " + entrenador.apellido]

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
                                           anchor="w",
                                           command=self.añadir_seleccion)
        self.boton_añadir_seleccion.place(x=940, y=350, width=190, height=40)

        self.boton_guardar_seleccion = tk.Button(self,
                                           text="💾 Guardar Cambios",
                                           font=("Arial", 14),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=azul,
                                           anchor="w",
                                           command=self.actualizar_seleccion,
                                           state="disabled")
        self.boton_guardar_seleccion.place(x=1150, y=350, width=170, height=40)

        self.boton_limpiar_seleccion = tk.Button(self,
                                  text="🧹Limpiar",
                                  font=("Arial", 14),
                                  bd=2,
                                  relief= "groove",
                                  fg=gris,
                                  bg=amarillo,
                                  anchor="w",
                                  command=self.limpiar_campos_seleccion)
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
                                      text="Total: " + numero_a_texto(contar(lista_selecciones)) + " selecciones",
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

        self.tree_frame_selecciones = tk.Frame(self,
                                               bd=1,
                                               relief="flat")
        self.tree_frame_selecciones.place(x=930, y=510, width=530, height=330)

        tree_scroll_selecciones = tk.Scrollbar(self.tree_frame_selecciones)
        tree_scroll_selecciones.pack(side="right", fill="y")

        self.tree_selecciones = ttk.Treeview(self.tree_frame_selecciones,
                                             yscrollcommand=tree_scroll_selecciones.set,
                                             selectmode="extended")
        self.tree_selecciones.pack()

        tree_scroll_selecciones.config(command=self.tree_selecciones.yview)

        self.tree_selecciones["columns"] = ("codigo", "pais", "entrenador", "jugadores", "fuerza")

        self.tree_selecciones.column("#0", width=0, stretch=False)
        self.tree_selecciones.column("codigo", anchor="center", width=70)
        self.tree_selecciones.column("pais", anchor="w", width=140)
        self.tree_selecciones.column("entrenador", anchor="w", width=150)
        self.tree_selecciones.column("jugadores", anchor="center", width=70)
        self.tree_selecciones.column("fuerza", anchor="center", width=70)

        self.tree_selecciones.heading("#0", text="", anchor="w")
        self.tree_selecciones.heading("codigo", text="Código", anchor="center")
        self.tree_selecciones.heading("pais", text="País", anchor="center")
        self.tree_selecciones.heading("entrenador", text="Entrenador", anchor="center")
        self.tree_selecciones.heading("jugadores", text="Jug.", anchor="center")
        self.tree_selecciones.heading("fuerza", text="Fuerza", anchor="center")

        self.cargar_tabla_selecciones()
        self.tree_selecciones.bind("<ButtonRelease-1>", self.seleccion_seleccionada)
        self.codigo_seleccion_original = ""

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
    Nombre: añadir
    Descripción: Registra un país nuevo desde el formulario
    Entrada: Código FIFA, nombre, continente y ranking
    Salida: País agregado a la lista, tabla y archivo
    Restricción: No se permite repetir código, nombre ni ranking
    """
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
        elif not texto_es_nombre(nombre):
            messagebox.showerror("¡Error!", "El nombre del país solo debe contener letras")
            return
        elif not texto_es_codigo(codigo_fifa):
            messagebox.showerror("¡Error!", "El código FIFA solo debe contener letras")
            return
        elif continente == "Seleccione un Continente":
            messagebox.showerror("¡Error!", "Debe seleccionar un continente para el país")
            return 
        elif ranking_fifa == "":
            messagebox.showerror("¡Error!", "Debe ingresar el ranking FIFA del país")
            return 
        elif contar(codigo_fifa) != 3:
            messagebox.showerror("!Error¡", "El códifo FIFA debe contener 3 letras")
            return
        elif not texto_es_entero(ranking_fifa):
            messagebox.showerror("¡Error!", "El ranking FIFA debe ser un número entero")
            return
        elif int(ranking_fifa) < 1 or int(ranking_fifa) > 100:
            messagebox.showerror("¡Error!", "El ranking FIFA debe estar entre 1 y 100")
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
            linea = codigo_fifa + ";" + nombre + ";" + continente + ";" + numero_a_texto(ranking_fifa)
            archivo.write(linea)
            archivo.close()

            nuevo_pais = Pais(codigo_fifa, nombre, continente, ranking_fifa)
            lista_paises += [nuevo_pais]

            numero = contar(lista_paises)

            if numero % 2 == 0:
                self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("evenrow",))
            else:
                self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("oddrow",))

            messagebox.showinfo("Información", "País registrado correctamente")

            self.entry_codigo.delete(0, "end")
            self.entry_nombre.delete(0, "end")
            self.combobox_continente.delete(0, "end")
            self.spinbox_ranking.delete(0, "end")
            
            self.entry_codigo.insert(0, "Ej: CRC")
            self.entry_nombre.insert(0, "Ej: Costa Rica")
            self.combobox_continente.set("Seleccione un Continente")
            return

        archivo = open("paises.txt", "a")
        linea = "\n" + codigo_fifa + ";" + nombre + ";" + continente + ";" + numero_a_texto(ranking_fifa)
        archivo.write(linea)
        archivo.close()

        nuevo_pais = Pais(codigo_fifa, nombre, continente, ranking_fifa)
        lista_paises += [nuevo_pais]

        numero = contar(lista_paises) - 1

        if numero % 2 == 0:
            self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("evenrow",))
        else:
            self.tree_view.insert(parent= "", index="end", iid=numero, text="", values=(codigo_fifa, nombre, continente, ranking_fifa), tags=("oddrow",))

        messagebox.showinfo("Información", "País registrado correctamente")
        
        self.entry_codigo.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.combobox_continente.delete(0, "end")
        self.spinbox_ranking.delete(0, "end")
            
        self.entry_codigo.insert(0, "Ej: CRC")
        self.entry_nombre.insert(0, "Ej: Costa Rica")
        self.combobox_continente.set("Seleccione un Continente")
        
        for pais in lista_paises:
            pais.mostrar_datos()

    def recargar_tabla_paises(self):
        filas = self.tree_view.get_children()

        for fila in filas:
            self.tree_view.delete(fila)

        numero = 0

        for pais in lista_paises:
            if numero % 2 == 0:
                self.tree_view.insert(parent="", index="end", iid=numero, text="", values=(pais.codigo_fifa, pais.nombre, pais.continente, pais.ranking_fifa), tags=("evenrow",))
            else:
                self.tree_view.insert(parent="", index="end", iid=numero, text="", values=(pais.codigo_fifa, pais.nombre, pais.continente, pais.ranking_fifa), tags=("oddrow",))

            numero = numero + 1

    """
    Nombre: actualizar
    Descripción: Cambia los datos de un país seleccionado
    Entrada: Nuevos datos escritos en el formulario
    Salida: País y archivo actualizados
    Restricción: Debe haber un país seleccionado en la tabla
    """
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
        elif not texto_es_nombre(nombre):
            messagebox.showerror("¡Error!", "El nombre del país solo debe contener letras")
            return
        elif not texto_es_codigo(codigo_fifa):
            messagebox.showerror("¡Error!", "El código FIFA solo debe contener letras")
            return
        elif continente == "Seleccione un Continente":
            messagebox.showerror("¡Error!", "Debe seleccionar un continente para el país")
            return 
        elif ranking_fifa == "":
            messagebox.showerror("¡Error!", "Debe ingresar el ranking FIFA del país")
            return 
        elif contar(codigo_fifa) != 3:
            messagebox.showerror("!Error¡", "El códifo FIFA debe contener 3 letras")
            return
        elif not texto_es_entero(ranking_fifa):
            messagebox.showerror("¡Error!", "El ranking FIFA debe ser un número entero")
            return
        elif int(ranking_fifa) < 1 or int(ranking_fifa) > 100:
            messagebox.showerror("¡Error!", "El ranking FIFA debe estar entre 1 y 100")
            return
        
        codigo_fifa = codigo_fifa.upper()
        continente = continente.title()
        nombre = nombre.title()  
        ranking_fifa = int(ranking_fifa)

        pais_actualizado = None

        for pais in lista_paises:
            if pais.codigo_fifa == codigo_fifa:
                pais_actualizado = pais
                break

        if pais_actualizado is None:
            messagebox.showerror("Error", "No se encontró el país seleccionado")
            return

        pais_actualizado.actualizar_datos(codigo_fifa, nombre, continente, ranking_fifa)
        mover_pais_a_ranking(pais_actualizado, ranking_fifa)
        self.recargar_tabla_paises()

        messagebox.showinfo("Información", "País actualizado correctamente. Los rankings se acomodaron automáticamente")
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

    def pais_seleccionado(self, e=""):  

        self.entry_codigo.config(state="normal")
        self.entry_nombre.config(state="normal")  
            
        self.entry_codigo.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.combobox_continente.delete(0, "end")
        self.spinbox_ranking.delete(0, "end")
    
        selected = self.tree_view.focus()
    
        values = self.tree_view.item(selected, "values")
        if not values or contar(values) < 4:
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

    def buscar_pais_seleccion(self, nombre_pais):

        for pais in lista_paises:
            if pais.nombre == nombre_pais:
                return pais

        return None

    def buscar_entrenador_seleccion(self, nombre_entrenador):

        for entrenador in lista_entrenadores:
            if entrenador.nombre + " " + entrenador.apellido == nombre_entrenador:
                return entrenador

        return None

    def cargar_tabla_selecciones(self):

        filas = self.tree_selecciones.get_children()

        for fila in filas:
            self.tree_selecciones.delete(fila)

        for seleccion in lista_selecciones:
            nombre_entrenador = "Sin entrenador"

            if seleccion.entrenador is not None and seleccion.entrenador != "":
                nombre_entrenador = seleccion.entrenador.nombre + " " + seleccion.entrenador.apellido

            completar_jugadores_seleccion(seleccion)
            seleccion.calcular_fuerza_equipo()

            self.tree_selecciones.insert("",
                                         "end",
                                         values=(seleccion.codigo_equipo,
                                                 seleccion.pais.nombre,
                                                 nombre_entrenador,
                                                 contar(seleccion.jugadores),
                                                 seleccion.fuerza_equipo))

    """
    Nombre: añadir_seleccion
    Descripción: Crea una selección con país y entrenador
    Entrada: Código, país y entrenador elegidos
    Salida: Selección agregada a la lista y archivo
    Restricción: El país y el entrenador deben existir
    """
    def añadir_seleccion(self):

        global lista_selecciones

        codigo = self.entry_codigo_seleccion.get().strip()
        pais_texto = self.pais_seleccion.get().strip()
        entrenador_texto = self.entrenador_seleccion.get().strip()

        if codigo == "" or codigo == "Ej: CRC":
            messagebox.showerror("Error", "Ingrese el código de la selección")
            return

        elif contar(codigo) != 3:
            messagebox.showerror("Error", "El código de la selección debe tener 3 letras")
            return

        elif not texto_es_codigo(codigo):
            messagebox.showerror("Error", "El código de la selección solo debe contener letras")
            return

        elif pais_texto == "" or pais_texto == "Seleccione un pais":
            messagebox.showerror("Error", "Seleccione el país de la selección")
            return

        elif entrenador_texto == "" or entrenador_texto == "Seleccione un entrenador":
            messagebox.showerror("Error", "Seleccione un entrenador")
            return

        codigo = codigo.upper()
        pais = self.buscar_pais_seleccion(pais_texto)
        entrenador = self.buscar_entrenador_seleccion(entrenador_texto)

        if pais is None:
            messagebox.showerror("Error", "No se encontró el país")
            return

        if entrenador is None:
            messagebox.showerror("Error", "No se encontró el entrenador")
            return

        for seleccion in lista_selecciones:
            if seleccion.codigo_equipo == codigo:
                messagebox.showerror("Error", "Ese código ya está registrado")
                return

            elif seleccion.pais.nombre == pais.nombre:
                messagebox.showerror("Error", "Ese país ya tiene selección")
                return

        nueva_seleccion = Seleccion(codigo, pais, entrenador)
        entrenador.seleccion = pais.nombre
        completar_jugadores_seleccion(nueva_seleccion)
        nueva_seleccion.calcular_fuerza_equipo()

        lista_selecciones += [nueva_seleccion]

        guardar_selecciones_archivo()
        guardar_entrenadores_archivo_general()
        self.cargar_tabla_selecciones()
        self.limpiar_campos_seleccion()

        messagebox.showinfo("Correcto", "Selección registrada correctamente")

    def limpiar_campos_seleccion(self):

        self.entry_codigo_seleccion.config(state="normal")
        self.entry_codigo_seleccion.delete(0, "end")
        self.entry_codigo_seleccion.insert(0, "Ej: CRC")
        self.combobox_pais.set("Seleccione un pais")
        self.combobox_entrenador.set("Seleccione un entrenador")
        self.boton_guardar_seleccion.config(state="disabled")
        self.boton_añadir_seleccion.config(state="normal")
        self.codigo_seleccion_original = ""

    def seleccion_seleccionada(self, e=""):
        selected = self.tree_selecciones.focus()
        values = self.tree_selecciones.item(selected, "values")

        if not values or contar(values) < 3:
            return

        self.codigo_seleccion_original = values[0]
        self.entry_codigo_seleccion.config(state="normal")
        self.entry_codigo_seleccion.delete(0, "end")
        self.entry_codigo_seleccion.insert(0, values[0])
        self.combobox_pais.set(values[1])
        self.combobox_entrenador.set(values[2])
        self.boton_guardar_seleccion.config(state="active")
        self.boton_añadir_seleccion.config(state="disabled")

    def actualizar_seleccion(self):
        global lista_selecciones

        if self.codigo_seleccion_original == "":
            messagebox.showerror("Error", "Seleccione una selección de la tabla")
            return

        codigo = self.entry_codigo_seleccion.get().strip()
        pais_texto = self.pais_seleccion.get().strip()
        entrenador_texto = self.entrenador_seleccion.get().strip()

        if codigo == "" or codigo == "Ej: CRC":
            messagebox.showerror("Error", "Ingrese el código de la selección")
            return
        elif contar(codigo) != 3:
            messagebox.showerror("Error", "El código de la selección debe tener 3 letras")
            return
        elif not texto_es_codigo(codigo):
            messagebox.showerror("Error", "El código de la selección solo debe contener letras")
            return
        elif pais_texto == "" or pais_texto == "Seleccione un pais":
            messagebox.showerror("Error", "Seleccione el país de la selección")
            return
        elif entrenador_texto == "" or entrenador_texto == "Seleccione un entrenador" or entrenador_texto == "Sin entrenador":
            messagebox.showerror("Error", "Seleccione un entrenador")
            return

        codigo = codigo.upper()
        pais = self.buscar_pais_seleccion(pais_texto)
        entrenador = self.buscar_entrenador_seleccion(entrenador_texto)

        if pais is None:
            messagebox.showerror("Error", "No se encontró el país")
            return
        if entrenador is None:
            messagebox.showerror("Error", "No se encontró el entrenador")
            return

        seleccion_actual = None
        for seleccion in lista_selecciones:
            if seleccion.codigo_equipo == self.codigo_seleccion_original:
                seleccion_actual = seleccion

        if seleccion_actual is None:
            messagebox.showerror("Error", "No se encontró la selección seleccionada")
            return

        for seleccion in lista_selecciones:
            if seleccion is not seleccion_actual and seleccion.codigo_equipo == codigo:
                messagebox.showerror("Error", "Ese código ya está registrado")
                return
            elif seleccion is not seleccion_actual and seleccion.pais.nombre == pais.nombre:
                messagebox.showerror("Error", "Ese país ya tiene selección")
                return

        if seleccion_actual.entrenador is not None and seleccion_actual.entrenador != "":
            if seleccion_actual.entrenador.seleccion == seleccion_actual.pais.nombre:
                seleccion_actual.entrenador.seleccion = ""

        seleccion_actual.codigo_equipo = codigo
        seleccion_actual.pais = pais
        seleccion_actual.entrenador = entrenador
        entrenador.seleccion = pais.nombre
        completar_jugadores_seleccion(seleccion_actual)
        seleccion_actual.calcular_fuerza_equipo()

        guardar_selecciones_archivo()
        guardar_entrenadores_archivo_general()
        self.cargar_tabla_selecciones()
        self.limpiar_campos_seleccion()
        messagebox.showinfo("Correcto", "Selección actualizada correctamente")

"""
Nombre: Administrar_Entrenadores_Jugadores
Descripción: Permite registrar, editar, asignar y eliminar entrenadores y jugadores
Entrada: Datos escritos en los formularios y opciones elegidas en combobox
Salida: Listas y archivos de entrenadores y jugadores actualizados
Restricción: Los nombres, dorsales y selecciones deben ser válidos
"""
class Administrar_Entrenadores_Jugadores(tk.Toplevel):

    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)
        self.principal = principal
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

        self.entry_nombre_entrenador.bind("<FocusIn>", self.borrar_nombre_entrenador)
        self.entry_nombre_entrenador.bind("<FocusOut>", self.restaurar_nombre_entrenador)

        self.entry_apellidos_entrenador = tk.Entry(self,
                                fg=gris,
                                insertwidth=1,
                                bd=1,
                                highlightcolor=azul,
                                highlightthickness=1)
        self.entry_apellidos_entrenador.insert(0, "Ej: Ancelotti")
        self.entry_apellidos_entrenador.place(x=145, y=160, width=155, height=30)    

        self.entry_apellidos_entrenador.bind("<FocusIn>", self.borrar_apellidos_entrenador)
        self.entry_apellidos_entrenador.bind("<FocusOut>", self.restaurar_apellidos_entrenador)                                          

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
                                           anchor="w",
                                           command=self.actualizar_entrenador)
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
            entrenadores += [entrenador.nombre + " " + entrenador.apellido]

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
                                           anchor="w",
                                           command=self.asignar_entrenador_a_seleccion)
        self.boton_asignar_entrenador_seleccion.place(x=620, y=350, width=290, height=40)

#Frame arriba derecha

        self.frame_entrenadores = tk.Frame(self,
                                           bd=1,
                                           relief="solid")
        self.frame_entrenadores.place(x=950, y=20, width=560, height=400)
        self.crear_tabla_entrenadores_registrados()

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

        self.entry_nombre_jugador.bind("<FocusIn>", self.borrar_nombre_jugador)
        self.entry_nombre_jugador.bind("<FocusOut>", self.restaurar_nombre_jugador)

        self.entry_apellidos_jugador = tk.Entry(self,
                                fg=gris,
                                insertwidth=1,
                                bd=1,
                                highlightcolor=azul,
                                highlightthickness=1)
        self.entry_apellidos_jugador.insert(0, "Ej: Messi")
        self.entry_apellidos_jugador.place(x=145, y=580, width=155, height=30)

        self.entry_apellidos_jugador.bind("<FocusIn>", self.borrar_apellidos_jugador)
        self.entry_apellidos_jugador.bind("<FocusOut>", self.restaurar_apellidos_jugador)

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
                                           anchor="w",
                                           command=self.actualizar_jugador)
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
                                          text="👤 Asignar Jugador a Selección",
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
            jugadores += [jugador.nombre + " " + jugador.apellido]

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
                                           anchor="w",
                                           command=self.asignar_jugador_a_seleccion)
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

        self.obtener_seleccion_para_ver_jugadores = tk.StringVar()

        self.combobox_selecciones = ttk.Combobox(self,
                                               values=paises,
                                               state="readonly",
                                               textvariable=self.obtener_seleccion_para_ver_jugadores)
        self.combobox_selecciones.set("Seleccione Selección")
        self.combobox_selecciones.place(x=710, y=690, width=150, height=30)

        self.boton_ver_jugadoress = tk.Button(self,
                                           text="Ver Jugadores",
                                           font=("Arial", 13),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=verde,
                                           anchor="center",
                                           command=self.ver_jugadores_por_seleccion)
        self.boton_ver_jugadoress.place(x=655, y=760, width=270, height=40)


        self.frame_jugadores = tk.Frame(self,
                                        bd=1,
                                        relief="solid")
        self.frame_jugadores.place(x=950, y=430, width=560, height=400)

        self.crear_tabla_jugadores_registrados()

        self.boton_volver = tk.Button(self,
                                      text="Regresar al menú principal",
                                      font=("Arial", 15, "bold"),
                                      fg=blanco,
                                      bg=gris_claro,
                                      activeforeground=negro,
                                      activebackground=gris,
                                      relief="flat",
                                      bd=5,
                                      cursor="hand2",
                                      command=self.volver)
        self.boton_volver.place(x=1160, y=850, width=330, height=45)

    def buscar_entrenador_por_nombre(self, nombre_completo):

        for entrenador in lista_entrenadores:
            if entrenador.nombre + " " + entrenador.apellido == nombre_completo:
                return entrenador

        return None

    def asignar_entrenador_a_seleccion(self):

        seleccion = self.obtener_entrenador_para_seleccion.get().strip()
        entrenador_texto = self.obtener_seleccion_para_entrenador.get().strip()

        if seleccion == "" or seleccion == "Seleccione Selección":
            messagebox.showerror("Error", "Seleccione una selección")
            return

        elif entrenador_texto == "" or entrenador_texto == "Seleccione Entrenador":
            messagebox.showerror("Error", "Seleccione un entrenador")
            return

        entrenador = self.buscar_entrenador_por_nombre(entrenador_texto)

        if entrenador is None:
            messagebox.showerror("Error", "No se encontró el entrenador")
            return

        entrenador.seleccion = seleccion

        self.guardar_entrenadores_archivo()
        self.cargar_tabla_entrenadores()

        messagebox.showinfo("Correcto", "Entrenador asignado correctamente")

    def limpiar_entrenador(self):

        self.entry_nombre_entrenador.delete(0, "end")
        self.entry_apellidos_entrenador.delete(0, "end")
        self.spinbox_experiencia.delete(0, "end")

        self.entry_nombre_entrenador.insert(0, "Ej: Carlo")
        self.entry_apellidos_entrenador.insert(0, "Ej: Ancelotti")
        self.combobox_nacionalidad_entrenador.set("Seleccione Nacionalidad")
        self.combobox_dias.set("Día")
        self.combobox_meses.set("Mes")
        self.combobox_año.set("Año")
        self.combobox_licencia.set("Seleccione Licencia")
        self.combobox_sistema_juego.set("Seleccione Sistema")

    def crear_tabla_entrenadores_registrados(self):

        label_entrenadores_registrados = tk.Label(self,
                                                  text="Entrenadores Registrados",
                                                  font=("Arial", 12, "bold"),
                                                  fg=azul,
                                                  anchor="w")
        label_entrenadores_registrados.place(x=970, y=30, width=300, height=30)

        self.tree_entrenadores = ttk.Treeview(self,
                                              columns=("nombre", "nacionalidad", "licencia", "experiencia", "sistema", "seleccion"),
                                              show="headings")

        self.tree_entrenadores.heading("nombre", text="Entrenador")
        self.tree_entrenadores.heading("nacionalidad", text="Nacionalidad")
        self.tree_entrenadores.heading("licencia", text="Licencia")
        self.tree_entrenadores.heading("experiencia", text="Años")
        self.tree_entrenadores.heading("sistema", text="Sistema")
        self.tree_entrenadores.heading("seleccion", text="Selección")

        self.tree_entrenadores.column("nombre", width=100, anchor="w")
        self.tree_entrenadores.column("nacionalidad", width=90, anchor="center")
        self.tree_entrenadores.column("licencia", width=75, anchor="center")
        self.tree_entrenadores.column("experiencia", width=45, anchor="center")
        self.tree_entrenadores.column("sistema", width=80, anchor="center")
        self.tree_entrenadores.column("seleccion", width=100, anchor="center")

        self.tree_entrenadores.place(x=970, y=70, width=515, height=270)

        self.boton_eliminar_entrenador = tk.Button(self,
                                                   text="Eliminar Entrenador",
                                                   font=("Arial", 12, "bold"),
                                                   bg=rojo,
                                                   fg=blanco,
                                                   bd=2,
                                                   relief="raised",
                                                   command=self.eliminar_entrenador)
        self.boton_eliminar_entrenador.place(x=1130, y=355, width=190, height=35)

        self.boton_volver_entrenadores = tk.Button(self,
                                                   text="Volver",
                                                   font=("Arial", 12, "bold"),
                                                   bg=gris_claro,
                                                   fg=negro,
                                                   bd=2,
                                                   relief="raised",
                                                   command=self.volver)
        self.boton_volver_entrenadores.place(x=1340, y=355, width=145, height=35)

        self.cargar_tabla_entrenadores()

    def cargar_tabla_entrenadores(self):

        filas = self.tree_entrenadores.get_children()

        for fila in filas:
            self.tree_entrenadores.delete(fila)

        for entrenador in lista_entrenadores:
            nombre_completo = entrenador.nombre + " " + entrenador.apellido

            self.tree_entrenadores.insert("",
                                          "end",
                                          values=(nombre_completo,
                                                  entrenador.nacionalidad,
                                                  entrenador.licencia,
                                                  entrenador.experiencia_anios,
                                                  entrenador.sistema_juego,
                                                  entrenador.seleccion))

    def actualizar_combobox_entrenadores(self):

        entrenadores = []

        for entrenador in lista_entrenadores:
            entrenadores += [entrenador.nombre + " " + entrenador.apellido]

        self.seleccion_entrenador_seleccion.config(values=entrenadores)

    def guardar_entrenadores_archivo(self):

        archivo = open("entrenadores.txt", "w", encoding="utf-8")

        primero = True

        for entrenador in lista_entrenadores:
            linea = entrenador.nombre + ";" + entrenador.apellido + ";" + entrenador.nacionalidad + ";" + entrenador.fecha_nacimiento + ";" + entrenador.licencia + ";" + numero_a_texto(entrenador.experiencia_anios) + ";" + entrenador.sistema_juego + ";" + entrenador.seleccion

            if primero == True:
                archivo.write(linea)
                primero = False
            else:
                archivo.write("\n" + linea)

        archivo.close()

    def eliminar_entrenador(self):

        global lista_entrenadores

        seleccionado = self.tree_entrenadores.focus()

        if seleccionado == "":
            messagebox.showerror("Error", "Seleccione un entrenador de la tabla")
            return

        valores = self.tree_entrenadores.item(seleccionado, "values")

        nombre_completo_tabla = valores[0]
        nacionalidad_tabla = valores[1]
        licencia_tabla = valores[2]
        experiencia_tabla = valores[3]
        sistema_tabla = valores[4]

        nueva_lista = []
        eliminado = False

        for entrenador in lista_entrenadores:
            nombre_completo = entrenador.nombre + " " + entrenador.apellido

            if eliminado == False and nombre_completo == nombre_completo_tabla and entrenador.nacionalidad == nacionalidad_tabla and entrenador.licencia == licencia_tabla and numero_a_texto(entrenador.experiencia_anios) == experiencia_tabla and entrenador.sistema_juego == sistema_tabla:
                eliminado = True
            else:
                nueva_lista += [entrenador]

        lista_entrenadores = nueva_lista

        self.guardar_entrenadores_archivo()
        self.cargar_tabla_entrenadores()
        self.actualizar_combobox_entrenadores()

        messagebox.showinfo("Correcto", "Entrenador eliminado correctamente")

    """
    Nombre: agregar_entrenador
    Descripción: Registra un entrenador con sus datos personales y deportivos
    Entrada: Nombre, apellido, nacionalidad, fecha, licencia, experiencia y sistema
    Salida: Entrenador agregado a la lista y archivo
    Restricción: Los campos obligatorios deben estar completos
    """
    def agregar_entrenador(self):

        global lista_entrenadores
        
        nombre = self.entry_nombre_entrenador.get().strip()
        apellido = self.entry_apellidos_entrenador.get().strip()
        nacionalidad = self.seleccion_nacionalidad_entrenador.get().strip()
        dia = self.dia_seleccionado.get().strip()
        mes = self.mes_seleccionado.get().strip()
        año = self.año_seleccionado.get().strip()
        licencia = self.seleccion_licencia.get().strip()
        experiencia_texto = self.spinbox_experiencia.get().strip()
        sistema_juego = self.seleccion_sistema_juego.get().strip()

        if nombre == "" or nombre == "Ej: Carlo":
            messagebox.showerror("¡Error!", "Ingrese el nombre del entrenador")
            return
        elif apellido == "" or apellido == "Ej: Ancelotti":
            messagebox.showerror("¡Error!", "Ingrese el apellido del entrenador")
            return 
        elif not texto_es_nombre(nombre):
            messagebox.showerror("¡Error!", "El nombre del entrenador solo debe contener letras")
            return
        elif not texto_es_nombre(apellido):
            messagebox.showerror("¡Error!", "El apellido del entrenador solo debe contener letras")
            return
        elif nacionalidad == "" or nacionalidad == "Seleccione Nacionalidad":
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
        elif experiencia_texto == "":
            messagebox.showerror("¡Error!", "Ingrese los años de experiencia del entrenador")
            return 
        elif sistema_juego == "Seleccione Sistema":
            messagebox.showerror("¡Error!", "Seleccione el sistema de juego del entrenador")
            return
        elif not texto_es_entero(experiencia_texto):
            messagebox.showerror("¡Error!", "La experiencia debe ser un número entero")
            return
        elif int(experiencia_texto) < 1 or int(experiencia_texto) > 50:
            messagebox.showerror("¡Error!", "La experiencia debe estar entre 1 y 50 años")
            return
        
        nombre = nombre.title()
        apellido = apellido.title()
        nacionalidad = nacionalidad.title()
        experiencia = int(experiencia_texto)

        fecha = dia + "/" + mes + "/" + año

        if not 1 <= experiencia <= 50:
            messagebox.showerror("¡Error!", "La experiencia debe estar entre 1 y 50 años")
            return 

        for entrenador in lista_entrenadores:
            if entrenador.nombre == nombre and entrenador.apellido == apellido and entrenador.nacionalidad == nacionalidad:
                messagebox.showerror("¡Error!", "Ese entrenador ya está registrado")
                return

        nuevo_entrenador = Entrenador(nombre,
                                      apellido,
                                      fecha,
                                      nacionalidad,
                                      licencia,
                                      experiencia,
                                      sistema_juego)
        lista_entrenadores += [nuevo_entrenador]

        self.guardar_entrenadores_archivo()
        self.cargar_tabla_entrenadores()
        self.actualizar_combobox_entrenadores()
        self.limpiar_entrenador()

        messagebox.showinfo("Correcto", "Entrenador registrado correctamente")


    """
    Nombre: actualizar_entrenador
    Descripción: modifica los datos de un entrenador seleccionado en la tabla
    Entrada: datos escritos o seleccionados en el formulario de entrenador
    Salida: entrenador actualizado en la lista, tabla y archivo de texto
    Restricción: se debe seleccionar un entrenador y los datos no pueden estar vacíos ni ser inválidos
    """

    def actualizar_entrenador(self):
        seleccionado = self.tree_entrenadores.focus()

        if seleccionado == "":
            messagebox.showerror("Error", "Seleccione un entrenador de la tabla")
            return

        valores = self.tree_entrenadores.item(seleccionado, "values")
        nombre_anterior = valores[0]
        entrenador_actual = ""

        for entrenador in lista_entrenadores:
            if entrenador.nombre + " " + entrenador.apellido == nombre_anterior:
                entrenador_actual = entrenador

        if entrenador_actual == "":
            messagebox.showerror("Error", "No se encontró el entrenador seleccionado")
            return

        nombre = self.entry_nombre_entrenador.get().strip()
        apellido = self.entry_apellidos_entrenador.get().strip()
        nacionalidad = self.seleccion_nacionalidad_entrenador.get().strip()
        dia = self.dia_seleccionado.get().strip()
        mes = self.mes_seleccionado.get().strip()
        año = self.año_seleccionado.get().strip()
        licencia = self.seleccion_licencia.get().strip()
        experiencia_texto = self.spinbox_experiencia.get().strip()
        sistema_juego = self.seleccion_sistema_juego.get().strip()

        if nombre == "" or nombre == "Ej: Carlo":
            messagebox.showerror("Error", "Ingrese el nombre del entrenador")
            return
        elif apellido == "" or apellido == "Ej: Ancelotti":
            messagebox.showerror("Error", "Ingrese el apellido del entrenador")
            return
        elif not texto_es_nombre(nombre):
            messagebox.showerror("Error", "El nombre del entrenador solo debe contener letras")
            return
        elif not texto_es_nombre(apellido):
            messagebox.showerror("Error", "El apellido del entrenador solo debe contener letras")
            return
        elif nacionalidad == "" or nacionalidad == "Seleccione Nacionalidad":
            messagebox.showerror("Error", "Seleccione la nacionalidad del entrenador")
            return
        elif dia == "Día" or mes == "Mes" or año == "Año":
            messagebox.showerror("Error", "Seleccione la fecha completa")
            return
        elif licencia == "Seleccione Licencia" or sistema_juego == "Seleccione Sistema":
            messagebox.showerror("Error", "Complete licencia y sistema de juego")
            return
        elif not texto_es_entero(experiencia_texto):
            messagebox.showerror("Error", "La experiencia debe ser un número entero")
            return
        elif int(experiencia_texto) < 1 or int(experiencia_texto) > 50:
            messagebox.showerror("Error", "La experiencia debe estar entre 1 y 50")
            return

        fecha = dia + "/" + mes + "/" + año
        entrenador_actual.actualizar_datos(nombre.title(), apellido.title(), fecha, nacionalidad.title(), licencia, int(experiencia_texto), sistema_juego)

        self.guardar_entrenadores_archivo()
        self.cargar_tabla_entrenadores()
        self.actualizar_combobox_entrenadores()
        self.limpiar_entrenador()
        messagebox.showinfo("Correcto", "Entrenador actualizado correctamente")

    def crear_tabla_jugadores_registrados(self):

        label_jugadores_registrados = tk.Label(self,
                                               text="Jugadores Registrados",
                                               font=("Arial", 12, "bold"),
                                               fg=azul,
                                               anchor="w")
        label_jugadores_registrados.place(x=970, y=440, width=300, height=30)

        self.tree_jugadores = ttk.Treeview(self,
                                           columns=("nombre", "nacionalidad", "dorsal", "posicion", "puntaje", "seleccion"),
                                           show="headings")

        self.tree_jugadores.heading("nombre", text="Jugador")
        self.tree_jugadores.heading("nacionalidad", text="Nacionalidad")
        self.tree_jugadores.heading("dorsal", text="Dorsal")
        self.tree_jugadores.heading("posicion", text="Posición")
        self.tree_jugadores.heading("puntaje", text="Puntaje")
        self.tree_jugadores.heading("seleccion", text="Selección")

        self.tree_jugadores.column("nombre", width=115, anchor="w")
        self.tree_jugadores.column("nacionalidad", width=90, anchor="center")
        self.tree_jugadores.column("dorsal", width=50, anchor="center")
        self.tree_jugadores.column("posicion", width=105, anchor="center")
        self.tree_jugadores.column("puntaje", width=60, anchor="center")
        self.tree_jugadores.column("seleccion", width=85, anchor="center")

        self.tree_jugadores.place(x=970, y=480, width=515, height=270)

        boton_eliminar_jugador = tk.Button(self,
                                           text="Eliminar Jugador",
                                           font=("Arial", 12, "bold"),
                                           bd=1,
                                           relief="groove",
                                           fg=blanco,
                                           bg=rojo,
                                           anchor="center",
                                           command=self.eliminar_jugador_registrado)
        boton_eliminar_jugador.place(x=1135, y=760, width=190, height=35)

        self.boton_volver_jugadores = tk.Button(self,
                                                text="Volver",
                                                font=("Arial", 12, "bold"),
                                                bd=2,
                                                relief="raised",
                                                fg=negro,
                                                bg=gris_claro,
                                                command=self.volver)
        self.boton_volver_jugadores.place(x=1340, y=760, width=145, height=35)

        self.cargar_tabla_jugadores()

    def cargar_tabla_jugadores(self):

        filas = self.tree_jugadores.get_children()

        for fila in filas:
            self.tree_jugadores.delete(fila)

        for jugador in lista_jugadores:
            nombre_completo = jugador.nombre + " " + jugador.apellido

            seleccion = jugador.seleccion
            if seleccion == "":
                seleccion = "Sin asignar"

            self.tree_jugadores.insert("",
                                       "end",
                                       values=(nombre_completo,
                                               jugador.nacionalidad,
                                               jugador.dorsal,
                                               jugador.posicion,
                                               jugador.puntaje_individual,
                                               seleccion))

    def actualizar_combobox_jugadores(self):

        jugadores = []

        for jugador in lista_jugadores:
            jugadores += [jugador.nombre + " " + jugador.apellido]

        self.combobox_jugadores.config(values=jugadores)



    """
    Nombre: ver_jugadores_por_seleccion
    Descripción: Filtra la tabla grande para ver los jugadores de una selección
    Entrada: Selección escogida en el combobox
    Salida: Tabla de jugadores mostrando solo esa selección
    Restricción: La selección debe existir en los datos cargados
    """
    def ver_jugadores_por_seleccion(self):

        seleccion = self.obtener_seleccion_para_ver_jugadores.get().strip()

        if seleccion == "" or seleccion == "Seleccione Selección":
            messagebox.showerror("Error", "Seleccione una selección")
            return

        filas = self.tree_jugadores.get_children()

        for fila in filas:
            self.tree_jugadores.delete(fila)

        cantidad = 0

        for jugador in lista_jugadores:
            if jugador.seleccion == seleccion:
                nombre_completo = jugador.nombre + " " + jugador.apellido

                self.tree_jugadores.insert("",
                                           "end",
                                           values=(nombre_completo,
                                                   jugador.nacionalidad,
                                                   jugador.dorsal,
                                                   jugador.posicion,
                                                   jugador.puntaje_individual,
                                                   jugador.seleccion))

                cantidad = cantidad + 1

        if cantidad == 0:
            messagebox.showinfo("Información", "Esa selección no tiene jugadores asignados")


    def buscar_jugador_por_nombre(self, nombre_completo):

        for jugador in lista_jugadores:
            if jugador.nombre + " " + jugador.apellido == nombre_completo:
                return jugador

        return ""

    """
    Nombre: asignar_jugador_a_seleccion
    Descripción: Relaciona un jugador con una selección
    Entrada: Jugador y selección escogidos en los combobox
    Salida: Jugador asignado y archivo actualizado
    Restricción: No se debe repetir dorsal ni pasar el máximo de jugadores
    """
    def asignar_jugador_a_seleccion(self):

        jugador_texto = self.obtener_jugador.get().strip()
        seleccion = self.obtener_pais_de_jugador.get().strip()

        if jugador_texto == "" or jugador_texto == "Seleccione Jugador":
            messagebox.showerror("Error", "Seleccione un jugador")
            return

        elif seleccion == "" or seleccion == "Seleccione Selección":
            messagebox.showerror("Error", "Seleccione una selección")
            return

        jugador = self.buscar_jugador_por_nombre(jugador_texto)

        if jugador == "":
            messagebox.showerror("Error", "No se encontró el jugador")
            return

        cantidad_asignados = 0
        for jugador_lista in lista_jugadores:
            if jugador_lista.seleccion == seleccion:
                cantidad_asignados += 1
                if jugador_lista.dorsal == jugador.dorsal and jugador_lista != jugador:
                    messagebox.showerror("Error", "Ya existe un jugador con ese dorsal en la selección")
                    return

        if cantidad_asignados >= 23 and jugador.seleccion != seleccion:
            messagebox.showerror("Error", "La selección ya tiene 23 jugadores")
            return

        jugador.seleccion = seleccion

        self.guardar_jugadores_archivo()
        self.cargar_tabla_jugadores()
        self.combobox_selecciones.set(seleccion)
        self.ver_jugadores_por_seleccion()

        messagebox.showinfo("Correcto", "Jugador asignado correctamente")

    """
    Nombre: añadir_jugador
    Descripción: Registra un jugador desde el formulario de la ventana
    Entrada: Datos personales, dorsal, posición y puntajes
    Salida: Jugador agregado a la lista y archivo
    Restricción: El nombre, dorsal y puntajes deben ser válidos
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
        elif not texto_es_nombre(nombre):
            messagebox.showerror("Error", "El nombre del jugador solo debe contener letras")
            return
        elif not texto_es_nombre(apellido):
            messagebox.showerror("Error", "El apellido del jugador solo debe contener letras")
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
        elif not texto_es_entero(dorsal_texto):
            messagebox.showerror("Error", "El dorsal debe ser un número entero")
            return
        elif not texto_es_entero(velocidad_texto):
            messagebox.showerror("Error", "La velocidad debe ser un número entero")
            return
        elif not texto_es_entero(estratega_texto):
            messagebox.showerror("Error", "Estratega debe ser un número entero")
            return
        elif not texto_es_entero(dominio_texto):
            messagebox.showerror("Error", "Dominio del balón debe ser un número entero")
            return
        elif not texto_es_entero(fuerza_texto):
            messagebox.showerror("Error", "La fuerza debe ser un número entero")
            return
        elif int(dorsal_texto) < 1 or int(dorsal_texto) > 99:
            messagebox.showerror("Error", "El dorsal debe estar entre 1 y 99")
            return
        elif int(velocidad_texto) < 1 or int(velocidad_texto) > 25 or int(estratega_texto) < 1 or int(estratega_texto) > 25 or int(dominio_texto) < 1 or int(dominio_texto) > 25 or int(fuerza_texto) < 1 or int(fuerza_texto) > 25:
            messagebox.showerror("Error", "Velocidad, estratega, dominio y fuerza deben estar entre 1 y 25")
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
        nuevo_jugador.seleccion = ""

        lista_jugadores += [nuevo_jugador]

        self.guardar_jugadores_archivo()
        self.cargar_tabla_jugadores()
        self.actualizar_combobox_jugadores()
        self.limpiar_jugador()

        messagebox.showinfo("Correcto", "Jugador registrado correctamente")


    """
    Nombre: actualizar_jugador
    Descripción: modifica los datos de un jugador seleccionado en la tabla
    Entrada: datos escritos o seleccionados en el formulario de jugador
    Salida: jugador actualizado en la lista, tabla y archivo de texto
    Restricción: se debe seleccionar un jugador y los datos deben ser válidos
    """

    def actualizar_jugador(self):
        seleccionado = self.tree_jugadores.focus()

        if seleccionado == "":
            messagebox.showerror("Error", "Seleccione un jugador de la tabla")
            return

        valores = self.tree_jugadores.item(seleccionado, "values")
        nombre_anterior = valores[0]
        nacionalidad_anterior = valores[1]
        dorsal_anterior = valores[2]
        jugador_actual = ""

        for jugador in lista_jugadores:
            if jugador.nombre + " " + jugador.apellido == nombre_anterior and jugador.nacionalidad == nacionalidad_anterior and numero_a_texto(jugador.dorsal) == dorsal_anterior:
                jugador_actual = jugador

        if jugador_actual == "":
            messagebox.showerror("Error", "No se encontró el jugador seleccionado")
            return

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
        elif not texto_es_nombre(nombre):
            messagebox.showerror("Error", "El nombre del jugador solo debe contener letras")
            return
        elif not texto_es_nombre(apellido):
            messagebox.showerror("Error", "El apellido del jugador solo debe contener letras")
            return
        elif nacionalidad == "" or nacionalidad == "Seleccione Nacionalidad":
            messagebox.showerror("Error", "Seleccione nacionalidad")
            return
        elif dia == "Día" or mes == "Mes" or año == "Año":
            messagebox.showerror("Error", "Seleccione fecha completa")
            return
        elif posicion == "Seleccione Posicion":
            messagebox.showerror("Error", "Seleccione la posición")
            return
        elif not texto_es_entero(dorsal_texto) or not texto_es_entero(velocidad_texto) or not texto_es_entero(estratega_texto) or not texto_es_entero(dominio_texto) or not texto_es_entero(fuerza_texto):
            messagebox.showerror("Error", "Dorsal y puntajes deben ser números enteros")
            return
        elif int(dorsal_texto) < 1 or int(dorsal_texto) > 99:
            messagebox.showerror("Error", "El dorsal debe estar entre 1 y 99")
            return
        elif int(velocidad_texto) < 1 or int(velocidad_texto) > 25 or int(estratega_texto) < 1 or int(estratega_texto) > 25 or int(dominio_texto) < 1 or int(dominio_texto) > 25 or int(fuerza_texto) < 1 or int(fuerza_texto) > 25:
            messagebox.showerror("Error", "Los puntajes deben estar entre 1 y 25")
            return

        puntaje = int(velocidad_texto) + int(estratega_texto) + int(dominio_texto) + int(fuerza_texto)
        fecha = dia + "/" + mes + "/" + año
        jugador_actual.actualizar_datos(nombre.title(), apellido.title(), fecha, nacionalidad.title(), int(dorsal_texto), posicion, jugador_actual.total_tarjetas_amarillas, jugador_actual.total_tarjetas_rojas, jugador_actual.goles, jugador_actual.asistencias, puntaje)

        self.guardar_jugadores_archivo()
        self.cargar_tabla_jugadores()
        self.actualizar_combobox_jugadores()
        self.limpiar_jugador()
        messagebox.showinfo("Correcto", "Jugador actualizado correctamente")

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

    def guardar_jugadores_archivo(self):

        archivo = open("jugadores.txt", "w", encoding="utf-8")

        primero = True

        for jugador in lista_jugadores:
            linea = jugador.nombre + ";" + jugador.apellido + ";" + jugador.fecha_nacimiento + ";" + jugador.nacionalidad + ";" + numero_a_texto(jugador.dorsal) + ";" + jugador.posicion + ";" + numero_a_texto(jugador.total_tarjetas_amarillas) + ";" + numero_a_texto(jugador.total_tarjetas_rojas) + ";" + numero_a_texto(jugador.goles) + ";" + numero_a_texto(jugador.asistencias) + ";" + numero_a_texto(jugador.puntaje_individual) + ";" + jugador.seleccion

            if primero == True:
                archivo.write(linea)
                primero = False
            else:
                archivo.write("\n" + linea)

        archivo.close()

    def eliminar_jugador_registrado(self):

        global lista_jugadores

        seleccionado = self.tree_jugadores.focus()

        if seleccionado == "":
            messagebox.showerror("Error", "Seleccione un jugador de la tabla")
            return

        valores = self.tree_jugadores.item(seleccionado, "values")

        nombre_completo = valores[0]
        nacionalidad = valores[1]
        dorsal_texto = valores[2]

        nueva_lista = []
        eliminado = False

        for jugador in lista_jugadores:
            nombre_jugador = jugador.nombre + " " + jugador.apellido

            if nombre_jugador == nombre_completo and jugador.nacionalidad == nacionalidad and numero_a_texto(jugador.dorsal) == dorsal_texto and eliminado == False:
                eliminado = True
            else:
                nueva_lista += [jugador]

        if eliminado == False:
            messagebox.showerror("Error", "No se encontró el jugador seleccionado")
            return

        lista_jugadores = nueva_lista

        self.guardar_jugadores_archivo()
        self.cargar_tabla_jugadores()
        self.actualizar_combobox_jugadores()

        messagebox.showinfo("Correcto", "Jugador eliminado correctamente")

    def volver(self):
        self.destroy()
        self.principal.deiconify()

    def borrar_nombre_entrenador(self, e=None):
        if self.entry_nombre_entrenador.get() == "Ej: Carlo":
            self.entry_nombre_entrenador.delete(0, "end")

    def restaurar_nombre_entrenador(self, e=None):
        if self.entry_nombre_entrenador.get() == "":
            self.entry_nombre_entrenador.insert(0, "Ej: Carlo")

    def borrar_apellidos_entrenador(self, e=None):
        if self.entry_apellidos_entrenador.get() == "Ej: Ancelotti":
            self.entry_apellidos_entrenador.delete(0, "end")

    def restaurar_apellidos_entrenador(self, e=None):
        if self.entry_apellidos_entrenador.get() == "":
            self.entry_apellidos_entrenador.insert(0, "Ej: Ancelotti")

    def borrar_nombre_jugador(self, e=None):
        if self.entry_nombre_jugador.get() == "Ej: Lionel":
            self.entry_nombre_jugador.delete(0, "end")

    def restaurar_nombre_jugador(self, e=None):
        if self.entry_nombre_jugador.get() == "":
            self.entry_nombre_jugador.insert(0, "Ej: Lionel")

    def borrar_apellidos_jugador(self, e=None):
        if self.entry_apellidos_jugador.get() == "Ej: Messi":
            self.entry_apellidos_jugador.delete(0, "end")

    def restaurar_apellidos_jugador(self, e=None):
        if self.entry_apellidos_jugador.get() == "":
            self.entry_apellidos_jugador.insert(0, "Ej: Messi")

# Pantalla donde se crean los grupos del mundial
"""
Nombre: Configuracion_Mundial
Descripción: Prepara los grupos antes de iniciar la simulación
Entrada: Cantidad de grupos y selecciones cargadas
Salida: Grupos formados y visibles en la tabla
Restricción: Debe haber suficientes selecciones válidas
"""
class Configuracion_Mundial(tk.Toplevel):

    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)
        self.principal = principal
        self.geometry("1535x930+-7+-0")
        self.title("Configuración del Mundial")
        self.resizable(False, False)
        self.config(bg=blanco)
        self.titulo()
        self.panel_configuracion()
        self.tabla_grupos()
        self.botones()
        self.actualizar_resumen()

    def titulo(self):
        tk.Label(self, text="Configurar Mundial", font=("Arial", 32, "bold"), bg=blanco, fg=azul_oscuro, anchor="w").place(x=40, y=25, width=600, height=55)
        tk.Label(self, text="Cree grupos con selecciones que tengan entrenador y de 11 a 23 jugadores", font=("Arial", 14), bg=blanco, fg=gris, anchor="w").place(x=45, y=80, width=900, height=30)

    def panel_configuracion(self):
        frame = tk.LabelFrame(self, text=" Configuración ", font=("Arial", 14, "bold"), fg=azul_oscuro, bg=blanco, bd=1, relief="solid")
        frame.place(x=40, y=130, width=430, height=220)
        tk.Label(frame, text="Cantidad de grupos:", font=("Arial", 13, "bold"), bg=blanco, anchor="w").place(x=25, y=35, width=210, height=30)
        self.spinbox_grupos = tk.Spinbox(frame, from_=2, to=12, font=("Arial", 13))
        self.spinbox_grupos.delete(0, "end")
        self.spinbox_grupos.insert(0, "12")
        self.spinbox_grupos.place(x=245, y=35, width=120, height=30)
        self.label_validas = tk.Label(frame, text="Selecciones válidas: 0", font=("Arial", 12), bg=blanco, fg=azul_oscuro, anchor="w")
        self.label_validas.place(x=25, y=90, width=350, height=30)
        tk.Label(frame, text="Cada grupo usa 4 selecciones.", font=("Arial", 11), bg=blanco, fg=gris, anchor="w").place(x=25, y=130, width=350, height=30)

    def tabla_grupos(self):
        frame = tk.LabelFrame(self, text=" Grupos Formados ", font=("Arial", 14, "bold"), fg=azul_oscuro, bg=blanco, bd=1, relief="solid")
        frame.place(x=520, y=130, width=960, height=690)
        columnas = ("grupo", "seleccion", "entrenador", "jugadores", "fuerza")

        scroll_y = tk.Scrollbar(frame, orient="vertical")
        scroll_x = tk.Scrollbar(frame, orient="horizontal")

        self.tree_grupos = ttk.Treeview(frame,
                                        columns=columnas,
                                        show="headings",
                                        yscrollcommand=scroll_y.set,
                                        xscrollcommand=scroll_x.set)

        scroll_y.config(command=self.tree_grupos.yview)
        scroll_x.config(command=self.tree_grupos.xview)

        for columna in columnas:
            self.tree_grupos.heading(columna, text=columna.title())

        self.tree_grupos.column("grupo", width=130, anchor="center", stretch=False)
        self.tree_grupos.column("seleccion", width=220, anchor="w", stretch=False)
        self.tree_grupos.column("entrenador", width=260, anchor="w", stretch=False)
        self.tree_grupos.column("jugadores", width=100, anchor="center", stretch=False)
        self.tree_grupos.column("fuerza", width=100, anchor="center", stretch=False)

        self.tree_grupos.place(x=20, y=30, width=900, height=600)
        scroll_y.place(x=920, y=30, width=18, height=600)
        scroll_x.place(x=20, y=630, width=900, height=18)

    def botones(self):
        tk.Button(self,
                  text="Crear Grupos",
                  font=("Arial", 14, "bold"),
                  bg=verde,
                  fg=blanco,
                  command=self.crear_grupos).place(x=70, y=390, width=180, height=45)

        tk.Button(self,
                  text="Actualizar Datos",
                  font=("Arial", 14, "bold"),
                  bg=azul,
                  fg=blanco,
                  command=self.actualizar_resumen).place(x=270, y=390, width=180, height=45)

        tk.Button(self,
                  text="Ir a Jugar Mundial",
                  font=("Arial", 14, "bold"),
                  bg=celeste,
                  fg=negro,
                  command=self.abrir_jugar_mundial).place(x=170, y=455, width=180, height=45)

        tk.Button(self,
                  text="Regresar al menú principal",
                  font=("Arial", 13, "bold"),
                  bg=gris_claro,
                  fg=negro,
                  command=self.volver).place(x=1180, y=30, width=300, height=40)

    def limpiar_tabla(self):
        for fila in self.tree_grupos.get_children():
            self.tree_grupos.delete(fila)

    def actualizar_resumen(self):
        mundial = crear_mundial_actual()
        self.label_validas.config(text="Selecciones válidas: " + numero_a_texto(contar(mundial.obtener_selecciones_validas())))

    def cargar_tabla_grupos(self):
        self.limpiar_tabla()
        mundial = crear_mundial_actual()
        for grupo in mundial.grupos:
            for seleccion in grupo.equipos:
                entrenador = "Sin entrenador"
                if seleccion.entrenador is not None and seleccion.entrenador != "":
                    entrenador = seleccion.entrenador.nombre + " " + seleccion.entrenador.apellido
                self.tree_grupos.insert("", "end", values=(grupo.nombre_grupo, seleccion.pais.nombre, entrenador, contar(seleccion.jugadores), seleccion.fuerza_equipo))

    """
    Nombre: crear_grupos
    Descripción: Crea los grupos desde la pantalla de configuración
    Entrada: Cantidad de grupos escrita por el usuario
    Salida: Grupos mostrados en la tabla
    Restricción: Debe haber selecciones válidas suficientes
    """
    def crear_grupos(self):
        cantidad_texto = self.spinbox_grupos.get().strip()
        if cantidad_texto == "":
            messagebox.showerror("Error", "Ingrese la cantidad de grupos")
            return
        elif not texto_es_entero(cantidad_texto):
            messagebox.showerror("Error", "La cantidad de grupos debe ser un número entero")
            return
        elif int(cantidad_texto) < 2 or int(cantidad_texto) > 12:
            messagebox.showerror("Error", "La cantidad de grupos debe estar entre 2 y 12")
            return
        mundial = crear_mundial_actual()
        resultado = mundial.crear_grupos(int(cantidad_texto))
        if resultado[0] == "E":
            messagebox.showerror("Error", resultado)
            return
        guardar_selecciones_archivo()
        self.actualizar_resumen()
        self.cargar_tabla_grupos()
        messagebox.showinfo("Correcto", resultado)

    def volver(self):
        self.destroy()
        self.principal.deiconify()

    def abrir_jugar_mundial(self):
        self.destroy()
        Jugar_Mundial(self.principal)

# Ventana para jugar y simular el Mundial
# Pantalla donde se simulan los partidos y fases
"""
Nombre: Jugar_Mundial
Descripción: Permite simular grupos y fases eliminatorias
Entrada: Mundial ya configurado desde la pantalla anterior
Salida: Resultados, tablas, llave eliminatoria y campeón actualizados
Restricción: Primero se deben crear los grupos
"""
class Jugar_Mundial(tk.Toplevel):

    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)
        self.principal = principal
        self.geometry("1535x930+-7+-0")
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
        self.actualizar_estado()

    def boton_menu(self, texto, y, color, comando):
        tk.Button(self, text=texto, font=("Arial", 13, "bold"), bg=color, fg=blanco, bd=1, relief="solid", anchor="w", command=comando).place(x=25, y=y, width=250, height=50)

    def menu_lateral(self):
        tk.Frame(self, bg=azul_oscuro).place(x=0, y=0, width=300, height=930)
        tk.Label(self, text="Copa Mundial", font=("Arial", 22, "bold"), bg=azul_oscuro, fg=blanco).place(x=25, y=30, width=250, height=45)
        tk.Label(self, text="Simulación del Torneo", font=("Arial", 14, "bold"), bg=azul_oscuro, fg=blanco).place(x=25, y=85, width=250, height=30)
        self.boton_menu("Inicio", 160, azul_oscuro, self.volver)
        self.boton_menu("Países y Selecciones", 225, azul_oscuro, self.abrir_paises)
        self.boton_menu("Entrenadores y Jugadores", 290, azul_oscuro, self.abrir_jugadores)
        self.boton_menu("Configurar Mundial", 355, azul_oscuro, self.abrir_configuracion)
        self.boton_menu("Jugar Mundial", 420, azul, self.actualizar_estado)
        self.boton_menu("Estadísticas", 485, azul_oscuro, self.abrir_estadisticas)
        tk.Label(self, text="COPA\nMUNDIAL\n2026", font=("Arial", 28, "bold"), bg=azul_oscuro, fg=celeste).place(x=25, y=680, width=250, height=150)

    def pantalla_titulo(self):
        tk.Label(self, text="Jugar Mundial", font=("Arial", 32, "bold"), bg=blanco, fg=azul_oscuro, anchor="w").place(x=340, y=25, width=500, height=55)
        tk.Label(self, text="Simule la fase de grupos y las rondas eliminatorias", font=("Arial", 14), bg=blanco, fg=gris, anchor="w").place(x=345, y=78, width=700, height=30)

    def estado_torneo(self):
        frame = tk.LabelFrame(self, text=" Estado del Torneo ", font=("Arial", 14, "bold"), fg=azul_oscuro, bg=blanco, bd=1, relief="solid")
        frame.place(x=340, y=120, width=390, height=220)

        tk.Label(frame, text="Fase actual:", font=("Arial", 12), bg=blanco, anchor="w").place(x=25, y=25, width=190, height=25)
        self.label_fase_actual = tk.Label(frame, text="Sin iniciar", font=("Arial", 12, "bold"), bg=blanco, fg=azul, anchor="e")
        self.label_fase_actual.place(x=215, y=25, width=130, height=25)

        tk.Label(frame, text="Grupos configurados:", font=("Arial", 12), bg=blanco, anchor="w").place(x=25, y=65, width=190, height=25)
        self.label_grupos = tk.Label(frame, text="0", font=("Arial", 12, "bold"), bg=blanco, fg=azul, anchor="e")
        self.label_grupos.place(x=215, y=65, width=130, height=25)

        tk.Label(frame, text="Partidos jugados:", font=("Arial", 12), bg=blanco, anchor="w").place(x=25, y=105, width=190, height=25)
        self.label_partidos = tk.Label(frame, text="0", font=("Arial", 12, "bold"), bg=blanco, fg=azul, anchor="e")
        self.label_partidos.place(x=215, y=105, width=130, height=25)

        tk.Label(frame, text="Equipos clasificados:", font=("Arial", 12), bg=blanco, anchor="w").place(x=25, y=145, width=190, height=25)
        self.label_clasificados = tk.Label(frame, text="0", font=("Arial", 12, "bold"), bg=blanco, fg=azul, anchor="e")
        self.label_clasificados.place(x=215, y=145, width=130, height=25)

    def simular_mundial(self):
        frame = tk.LabelFrame(self, text=" Acciones ", font=("Arial", 14, "bold"), fg=azul_oscuro, bg=blanco, bd=1, relief="solid")
        frame.place(x=750, y=120, width=330, height=220)

        self.boton_simular_grupos = tk.Button(frame,
                                              text="Simular Fase de Grupos",
                                              font=("Arial", 12, "bold"),
                                              bg=verde,
                                              fg=blanco,
                                              command=self.simular_fase_grupos)
        self.boton_simular_grupos.place(x=25, y=25, width=280, height=35)

        tk.Button(frame,
                  text="Avanzar a Siguiente Fase",
                  font=("Arial", 12, "bold"),
                  bg=gris_claro,
                  fg=negro,
                  command=self.avanzar_fase).place(x=25, y=68, width=280, height=35)

        tk.Button(frame,
                  text="Ver Campeón",
                  font=("Arial", 12, "bold"),
                  bg=amarillo,
                  fg=negro,
                  command=self.ver_campeon).place(x=25, y=111, width=280, height=35)

        tk.Button(frame,
                  text="Volver al Inicio",
                  font=("Arial", 12, "bold"),
                  bg=celeste,
                  fg=negro,
                  command=self.volver).place(x=25, y=154, width=280, height=35)

    def resultados_recientes(self):
        frame = tk.LabelFrame(self, text=" Resultados Recientes ", font=("Arial", 14, "bold"), fg=azul_oscuro, bg=blanco, bd=1, relief="solid")
        frame.place(x=340, y=360, width=740, height=210)

        scroll_y = tk.Scrollbar(frame, orient="vertical")
        scroll_x = tk.Scrollbar(frame, orient="horizontal")

        self.tabla_resultados = ttk.Treeview(frame,
                                             columns=("partido", "fase", "resultado", "ganador"),
                                             show="headings",
                                             height=6,
                                             yscrollcommand=scroll_y.set,
                                             xscrollcommand=scroll_x.set)

        scroll_y.config(command=self.tabla_resultados.yview)
        scroll_x.config(command=self.tabla_resultados.xview)

        for columna in ("partido", "fase", "resultado", "ganador"):
            self.tabla_resultados.heading(columna, text=columna.title())

        self.tabla_resultados.column("partido", width=260, stretch=False)
        self.tabla_resultados.column("fase", width=150, stretch=False)
        self.tabla_resultados.column("resultado", width=260, stretch=False)
        self.tabla_resultados.column("ganador", width=160, stretch=False)

        self.tabla_resultados.place(x=20, y=25, width=670, height=145)
        scroll_y.place(x=690, y=25, width=18, height=145)
        scroll_x.place(x=20, y=170, width=670, height=18)

    def tabla_grupo(self):
        frame = tk.LabelFrame(self, text=" Tabla de Grupo ", font=("Arial", 14, "bold"), fg=azul_oscuro, bg=blanco, bd=1, relief="solid")
        frame.place(x=340, y=595, width=620, height=245)

        tk.Label(frame, text="Grupo:", font=("Arial", 11, "bold"), bg=blanco, anchor="w").place(x=20, y=5, width=70, height=25)
        self.grupo_tabla_seleccionado = tk.StringVar()
        self.combo_grupos_tabla = ttk.Combobox(frame,
                                               values=[],
                                               state="readonly",
                                               textvariable=self.grupo_tabla_seleccionado)
        self.combo_grupos_tabla.place(x=90, y=5, width=160, height=25)
        self.combo_grupos_tabla.bind("<<ComboboxSelected>>", self.cargar_tabla_grupo_seleccionado)

        scroll_y = tk.Scrollbar(frame, orient="vertical")
        scroll_x = tk.Scrollbar(frame, orient="horizontal")

        columnas = ("pos", "equipo", "pts", "pj", "pg", "pe", "pp", "gf", "gc", "dg")
        self.tabla_posiciones = ttk.Treeview(frame,
                                             columns=columnas,
                                             show="headings",
                                             height=6,
                                             yscrollcommand=scroll_y.set,
                                             xscrollcommand=scroll_x.set)

        scroll_y.config(command=self.tabla_posiciones.yview)
        scroll_x.config(command=self.tabla_posiciones.xview)

        encabezados = (("pos", "#"), ("equipo", "Equipo"), ("pts", "Pts"), ("pj", "PJ"), ("pg", "PG"), ("pe", "PE"), ("pp", "PP"), ("gf", "GF"), ("gc", "GC"), ("dg", "DG"))

        for columna, texto in encabezados:
            self.tabla_posiciones.heading(columna, text=texto)

        self.tabla_posiciones.column("pos", width=45, anchor="center", stretch=False)
        self.tabla_posiciones.column("equipo", width=210, anchor="w", stretch=False)
        self.tabla_posiciones.column("pts", width=55, anchor="center", stretch=False)
        self.tabla_posiciones.column("pj", width=55, anchor="center", stretch=False)
        self.tabla_posiciones.column("pg", width=55, anchor="center", stretch=False)
        self.tabla_posiciones.column("pe", width=55, anchor="center", stretch=False)
        self.tabla_posiciones.column("pp", width=55, anchor="center", stretch=False)
        self.tabla_posiciones.column("gf", width=55, anchor="center", stretch=False)
        self.tabla_posiciones.column("gc", width=55, anchor="center", stretch=False)
        self.tabla_posiciones.column("dg", width=55, anchor="center", stretch=False)

        self.tabla_posiciones.place(x=20, y=35, width=540, height=155)
        scroll_y.place(x=560, y=35, width=18, height=155)
        scroll_x.place(x=20, y=190, width=540, height=18)

    def campeon_actual(self):
        frame = tk.LabelFrame(self, text=" Campeón Actual ", font=("Arial", 14, "bold"), fg=azul_oscuro, bg="#FFF4C2", bd=2, relief="solid")
        frame.place(x=980, y=575, width=520, height=160)
        self.label_campeon = tk.Label(frame, text="Sin definir", font=("Arial", 27, "bold"), bg="#FFF4C2", fg=azul_oscuro)
        self.label_campeon.place(x=40, y=35, width=440, height=45)
        self.label_estado_campeon = tk.Label(frame, text="Esperando final", font=("Arial", 14, "italic"), bg="#FFF4C2", fg=gris)
        self.label_estado_campeon.place(x=40, y=98, width=440, height=30)

    def llave_eliminatoria(self):
        frame = tk.LabelFrame(self, text=" Llave Eliminatoria ", font=("Arial", 14, "bold"), fg=azul_oscuro, bg=blanco, bd=1, relief="solid")
        frame.place(x=1100, y=120, width=400, height=430)
        self.canvas_llave = tk.Canvas(frame, bg=blanco, highlightthickness=0)
        self.canvas_llave.place(x=10, y=10, width=370, height=385)
        self.canvas_llave.create_text(185, 40, text="Esperando fase eliminatoria", font=("Arial", 12, "bold"))

    def limpiar_tabla(self, tabla):
        for fila in tabla.get_children():
            tabla.delete(fila)

    def actualizar_estado(self):
        mundial = crear_mundial_actual()
        self.label_fase_actual.config(text=mundial.fase_actual)
        self.label_grupos.config(text=numero_a_texto(contar(mundial.grupos)))
        self.label_partidos.config(text=numero_a_texto(contar(mundial.partidos_jugados)))
        self.label_clasificados.config(text=numero_a_texto(contar(mundial.clasificados_actuales)))

        self.cargar_nombres_grupos()

        if mundial.fase_actual == "Grupos configurados":
            self.boton_simular_grupos.config(state="normal")
        else:
            self.boton_simular_grupos.config(state="disabled")

    def cargar_resultados(self, partidos):
        self.limpiar_tabla(self.tabla_resultados)
        contador = 1
        for partido in partidos:
            ganador = partido.generar_ganador()
            if partido.penales_equipo1 != 0 or partido.penales_equipo2 != 0:
                ganador = partido.ganador_eliminatoria()
            nombre_ganador = "Empate"
            if ganador is not None:
                nombre_ganador = ganador.pais.nombre
            self.tabla_resultados.insert("", "end", values=(numero_a_texto(contador), partido.fase, partido.mostrar_resultado(), nombre_ganador))
            contador += 1

    def cargar_nombres_grupos(self):
        mundial = crear_mundial_actual()
        nombres = []

        for grupo in mundial.grupos:
            nombres += [grupo.nombre_grupo]

        self.combo_grupos_tabla.config(values=nombres)

        if contar(nombres) > 0:
            seleccionado = self.grupo_tabla_seleccionado.get()
            existe = False
            for nombre in nombres:
                if nombre == seleccionado:
                    existe = True

            if existe == False:
                self.combo_grupos_tabla.set(nombres[0])

    def buscar_grupo_por_nombre(self, nombre_grupo):
        mundial = crear_mundial_actual()
        for grupo in mundial.grupos:
            if grupo.nombre_grupo == nombre_grupo:
                return grupo
        return None

    def cargar_tabla_grupo_seleccionado(self, evento=None):
        self.limpiar_tabla(self.tabla_posiciones)
        self.cargar_nombres_grupos()

        nombre_grupo = self.grupo_tabla_seleccionado.get()
        grupo = self.buscar_grupo_por_nombre(nombre_grupo)

        if grupo is None:
            return

        posicion = 1
        for seleccion in grupo.calcular_tabla():
            self.tabla_posiciones.insert("",
                                         "end",
                                         values=(posicion,
                                                 seleccion.pais.nombre,
                                                 seleccion.puntos,
                                                 seleccion.partidos_jugados,
                                                 seleccion.partidos_ganados,
                                                 seleccion.partidos_empatados,
                                                 seleccion.partidos_perdidos,
                                                 seleccion.total_goles_a_favor,
                                                 seleccion.total_goles_en_contra,
                                                 seleccion.diferencia_goles))
            posicion += 1

    def cargar_tabla_primer_grupo(self):
        self.cargar_tabla_grupo_seleccionado()

    def actualizar_llave(self, fase):
        self.canvas_llave.delete("all")
        self.canvas_llave.create_text(185, 25, text=fase.nombre_fase, font=("Arial", 13, "bold"))
        y = 60
        for partido in fase.partidos:
            ganador = partido.ganador_eliminatoria()
            self.canvas_llave.create_rectangle(25, y, 345, y + 35, outline=azul)
            self.canvas_llave.create_text(185, y + 10, text=partido.mostrar_resultado(), font=("Arial", 8))
            self.canvas_llave.create_text(185, y + 25, text="Avanza: " + ganador.pais.nombre, font=("Arial", 8, "bold"))
            y += 48

    """
    Nombre: simular_fase_grupos
    Descripción: Ejecuta la fase de grupos desde la pantalla de juego
    Entrada: Mundial actual con grupos formados
    Salida: Resultados, tablas y estado del torneo actualizados
    Restricción: La fase de grupos no debe haberse simulado antes
    """
    def simular_fase_grupos(self):
        mundial = crear_mundial_actual()
        if contar(mundial.grupos) == 0:
            messagebox.showerror("Error", "Primero configure los grupos en Configurar Mundial")
            return
        resultado = mundial.jugar_fase_grupos()
        if resultado[0] == "E":
            messagebox.showerror("Error", resultado)
            return
        if resultado[0] == "A":
            messagebox.showinfo("Aviso", resultado)
            self.actualizar_estado()
            return
        guardar_jugadores_archivo_general()
        mundial.generar_reporte()
        self.cargar_resultados(mundial.partidos_jugados)
        self.cargar_tabla_primer_grupo()
        self.actualizar_estado()
        self.boton_simular_grupos.config(state="disabled")
        messagebox.showinfo("Correcto", resultado)

    """
    Nombre: avanzar_fase
    Descripción: Juega la siguiente ronda del Mundial
    Entrada: Estado actual del torneo
    Salida: Siguiente fase jugada o campeón definido
    Restricción: La fase de grupos debe estar terminada
    """
    def avanzar_fase(self):
        mundial = crear_mundial_actual()
        resultado = mundial.jugar_siguiente_fase()
        if resultado[0] == "E":
            messagebox.showerror("Error", resultado)
            return
        ultima_fase = None
        for fase in mundial.fases:
            ultima_fase = fase
        if ultima_fase is not None:
            self.cargar_resultados(ultima_fase.partidos)
            self.actualizar_llave(ultima_fase)
        guardar_jugadores_archivo_general()
        mundial.generar_reporte()
        self.cargar_tabla_primer_grupo()
        self.actualizar_estado()
        if mundial.campeon is not None:
            self.label_campeon.config(text=mundial.campeon.pais.nombre)
            self.label_estado_campeon.config(text="Campeón definido")
        messagebox.showinfo("Correcto", resultado)

    def ver_campeon(self):
        mundial = crear_mundial_actual()
        if mundial.campeon is None:
            messagebox.showinfo("Información", "Todavía no hay campeón")
            return
        self.label_campeon.config(text=mundial.campeon.pais.nombre)
        self.label_estado_campeon.config(text="Campeón del torneo")
        messagebox.showinfo("Campeón", "El campeón es: " + mundial.campeon.pais.nombre)

    def abrir_paises(self):
        self.destroy()
        Administrar_Paises_Selecciones(self.principal)

    def abrir_jugadores(self):
        self.destroy()
        Administrar_Entrenadores_Jugadores(self.principal)

    def abrir_configuracion(self):
        self.destroy()
        Configuracion_Mundial(self.principal)

    def abrir_estadisticas(self):
        self.destroy()
        Estadisticas(self.principal)

    def volver(self):
        self.destroy()
        self.principal.deiconify()

# Pantalla de rankings y resumen general
"""
Nombre: Estadisticas
Descripción: Muestra resúmenes y rankings del torneo
Entrada: Datos de países, selecciones, jugadores y partidos
Salida: Tablas y estadísticas generales en pantalla
Restricción: Algunos datos dependen de que ya se haya simulado el Mundial
"""
class Estadisticas(tk.Toplevel):

    def __init__(self, principal):
        tk.Toplevel.__init__(self, principal)

        self.principal = principal

        self.geometry("1535x930+-7+-0")
        self.title("Estadísticas / Ranking")
        self.resizable(False, False)
        self.config(bg=blanco)

        self.encabezado()
        self.boton_volver_superior()
        self.resumen_general()
        self.ranking_paises()
        self.ranking_jugadores()
        self.resumen_torneo_estadisticas()
        self.estadisticas_selecciones()
        self.botones()
        self.actualizar_estadisticas()

    def boton_volver_superior(self):
        boton_volver = tk.Button(self,
                                 text="Regresar al menú principal",
                                 font=("Arial", 12, "bold"),
                                 bg=gris_claro,
                                 fg=negro,
                                 bd=2,
                                 relief="raised",
                                 command=self.volver)
        boton_volver.place(x=1230, y=20, width=270, height=40)

    def contar_lista(self, lista):
        cantidad = 0

        for elemento in lista:
            cantidad = cantidad + 1

        return cantidad

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

    def ranking_paises(self):
        frame_ranking_paises = tk.LabelFrame(self,
                                             text=" Ranking FIFA de Países ",
                                             font=("Arial", 14, "bold"),
                                             fg=azul_oscuro,
                                             bg=blanco,
                                             bd=1,
                                             relief="solid")
        frame_ranking_paises.place(x=40, y=270, width=700, height=280)

        scroll_y_paises = tk.Scrollbar(frame_ranking_paises, orient="vertical")
        scroll_x_paises = tk.Scrollbar(frame_ranking_paises, orient="horizontal")

        self.tabla_paises = ttk.Treeview(frame_ranking_paises,
                                         columns=("posicion", "codigo", "pais", "continente", "ranking"),
                                         show="headings",
                                         height=8,
                                         yscrollcommand=scroll_y_paises.set,
                                         xscrollcommand=scroll_x_paises.set)

        scroll_y_paises.config(command=self.tabla_paises.yview)
        scroll_x_paises.config(command=self.tabla_paises.xview)

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

        self.tabla_paises.place(x=20, y=25, width=630, height=200)
        scroll_y_paises.place(x=650, y=25, width=18, height=200)
        scroll_x_paises.place(x=20, y=225, width=630, height=18)

    def ranking_jugadores(self):
        frame_ranking_jugadores = tk.LabelFrame(self,
                                                text=" Ranking de Jugadores ",
                                                font=("Arial", 14, "bold"),
                                                fg=azul_oscuro,
                                                bg=blanco,
                                                bd=1,
                                                relief="solid")
        frame_ranking_jugadores.place(x=780, y=270, width=700, height=280)

        scroll_y_jugadores = tk.Scrollbar(frame_ranking_jugadores, orient="vertical")
        scroll_x_jugadores = tk.Scrollbar(frame_ranking_jugadores, orient="horizontal")

        self.tabla_jugadores = ttk.Treeview(frame_ranking_jugadores,
                                            columns=("posicion", "jugador", "seleccion", "posicion_juego", "goles", "asistencias", "puntaje"),
                                            show="headings",
                                            height=8,
                                            yscrollcommand=scroll_y_jugadores.set,
                                            xscrollcommand=scroll_x_jugadores.set)

        scroll_y_jugadores.config(command=self.tabla_jugadores.yview)
        scroll_x_jugadores.config(command=self.tabla_jugadores.xview)

        self.tabla_jugadores.heading("posicion", text="#")
        self.tabla_jugadores.heading("jugador", text="Jugador")
        self.tabla_jugadores.heading("seleccion", text="Selección")
        self.tabla_jugadores.heading("posicion_juego", text="Posición")
        self.tabla_jugadores.heading("goles", text="Goles")
        self.tabla_jugadores.heading("asistencias", text="Asist.")
        self.tabla_jugadores.heading("puntaje", text="Puntaje")

        self.tabla_jugadores.column("posicion", width=50, anchor="center")
        self.tabla_jugadores.column("jugador", width=180, anchor="w")
        self.tabla_jugadores.column("seleccion", width=115, anchor="center")
        self.tabla_jugadores.column("posicion_juego", width=120, anchor="center")
        self.tabla_jugadores.column("goles", width=80, anchor="center")
        self.tabla_jugadores.column("asistencias", width=80, anchor="center")
        self.tabla_jugadores.column("puntaje", width=90, anchor="center")

        self.tabla_jugadores.place(x=20, y=25, width=630, height=200)
        scroll_y_jugadores.place(x=650, y=25, width=18, height=200)
        scroll_x_jugadores.place(x=20, y=225, width=630, height=18)

    def resumen_torneo_estadisticas(self):
        frame_goles = tk.LabelFrame(self,
                                    text=" Selección con más goles ",
                                    font=("Arial", 13, "bold"),
                                    fg=azul_oscuro,
                                    bg=blanco,
                                    bd=1,
                                    relief="solid")
        frame_goles.place(x=40, y=555, width=700, height=75)

        self.label_mas_goles = tk.Label(frame_goles,
                                        text="Sin datos",
                                        font=("Arial", 14, "bold"),
                                        bg=blanco,
                                        fg=verde,
                                        anchor="center")
        self.label_mas_goles.place(x=20, y=15, width=650, height=35)

        frame_tarjetas = tk.LabelFrame(self,
                                       text=" Selección con más tarjetas ",
                                       font=("Arial", 13, "bold"),
                                       fg=azul_oscuro,
                                       bg=blanco,
                                       bd=1,
                                       relief="solid")
        frame_tarjetas.place(x=780, y=555, width=700, height=75)

        self.label_mas_tarjetas = tk.Label(frame_tarjetas,
                                           text="Sin datos",
                                           font=("Arial", 14, "bold"),
                                           bg=blanco,
                                           fg=rojo,
                                           anchor="center")
        self.label_mas_tarjetas.place(x=20, y=15, width=650, height=35)

    def estadisticas_selecciones(self):
        frame_selecciones = tk.LabelFrame(self,
                                          text=" Tabla de Selecciones por Desempeño ",
                                          font=("Arial", 14, "bold"),
                                          fg=azul_oscuro,
                                          bg=blanco,
                                          bd=1,
                                          relief="solid")
        frame_selecciones.place(x=40, y=645, width=1440, height=195)

        scroll_y_selecciones = tk.Scrollbar(frame_selecciones, orient="vertical")
        scroll_x_selecciones = tk.Scrollbar(frame_selecciones, orient="horizontal")

        self.tabla_selecciones = ttk.Treeview(frame_selecciones,
                                              columns=("codigo", "pais", "pts", "dg", "gf", "gc", "fase", "amarillas", "rojas", "fuerza"),
                                              show="headings",
                                              height=6,
                                              yscrollcommand=scroll_y_selecciones.set,
                                              xscrollcommand=scroll_x_selecciones.set)

        scroll_y_selecciones.config(command=self.tabla_selecciones.yview)
        scroll_x_selecciones.config(command=self.tabla_selecciones.xview)

        self.tabla_selecciones.heading("codigo", text="Código")
        self.tabla_selecciones.heading("pais", text="País")
        self.tabla_selecciones.heading("pts", text="Pts")
        self.tabla_selecciones.heading("dg", text="DG")
        self.tabla_selecciones.heading("gf", text="GF Torneo")
        self.tabla_selecciones.heading("gc", text="GC Torneo")
        self.tabla_selecciones.heading("fase", text="Fase Alcanzada")
        self.tabla_selecciones.heading("amarillas", text="Amarillas")
        self.tabla_selecciones.heading("rojas", text="Rojas")
        self.tabla_selecciones.heading("fuerza", text="Fuerza")

        self.tabla_selecciones.column("codigo", width=80, anchor="center", stretch=False)
        self.tabla_selecciones.column("pais", width=220, anchor="w", stretch=False)
        self.tabla_selecciones.column("pts", width=70, anchor="center", stretch=False)
        self.tabla_selecciones.column("dg", width=70, anchor="center", stretch=False)
        self.tabla_selecciones.column("gf", width=70, anchor="center", stretch=False)
        self.tabla_selecciones.column("gc", width=70, anchor="center", stretch=False)
        self.tabla_selecciones.column("fase", width=220, anchor="center", stretch=False)
        self.tabla_selecciones.column("amarillas", width=100, anchor="center", stretch=False)
        self.tabla_selecciones.column("rojas", width=80, anchor="center", stretch=False)
        self.tabla_selecciones.column("fuerza", width=80, anchor="center", stretch=False)

        self.tabla_selecciones.place(x=20, y=25, width=1370, height=115)
        scroll_y_selecciones.place(x=1390, y=25, width=18, height=115)
        scroll_x_selecciones.place(x=20, y=140, width=1370, height=18)

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

    def limpiar_tabla(self, tabla):
        filas = tabla.get_children()

        for fila in filas:
            tabla.delete(fila)

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

    def seleccion_va_antes_estadistica(self, seleccion1, seleccion2):
        if seleccion1.puntos != seleccion2.puntos:
            return seleccion1.puntos > seleccion2.puntos
        if seleccion1.diferencia_goles != seleccion2.diferencia_goles:
            return seleccion1.diferencia_goles > seleccion2.diferencia_goles
        if seleccion1.goles_torneo_favor != seleccion2.goles_torneo_favor:
            return seleccion1.goles_torneo_favor > seleccion2.goles_torneo_favor
        return seleccion1.fuerza_equipo > seleccion2.fuerza_equipo

    def ordenar_selecciones(self):
        selecciones_ordenadas = []

        for seleccion in lista_selecciones:
            selecciones_ordenadas += [seleccion]

        cantidad = self.contar_lista(selecciones_ordenadas)

        i = 0

        while i < cantidad - 1:
            j = i + 1

            while j < cantidad:
                if self.seleccion_va_antes_estadistica(selecciones_ordenadas[j], selecciones_ordenadas[i]):
                    temporal = selecciones_ordenadas[i]
                    selecciones_ordenadas[i] = selecciones_ordenadas[j]
                    selecciones_ordenadas[j] = temporal

                j = j + 1

            i = i + 1

        return selecciones_ordenadas

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

    def cargar_jugadores(self):
        jugadores_ordenados = self.ordenar_jugadores()

        contador = 0

        for jugador in jugadores_ordenados:
            nombre_completo = jugador.nombre + " " + jugador.apellido

            self.tabla_jugadores.insert("",
                                        "end",
                                        values=(contador + 1,
                                                nombre_completo,
                                                jugador.seleccion,
                                                jugador.posicion,
                                                jugador.goles,
                                                jugador.asistencias,
                                                jugador.puntaje_individual))

            contador = contador + 1

    def cargar_selecciones(self):
        selecciones_ordenadas = self.ordenar_selecciones()

        for seleccion in selecciones_ordenadas:
            self.tabla_selecciones.insert("",
                                          "end",
                                          values=(seleccion.codigo_equipo,
                                                  seleccion.pais.nombre,
                                                  seleccion.puntos,
                                                  seleccion.diferencia_goles,
                                                  seleccion.goles_torneo_favor,
                                                  seleccion.goles_torneo_contra,
                                                  seleccion.fase_alcanzada,
                                                  seleccion.tarjetas_amarillas_torneo,
                                                  seleccion.tarjetas_rojas_torneo,
                                                  seleccion.fuerza_equipo))

    def buscar_seleccion_mas_goles(self):
        seleccion_mayor = None

        for seleccion in lista_selecciones:
            if seleccion_mayor is None:
                seleccion_mayor = seleccion
            elif seleccion.goles_torneo_favor > seleccion_mayor.goles_torneo_favor:
                seleccion_mayor = seleccion

        return seleccion_mayor

    def buscar_seleccion_mas_tarjetas(self):
        seleccion_mayor = None
        mayor_tarjetas = 0

        for seleccion in lista_selecciones:
            total_tarjetas = seleccion.tarjetas_amarillas_torneo + seleccion.tarjetas_rojas_torneo

            if seleccion_mayor is None:
                seleccion_mayor = seleccion
                mayor_tarjetas = total_tarjetas
            elif total_tarjetas > mayor_tarjetas:
                seleccion_mayor = seleccion
                mayor_tarjetas = total_tarjetas

        return seleccion_mayor

    def actualizar_resumen_torneo(self):
        seleccion_goles = self.buscar_seleccion_mas_goles()
        seleccion_tarjetas = self.buscar_seleccion_mas_tarjetas()

        if seleccion_goles is None:
            self.label_mas_goles.config(text="Sin datos")
        else:
            self.label_mas_goles.config(text=seleccion_goles.pais.nombre + " - " + numero_a_texto(seleccion_goles.goles_torneo_favor) + " goles")

        if seleccion_tarjetas is None:
            self.label_mas_tarjetas.config(text="Sin datos")
        else:
            total_tarjetas = seleccion_tarjetas.tarjetas_amarillas_torneo + seleccion_tarjetas.tarjetas_rojas_torneo
            self.label_mas_tarjetas.config(text=seleccion_tarjetas.pais.nombre + " - A: " + numero_a_texto(seleccion_tarjetas.tarjetas_amarillas_torneo) + " R: " + numero_a_texto(seleccion_tarjetas.tarjetas_rojas_torneo) + " Total: " + numero_a_texto(total_tarjetas))

    """
    Nombre: actualizar_estadisticas
    Descripción: Actualiza las tablas y los resúmenes estadísticos
    Entrada: Listas actuales de países, jugadores y selecciones
    Salida: Rankings y estadísticas visibles en pantalla
    Restricción: Las listas deben estar cargadas
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
        self.actualizar_resumen_torneo()

    def volver(self):
        self.destroy()
        self.principal.deiconify()

if __name__ == "__main__":
    app = Pantalla_Principal()
    app.mainloop()

