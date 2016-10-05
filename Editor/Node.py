import pygame
import UnitConv

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
    __mKey = None
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
        self.__name = str(idPool)
        self.__id = idPool
        self.__color = BLACK
        self.__unitX = nextX
        self.__unitY = nextY

        px = UnitConv.unitToPx((self.__unitX, self.__unitY))
        self.__pxX = px[0]
        self.__pxY = px[1]
        
        dimPx = UnitConv.unitDimToPx((nodeWidth,nodeHeight))
        self.__pxWidth = dimPx[0]
        self.__pxHeight = dimPx[1]

        fontSizePx = UnitConv.unitDimToPx((0,0.5))
        fontObj = pygame.font.Font('freesansbold.ttf',int(fontSizePx[1]))
        self.__textSurf = fontObj.render(self.__name, True, BLACK, WHITE)
        self.__textObj = self.__textSurf.get_rect()
        # Increment idPool
        idPool += 1

        

    def getId(self):
        return self.__id
    
    def isSelected(self):
        return (self.__selected,self.__mKey)

    def select(self, mKey):
        if mKey == 1:
            self.__mKey = "LEFT"
        elif mKey == 2:
            self.__mKey = "MIDDLE"
        elif mKey == 3:
            self.__mKey = "RIGHT"

        self.__selected = True
        self.__color = BLUE
       # print "Node %d selected with %s mouse key" % (self.__id, self.__mKey)

    # Drag-n-Drop Functions
    def followCursor(self,mouse_pos):
        print mouse_pos[0], self.__pxX, self.__offsetX
        unit = UnitConv.pxToUnit((mouse_pos[0]-self.__offsetX, mouse_pos[1]-self.__offsetY))
        self.__unitX = unit[0]
        self.__unitY = unit[1]
        
        px = UnitConv.unitToPx((self.__unitX, self.__unitY))
        self.__pxX = px[0]
        self.__pxY = px[1]
        print ("X:%d  Y:%d" % (self.__unitX, self.__unitY))

    # End Drag-n-Drop Functions

    def clicked(self,mouse_position):
        if mouse_position[0] > self.__pxX and mouse_position[0] < (self.__pxX + self.__pxWidth):
            if mouse_position[1] > self.__pxY and mouse_position[1] < (self.__pxY + self.__pxHeight):               
                return True
        return False

    def released(self):
        self.__selected = False
        self.__color = BLACK

    # Updates Coords
    def updateCoords(self):
        global nodeHeight, nodeWidth
        if not self.__selected:
            px = UnitConv.unitToPx((self.__unitX, self.__unitY))
            self.__pxX = px[0]
            self.__pxY = px[1]
            
            dimPx = UnitConv.unitDimToPx((nodeWidth,nodeHeight))
            self.__pxWidth = dimPx[0]
            self.__pxHeight = dimPx[1]

            fontSizePx = UnitConv.unitDimToPx((0,0.5))
            fontObj = pygame.font.Font('freesansbold.ttf',int(fontSizePx[1]))
            self.__textSurf = fontObj.render(self.__name, True, BLACK, WHITE)
            self.__textObj = self.__textSurf.get_rect()

    def calcOffset(self,mouse_pos):
        self.__offsetX = mouse_pos[0] - self.__pxX
        self.__offsetY = mouse_pos[1] - self.__pxY

    def draw(self, surface):
        pygame.draw.rect(surface,self.__color,(self.__pxX,self.__pxY,self.__pxWidth,self.__pxHeight),self.__border)
        pygame.draw.rect(surface,WHITE,(self.__pxX + self.__border,self.__pxY + self.__border,self.__pxWidth - self.__border,self.__pxHeight - self.__border),0)
        self.__textObj.center = (self.__pxX+int(self.__pxWidth/2),self.__pxY+int(self.__pxHeight/2))
        surface.blit(self.__textSurf, self.__textObj)
