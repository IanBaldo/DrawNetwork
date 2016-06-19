import pygame
import Zoom

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

#Id Pool
idPool = 1
# Coords for the next node to be added
nextX = 0
nextY = 0

# Fictional Unit Size
nodeWidth = float(1.5)
nodeHeight = float(1)

class NodeClass(object):
    __id = 0
    __name = ""
    __color = BLACK
    # Fictional Unit Coords
    __unitX = 0
    __unitY = 0

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

    # Constructor
    def __init__(self):
        global idPool, nodeWidth, nodeHeight, nextX, nextY
        self.__name = "Mote "+str(idPool)
        self.__id = idPool
        self.__color = BLACK
        self.__unitX = nextX
        self.__unitY = nextY
        self.__pxX = Zoom.posXtoPixel(self.__unitX)
        self.__pxY = Zoom.posYtoPixel(self.__unitY)
        self.__pxWidth = Zoom.dimToPixels(nodeWidth)
        self.__pxHeight = Zoom.dimToPixels(nodeHeight)
        # Text
        fontObj = pygame.font.Font('freesansbold.ttf', 12)
        self.__textSurf = fontObj.render(self.__name, True, BLACK, WHITE)
        self.__textObj = self.__textSurf.get_rect()
        # Increment idPool
        idPool += 1

        tempX = nextX + nodeWidth + 1
        if tempX < Zoom.getMaxX():
            global nextX, nodeWidth
            nextX = nextX + nodeWidth + 1
        else:
            global nextY, nodeHeight
            nextY = nextY + nodeHeight + 1
            nextX = 0

    def getId(self):
        return self.__id
    
    def isSelected(self):
        return self.__selected

    # Drag-n-Drop Functions
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
    # End Drag-n-Drop Functions
    

    def updateCoords(self):
        global nodeHeight, nodeWidth
        if not self.__selected:
            self.__pxX = Zoom.posXtoPixel(self.__unitX)
            self.__pxY = Zoom.posYtoPixel(self.__unitY)
            self.__pxWidth = Zoom.dimToPixels(nodeWidth)
            self.__pxHeight = Zoom.dimToPixels(nodeHeight)

    def draw(self, surface):
        pygame.draw.rect(surface,self.__color,(self.__pxX,self.__pxY,self.__pxWidth,self.__pxHeight),self.__border)
        pygame.draw.rect(surface,WHITE,(self.__pxX + self.__border,self.__pxY + self.__border,self.__pxWidth - self.__border,self.__pxHeight - self.__border),0)
        self.__textObj.center = (self.__pxX+int(self.__pxWidth/2),self.__pxY+int(self.__pxHeight/8))
        surface.blit(self.__textSurf, self.__textObj)