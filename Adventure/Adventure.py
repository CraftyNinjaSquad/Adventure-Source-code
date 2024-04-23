import pygame, sceneEngine, spriteEngine, uiEngine, Config
import sprites
from Rooms import *

class Game(sceneEngine.Scene):
    def __init__(self):
        sceneEngine.Scene.__init__(self)
        self.background = pygame.image.load("Rooms/Room.png")
        
        #Getting config info
        self.configroom = Config.room()
        self.configkey1 = Config.hasKey1()
        self.configkey2 = Config.hasKey2()
        self.configkey3 = Config.hasKey3()
        self.configBow = Config.hasBow()
        self.configroom.set_room("South")
        self.roomloaded = False
        self.startgame = True
        self.win = False
        self.itemget= False
        
    #Sprites
        
	#doors
        self.north = sprites.North_Door(self)
        self.south = sprites.South_Door(self)
        self.east = sprites.East_Door(self)
        self.west = sprites.West_Door(self)
        self.boss_door = sprites.Boss_Door(self)

	#enemy sprites
        self.boss = sprites.Boss(self)
        self.bosspit = sprites.Pit(self)
        self.skeleton = sprites.Skeleton(self)
        self.bonearrow = sprites.BoneArrow(self)
        self.bat = sprites.Bat(self)
        self.slime = sprites.Slime(self)

	#room misc.
        self.key1 =  sprites.Key1(self)
        self.key2 =  sprites.Key2(self)
        self.key3 =  sprites.Key3(self)
        self.target = sprites.Target(self)
        self.switch = sprites.Switch(self)
        self.pit = sprites.Pit(self)
        self.bosspit = sprites.BossPit(self)

	#Hero
        self.hero = sprites.Hero(self)
        self.sheild = sprites.Sheild(self)
        self.arrow = sprites.Arrow(self)
        self.sword = sprites.Sword(self)
        self.bow = sprites.Bow(self)
        self.lives = []
        self.health = 6

        #text
        self.starttext = sprites.Start_Text(self)
        self.keytext = sprites.Key_Text(self)
        self.bowtext = sprites.Bow_Text(self)
        self.bosskeytext = sprites.Boss_Key_Text(self)
        self.wintext = sprites.Win_Text(self)

        self.runLocation()
        self.hit()

    def hit(self):
        self.health -= 1
        self.lives = []
        if self.health > 0:
            i = 0
            for i in range(self.health):
                self.lives.append(sprites.Heart(self))
                self.lives[i].x += i * 60
        elif self.health == 0:
            print("GAME OVER")
            pygame.quit()
        

    def update(self):
        self.runLocation()
        self.mainSprites.remove(self.mainSprites)
        self.mainSprites = pygame.sprite.OrderedUpdates(self.sprites)
        self.groups.append(self.mainSprites)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.sheild.use()
        else:
            self.sheild.stop()
        if self.configBow.get_bow():
            if keys[pygame.K_s]:
                if self.hero.facing == "West":
                    self.arrow.setAngle(180)
                if self.hero.facing == "East":
                    self.arrow.setAngle(0)
                if self.hero.facing == "North":
                    self.arrow.setAngle(90)
                if self.hero.facing == "South":
                    self.arrow.setAngle(-90)
                self.arrow.fire()

        
        self.checkColisions()

    def checkColisions(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        herohitpit = self.hero.collidesWith(self.pit)
        killslime = self.sword.collidesWith(self.slime)
        slimehithero = self.hero.collidesWith(self.slime)
        key1get = self.hero.collidesWith(self.key1)
        key2get = self.hero.collidesWith(self.key2)
        key3get = self.hero.collidesWith(self.key3)
        targethit = self.arrow.collidesWith(self.target)
        bathitsheild = self.sheild.collidesWith(self.bat)
        bathithero = self.hero.collidesWith(self.bat)
        herohitbat = self.sword.collidesWith(self.bat)
        herohitswitch = self.sword.collidesWith(self.switch)
        herohitskele = self.sword.collidesWith(self.skeleton)
        skelehithero = self.hero.collidesWith(self.bonearrow)
        skelehitsheild = self.sheild.collidesWith(self.bonearrow)
        bowget = self.hero.collidesWith(self.bow)
        herohitbosspit = self.hero.collidesWith(self.bosspit)
        bosshitshero = self.hero.collidesWith(self.boss)
        herohitsboss = self.sword.collidesWith(self.boss)
        shootboss = self.arrow.collidesWith(self.boss)
        bosshitshield = self.sheild.collidesWith(self.boss)

        

        """collisions were being detected right on start up (tested with a print statement)
           to fix it I made it also check if the room was correct. This was found out after the doors
           were fixed so the doors will remain the same."""


        if herohitpit and self.configroom.get_room() == "SouthWest":
            self.hero.x += 20
            
        if killslime and self.configroom.get_room() == "SouthEast":
            self.slime.setPosition((-1000, -1000))
            self.key1.setPosition((width/2, height/2))
            
        if key1get and self.configroom.get_room() == "SouthEast":
            self.configkey1.set_key1(True)
            self.key1.setPosition((-300, -100))
            self.keytext.center = (width/2, height/2)
            self.itemget = True
            
        if targethit and self.configroom.get_room() == "SouthWest":
            self.arrow.reset()
            self.target.setPosition((-200, -100))
            self.key3.setPosition((width - 80, 80))

        if key3get and self.configroom.get_room() == "SouthWest":
            self.key3.setPosition((-300, -100))
            self.configkey3.set_key3(True)
            self.bosskeytext.center = (width/2, height/2)
            self.itemget = True

        if slimehithero and self.configroom.get_room() == "SouthEast":
            self.hit()
            self.hero.setPosition((100, height/2))
            
        if bathitsheild and self.sheild.using == True:
            self.bat.stunned = True
            
        if herohitbat and self.bat.stunned:
            self.bat.setPosition((-400, -400))
            
        if bathithero and self.roomloaded and not self.bat.stunned:
            self.hit()
            self.bat.setPosition((50, 50))
            
        if herohitswitch and self.roomloaded:
            event = pygame.event.wait()
            if event.type == pygame.KEYUP:
                self.switch.interact()

        if key2get and self.roomloaded:
            self.key2.setPosition((-300, -100))
            self.configkey2.set_key2(True)
            self.keytext.center = (width/2, height/2)
            self.itemget = True

        if herohitskele and self.roomloaded:
            if self.skeleton.hits < 1:
                self.skeleton.setPosition((150, 150))
                self.skeleton.hits = 1
            elif self.skeleton.hits == 1:
                self.bow.setPosition((self.skeleton.x, self.skeleton.y))
                self.skeleton.setPosition((-500, -500))

        if skelehithero and self.roomloaded:
            self.hit()
            self.hero.setPosition((width - 100, height/2))
            self.bonearrow.reset()

        if skelehitsheild and self.roomloaded:
            self.bonearrow.reset()

        if bowget and self.roomloaded:
            self.bow.setPosition((-300, -200))
            self.configBow.set_bow(True)
            self.bowtext.center = (width/2, height/2)
            self.itemget = True

        if herohitsboss and self.roomloaded:
            if self.boss.hits == 0:
                self.boss.hits = 1
                self.boss.setPosition((100,100))

        if bosshitshero and self.roomloaded:
            self.hit()
            self.hero.setPosition((width/2, height - 100))
            if self.boss.hits == 1:
                self.boss.setPosition((100,100))

        if bosshitshield and self.roomloaded:
            self.boss.hits = 2
            self.boss.setPosition((200,200))
            self.boss.setDY(0)
            self.boss.setDX(25)
            self.bosspit.setPosition((width/2, height/2))
            self.hero.setPosition((width/2, height - 200))

        if herohitbosspit and self.roomloaded:
            self.hero.y += 20

        if shootboss and self.roomloaded:
            if self.boss.hits == 2:
                self.boss.setPosition((-1000, -1000))
                self.arrow.reset()
                self.wintext.center = (width/2, height/2)
                self.win = True
                

    def findDoor(self):  #I couldnt get the doors to behave with the collidesWith sprite engine so this was the next best thing.
        self.goUp = False
        self.goDown = False
        self.goLeft = False
        self.goRight = False
        width = self.screen.get_width()
        height = self.screen.get_height()
        if self.hero.x > width - 80 and self.hero.y > height/2 - 30 and self.hero.y < height/2 +30:
            self.goRight = True
        if self.hero.x < 80 and self.hero.y > height/2 - 30 and self.hero.y < height/2 +30:
            self.goLeft = True
        if self.hero.y < 80 and self.hero.x > width/2 - 30 and self.hero.x < width/2 +30:
            self.goUp = True
        if self.hero.y > height - 100 and self.hero.x > width/2 - 30 and self.hero.x < width/2 +30:
            self.goDown = True
        
    def runLocation(self):   #This decides what rooms to show and how to load each room.
        self.findDoor()
        width = self.screen.get_width()
        height = self.screen.get_height()

        """A fun little detail that came up while I was making this
           is that if config.get_room() returns a room that either doesn't
           exsist or just hasn't been made yet, then it generates the room
           you just left but you can't interact with anything, basically making
           a softlocked kill screen"""
        #South room
        if self.configroom.get_room() == "South":
            self.sprites = [self.north, self.east, self.west, self.hero,
                            self.sheild, self.sword, self.arrow, self.starttext, self.lives]
            self.west.setImage("Rooms/West_Door.gif")
            if self.goRight:
                self.configroom.set_room("SouthEast")
                self.hero.x = 100
                self.startgame = False
            if self.goLeft:
                self.configroom.set_room("SouthWest")
                self.hero.x = width - 100
                self.startgame = False
            if self.goUp and self.configkey1.get_key1() == True:
                self.hero.y = height - 100
                self.goUp = False
                self.configroom.set_room("Center")
                self.startgame = False
            if self.configkey1.get_key1() == True:
                self.north.setImage("Rooms/North_Door.gif")
                self.startgame = False
            if self.startgame:
                self.starttext.center = (width/2, height/2)
            else:    
                self.starttext.center = (-1000, -1000)
                
        #SouthEast room        
        if self.configroom.get_room() == "SouthEast":
            self.sprites = [self.key1, self.slime, self.west, self.hero,
                            self.sheild, self.sword, self.arrow, self.keytext, self.lives]
            if self.goLeft:
                self.configroom.set_room("South")
                self.hero.x = width - 100

            if self.itemget:
                pygame.time.delay(3000)
                self.keytext.center = (-1000, -1000)
                self.itemget = False
                
        #SouthWest Room        
        if self.configroom.get_room() == "SouthWest":
            self.sprites = [self.east, self.hero, self.sheild, self.pit, self.sheild,
                            self.sword, self.target, self.key3, self.arrow, self.bosskeytext, self.lives]
            if self.goRight:
                self.configroom.set_room("South")
                self.hero.x = 100
            if self.itemget:
                pygame.time.delay(3000)
                self.bosskeytext.center = (-1000, -1000)
                self.itemget = False
                
        #Center Room    
        if self.configroom.get_room() == "Center":
           self.roomloaded = False
           self.sprites = [self.south, self.east, self.west, self.boss_door, self.hero,
                           self.sheild, self.sword, self.arrow, self.bat, self.key2, self.keytext, self.lives]
           self.roomloaded = True
           height = self.screen.get_height()
           width = self.screen.get_width()
           if self.configkey2.get_key2() == False and self.configroom.get_room() == "Center":
               self.west.setImage("Rooms/West_Door_locked.gif")
               
           if self.configkey2.get_key2() == True:
              self.west.setImage("Rooms/West_Door.gif")
               
           if self.configkey3.get_key3() == True:
              self.boss_door.setImage("Rooms/Boss_Door_Open.gif")
           
           if self.goDown:
              self.configroom.set_room("South")
              self.hero.y = 100
           if self.goRight:
              self.configroom.set_room("East")
              self.hero.x = 100
           if self.goLeft and self.configkey2.get_key2() == True:
              self.configroom.set_room("West")
              self.hero.x = width - 100
           if self.goUp and self.configkey3.get_key3() == True:
               self.configroom.set_room("North")
               self.hero.y = height - 100
               
           if self.switch.active and self.configkey2.get_key2() == False:
              self.key2.setPosition((width/2, height/2))
           if not self.switch.active:
               self.key2.setPosition((-300, -100))

           if self.itemget:
                pygame.time.delay(3000)
                self.keytext.center = (-1000, -1000)
                self.itemget = False
              
        #East Room   
        if self.configroom.get_room() == "East":
            self.roomloaded = False
            self.sprites = [self.west, self.switch, self.hero, self.sheild,
                            self.sword, self.arrow, self.lives]
            self.roomloaded = True
            self.west.setImage("Rooms/West_Door.gif")
            if self.goLeft:
                self.configroom.set_room("Center")
                self.hero.x = width - 100
            
        #West room (mini boss room)
        if self.configroom.get_room() == "West":
            self.roomloaded = False
            self.sprites = [self.east, self.hero, self.sheild,
                            self.sword, self.arrow, self.skeleton, self.bonearrow,
                            self.bowtext, self.bow, self.lives]
            self.roomloaded = True
            if self.goRight:
                self.configroom.set_room("Center")
                self.hero.x = 100
            if self.itemget:
                pygame.time.delay(3000)
                self.bowtext.center = (-1000, -1000)
                self.itemget = False

        #North room (boss room)
        if self.configroom.get_room() == "North":
            self.roomloaded = False
            self.sprites = [self.bosspit, self.hero, self.sheild, self.sword,
                            self.arrow, self.boss, self.wintext, self.lives]
            self.roomloaded = True
            if self.win:
                pygame.time.delay(3000)
                pygame.quit()
            
            
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
