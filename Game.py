# Below are my classes.

# Here is the player class.

class Player():

    def __init__(self, items, score, name):

        self.items = items
        self.score = score
        self.name = name



# This is the room class, it contains information surrounding the room and its items.

class Room:

    def __init__(self, description, items):

        self.description = description
        self.items = items


# This is the item class where all the characteristics of an item are defined.

class Item:

    def __init__(self, description, actions):

        self.description = description
        self.actions = actions

#  Here i will be defining all of the instances of my classes.

# Here is the player instance where all the attributes are defined.

player = Player([] , 100 , "")

# Here is the room instances.

Room1 = Room(  "A small room with a locked door preventing you from leaving" , ['table', 'bed'])

Room2 = Room( "A narrow corridor with a door on every wall" , [''])

Room3 = Room(  "You are in what seems to be a staff room" , ['wall safe' , 'lockers'])

Room4 = Room( "You find yourself in a glass room surrounded by thousands of people" , ['keypad' , 'painting'])

# Here are all of the item instances

table = Item("A solid oak table, looks like it can be moved" , ['describe' , 'move'])

bed = Item("A metal framed bed, its attached to the wall" , ['Describe'])

paperclip = Item("A small paperclip, maybe you can pick a lock with that" , ['describe' , 'pick lock'])

wallsafe = Item("A locked wallsafe, maybe the code is around here somewhere..." , ['describe'])

lockers = Item("A set of lockers, all of which are open." , ['describe', 'search'])

keypad = Item("A keypad, it must open the doors to this place." , ['use' 'describe'])

painting = Item("an exact replica of the Mona Lisa" , ['take' 'describe' ])

# Below are all the functions used within the game

# This function is used to print the current room description

def DescribeRoom():

    if CurrentRoom == Room1:
        return Room1.description
    elif CurrentRoom == Room2:
        return Room2.description
    elif CurrentRoom == Room3:
        return Room3.description
    elif CurrentRoom == Room4:
        return Room4.description

# This function prints the items within a room

def RoomItems():

    if CurrentRoom == Room1:
        return Room1.items
    elif CurrentRoom == Room2:
        return Room2.items
    elif CurrentRoom == Room3:
        return Room3.items
    elif CurrentRoom == Room4:
        return Room4.items

# This function print the description of an item

def ItemDescription():

    SelectedItem = input("What item would you like to describe? " )

    if SelectedItem == "table" and CurrentRoom == Room1:
        return table.description
    elif SelectedItem == "bed" and CurrentRoom == Room1:
        return bed.description
    elif SelectedItem == "paperclip" and "paperclip" in player.items:
        return paperclip.description
    elif SelectedItem == "wallsafe" and CurrentRoom == Room3:
        return wallsafe.description
    elif SelectedItem == "lockers" and CurrentRoom == Room3:
        return lockers.description
    elif SelectedItem == "keypad" and CurrentRoom == Room4:
        return keypad.description
    elif SelectedItem == "painting" and CurrentRoom == Room4:
        return painting.description

# This function describes the availible actions of an item

def AvailibleActions():

    SelectedItem = input("Which item would you like to know the actions for? ")

    if SelectedItem == "table" and CurrentRoom == Room1:
        return table.actions
    elif SelectedItem == "bed" and CurrentRoom == Room1:
        return bed.actions
    elif SelectedItem == "paperclip" and "paperclip" in player.items:
        return paperclip.actions
    elif SelectedItem == "wallsafe" and CurrentRoom == Room3:
        return wallsafe.actions
    elif SelectedItem == "lockers" and CurrentRoom == Room3:
        return lockers.actions
    elif SelectedItem == "keypad" and CurrentRoom == Room4:
        return keypad.actions
    elif SelectedItem == "painting" and CurrentRoom == Room4:
        return painting.actions

# This function is used for when the player moves the table.

def MoveTable():

    global TableMoved

    if TableMoved == True:
        print("You already did that")
    else:
        print("You find a paperclip, it is added to you inventory")
        player.items.append('paperclip')
        TableMoved = True
        return TableMoved

# This fucntion is used when the player picks the lock

def PickLock():

    global Door1Locked

    if "paperclip" in player.items and Door1Locked == True:
        print("You pick the lock and the door swings open.")
        Door1Locked = False
        return Door1Locked
    else:
        print("You cannot open this door")

# This function allows players to walk through the different Room

def Walk():

    global CurrentRoom

    Direction = input("Which direction would you like to walk? ")

    if Direction == "n" and CurrentRoom == Room1:
        if Door1Locked == True:
            print("The door is locked")
        else:
            print("You walk through the doorway.")
            CurrentRoom = Room2
            return CurrentRoom


# The game code starts Here

CurrentRoom = Room1
TableMoved = False
Door1Locked = True

# This function allows the user to interact with room 1

def Room1Actions():

    CurrentAction = input("What would you like to do? ")

    if CurrentAction == "describe room":
        print(DescribeRoom())
    elif CurrentAction == "items":
        print(RoomItems())
    elif CurrentAction == "describe item":
        print(ItemDescription())
    elif CurrentAction == "item actions":
        print(AvailibleActions())
    elif CurrentAction == "inventory":
        print(player.items)
    elif CurrentAction == "move table":
        MoveTable()
    elif CurrentAction == "pick lock":
        PickLock()
    elif CurrentAction == "walk":
        Walk()
    else:
        print("You cant do that")

# This while loop enables the user to do multiple things in a room before moving on.

Swhile CurrentRoom == Room1:
    Room1Actions()
