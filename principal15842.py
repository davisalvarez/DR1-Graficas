"""
UVG
GRAFICAS POR COMPUTADORA - seccion 20

Davis Alvarez - 15842

"""
from render import *
from ModeloOBJ import *
from shader import *
from Esfera import *

ancho = 600
alto = 600

img = render(ancho, alto)

img.glInit()
img.glClearColor(0.5,1,0.36)
#img.glViewport(200,100,600,300)
img.glClear()

#______________________________

nieve = Material(diffuse=color(1, 1, 1))
wakanda = Material(diffuse=color(0, 0, 0))
zanahoria = Material(diffuse=color(1, 0.26, 0))
cielo = Material(diffuse=color(0.53,0.81,0.92))

#Cuerpo
img.scene.append(Esfera((0, 10, -31), 4, nieve))
img.scene.append(Esfera((0, 2, -30), 5, nieve))
img.scene.append(Esfera((0, -8, -30), 7, nieve))

#Cara
#img.scene.append(Esfera((0, -1, -4.5), 0.25, wakanda))

#Botones
img.scene.append(Esfera((0, 1.5, -25), 1, wakanda))
img.scene.append(Esfera((0, -1.8, -25), 1.2, wakanda))
img.scene.append(Esfera((0, -7, -25), 2.3, wakanda))

img.mcqueenRender()


img.glFinish() #5
print("Codigo de prueba")






