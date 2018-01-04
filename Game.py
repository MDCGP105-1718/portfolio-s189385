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

# This is the class for room1

Room1 = Room(['table' , 'bed'] , "A small room with no windows and a single door on the north wall", "In this room you can walk north")

# This is the item class

class Item(object):

    def __init__(self, ):
        
        

# This is the help function which prints when the user types 'help'

def Help():

    print('You have been trapped in a building, the aim of the game is to escape')
    print("To list current held type 'inventory' ")
    print("To print your current score type 'score' ")
    print("To list the current items in the room type 'items' ")
    print("To print the description of the room type 'description' ")
    print("To list all the directions you can walk in the current room type 'directions' ")

def ItemActions():

    SelectedItems = input("What item would you like to know the actions for? ")
    
    SelectedItems = StringStripper(SelectedItems)

    if SelectedItems == ("table") and CurrentRoom == room1:
        print("With actions for this item include" + table.actions)




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

# This takes the users input and performs an action based on their choice

def Actions():

    CurrentAction = input("What would you like to do? ")

    CurrentAction = StringStripper(CurrentAction)

    if CurrentAction == "inventory":
        if len(Player1.items) == 0:
            print('You dont have any items')
        else:
            print('Player1.items')
    elif CurrentAction == "score":
        print(Player1.score)
    elif CurrentAction == "help":
        Help()
    elif CurrentAction == "items":
        print("In this room are the following items" + ' ' + str(CurrentRoom.items))
    elif CurrentAction == "description":
        print(CurrentRoom.description)
    elif CurrentAction == "directions":
        print(CurrentRoom.directions)
    elif CurrentAction == "itemactions":
        ItemActions()
    else:
        print('You cant do that')


i = 1

while i == 1:
    Actions()
        



