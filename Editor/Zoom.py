# Handles All Zoom functions and convertions

# Global Control Variables
# pixels
win_width = 0
win_height = 0

max_x_unit = 0
max_y_unit = 0
# fictional unit convertion
x_factor = 0
y_factor = 0

zoom = 1

# Initialize Module
def init(w_width, w_height):
    global win_height, win_width, x_factor, y_factor, max_x_unit, max_y_unit
    win_width = w_width
    win_height = w_height
    max_x_unit = float(2*w_width/64)
    max_y_unit = float(2*w_height/64)
    x_factor = float(win_width/max_x_unit)
    y_factor = float(win_height/max_y_unit)
    print "Zoom Module Initialized %f %f" % (max_x_unit, max_y_unit)

def zoomIn():
    global zoom, win_height, win_width, max_x_unit, max_y_unit
    zoom = zoom + 0.5
    max_x_unit = float(2*win_width/(64*zoom))
    max_y_unit = float(2*win_height/(64*zoom))
    print ("max_X: %f  max_Y:%f" % (max_x_unit, max_y_unit))

def zoomOut():
    global zoom, win_height, win_width, max_x_unit, max_y_unit
    if zoom == 1:
        return
    zoom = zoom - 0.5
    max_x_unit = float(2*win_width/(64*zoom))
    max_y_unit = float(2*win_height/(64*zoom))
    print ("max_X: %f  max_Y:%f" % (max_x_unit, max_y_unit))

def pxXToUnit(pos):
    global win_width, zoom, x_factor
    offset = int((win_width - win_width/zoom)/2)
    return ((pos/zoom)+ offset)/x_factor

def pxYToUnit(pos):
    global win_height, zoom, y_factor
    offset = int((win_height - win_height/zoom)/2)
    return (((pos/zoom)+ offset)/y_factor)

def posXtoPixel(pos):
    global zoom, win_width, x_factor
    offset = int((win_width - win_width/zoom)/2)
    return (((pos * x_factor) - offset) * zoom)

def posYtoPixel(pos):
    global zoom, win_height, y_factor
    offset = int((win_height - win_height/zoom)/2)
    return (((pos * y_factor) - offset) * zoom)
    
def dimToPixels(dim):
    global zoom, x_factor
    return dim * x_factor * zoom

def getMaxX():
    return max_x_unit

def getMaxY():
    return max_y_unit