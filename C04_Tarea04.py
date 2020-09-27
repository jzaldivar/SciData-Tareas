# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 23:54:59 2020

@author: JorgeZaldivar
"""

# Ejemplo de clases SciDatMath
class Carro:
    def __init__(self, modelo, velocidad_maxima, color = "negro"):
        self.color = color # Esto es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 # el carro está detenido
        
    def describir(self):
        descripcion = f"Carro modelo {self.modelo} de color {self.color} con velocidad máxima de {self.velocidad_maxima} km/h"
        return descripcion
    
    def __repr__(self):
        return self.describir()
    
    def estado(self):
        if self.velocidad == 0:
            print("El carro está detenido")
        elif self.velocidad > 0:
            print(f"El carro va a {self.velocidad} km/h")
        else:
            print(f"El vehículo va marcha atrás a {-self.velocidad} km/h")
            
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self, diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Subiendo la velocidad en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad + diferencia_velocidad
            self.velocidad = min(self.velocidad, self.velocidad_maxima)
        else:
            print("No se puede acelerar negativamente")
            
    def frenar(self, diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Frenando en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad - diferencia_velocidad
            self.velocidad = max(self.velocidad, -5)
            

# C04.Tarea04
            
class Taxi(Carro):
    
    def __init__(self, modelo, velocidad_maxima, color = "amarillo"):
        super().__init__(modelo, velocidad_maxima, color)
        self.distancia_recorrida = 0
        self.tiempo = 0
        self.tarifa = 1.07 * 4
        
    def cobrar(self, distancia):
        self.distancia_recorrida = distancia
        if self.velocidad != 0:
            self.tiempo = distancia / self.velocidad
        return distancia * self.tarifa
        
            
class Parking:
    
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.nivel_ocupacion = {"estacionados": 0,
                                "porcentaje": 0}
        self.estacionados = []
        
    def estacionar(self, carro):
        if type(carro) != Carro:
            print("Error: Sólo se permite estacionar carros")
        elif carro in self.estacionados:
            print("Error: Ese carro ya está estacionado")
        elif self.nivel_ocupacion["estacionados"] == self.capacidad:
            print("Error: Estacionamiento lleno")
        else:
            self.estacionados.append(carro)
            self.nivel_ocupacion["estacionados"] += 1
            self.calcular()
            print("Auto estacionado")
            
    def sacar(self, carro):
        if carro not in self.estacionados:
            print("Error: Ese carro no está estacionado aquí")
        else:
            self.estacionados.remove(carro)
            self.nivel_ocupacion["estacionados"] -= 1
            self.calcular()
            print("Se sacó el auto")
            
    def calcular(self):
        self.nivel_ocupacion["porcentaje"] = self.nivel_ocupacion["estacionados"] / self.capacidad * 100
        
    def estatus(self):   # Para depurar
        print(self.estacionados)
        print(self.nivel_ocupacion)
        
    
    