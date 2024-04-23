import pygame, sceneEngine, spriteEngine, uiEngine
from Rooms import *

#Doors

class West_Door(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/West_Door.gif")
        height = self.screen.get_height()
        self.x = 65
        self.y = height/2

class North_Door(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.locked = True
        width = self.screen.get_width()
        if self.locked == True:
            self.setImage("Rooms/North_Door_Locked.gif")
        else:
            self.setImage("Rooms/North_Door.gif")

        self.x = width/2
        self.y = 60
        
class East_Door(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/East_Door.gif")
        height = self.screen.get_height()
        self.x = self.screen.get_width() - 55
        self.y = height/2

class South_Door(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        width = self.screen.get_width()
        height = self.screen.get_height()
        self.setImage("Rooms/South_Door.gif")
        self.x = width/2
        self.y = height - 65

class Boss_Door(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.locked = True
        width = self.screen.get_width()
        self.setImage("Rooms/Boss_Door_Locked.gif")
        self.x = width/2
        self.y = 60
        
#Enemies
        
class Slime(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Slime.gif")
        self.setBoundAction(self.CONTINUE)
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.x = width/2
        self.y = height/2
        self.rect.move(self.x, self.y)

class Bat(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Bat.gif")
        self.setBoundAction(self.BOUNCE)
        self.stunned = False
        self.x = 50
        self.y = 50

    def checkEvents(self):
        if self.stunned == False:
            if self.x > self.scene.hero.x:
                if self.dx >= -20:
                    self.dx -= 1
            if self.x < self.scene.hero.x:
                if self.dx <= 20:
                    self.dx += 1
            if self.y > self.scene.hero.y:
                if self.dy >= -20:
                    self.dy -= 1
            if self.y < self.scene.hero.y:
                if self.dy <= 20:
                    self.dy += 1
        elif self.stunned == True:
            self.setImage("Rooms/Stunned_Bat.gif")
            self.dx = 0
            self.dy = 0
        self.updateVector()

class Skeleton(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Skeleton.gif")
        self.setBoundAction(self.BOUNCE)
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.x = width/2
        self.y = 150
        self.dy = 5
        self.hits = 0

    def checkEvents(self):
        self.updateVector()
        shoot = pygame.USEREVENT + 0
        pygame.time.set_timer(shoot,1500)
        for event in pygame.event.get():
            if event.type == shoot:
                self.scene.skeleton.fire()
        

    def fire(self):
        self.scene.bonearrow.setPosition((self.scene.skeleton.x, self.scene.skeleton.y))
        self.scene.bonearrow.setSpeed(15)

class Boss(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Boss.gif")
        self.setBoundAction(self.BOUNCE)
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.x = width/2
        self.y = height/2
        self.dx = 0
        self.dy = 0
        self.hits = 0

    def checkEvents(self):
        if self.hits == 1:
            if self.x > self.scene.hero.x:
                if self.dx >= -20:
                    self.dx -= 1
            if self.x < self.scene.hero.x:
                if self.dx <= 20:
                    self.dx += 1
            if self.y > self.scene.hero.y:
                if self.dy >= -20:
                    self.dy -= 1
            if self.y < self.scene.hero.y:
                if self.dy <= 20:
                    self.dy += 1
            
        self.updateVector()

class BoneArrow(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Arrow.gif")
        self.setBoundAction(self.HIDE)
        self.reset()

        
    def reset(self):
        self.setPosition ((-100, -100))
        self.setSpeed(0)

#Room Interactables

class Pit(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Pit.png")
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.x = width/2
        self.y = height/2
        self.image.set_colorkey((255, 255, 255))

class BossPit(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Boss_Pit.gif")
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.setBoundAction(self.BOUNCE)
        self.x = -500
        self.y = -500
        
class Key1(spriteEngine.SuperSprite):    #seperate instances of the smaller keys to make collecting them and organizing easier
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Small_key.gif")
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.setBoundAction(self.CONTINUE)
        self.x = -300
        self.y = -100
        
class Key2(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Small_key.gif")
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.setBoundAction(self.CONTINUE)
        self.x = -300
        self.y = -100

class Key3(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Boss_key.gif")
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.setBoundAction(self.CONTINUE)
        self.x = -300
        self.y = -100

class Target(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Target.gif")
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.setBoundAction(self.CONTINUE)
        self.x = 150
        self.y = height/2

class Switch(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Switch_off.gif")
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.x = width/2
        self.y = height/2
        self.active = False
        
    def interact(self):
        if self.active:
            self.active = False
            self.setImage("Rooms/Switch_off.gif")
        elif not self.active:
            self.active = True
            self.setImage("Rooms/Switch_on.gif")
            
class Bow(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Bow.gif")
        self.setBoundAction(self.CONTINUE)
        self.x = -300
        self.y = -200

#Text
class Start_Text(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA , 0x00))
        self.bgColor = ((0xFF, 0xFF, 0xFF))
        self.center = (-100, -100)
        self.text = "Arrow keys to move, A to attack, D to defend"
        self.size = (450, 30)

class Key_Text(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA , 0x00))
        self.bgColor = ((0xFF, 0xFF, 0xFF))
        self.center = (-100, -100)
        self.text = "You Got A Key!"
        self.size = (230, 30)

class Bow_Text(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA , 0x00))
        self.bgColor = ((0xFF, 0xFF, 0xFF))
        self.center = (-100, -100)
        self.text = "You Got The Bow! S to shoot"
        self.size = (350, 30)

class Boss_Key_Text(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA , 0x00))
        self.bgColor = ((0xFF, 0xFF, 0xFF))
        self.center = (-100, -100)
        self.text = "You Got The Boss Key!"
        self.size = (300, 30)

class Win_Text(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA , 0x00))
        self.bgColor = ((0xFF, 0xFF, 0xFF))
        self.center = (-100, -100)
        self.text = "You Win!"
        self.size = (300, 30)
        
#Player
        
class Hero(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Hero_South.gif")
        self.facing = "South"
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.x = width/2
        self.y = height - 110
        self.setBoundAction(self.STOP)
        self.hasBow = False

    def checkEvents(self):
        self.checkKeys()
        
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.setImage("Rooms/Hero_West.gif")
            self.dx = -20
            self.facing = "West"
        elif keys[pygame.K_RIGHT]:
            self.setImage("Rooms/Hero_East.gif")
            self.dx = 20
            self.facing = "East"
        else:
            self.dx = 0

        if keys[pygame.K_UP]:
            self.setImage("Rooms/Hero_North.gif")
            self.dy = -20
            self.facing = "North"
        elif keys[pygame.K_DOWN]:
            self.setImage("Rooms/Hero_South.gif")
            self.dy = 20
            self.facing = "South"
        else:
            self.dy = 0
        self.updateVector()


class Sheild(spriteEngine.SuperSprite): #Shield
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Shield.gif")
        self.setBoundAction(self.CONTINUE)
        self.x = -100
        self.y = -100
        self.using = False

    def use(self):
        self.setPosition((self.scene.hero.x, self.scene.hero.y))
        self.using = True

    def stop(self):
        self.setPosition((-100, -100))
        self.using = False
        
class Arrow(spriteEngine.SuperSprite): #Arrow
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Arrow.gif")
        self.setBoundAction(self.HIDE)
        self.reset()
        
        def checkEvents(self):
            self.checkKeys()

        def checkKeys(self):
            keys = pygame.key.get_pressed()
            if self.scene.hero.hasBow:
                if keys[pygame.K_s]:
                    if self.scene.hero.facing == "West":
                        self.setAngle(-90)
                    if self.scene.hero.facing == "East":
                        self.setAngle(90)
                    if self.scene.hero.facing == "North":
                        self.setAngle(0)
                    if self.scene.hero.facing == "South":
                        self.setAngle(180)
                    self.fire()

    def fire(self):
        self.setPosition((self.scene.hero.x, self.scene.hero.y))
        self.setSpeed(35)

    def reset(self):
        self.setPosition ((-200, -200))
        self.setSpeed(0)

class Sword(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Sword.gif")
        self.setBoundAction(self.CONTINUE)
        self.x = -300
        self.y = -300

    def checkEvents(self):
        self.checkKeys()
        self.rect.move(self.x, self.y)
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.scene.hero.facing == "West":
                self.rotation = 90
                self.x = self.scene.hero.x - 50
                self.y = self.scene.hero.y
            elif self.scene.hero.facing == "East":
                self.rotation = -90
                self.x = self.scene.hero.x + 50
                self.y = self.scene.hero.y
            elif self.scene.hero.facing == "North":
                self.rotation = 0
                self.x = self.scene.hero.x
                self.y = self.scene.hero.y -50
            elif self.scene.hero.facing == "South":
                self.rotation = 180
                self.x = self.scene.hero.x
                self.y = self.scene.hero.y + 50
        else:
                self.x = -300
                self.y = -300
        self.updateVector()

class Heart(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("Rooms/Heart.gif")
        self.x = 60
        self.y = 60
