# -*- coding: utf-8 -*-
"""
C01.Tarea02a
"""

# Entradas
x = eval(input('x = '))
y = eval(input('y = '))
t = input('t = ')

# Proceso
if t == 'a':
    r = x + y
elif t == 'b':
    r = x - y
elif t == 'c':
    r = x * y
elif t == 'd':
    r = x / y
elif t == 'e':
    r = x ** y
else:
    r = 'Undefined'

# Salidas
print('Resultado:', r)
