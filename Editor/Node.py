import pygame
import Zoom

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

class NodeClass(object):
    __id = 0
    __name = ""
    __color = BLACK
    # Fictional Unit Coords
    __unitX = 0
    __unitY = 0
    # Fictional Unit Size
    __width = 8
    __height = 5

    # Pixel Coords
    __pxX = 0
    __pxY = 0
    __pxWidth = 0
    __pxHeight = 0

    # Text Related Variables
    __textSurf = None
    __textObj = None

    # Border Thickness
    __border = 2

    __selected = False

    def __init__(self,id,x,y):
        self.__name = "Mote "+str(id)
        self.__id = id
        self.__color = BLACK
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
    
    def isSelected(self):
        return self.__selected

    def followCursor(self,mCoords):
        self.__unitX = Zoom.pxXToUnit(mCoords[0])
        self.__unitY = Zoom.pxYToUnit(mCoords[1])
        self.__pxX = Zoom.posXtoPixel(self.__unitX)
        self.__pxY = Zoom.posYtoPixel(self.__unitY)
        print ("X:%d  Y:%d" % (self.__unitX, self.__unitY))

    def clicked(self,mouse_position):
        if mouse_position[0] > self.__pxX and mouse_position[0] < (self.__pxX + self.__pxWidth):
            if mouse_position[1] > self.__pxY and mouse_position[1] < (self.__pxY + self.__pxHeight):
                self.__selected = True
                self.__color = BLUE
                print "Node %d selected" % self.__id

    def released(self):
        self.__selected = False
        self.__color = BLACK

    def updateCoords(self):
        if not self.__selected:
            self.__pxX = Zoom.posXtoPixel(self.__unitX)
            self.__pxY = Zoom.posYtoPixel(self.__unitY)
            self.__pxWidth = Zoom.dimToPixels(self.__width)
            self.__pxHeight = Zoom.dimToPixels(self.__height)

    def draw(self, surface):
        pygame.draw.rect(surface,self.__color,(self.__pxX,self.__pxY,self.__pxWidth,self.__pxHeight),self.__border)
        pygame.draw.rect(surface,WHITE,(self.__pxX + self.__border,self.__pxY + self.__border,self.__pxWidth - self.__border,self.__pxHeight - self.__border),0)
        self.__textObj.center = (self.__pxX+int(self.__pxWidth/2),self.__pxY+int(self.__pxHeight/8))
        surface.blit(self.__textSurf, self.__textObj)
