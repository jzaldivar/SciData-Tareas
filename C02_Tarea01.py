# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:15:11 2020

@author: JorgeZaldivar
"""

# Tarea C02.1 
import numpy as np

# 1. Crear array
arreglo = np.arange(1, 16)
arreglo = arreglo.reshape(3, 5)
arreglo = arreglo.transpose()
print(arreglo)

# 2. Imprimir dimensiones
print(f"Este arreglo tiene {arreglo.ndim} dimensiones, ", end="")
print(f"las cuales valen {arreglo.shape}, ", end="")
print(f"y, por lo tanto, tiene {arreglo.size} elementos.")

# 3. Seleccionar la columna 2
seleccion = arreglo[:, 1]
print(seleccion)

# 4. Crear un segundo arreglo
array2 = np.arange(15, 56)

# 5. Cambiar elemento en quinta posición
array2[4] = 23

# 6. "Invertir" el arreglo
array2 = array2[::-1]

# 7. Crear matriz diagonal
matriz_diag = np.diag(array2[:5])

# 8. Imprimir dimensiones
print(f"matriz_diag tiene {matriz_diag.ndim} dimensiones, ", end="")
print(f"las cuales valen {matriz_diag.shape}, ", end="")
print(f"y, por lo tanto, tiene {matriz_diag.size} elementos.")

# 9. Crear matriz aleatoria
matriz_aleatoria = np.random.rand(5, 3)

# 10. Multiplicar matriz_aleatoria por matriz_diag
if matriz_aleatoria.shape[1] == matriz_diag.shape[0]:
    producto1 = np.matmul(matriz_aleatoria, matriz_diag)
    print("Producto de matriz_aleatoria por matriz_diag:")
    print(producto1)
else:
    print("No es posible multiplicar matriz_aleatoria por matriz_diag")

# 11. Multiplicar matriz_diag por matriz_aleatoria 
if matriz_diag.shape[1] == matriz_aleatoria.shape[0]:
    producto2 = np.matmul(matriz_diag, matriz_aleatoria)
    print("Producto de matriz_diag por matriz_aleatoria:")
    print(producto2)
else:
    print("No es posible multiplicar matriz_diag por matriz_aleatoria")
