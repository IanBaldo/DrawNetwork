import pygame
import UnitConv

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (230, 126, 34)
GREEN = (46, 204, 113)
Light_GREEN = (96, 254, 163)
Dark_GREEN = (6, 164, 73)
CARROT = (230, 126, 34)
ORANGE = (243, 156, 18)
RED = (192, 57, 43)


#Id Pool
idPool = 1
# Coords for the next node to be added
nextX = 0
nextY = 0

prevCorner = None

# Fictional Unit Size
nodeSize = 1
fontSize = nodeSize * 1
nodeWidth = float(nodeSize * 2.5)
nodeHeight = float(nodeSize * 2)

# Radio range
radioSpecs = [(10,99),(15,85),(20,60)]

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
    def __init__(self, corner, nodeData=None):
        global idPool, nodeWidth, nodeHeight, nextX, nextY, radioSpecs, prevCorner
        if  corner != prevCorner:
            prevCorner = corner
            nextX = 0
            nextY = 0

        if(nodeData):
            self.__name = nodeData['name']
            self.__id = nodeData['id']
            self.__unitX = nodeData['pos']['unitB'][0]
            self.__unitY = nodeData['pos']['unitB'][1]
            self.__radio = nodeData['radio']
        else:
            self.__name = str(idPool)
            self.__id = idPool
            self.__unitX = corner[0] + nextX
            self.__unitY = corner[1] + nextY
            self.__radio = radioSpecs
        
        self.__color = BLACK

        px = UnitConv.unitToPx((self.__unitX, self.__unitY))
        self.__pxX = px[0]
        self.__pxY = px[1]
        
        dimPx = UnitConv.unitDimToPx((nodeWidth,nodeHeight))
        self.__pxWidth = dimPx[0]
        self.__pxHeight = dimPx[1]

        fontSizePx = UnitConv.unitDimToPx((0,fontSize))
        fontObj = pygame.font.Font('freesansbold.ttf',int(fontSizePx[1]))
        self.__textSurf = fontObj.render(self.__name, True, BLACK, WHITE)
        self.__textObj = self.__textSurf.get_rect()
        # Increment idPool
        idPool += 1
        nextX += 0.2
        nextY += 0.2
        

    def getId(self):
        return self.__id

    def getPos(self):
        temp = {}
        temp['unitB'] = (self.__unitX, self.__unitY)
        temp['pixels'] = (self.__pxX, self.__pxY)
        return temp

    def getRadioRange(self):
        return self.__radio

    def getName(self):
        return self.__name
    
    def isSelected(self):
        return (self.__selected,self.__mKey)

    def select(self, mKey):
        if mKey == 1:
            self.__mKey = "LEFT"
        elif mKey == 2:
            self.__mKey = "MIDDLE"
        elif mKey == 3:
            self.__mKey = "RIGHT"
            if self.__selected:
                self.deselect()
                return

        self.__selected = True
        self.__color = CARROT
       # print "Node %d selected with %s mouse key" % (self.__id, self.__mKey)

    def deselect(self):
        self.__selected = False
        self.__color = BLACK

    # Drag-n-Drop Functions
    def followCursor(self,mouse_pos):
        #print mouse_pos[0], self.__pxX, self.__offsetX
        unit = UnitConv.pxToUnit((mouse_pos[0]-self.__offsetX, mouse_pos[1]-self.__offsetY))
        self.__unitX = unit[0]
        self.__unitY = unit[1]
        
        px = UnitConv.unitToPx((self.__unitX, self.__unitY))
        self.__pxX = px[0]
        self.__pxY = px[1]
        #print ("X:%d  Y:%d" % (self.__unitX, self.__unitY))

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
        # if not self.__selected:
        px = UnitConv.unitToPx((self.__unitX, self.__unitY))
        self.__pxX = px[0]
        self.__pxY = px[1]
        
        dimPx = UnitConv.unitDimToPx((nodeWidth,nodeHeight))
        self.__pxWidth = dimPx[0]
        self.__pxHeight = dimPx[1]


        fontSizePx = UnitConv.dimYtoPx(fontSize)
        fontObj = pygame.font.Font('freesansbold.ttf',int(fontSizePx))
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

    def drawRange(self, surface):
        pygame.draw.circle(surface,Light_GREEN,(self.__pxX+int(self.__pxWidth/2),self.__pxY+int(self.__pxHeight/2)),int(UnitConv.dimXtoPx(self.__radio[2][0])),0)
        pygame.draw.circle(surface,GREEN,(self.__pxX+int(self.__pxWidth/2),self.__pxY+int(self.__pxHeight/2)),int(UnitConv.dimXtoPx(self.__radio[1][0]) ) ,0)
        pygame.draw.circle(surface,Dark_GREEN,(self.__pxX+int(self.__pxWidth/2),self.__pxY+int(self.__pxHeight/2)),int(UnitConv.dimXtoPx(self.__radio[0][0])),0)