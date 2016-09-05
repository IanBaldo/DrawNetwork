import pygame, sys
from pygame import mouse
from pygame.locals import *
import Network

# Window
window_dimensions = window_width, window_height = (800,600)
MAINsurf = pygame.display.set_mode(window_dimensions)

menuWidth = 100

NetworkObj = Network.NetworkClass(MAINsurf.subsurface((menuWidth,0,(window_width-menuWidth),window_height)))

MENUsurf = MAINsurf.subsurface((0,0,menuWidth,window_height))

# Window Caption
pygame.display.set_caption("Editor")

# Initializes pygame
pygame.init()


# Clock
clock = pygame.time.Clock()

# Colors
LIME = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (210,210,210)
BLUE = (0,0,255)


def surfaceClick(mouse_pos):
    displayCoord = NetworkObj.getSurface().get_abs_offset()
    if mouse_pos[0] < displayCoord[0]:
        # Clicked outside of the DISPLAYsurf
        return MENUsurf, mouse_pos
    else:
        # Clicked inside of the DISPLAYsurf
        return NetworkObj.getSurface(), (mouse_pos[0]-displayCoord[0],mouse_pos[1])


NetworkObj.addNode()

# Main Loop
while True:
    
    MENUsurf.fill(GREY)

    CURRENTsurf,mouse_pos = surfaceClick(mouse.get_pos())
    if (CURRENTsurf == NetworkObj.getSurface()):
        NetworkObj.procNetwork(mouse_pos)
    #    print "Networksurf"
    else:
        print "MENUsurf"

    NetworkObj.refresh()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            NetworkObj.eventsHandler("mouse","BUTTONDOWN", values={"key":event.button,"mouse_pos":mouse_pos})
        elif event.type == pygame.MOUSEBUTTONUP:
            NetworkObj.eventsHandler("mouse","BUTTONUP"  , values={"key":event.button,"mouse_pos":mouse_pos})
        elif event.type == pygame.KEYDOWN:
            NetworkObj.eventsHandler("keyboard","KEYDOWN", values={"key":event.key,"mouse_pos":mouse_pos})
        elif event.type == pygame.KEYUP:
            NetworkObj.eventsHandler("keyboard","KEYUP"  , values={"key":event.key,"mouse_pos":mouse_pos})
            
    # Updates the display
    pygame.display.update()
    # Limits FPS to 60
    clock.tick(60)