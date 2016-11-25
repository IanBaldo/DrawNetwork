import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

class BtnClass(object):
    __surface = None
    __color = None

    __height = 1
    __width = 0

    __posX = None
    __posY = None

    # Text Related Variables
    __text = "Button"
    __textSurf = None
    __textObj = None

    __func = None

    def __init__(self, text, posx, posy, width, height, function, color):
        self.__text = text
        self.__posX = posx
        self.__posY = posy
        self.__width = width
        self.__height = height
        self.__func = function
        self.__color = color
        # Text
        fontObj = pygame.font.Font('freesansbold.ttf', 10)
        self.__textSurf = fontObj.render(self.__text, True, WHITE, color)
        self.__textObj = self.__textSurf.get_rect()

    def draw(self,surface):
        pygame.draw.rect(surface,self.__color,(self.__posX,self.__posY,self.__width,self.__height),0)
        self.__textObj.center = (self.__posX+int(self.__width/2),self.__posY+int(self.__height/2))
        surface.blit(self.__textSurf, self.__textObj)

    def clicked(self, mouse_position):
        if mouse_position[0] > self.__posX and mouse_position[0] < (self.__posX + self.__width):
            if mouse_position[1] > self.__posY and mouse_position[1] < (self.__posY + self.__height):               
                self.__func()
                return True
        return False

    