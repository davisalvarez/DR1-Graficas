
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

        L = mySubtract(self.centro, orig)
        tca = dotProduct(L, dir)
        l = magnitudVector(L)
        d = (l**2 - tca**2) ** 0.5
        if d > self.radio:
            return None

        thc = (self.radio ** 2 - d**2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None

        return Intersect(distance = t0)