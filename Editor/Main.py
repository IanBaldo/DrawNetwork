import pygame, sys
from pygame import mouse
from pygame.locals import *
import Node
import Zoom

# Window
window_dimensions = window_width, window_height = (800,600)
DISPLAYsurf = pygame.display.set_mode(window_dimensions)
# Window Caption
pygame.display.set_caption("Editor")

# Initializes pygame
pygame.init()
# Initialize Zoom Module
Zoom.init(window_width,window_height)

# Clock
clock = pygame.time.Clock()

# Colors
LIME = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

# Node list
nodeList = []
for i in range(0,60):
    nodeList.append(Node.NodeClass())



# Main Loop
while True:
    DISPLAYsurf.fill(WHITE)

    for node in nodeList:
        node.draw(DISPLAYsurf)

    for node in nodeList:
        if node.isSelected():
            mouse_pos = mouse.get_pos()
            node.followCursor(mouse_pos)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            for node in nodeList:
                node.clicked(mouse_pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            for node in nodeList:
                if node.isSelected():
                    node.released()

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