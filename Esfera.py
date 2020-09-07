
import numpy as np
from utilidades import *


WHITE = color(1,1,1)

class Material(object):
    def __init__(self, diffuse = WHITE):
        self.diffuse = diffuse

class Intersect(object):
    def __init__(self, distance):
        self.distance = distance

class Esfera(object):
    def __init__(self, centro, radio, material):
        self.centro = centro
        self.radio = radio
        self.material = material

    def ray_intersect(self, orig, dir):
        # Regresa falso o verdadero si hace interseccion con una esfera

        # Formula para un punto en un rayo
        # t es igual a la distancia en el rayo
        # P = O + tD
        # P0 = O + t0 * D
        # P1 = O + t1 * D
        #d va a ser la magnitud de un vector que es
        #perpendicular entre el rayo y el centro de la esfera
        # d > radio, el rayo no intersecta
        #tca es el vector que va del orign al punto perpendicular al centro

        L = np.subtract(self.centro, orig)
        tca = np.dot(L, dir)
        l = np.linalg.norm(L) # magnitud de L
        d = (l**2 - tca**2) ** 0.5
        if d > self.radio:
            return None

        # thc es la distancia de P1 al punto perpendicular al centro
        thc = (self.radio ** 2 - d**2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0: # t0 tiene el valor de t1
            return None

        return Intersect(distance = t0)