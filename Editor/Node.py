import pygame
import Zoom

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

class NodeClass(object):
    __id = 0
    __name = ""
    # Fictional Unit Coords
    __unitX = 0
    __unitY = 0
    # Fictional Unit Size
    __width = 15
    __height = 10

    # Pixel Coords
    __pxX = 0
    __pxY = 0
    __pxWidth = 0
    __pxHeight = 0

    __textSurf = None
    __textObj = None

    def __init__(self,id,x,y):
        self.__name = "Mote "+str(id)
        self.__id = id
        self.__unitX = x
        self.__unitY = y
        self.__pxX = Zoom.posXtoPixel(self.__unitX)
        self.__pxY = Zoom.posYtoPixel(self.__unitY)
        self.__pxWidth = Zoom.dimToPixels(self.__width)
        self.__pxHeight = Zoom.dimToPixels(self.__height)
        # Text
        fontObj = pygame.font.Font('freesansbold.ttf', 12)
        self.__textSurf = fontObj.render(self.__name, True, BLACK, WHITE)
        self.__textObj = self.__textSurf.get_rect()

    def getId(self):
        return self.__id

    def updateCoords(self):
        self.__pxX = Zoom.posXtoPixel(self.__unitX)
        self.__pxY = Zoom.posYtoPixel(self.__unitY)
        self.__pxWidth = Zoom.dimToPixels(self.__width)
        self.__pxHeight = Zoom.dimToPixels(self.__height)

    def draw(self, surface, color):
        rect = pygame.draw.rect(surface,color,(self.__pxX,self.__pxY,self.__pxWidth,self.__pxHeight),1)
        self.__textObj.center = (self.__pxX+int(self.__pxWidth/2),self.__pxY+int(self.__pxHeight/8))
        surface.blit(self.__textSurf, self.__textObj)
