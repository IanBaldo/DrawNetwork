import pygame, sys
from pygame import mouse
from pygame.locals import *
import Node
import Zoom

# Window
window_dimensions = window_width, window_height = (800,600)
MAINsurf = pygame.display.set_mode(window_dimensions)
DISPLAYsurf = MAINsurf.subsurface((100,0,(window_width-100),window_height))
MENUsurf = MAINsurf.subsurface((0,0,100,window_height))

# Window Caption
pygame.display.set_caption("Editor")

# Initializes pygame
pygame.init()
# Initialize Zoom Module
Zoom.init(DISPLAYsurf.get_width(),DISPLAYsurf.get_height())

# Clock
clock = pygame.time.Clock()

# Colors
LIME = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (210,210,210)
BLUE = (0,0,255)

# Node list
nodeList = []
for i in range(0,60):
    nodeList.append(Node.NodeClass())


def surfaceClick(mouse_pos):
    displayCoord = DISPLAYsurf.get_abs_offset()
    if mouse_pos[0] < displayCoord[0]:
        # Clicked outside of the DISPLAYsurf
        return MENUsurf, mouse_pos
    else:
        # Clicked inside of the DISPLAYsurf
        return DISPLAYsurf, (mouse_pos[0]-displayCoord[0],mouse_pos[1])


# Main Loop
while True:
    DISPLAYsurf.fill(WHITE)
    MENUsurf.fill(GREY)

    for node in nodeList:
        node.draw(DISPLAYsurf)

    for node in nodeList:
        n = node.isSelected() # n[0]: Boolean (isSelected)  n[1]: String (MouseKey)
        if (n[0]) and (n[1] == "LEFT"):
            surface ,mouse_pos = surfaceClick(mouse.get_pos())
            if surface == DISPLAYsurf:
                node.followCursor(mouse_pos)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
         #   mouse_pos = mouse.get_pos()
            xxxSurf,mouse_pos = surfaceClick(mouse.get_pos())
            
            print pygame.mouse.get_pressed()
            if event.button == 1: # Left Mouse Key
                for node in nodeList:
                    if node.clicked(mouse_pos):
                        node.select(event.button)
                        break
            
            if event.button == 3: # Right Mouse Key
                for node in nodeList:
                    if node.clicked(mouse_pos):
                        node.select(event.button)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # Left Mouse Key
                for node in nodeList:
                    if node.isSelected():
                        node.released()

            if event.button == 3: # Right Mouse Key
                mouse_pos = mouse.get_pos()
                for node in nodeList:
                    if node.clicked(mouse_pos):
                        print "RIGHT MOUSE UP FOR %d" % node.getId() 
                        n = node.isSelected() # n[0]: Boolean (isSelected)  n[1]: String (MouseKey)
                        if (n[0]) and (n[1] == "RIGHT"):
                            nodeList.remove(node)
                        

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
            
    # Updates the display
    pygame.display.update()
    # Limits FPS to 60
    clock.tick(60)