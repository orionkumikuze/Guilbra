import pygame

class framData:
    frames = []
    mx, my = 0, 0
    clicked = []
    debugMode = False
    
    def collision(x,y,x2,y2,hitbox):
        dx = x - x2
        dy = y - y2
        if(hitbox/2>dx>-hitbox/2 and hitbox/2>dy>-hitbox/2):
            return True
        return False
    def update(self):
        self.mx, self.my = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed()
class frame():
    def __init__(self,screen,X,Y,WIDTH,HEIGHT,SPRITE,SPRITEWIDTH,SPRITEHEIGHT,HITBOX,HOVEREDSPRITE,onClick):
        self.X = X
        self.Y = Y
        self.HOVEREDSPRITE = HOVEREDSPRITE
        self.HITBOX = HITBOX
        self.WIDTH = WIDTH * SPRITEWIDTH
        self.HEIGHT = HEIGHT * SPRITEHEIGHT
        self.screen = screen
        self.SPRITE = SPRITE
        self.SPRITEWIDTH = SPRITEWIDTH
        self.SPRITEHEIGHT = SPRITEHEIGHT
        self.clicks = []
        self.onClick = onClick
        for WIDTH in range(int(self.WIDTH/self.SPRITEWIDTH)):
            for HEIGHT in range(int(self.HEIGHT/self.SPRITEHEIGHT)):
                self.clicks.append(False)
        framData.frames.append(self)
        
    def update(self):
        for i in self.clicks:
            i = False
        for WIDTH in range(int(self.WIDTH/self.SPRITEWIDTH)):
            for HEIGHT in range(int(self.HEIGHT/self.SPRITEHEIGHT)):
                Y = (self.Y+HEIGHT)*self.SPRITEHEIGHT
                X = (self.X+WIDTH)*self.SPRITEWIDTH
                self.screen.blit(self.SPRITE,(X,Y))
                hover = framData.collision(X,Y,framData.mx-32,framData.my-32,self.HITBOX)
                if(hover):
                    if(framData.clicked[0]):
                        self.clicks[WIDTH*HEIGHT] = True
                        self.onClick(WIDTH*HEIGHT)
                    self.screen.blit(self.HOVEREDSPRITE,(X,Y))
                    if(framData.debugMode==True):
                        print("hovered")
