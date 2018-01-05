# This is the player class

class Player():

    def __init__(self, score, items, name):

        self.score = score
        self.items = items
        self.name = name

# This is the player instance

Player1 = Player(0, [], "")

# This is the room class

class Room(object):
    
    def __init__(self, items, description, directions ):
       
        self.items = items
        self.description = description
        self.directions = directions

# Here are all the instances for the rooms

Room1 = Room(['table' , 'bed'] , "A small room with no windows and a single door on the north wall", "In this room you can walk north")
Room2 = Room([''], "A narrow room with a door on every wall", "in this room you can walk north, east, south and west")
Room3 = Room(['keypad'], "An empty room with a keypad on the wall, maybe the code is around here somewhere...", "In this room you can walk east")
Room4 = Room(['lockers'], "You find yourself in what looks like a staff room","In this room you can walk south")
Room5 = Room(['Painting'], "An empty room with nothing put a picture on the wall", "In this room you can walk west")

# This is the item class

class Item(object):

    def __init__(self, description, actions):

        self.description = description
        self.actions = actions

# Here are the instances for all the items in the game

table = Item("A small wooden table, looks like it can be moved", ['describe', 'move'])
bed = Item("A metal framed bed, it is bolted to the wall", ['describe'])
paperclip = Item("A small paperclip, maybe you can pick a lock with that", ['describe' , 'pick lock'])
keypad = Item("A small plastic keypad with the numbers 0-9", ['use', 'describe'])
lockers = Item("A metal set of lockers, maybe there is something inside...",['describe','search'])
Painting = Item("A large paiting maybe its worth something...", ['describe','take'])
        
        

# This is the help function

def Help():

    print('You have been trapped in a building, the aim of the game is to escape')
    print("To list current held type 'inventory' ")
    print("To print your current score type 'score' ")
    print("To list the current items in the room type 'items' ")
    print("To print the description of the room type 'describe room' ")
    print("To list all the directions you can walk in the current room type 'directions' ")
    print("To list all the availible actions for an item type 'item actions' ")
    print("to print the description of an item type 'describe item' ")
    print("To interact with an item type a command, for example 'move' which will then prompt you to select and object")
    print("To walk throughout the game type 'walk' it will then prompt you to enter a direction which is either 'n','e','s' or 'w'")

# This function prints all the availible actions for the selected item

def ItemActions():

    SelectedItems = input("What item would you like to know the actions for? ")
    
    SelectedItems = StringStripper(SelectedItems)

    if SelectedItems == ("table") and CurrentRoom == Room1:
        print("actions for this item include;" + " " + str(table.actions))
    elif SelectedItems == ("bed") and CurrentRoom == Room1:
        print("actions for this item include;" + " " + str(bed.actions))
    elif SelectedItems == ("paperclip") and "paperclip" in Player1.items:
        print("actions for this item include;" + " " + str(paperclip.actions))
    elif SelectedItems == ("keypad") and CurrentRoom == Room3:
        print("actions for this item include;" + " " + str(keypad.actions))
    else:
        print("There is no such item")

# This function prints the description for a selected object

def DescribeItem():

    SelectedItems = input("What item would you like to know the description for? ")
    
    SelectedItems = StringStripper(SelectedItems)

    if SelectedItems == ("table") and CurrentRoom == Room1:
        print(table.description)
    elif SelectedItems == ("bed") and CurrentRoom == Room1:
        print(bed.description)
    elif SelectedItems == ("paperclip") and "paperclip" in Player1.items:
        print(paperclip.description)
    elif SelectedItems == ("keypad") and CurrentRoom == Room3:
        print(keypad.description)
    elif SelectedItems == ("Lockers") and CurrentRoom == Room4:
        print(paiting.description)
    elif SelectedItems == ("Painting") and CurrentRoom == Room5:
        print(Painting.description)

    else:
        print("There is no such item")

# This function allows the user to select the item they wish to move

def Move():

    global TableMoved

    SelectedItems = input("What item would you like to move? ")
    
    SelectedItems = StringStripper(SelectedItems)

    if SelectedItems == "table":
        if TableMoved == False:
            print("You move the table to find a paperclip, it is added to your inventory.")
            Player1.items.append('paperclip')
            TableMoved = True
        else:
            print("You already did that")
    else:
        print("You cannot move this item or it does not exist")

# This function allows users to use items

def Use():

    keypadCode = ['1','4','1','7']
    CurrentGuess = []

    SelectedItems = input("What item would you like to use? ")
    
    SelectedItems = StringStripper(SelectedItems)

    if SelectedItems == "keypad" and CurrentRoom == Room3:
        
        digit1 = input("Please input the first digit ")
        CurrentGuess.append(digit1)
        digit2 = input("Please input the second digit ")
        CurrentGuess.append(digit2)
        digit3 = input("Please input the third digit ")
        CurrentGuess.append(digit3)
        digit4 = input("Please input the fourth digit ")
        CurrentGuess.append(digit4)

        if CurrentGuess == keypadCode:
            print("The floor collapses around you, you black out")
            print("You awaken back in your home, free at last")
            print("Your score was" + " " + str(Player1.score))
            print("Thanks for playing")
        else:
            print("Nothing happend")
    else:
        print("You cant do that")

        




# This function allows the user to pick the lock

def PickLock():

    global Door1Locked

    if "paperclip" in Player1.items:
        print("You pick the lock and the door swings open")
        Door1Locked = False
    else:
        print("You have nothing to pick the lock with")



# This function allows the player to walk through the game

def Walk():

    global CurrentRoom
    global Door1Locked

    direction = input("What direction would you like to walk? ")
    
    direction = StringStripper(direction)

    if CurrentRoom == Room1:
        if direction == "n" and Door1Locked == True:
            print("The door is locked")
        else:
            print("You walk through the door in to the next room")
            CurrentRoom = Room2

    elif CurrentRoom == Room2 and direction == "s":
        print("You walk back into the starting room")
        CurrentRoom = Room1
    elif CurrentRoom == Room2 and direction == "w":
        print("You walk through the door into an empty room")
        CurrentRoom = Room3
    elif CurrentRoom == Room3 and direction == "e":
        print("You walk back into the hallway")
        CurrentRoom = Room2
    elif CurrentRoom == Room2 and direction == "n":
        print("You walk through the door")
        CurrentRoom = Room4
    elif CurrentRoom == Room4 and direction == "s":
        print("You walk back into the hallway")
        CurrentRoom = Room2
    elif CurrentRoom == Room2 and direction == "e":
        print("You walk into the room")
        CurrentRoom = Room5
    else:
        ("You cant go that way")


# This function makes the inputted string readable by the program

def StringStripper(str):

    Alpha = "abcdefghijklmnopqrstuvwxyz"

    String = ""

    str = str.lower() 

    for c in str:
        if c in Alpha:
            String = String + c

    return String

# Here are some variables used within the game

CurrentRoom = Room1
TableMoved = False
Door1Locked = True

# This takes the users input and performs an action based on their choice

def Actions():

    CurrentAction = input("What would you like to do? ")

    CurrentAction = StringStripper(CurrentAction)

    if CurrentAction == "inventory":
        if len(Player1.items) == 0:
            print('You dont have any items')
        else:
            print("You have to following items in your inventory; " + " " + str(Player1.items))
    elif CurrentAction == "score":
        print(Player1.score)
    elif CurrentAction == "help":
        Help()
    elif CurrentAction == "items":
        if CurrentRoom == Room2:
            print("There are no items in this room")
        else:
            print("In this room are the following items;" + ' ' + str(CurrentRoom.items))
    elif CurrentAction == "describeroom":
        print(CurrentRoom.description)
    elif CurrentAction == "directions":
        print(CurrentRoom.directions)
    elif CurrentAction == "itemactions":
        ItemActions()
    elif CurrentAction == "describeitem":
        DescribeItem()
    elif CurrentAction == "move":
        Move()
    elif CurrentAction == "walk":
        Walk()
    elif CurrentAction == "picklock":
        PickLock()
    elif CurrentAction == "use":
        Use()
    else:
        print('You cant do that')


i = 1

while i == 1:
    Actions()
        



