# Handles All Zoom functions and convertions

# Global Control Variables
# pixels
win_width = 0
win_height = 0
# fictional unit convertion
x_factor = 0
y_factor = 0

zoom = 1

# Initialize Module
def init(w_width, w_height, max_x_unit, max_y_unit):
    global win_height, win_width, x_factor, y_factor
    win_width = w_width
    win_height = w_height
    x_factor = int(win_width/max_x_unit)
    y_factor = int(win_height/max_y_unit)
    print "Zoom Module Initialized"

def zoomIn():
    global zoom
    zoom = zoom + 0.5

def zoomOut():
    global zoom
    if zoom == 0.5:
        return
    zoom = zoom - 0.5

def pxXToUnit(pos):
    return pos/x_factor

def pxYToUnit(pos):
    return pos/y_factor

def posXtoPixel(pos):
    global zoom
    if zoom == 1:
        offset = 0
    else:
        offset = int((win_width - win_width/zoom)/2)
    return (((pos * x_factor) - offset) * zoom)

def posYtoPixel(pos):
    global zoom
    if zoom == 1:
        offset = 0
    else:
        offset = int((win_height - win_height/zoom)/2)
    return (((pos * y_factor) - offset) * zoom)
    
def dimToPixels(dim):
    global zoom
    return dim * x_factor * zoom