import pygame
import Node, Zoom

WHITE = (255,255,255)

class NetworkClass(object):

    __surface = None
    __nodeList = None

    def __init__(self, surface):
        self.__surface = surface
        self.__nodeList = []

        # Initialize Zoom Module
        Zoom.init(self.__surface.get_width(),self.__surface.get_height())

    def getSurface(self):
        return self.__surface

    def getNodeList(self):
        return self.__nodeList

    def getNode(self, id):
        for node in self.__nodeList:
            if node.id == id:
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

            if values["key"] == 3: # Right Mouse Button
                for node in self.__nodeList:
                    if node.clicked(values["mouse_pos"]):
                        node.select(values["key"])

        elif evtType == "BUTTONUP":
            if values["key"] == 1: # LEFT Mouse Button
                for node in self.__nodeList:
                    if node.isSelected():
                        node.released()

            if values["key"] == 3: # Right Mouse Button
                for node in self.__nodeList:
                    if node.clicked(values["mouse_pos"]):
                    #    print "RIGHT MOUSE UP FOR %d" % node.getId() 
                        n = node.isSelected() # n[0]: Boolean (isSelected)  n[1]: String (MouseKey)
                        #if (n[0]) and (n[1] == "RIGHT"):
							#self.deleteNode(node)

    def __keyboardHandler(self, evtType, values=None):
        if evtType == "KEYDOWN":
            if values["key"] == 273: # "K_UP"
                Zoom.zoomIn()
                for node in self.__nodeList:
                    node.updateCoords()

            elif values["key"] == 274: # "K_DOWN"
                Zoom.zoomOut()
                for node in self.__nodeList:
                    node.updateCoords()

            print ("Zoom:%f" %(Zoom.zoom))

    # Values ["key","mouse_pos"]
    def eventsHandler(self, source, eType, values=None):
        if source == "mouse":
            self.__mouseHandler(eType,values)
        elif source == "keyboard":
            self.__keyboardHandler(eType,values)
        else:
            print "Unknown input source"
            
      
