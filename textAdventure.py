startText = """You Have entered the southernmost part of the dungeon.
All you have is your sword and your sheild. It is said 
that this dungeon holds a magical bow that does not require
arrows to shoot. It is also said that this dungeon holds a terible 
monster that, if not defeated, will destroy the nearby village.
It is up to you to find that bow and slay the monster.
"""

def north(): #Boss room!!!
    global choice
    global keepGoing
    print("You are in the Northernmost room.")
    global step
    if step < 1: #part 1
        print("There you see the monster ready to defend itself.")
        select = input("Type 'a' to attack with your sword,\n'd' to ready your shield,\n'b' to shoot it with your bow,\nor 's' to run.\n> ")
        if select == "a":
            print("The monster parries your attack sending your sword across the room. The monster readies it's next attack.")
            step +=1
            north()
        elif select == "d":
            print("The monster swipes at your legs with it's tail. Ouch!")
            ouch()
            north()
        elif select == "b":
            print("The monster catches your arrow and throws it at your knee. Ouch!")
            ouch()
            north()
        elif select == "s":
            print("The door apears to be magically locked by the monster. It seems running isn't an option.")
            north()
        else:
            print("Please enter a valid input")
            north()
    elif step == 1: #part 2
        print("The monster seems like it is about to attack.")
        select = input("Type 'd' to ready your shield,\n'b' to shoot it with your bow,\nor 's' to run.\n> ")
        if select == "d":
            print("This time You parry the monster's attack and send in off balance tumbling backwards. Now is your chance to finish this!")
            step += 1
            north()
        elif select == "b":
            print("The monster swipes at you before you could even draw the arrow. Ouch!")
            ouch()
            north()
        elif select == "s":
            print("The door apears to be magically locked by the monster. It seems running isn't an option.")
            north()
        else:
            print("Please enter a valid input")
            north()
    elif step > 1: #part 3
        print("The monster is wide open. Finish them!")
        select = input("Type 'd' to ready your shield,\n'b' to shoot it with your bow,\nor 's' to run.\n> ")
        if select == "d":
            print("Your hesitaion allows the monster to get back up and ready another attack")
            step = 1
            north()
        elif select == "b":
            print("With aim as true as ever, You send an arrow right into the heart of the monster,\nputting an end to it's reign of terror. The Village is saved and you have an awesome new bow.\n>>>YOU WIN<<<")
            step = 0
            keepGoing = False
            exit() #Just writing this was exciting.
        elif select == "s":
            print("The door apears to be magically locked by the monster. It seems running isn't an option.")
            north()
        else:
            print("Please enter a valid input")
            north()
    
    
def south():
    global choice
    global hasKey1
    print("You are in the southern room.")
    select = input("Type 'n' to go north,\n'e' to go to the southeastern room,\nor 'w' to go to the southwestern room.\n> ")
    if select == "n":
        if hasKey1:
            choice = "goCenter"
            center()
                   
        elif not hasKey1:
            print("There is a small lock on the door, preventing you form proceeding.") #Requires key 1
            south()
            
    elif select == "e":
        choice = "goSouthEast"
        southEast()
        
    elif select == "w":
        choice = "goSouthWest"
        southWest()
    else:
        print("Please enver a valid input")
        south()
    
def east():
    global choice
    global switch
    global hasKey2
    print("You are in the eastern room. There is a switch in the middle of the room.")
    if not switch:
        select = input("Type 's' to flip the switch,\nor 'w' to go to the centeral room.")
        if select == "s":
            print("You flipped the switch and a chest appeared")
            switch = True
            east()
        elif select == "w":
            choice = "goCenter"
            center()
        else:
            print("Please enver a valid input")
    if switch:
        select = input("Type 's' to flip the switch,\n'c' to open the chest,\nor 'w' to go to the centeral room.\n> ")
        if select == "s":
            print("You flipped the switch and the chest disappeared")
            switch = False
            east()
        elif select == "c":
            if not hasKey2:
                getKey("key2") #Get key 2
                east()
            elif hasKey2:
                print("The chest is empty")
                east()
        elif select == "w":
            choice = "goCenter"
            center()
    
    
def west():
    global choice
    global hasBow
    global skeleton
    global step
    if skeleton: #Third encounter with 3 steps
        print("A skeleton archer blocks your path.")
        if step < 1: #part 1
            print("It seems you caught it off guard.")
            select = input("Type 'a' to attack with your sword,\n'd' to ready your sheild,\nor 'e' to go to the centeral room.\n> ")
            if select == "a":
                print("You hit the skeleton and it takes a step back and readies it's bow")
                step += 1
                west()
            elif select == "d":
                print("In your hesitaion the skeleton had plety of time to aim and shoot you in the knee. Ouch!")
                ouch()
                west()
            elif select == "e":
                choice = "goCenter"
                center()
            else:
                print("Please enter a valid input")
                west()
        elif step == 1: #part 2
            print("The skeleton stands at a distance with it's bow aimed at you.")
            select = input("Type 'a' to attack with your sword,\n'd' to ready your sheild,\nor 'e' to go to the centeral room.\n> ")
            if select == "a":
                print("The skeleton was to far away to hit with a sword but close enough for it to shoot you. Ouch!")
                ouch()
                west()
            elif select == "d":
                 print("You block the arrow with your shield as you close the distance on the skeleton.")
                 step += 1
                 west()
            elif select == "e":
                choice = "goCenter"
                center()
            else:
                print("Please enter a valid input")
                west()
        elif step > 1: #Part 3
            print("The skeleton is cornered against a wall. Now is your chance!")
            select = input("Type 'a' to attack with your sword,\n'd' to ready your sheild,\nor 'e' to go to the centeral room.\n> ")
            if select == "a":
                skeleton = False
                print("You defeated the skeleton and received it's magical bow that requires no arrows to shoot.")
                hasBow = True
                step = 0
                west()
            elif select == "d":
                print("In your hesitaion the skeleton had plety of time to aim and shoot you in the knee. Ouch!")
                ouch()
                west()
            elif select == "e":
                choice = "goCenter"
                center()
            else:
                print("Please enter a valid input")
                west()
    if not skeleton:
        print("You are in the western room. There is nothing left but a pile of bones.")
        select = input("Type 'e' to go to the centeral room.\n> ")
        if select == "e":
            choice = "goCenter"
            center()
        else:
            print("YOU HAD ONE JOB! you tripped over a bone on the way out.") #easter egg
            ouch()
            choice = "goCenter"
            center()
            
def southEast():
    global choice
    global hasKey1
    global slime
    if slime:
        print("You find your path blocked by a slime.") #First encounter
        select = input("Type 'a' to attack with your sword,\n'd' to defend with your sheild,\nor 'w' to go to the southern room.\n> ")
        if select == "a":
            slime = False
            print("You have defeated the slime and revealed a chest")
            southEast()
        elif select == "d":
            print("The slime attacked your feet. Ouch!")
            ouch()
            southEast()
        elif select == "w":
            choice = "goSouth"
            south()
        else:
            print("Please enver a valid input")
            southEast()
    elif not slime:
        print("You are in the southeastern room.")
        select = input("Type 'c' to open the chest,\nor 'w' to go to the southern room.\n> ")
        if select == "c":
            if hasKey1:
                print("The chest is empty")
                southEast()
            else:
                getKey("key1")
                southEast()
        elif select == "w":
            choice = "goSouth"
            south()
        else:
            print("Please enter a valid input")
            southEast()
    
def southWest():
    global choice
    global hasKey3
    global hasBow

    if not hasBow:
        print("You are in the southwestern room. There is a target on the wall but you dont seem to have anything that can shoot it.")
        select = input("Type 'e' to go to the southern room.\n> ")
        if select == "e":
            choice = "goSouth"
            south()
        else:
            print("Please type a valid input.")
    if hasBow:
        print("You are in the southwestern room. There is a target on the wall.")
        select = input("Type 'b' to shoot the target with your bow,\nor 'e' to go to the southern room.\n> ")
        if select == "b": #at this point I didn't feel like making another switch like in the eastern room. Just shoot the target and get a key. Seems easy enough.
            if not hasKey3:
                print("You hit the target dead in the center and a spot in the ceailing opened dropping a key.")
                getKey("key3")
                southWest()
            elif hasKey3:
                print("Practice makes perfect.")
                southWest()
        elif select == "e":
                choice = "goSouth"
                south()
        else:
                print("Please type a valid input.")
            
    
def center():
    global choice
    global hasKey2
    global hasKey3
    global bat
    global step
    if bat:
        if step < 1:
            print("You are suddenly attacked by a bat") #Second encounter and features multiple steps that can loop
            select = input("Type 'a' to attack with your sword,\n'd' to defend with your sheild,\n'or 's' to go back to the southern room.\n> ")
            if select == "a":
                print("You were to slow to dram your sword and was hit. Ouch!")
                ouch()
                center()
            elif select == "d":
                print("You blocked the attack, now is your chance!")
                step += 1
                center()
            elif select == "s":
                choice = "goSouth"
                south()
            else:
                print("Please enter a valid input.")
        elif step >= 1:
            print("The bat is stunned")
            select = input("Type 'a' to attack with your sword,\n'd' to defend with your sheild,\n'or 's' to go back to the southern room.\n> ")
            if select == "a":
                print("You have slain the bat.")
                bat = False
                step = 0
                center()
            elif select == "d":
                print("In your hesitaion the bat is no longer stunned.")
                step = 0
                center()
            elif select == "w":
                choice = "goSouth"
                south()
            else:
                print("Please enter a valid input.")
                center()
    if not bat:
        print("You are in the central room. There are rooms in four directions.")
        select = input("Type 'n' to go north,\n'e' to go east,\n's' to go south,\nor 'w' to go west.\n> ")
        if select == "n":
            if not hasKey3:
                print("The door has a very large and elegant looking lock preventing you from entry.") #door requires key 3
                center()
            elif hasKey3:
                choice = "goNorth"
                north()
        elif select == "e":
            choice = "goEast"
            east()
        elif select == "s":
            choice = "goSouth"
            south()
        elif select == "w":
            if not hasKey2:
                print("There is a small lock preventing your entry. It seems the previous key won't fit.") #door requires key 2
                center()
            elif hasKey2:
                choice = "goWest"
                west()
        else:
            print("Please enter a valid input.")
            center()
    
    
def getKey(whichKey):
    if whichKey == "key1":
        print("You received a small key.")
        global hasKey1
        hasKey1 = True
                  
    elif whichKey == "key2":
        print("You received another small key.")
        global hasKey2
        hasKey2 = True

    elif whichKey == "key3":
        print("You received a large, elegant key. It seems important.")
        global hasKey3
        hasKey3 = True

def ouch():
    global lives
    lives -= 1
    print("You have %d health remaining" % lives)

#main loop

keepGoing = True
lives = 5
choice = "start"
hasKey1 = False
hasKey2 = False
hasKey3 = False #boss key
hasBow = False
slime = True
skeleton = True
bat = True
switch = False
step = 0

while keepGoing:
    print("You choose: ", choice) # I made a map for this "dungeon"
    if lives > 0:
        if choice == "start":
            print(startText)
            south()
            
        elif choice == "goSouth":
            south()
            
        elif choice == "goSouthWest": #it would sometimes loop the same rooms if the room featured an encounter of somekind so i added a bit of redundancy that made this 'choice' system just for starting the game and for show.
            southWest()
            
        elif choice == "goSouthEast":
            southEast()
            
        elif choice == "goNorth":
            north()
            
        elif choice == "goCenter":
            center()
            
        elif choice == "goEast":
            east()
            
        elif choice == "goWest":
            west()
    else:
        print("You have died.\nGAME OVER")
        keepGoing = False
