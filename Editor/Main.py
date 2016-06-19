import pygame, sys
from pygame.locals import *
import Node
import Zoom

# Window
window_dimensions = window_width, window_height = (640,640)
DISPLAYsurf = pygame.display.set_mode(window_dimensions)
# Window Caption
pygame.display.set_caption("Editor")

# Initializes pygame
pygame.init()

# Initialize Zoom Module
Zoom.init(window_width,window_height,100,100)


# Colors
LIME = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

# Node list
nodeList = []
nodeList.append(Node.NodeClass(1,50,50))
nodeList.append(Node.NodeClass(2,0,0))
nodeList.append(Node.NodeClass(3,10,40))
nodeList.append(Node.NodeClass(4,100,100))


# Main Loop
while True:
    DISPLAYsurf.fill(WHITE)

    for node in nodeList:
        node.draw(DISPLAYsurf,BLUE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Zoom.zoomIn()
                for node in nodeList:
                    node.updateCoords()
            elif event.key == pygame.K_DOWN:
                Zoom.zoomOut()
                for node in nodeList:
                    node.updateCoords()
            print ("Zoom:%f" %(Zoom.zoom))
           # print ("X:%d ; Y:%d ; Width:%d ; Height:%d" % ())
    pygame.display.update()