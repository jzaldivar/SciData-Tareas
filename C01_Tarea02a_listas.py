# -*- coding: utf-8 -*-
"""
C01.Tarea02a con listas
"""

# Definiciones
ts = ['a', 'b', 'c', 'd', 'e']
ops = ['+', '-', '*', '/', '**']

# Entradas
x = input('x = ')
y = input('y = ')
t = input('t = ')

# Proceso
try:
    op = ts.index(t)
    op = ops[op]
    r = eval(x + op + y)
except ValueError:
    r = 'Undefined'

# Salidas
print('Resultado:', r)
