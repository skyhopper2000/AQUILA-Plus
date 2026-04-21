import pygame

pygame.init()
DEFAULT_FONT = pygame.font.SysFont('lucidaconsole', 16)

class App():
    def __init__(self, 
                 icon : pygame.Surface, 
                 name : str = 'Canvas', 
                 screenWidth : int = 400, 
                 screenHeight : int = 400,
                 fps : int = 30,
                 background : tuple[int, int, int] = (0,0,0)
                 ): 
        self.icon = icon
        self.name = name
        self.width = screenWidth
        self.height = screenHeight
        self.fps = fps
        self.background = background
        self.group = pygame.sprite.Group()


class Item(pygame.sprite.Sprite):
    def __init__(self, x : int, y : int, width : int, height : int):
        """
        Simple base class for visual objects,
        
        :param x: leftmost pixel
        :param y: rightmost pixel
        :param width: width (right from the x) of object in pixels
        :param height: height (down from the y) of the object in pixels
        """
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, surface):
        """
        Abstract mmethod that all children classes should have,
        should draw item to surface
        """
        pass

class Graphic(Item):

    def __init__(self, x : int, y : int, width : int, height : int,
                 sprite : pygame.Surface):
        """
        An base level implementation of Item for static visuals
        :param sprite: the sprite to be displayed
        """
        super().__init__(x, y, width, height)
        if sprite.get_rect() != self.rect:
            self.sprite = pygame.transform.scale(sprite, (width, height))
        else:
            self.sprite = sprite

    def draw(self, surface : pygame.Surface):
        surface.blit(self.sprite, self.rect)

class Button(Item):

    def __init__(self, x : int, y : int, width : int, height : int,
                sprites : tuple[pygame.Surface, pygame.Surface, pygame.Surface],
                label : str = "", font : pygame.Font = DEFAULT_FONT, labelColor : tuple[int, int, int] = (0,0,0)):
        """
        Pressable button class, takes Item arguments and additional arguments

        :param sprites: a 3-tuple of images in (idle, hovered, active) order
        :param label: text for the button
        :param font: a loaded pygame font for the label
        """
        
        super().__init__(x, y, width, height)

        self.idleSprite, self.hoverSprite, self.activeSprite = sprites
        self.label = label
        self.font = font
        self.labelColor = labelColor
        self.isHovered = False
        self.isPressed = False

    def draw(self, surface : pygame.Surface):
        """Draw a rectangle button with hover / pressed visual states."""
        drawnSprite = self.idleSprite
        if self.isPressed:
            drawnSprite = self.activeSprite
        elif self.isHovered:
            drawnSprite = self.hoverSprite
        surface.blit(drawnSprite, self.rect.topleft)
        
        if self.label != "":
            text_surface = self.font.render(self.label, True, self.labelColor)
            text_rect    = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def update(self, mousePos : tuple[int, int], mouseIsPressed : bool):
        """
        Updates the model of the Button Object
        Takes two controller arguments
        mousePos: the coordinates (x,y) of the mouse
        mousIsPressed: the status of the mouse
        """
        if self.rect.collidepoint(mousePos):
            self.isHovered = True
            if mouseIsPressed:
                self.isPressed = True
            else:
                self.isPressed = False
        else:
            self.isHovered = False
    
    def setLabel(self, text : str):
        self.label = text
        

class Timer(Item):
    def __init__(self,x : int, y : int, width : int, height : int,
                 initialValue : float, font : pygame.Font, color : tuple[int, int, int] = (0, 0, 0)):
        """
        Creates a model object which represents a timer.
        """
        super().__init__(x, y, width, height)
        self.time = initialValue
        self.font = font
        self.color = color
        self.paused = True
    
    def tick(self, dt : float) -> None:
        if not self.paused:
            self.time -= dt
    
    def getTime(self) -> float:
        return self.time
    
    def pause(self) -> None:
        self.paused = True
    
    def unpause(self) -> None:
        self.paused = False
    
    def reset(self) -> None:
        self.time = 30.0

    def getPrettyTime(self) -> str:
        time = self.time
        time = round(time, 2)
        centiseconds = (time * 100) % 100
        seconds = time % 100
        csecString = str(round(centiseconds))
        if len(csecString) < 2:
            csecString = csecString + "0"
        outString = str(round(seconds)) + ":" + csecString
        return outString
    
    def draw(self, surface : pygame.Surface) -> None:
        #pygame.draw.rect(surface, (0,0,0), self.rect)
        text = self.font.render(self.getPrettyTime(), True, self.color)
        textRect = text.get_rect(center = self.rect.center)
        surface.blit(text, textRect)


class TextBox(Item):
    def __init__(self, x : int, y : int, width : int, height : int,
                 sprite : pygame.Surface, text : str, font : pygame.Font = DEFAULT_FONT,
                 label : str = "", labelFont : pygame.Font = DEFAULT_FONT, labelHeight : int = 0,
                 mode : str = "autowrap"):
        """
        Creates a rectangular text box. Takes Item arguments plus
        :param sprite: the image behind the text
        :param text: the body text
        optionals - 
        :param font: the body's font (defaults to the default font)
        label, labelFont, labelHeight: parameters for a label box
        label must not be "" for the label box to be drawn.
        """
        super().__init__(x, y, width, height)
        self.sprite = sprite
        self.bodyText = text
        self.showingText = True
        self.font = font
        self.mode = mode
        self.label = label
        self.labelFont = labelFont
        self.labelHeight = labelHeight
        self.bodyRect = pygame.Rect(x, y + labelHeight, width, height - labelHeight)
        self.labelWidth = width
        self.labelRect = pygame.Rect(x, y, self.labelWidth, labelHeight)
    
    def draw(self, surface : pygame.Surface):

        # For the text
        if self.label != "":
            screenLabelRect = pygame.draw.rect(surface, (255, 0, 0, 0), self.labelRect)
        screenBodyRect = pygame.draw.rect(surface, (0, 255, 0, 0), self.bodyRect)

        screen_rect = pygame.draw.rect(surface, (0, 0, 255, 0), self.rect)
        surface.blit(self.sprite, screen_rect)

        if self.label != "":
            labelItem = self.labelFont.render(self.label, True, (0,0,0))
            surface.blit(labelItem, labelItem.get_rect(centerx = screenLabelRect.centerx, 
                                                        centery = screenLabelRect.centery))

        if self.showingText:
            if self.mode == "autowrap":
                padding = 20
                dx_line = 16
                words = self.bodyText.split(' ')
                lines = []
                current_line = []
                
                for word in words:
                    test_line = ' '.join(current_line + [word])
                    test_surface = self.font.render(test_line, True, (255, 255, 255))
                    
                    if test_surface.get_width() <= screenBodyRect.width - (padding * 2):
                        current_line.append(word)
                    else:
                        if current_line:
                            lines.append(' '.join(current_line))
                        current_line = [word]
                
                if current_line:
                    lines.append(' '.join(current_line))
                
                # Draw wrapped lines
                text_y = screenBodyRect.y + padding
                text_x = screenBodyRect.x + padding
                for line in lines:
                    line_surface = self.font.render(line, True, (0, 0, 0))
                    surface.blit(line_surface, (text_x, text_y))
                    text_y += dx_line
            
            elif self.mode == "formatted":
                padding = 20
                dx_line = 16

                lines = self.bodyText.split("\n")

                text_y = screenBodyRect.y + padding
                text_x = screenBodyRect.x + padding
                for line in lines:
                    line_surface = self.font.render(line, True, (0, 0, 0))
                    surface.blit(line_surface, (text_x, text_y))
                    text_y += dx_line

    def showText(self):
        "Set the bottom text to show"
        if not self.showingText:
            self.showingText = True

    def hideText(self):
        "Set the bottom to hide"
        if self.showingText:
            self.showingText = False

    def update(self):
        pass

    def setText(self, text : str):
        "update the text in the body"
        self.bodyText = text

    def setLabelWidth(self, width : int):
        self.labelWidth = width
        self.labelRect = pygame.Rect(self.x, self.y, self.labelWidth, self.labelHeight)

class Light(Item):
    
    def __init__(self, x : int, y : int, width : int, height : int,
                 sprites: tuple[pygame.Surface, pygame.Surface], status : bool = False):
        
        """
        Creates a two-state indicator light, two additional parameters
        :param sprites: a tuple of sprites, (off, on)
        optionals - 
        :param status: the initial on/off defaults to False
        """

        super().__init__(x, y, width, height)
        self.status = status
        self.offSprite = sprites[0]
        self.onSprite = sprites[1]

    def draw(self, surface : pygame.Surface):
        sprite = self.onSprite if self.status == True else self.offSprite
        debugRect = surface.blit(sprite, self.rect.topleft)

    def update(self):
        pass

    def turnOn(self):
        if self.status == False:
            self.status = True

    def turnOff(self):
        if self.status == True:
            self.status = False