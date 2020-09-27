# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:28:03 2020

@author: JorgeZaldivar
"""

# Tarea C01.Tarea05

# 1. Calcular índice de Jaccard
def jaccard(A, B):
    return len(A & B) / len(A | B)


# 2. Palabras en común entre dos frases
def palabras_en_comun(s1, s2):
    palabras1 = set(s1.lower().split())
    palabras2 = set(s2.lower().split())
    en_comun = palabras1 & palabras2
    return en_comun


# 3a. Línea más larga de un archivo
def linea_mas_larga(file):
    with open(file, "r") as f:
        mayor = ""
        for li in f:
            if len(li) > len(mayor):
                mayor = li
    return mayor


# 3b. Últimas n líneas de un archivo
def ultimas_n_lineas(file, n):
    lineas = []
    with open(file, "r") as f:
        for li in f:
            lineas.append(li)
            if len(lineas) > n:
                # Eliminar la primera
                lineas = lineas[1:]
    for i in range(n - len(lineas)):
        lineas.append("Error: Líneas insuficientes.")
    return lineas


# Código para probar función palabras_en_comun
# Entradas
frase1 = input("Introduzca una frase: ")
frase2 = input("Introduzca otra frase: ")
# Proceso
en_comun = palabras_en_comun(frase1, frase2)
# Salidas
if len(en_comun) > 1:
    print(f"Las frases tienen las siguientes {len(en_comun)} palabras en común:")
    for palabra in en_comun:
        print("-", palabra)
elif len(en_comun) == 1:
    print(f"Las frases tienen en común la palabra '{en_comun.pop()}'.")
else:
    print("Las frases no tienen ninguna palabra en común.")
