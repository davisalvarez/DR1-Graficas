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

brick = Material(diffuse=color(0.8, 0.25, 0.25))
stone = Material(diffuse=color(0.4, 0.4, 0.4))
grass = Material(diffuse=color(0.5, 1, 0))

nieve = Material(diffuse=color(1, 1, 1))
wakanda = Material(diffuse=color(0, 0, 0))

#Botones
#img.scene.append(Esfera((0, -1., -4.5), 1, wakanda))
#img.scene.append(Esfera((0, 0, -4.5), 1, wakanda))
img.scene.append(Esfera((0, -1.4, -4.5), 0.3, wakanda))

#Cuerpo
#img.scene.append(Esfera((0, 1.6, -5), 0.6, nieve))
#img.scene.append(Esfera((0, 0.2, -5), 0.8, nieve))
img.scene.append(Esfera((0, -1.6, -5), 1, nieve))



img.mcqueenRender()



img.glFinish() #5
print("Codigo de prueba")






