from utilidades import *
from ModeloOBJ import *
from Poligono import *
from numpy import cos, sin, tan
import numpy as np

BLACK = color(0,0,0)
WHITE = color(1,1,1)
YELLOW = color(1,1,0)

class render(object):

    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        self.default_color = BLACK
        self.vetex_color = WHITE
        self.pixels = []
        self.zBuffer = []
        self.xVP=0
        self.yVP = 0
        self.widthVP = 0
        self.heightVP = 0

        self.fov = 60
        self.scene = []
        self.camPosition = (0,0,0)

        self.glCreateWindow(width, height)

    def glInit(self):
        self.iniciarFramebuffer(BLACK)

    def glCreateWindow(self, w, h):
        self.width = w
        self.height = h
        self.iniciarFramebuffer(BLACK)
        self.glViewport(0, 0, w, h)

    def iniciarFramebuffer(self, _color):
        self.pixels = []
        for y in range(self.height):
            linea=[]
            for x in range(self.width):
                linea.append(_color)
            self.pixels.append(linea)


    # Z-Buffer A.K.A  buffer de profundidad
    def iniciarZbuffer(self):
        self.zBuffer = []
        for y in range(self.height):
            linea = []
            for x in range(self.width):
                linea.append(float('inf'))
            self.zBuffer.append(linea)

    def glViewport(self, x, y, width, height):
        self.xVP= x
        self.yVP = y
        self.widthVP = width
        self.heightVP = height

    def glClear(self):
        self.iniciarFramebuffer(self.default_color)
        self.iniciarZbuffer()


    def glClearColor(self, r, g, b):
        self.default_color=color(r, g, b)

    def glVertex(self, x, y):
        #pos X
        xIMG = self.xVP + (x+1)* (self.widthVP/2)
        #pos Y
        yIMG = self.yVP + (y+1)*(self.heightVP / 2)

        self.pintarPixelIMG(round(xIMG),round(yIMG))


    def pintarPixelIMG(self, x, y, _color = None):

        if x < self.xVP or x >= self.xVP + self.widthVP or y < self.yVP or y >= self.yVP + self.heightVP:
            return

        if x >= self.width or x < 0 or y >= self.height or y < 0:
            return
        try:
            self.pixels[y][x] = _color or color(self.vetex_color)
        except:
            pass

    def glColor(self, r, g, b):
        self.vetex_color=color(r, g, b)

    def glFinish(self):
        self.generar("gotham.bmp")
        #self.glZBuffer("profundidad.bmp")

    def glZBuffer(self, filename):

        imagen = open(filename, 'wb')

        #BITMAPFILEHEADER
        #14 Bytes

        imagen.write(bytes('B'.encode('ascii')))
        imagen.write(bytes('M'.encode('ascii')))
        imagen.write(dword(14+40+ self.width * self.height * 3))  #4
        imagen.write(word(0)) #2
        imagen.write(word(0)) #2
        imagen.write(dword(14+40)) #4

        #BITMAPINFOHEADER
        #40 Bytes

        imagen.write(dword(40)) #4
        imagen.write(dword(self.width)) #4
        imagen.write(dword(self.height)) #4
        imagen.write(word(1)) #2
        imagen.write(word(24)) # 2
        imagen.write(dword(0)) # 4
        imagen.write(dword(self.width * self.height * 3))  # 4

        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4

        # Minimo y el maximo
        minZ = float('inf')
        maxZ = -float('inf')
        for x in range(self.height):
            for y in range(self.width):
                if self.zBuffer[x][y] != float('inf'):
                    if self.zBuffer[x][y] < minZ:
                        minZ = self.zBuffer[x][y]

                    if self.zBuffer[x][y] > maxZ:
                        maxZ = self.zBuffer[x][y]

        for x in range(self.height):
            for y in range(self.width):
                depth = self.zBuffer[x][y]
                if depth == float('inf'):
                    depth = minZ
                depth = (depth - minZ) / (maxZ - minZ)
                imagen.write(color(depth,depth,depth))

        imagen.close()

    def generar(self, filename):

        imagen = open(filename, 'wb')

        #BITMAPFILEHEADER
        #14 Bytes

        imagen.write(bytes('B'.encode('ascii')))
        imagen.write(bytes('M'.encode('ascii')))
        imagen.write(dword(14+40+ self.width * self.height * 3))  #4
        imagen.write(word(0)) #2
        imagen.write(word(0)) #2
        imagen.write(dword(14+40)) #4

        #BITMAPINFOHEADER
        #40 Bytes

        imagen.write(dword(40)) #4
        imagen.write(dword(self.width)) #4
        imagen.write(dword(self.height)) #4
        imagen.write(word(1)) #2
        imagen.write(word(24)) # 2
        imagen.write(dword(0)) # 4
        imagen.write(dword(self.width * self.height * 3))  # 4

        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4

        #self.pixels[11][11]=color(162,0,255)

        for y in range(self.height):
            for x in range(self.width):
                imagen.write(self.pixels[y][x])

        imagen.close()

    #Algoritmo de Ray Tracing
    def mcqueenRender(self):
        #Recorremos cada uno de los pixeles de la IMG
        for y in range(self.height):
            for x in range(self.width):

                Px = 2 * ( (x+0.5) / self.width) - 1
                Py = 2 * ( (y+0.5) / self.height) - 1

                #FOV(angulo de vision), asumiendo que el near plane esta a 1 unidad de la camara
                t = tan( (self.fov * np.pi / 180) / 2 )
                r = t * self.width / self.height
                Px *= r
                Py *= t

                #Nuestra camara siempre esta viendo hacia -Z
                direction = [Px, Py, -1]
                #direction = direction / np.linalg.norm(direction)
                direction = normalizarVector(direction)
                material = None

                for obj in self.scene:
                    intersect = obj.ray_intersect(self.camPosition, direction)
                    if intersect is not None:
                        if intersect.distance < self.zBuffer[y][x]:
                            self.zBuffer[y][x] = intersect.distance
                            material = obj.material

                if material is not None:
                    self.pintarPixelIMG(x, y, material.diffuse)

