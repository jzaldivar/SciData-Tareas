# -*- coding: utf-8 -*-
"""
C01.Tarea02b
"""

# Definiciones
estaciones = {'PRIMAVERA': ['abril', 'mayo', 'junio'],
              'VERANO': ['julio', 'agosto', 'septiembre'],
              'OTOÑO': ['octubre', 'noviembre', 'diciembre'],
              'INVIERNO': ['enero', 'febrero', 'marzo']}

# Entradas
mes = input('mes = ')

# Proceso
mes = mes.lower()
for estacion, meses in estaciones.items():
    if mes in meses:
        break
else:
    estacion = 'Error de entrada'

# Salidas
print(estacion)
