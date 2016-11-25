import pygame
import Node, UnitConv

WHITE = (255,255,255)

class NetworkClass(object):

    __surface = None
    __nodeList = None

    __corner = None
    __width = None
    __windowRatio = None

    __mouseLastPos = None


    def __init__(self, surface, width=30, corner=(-10,-10)):
        self.__surface = surface
        self.__nodeList = []

        self.__corner = corner
        self.__width = width
        self.__windowRatio = self.__surface.get_width()/self.__surface.get_height()
        height = width * self.__windowRatio

        UnitConv.update(surface,width,height,corner)

    def getSurface(self):
        return self.__surface

    def getNodeList(self):
        return self.__nodeList

    def getNode(self, id):
        for node in self.__nodeList:
            if node.getId() == id:
                return node
        return -1

    def addNode(self):
        self.__nodeList.append(Node.NodeClass())

    def deleteNode(self, node):
        self.__nodeList.remove(node)

    def deleteSelectedNodes(self):
        self.__nodeList[:] = [node for node in self.__nodeList if not node.isSelected()[0]]

    def refresh(self):
        self.__surface.fill(WHITE)
        for node in self.__nodeList:
            node.draw(self.__surface)

    def procNetwork(self, mouse_pos):
        if (self.__mouseLastPos != None):
            # Pan Mode on
            # print "Dentro IF C x:%f y:%f" % (self.__corner)
            mouse_Unit = UnitConv.pxToUnit(mouse_pos)
            mouseDelta = (mouse_Unit[0] - self.__mouseLastPos[0], mouse_Unit[1] - self.__mouseLastPos[1])
            self.__corner = (self.__corner[0] - mouseDelta[0] , self.__corner[1] - mouseDelta[1] )
            height = self.__width * self.__windowRatio
            UnitConv.update(self.__surface,self.__width,height,self.__corner)
            for node in self.__nodeList:
                node.updateCoords()
        else:
            for node in self.__nodeList:
                n = node.isSelected() # n[0]: Boolean (isSelected)  n[1]: String (MouseKey)
                if (n[0]) and (n[1] == "LEFT"):
                    node.followCursor(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.eventsHandler("mouse","BUTTONDOWN", values={"key":event.button,"mouse_pos":mouse_pos})
            elif event.type == pygame.MOUSEBUTTONUP:
                self.eventsHandler("mouse","BUTTONUP"  , values={"key":event.button,"mouse_pos":mouse_pos})
            elif event.type == pygame.KEYDOWN:
                self.eventsHandler("keyboard","KEYDOWN", values={"key":event.key,"mouse_pos":mouse_pos})
            elif event.type == pygame.KEYUP:
                self.eventsHandler("keyboard","KEYUP"  , values={"key":event.key,"mouse_pos":mouse_pos})

    def __mouseHandler(self, evtType, values=None):
        if values == None:
            return # Something went wrong...
        if evtType == "BUTTONDOWN":
            if values["key"] == 1: # LEFT Mouse Button
                lastNode = None
                for node in self.__nodeList:
                  #  print node.clicked(values["mouse_pos"])
                    if node.clicked(values["mouse_pos"]):
                        lastNode = node
                if (lastNode != None):    
                    self.__nodeList.append(lastNode)
                    self.__nodeList.remove(lastNode)
                    lastNode.calcOffset(values["mouse_pos"])
                    lastNode.select(values["key"])

            elif values["key"] == 2: # MIDDLE Mouse Button
                print "Apertou C x:%f y:%f" % (self.__corner)
                lastNode = None
                for node in self.__nodeList:
                  #  print node.clicked(values["mouse_pos"])
                    if node.clicked(values["mouse_pos"]):
                        lastNode = node
                if (lastNode == None):
                    # Drag background
                    self.__mouseLastPos = UnitConv.pxToUnit(values["mouse_pos"])
                    #update coords
                else:
                    print "MIDDLE Mouse on %d" % lastNode.getId()

            elif values["key"] == 3: # Right Mouse Button
                for node in self.__nodeList:
                    if node.clicked(values["mouse_pos"]):
                        node.select(values["key"])

        elif evtType == "BUTTONUP":
            if values["key"] == 1: # LEFT Mouse Button
                for node in self.__nodeList:
                    if node.isSelected():
                        node.released()

            elif values["key"] == 2: # MIDDLE Mouse Button
                self.__mouseLastPos = None

            elif values["key"] == 3: # Right Mouse Button
                for node in self.__nodeList:
                    if node.clicked(values["mouse_pos"]):
                    #    print "RIGHT MOUSE UP FOR %d" % node.getId() 
                        n = node.isSelected() # n[0]: Boolean (isSelected)  n[1]: String (MouseKey)
                        #if (n[0]) and (n[1] == "RIGHT"):
							#self.deleteNode(node)

    def __keyboardHandler(self, evtType, values=None):
        if evtType == "KEYDOWN":
            if values["key"] == 273: # "K_UP"
                self.__width = self.__width * 0.5
                height = self.__width * self.__windowRatio
                self.__corner = (self.__corner[0]+(self.__width/2),self.__corner[1]+(height/2))
                UnitConv.update(self.__surface,self.__width,height,self.__corner)
                for node in self.__nodeList:
                    node.updateCoords()

            elif values["key"] == 274: # "K_DOWN"
                self.__width = self.__width * 2
                height = self.__width * self.__windowRatio
                self.__corner = (self.__corner[0]-(self.__width/4),self.__corner[1]-(height/4))
                UnitConv.update(self.__surface,self.__width,height,self.__corner)
                for node in self.__nodeList:
                    node.updateCoords()


    # Values ["key","mouse_pos"]
    def eventsHandler(self, source, eType, values=None):
        if source == "mouse":
            self.__mouseHandler(eType,values)
        elif source == "keyboard":
            self.__keyboardHandler(eType,values)
        else:
            print "Unknown input source"