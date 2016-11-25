import pygame, sys
from pygame import mouse
from pygame.locals import *
import Network, Menu

# Window
window_dimensions = window_width, window_height = (900,600)
MAINsurf = pygame.display.set_mode(window_dimensions)

menuWidth = 100

# Initializes pygame
pygame.init()

NetworkObj = Network.NetworkClass(MAINsurf.subsurface((menuWidth,0,(window_width-menuWidth),window_height)))
MenuObj = Menu.MenuClass(MAINsurf.subsurface((0,0,menuWidth,window_height)), NetworkObj)


# Window Caption
pygame.display.set_caption("Editor")


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
        return MenuObj.getSurface(), mouse_pos
    else:
        # Clicked inside of the DISPLAYsurf
        return NetworkObj.getSurface(), (mouse_pos[0]-displayCoord[0],mouse_pos[1])



# Main Loop
while True:
    
    CURRENTsurf,mouse_pos = surfaceClick(mouse.get_pos())
    if (CURRENTsurf == NetworkObj.getSurface()):
        NetworkObj.procNetwork(mouse_pos)
    #    print "Networksurf"
    else:
        MenuObj.procMenu(mouse_pos)

    NetworkObj.refresh()
    MenuObj.refresh()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
            
    # Updates the display
    pygame.display.update()
    # Limits FPS to 60
    clock.tick(60)