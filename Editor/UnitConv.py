# Handles All Zoom functions and convertions

# pixels
pxCorner = (0,0)

# fictional unit convertion
x_factor = 0
y_factor = 0

# zoom = 1


def update(surface,w_width, w_height, corner):
    global x_factor, y_factor, pxCorner

    x_factor = float(surface.get_width() / w_width)
    y_factor = float(surface.get_height() / w_height)

    pxCorner = (corner[0] * x_factor, corner[1] * y_factor)

def unitToPx(unit):
    global x_factor, y_factor, pxCorner
    pxX = int((unit[0]*x_factor)-pxCorner[0])
    pxY = int((unit[1]*y_factor)-pxCorner[1])
    return (pxX,pxY)

def pxToUnit(px):
    global x_factor, y_factor, pxCorner
    unitX = float((px[0]+pxCorner[0])/x_factor)
    unitY = float((px[1]+pxCorner[1])/y_factor)
    return (unitX,unitY)

def unitDimToPx(dim):
    global x_factor,y_factor
    return (dim[0]*x_factor,dim[1]*y_factor)