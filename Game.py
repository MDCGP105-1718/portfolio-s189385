# In this section i will be defining classes and thir methods and attributes.

# Here is the player class.

class Player():

    def __init__(self, items, score, name):

        self.items = items
        self.score = score
        self.name = name



# This is the room class, it contains information surrounding the room and its items.

class Room:

    def __init__(self, description, items):

        self.items = items
        self.description = description

# This is the item class where all the characteristics of an item are defined

class Item:

    def __init__(self, description, actions):

        self.description = description
        self.actions = actions

    def DescribeItem(self):
        return self.description

    def PrintActions(self):
        return "You can" + str(self.actions) + "this item"

# In this section I am defining class instances

# Here are all of my room instances collected together

Room1 = Room("A small room with no windows and a locked door preventing you from leaving", ['Table', 'Bed'])

# Here are all of my item instances collected together

table = Item('A small round table' , ['descibe' , 'move'])
bed = Item('A single bed with a metal frame attaching it to the wall', ['describe'])

# Here is the player instance

player = Player( [] , 100, "" )

# Here are all the functions i will use throughout the whole game.

# This fucntion takes in the variable of CurrentRoom and prints the room description

def DescribeCurrentRoom(CurrentRoom):

    if CurrentRoom == Room1:
        return Room1.description


# This fucntion prints the items in the room

def DescribeCurrentRoomItems(CurrentRoom):

    if CurrentRoom == Room1:
        return "in this room there is" + str(Room1.items)

# This function prints the players items

def PlayerItems(player):

    if len(player.items) > 0:
        return str(player.items)
    else:
        return "You dont have any items"

# My game code starts here

# Below are some variables needed for the functions to display the correct data for this room.

CurrentRoom = Room1

# Below in a function which allows specific intereactions for this room


def Room1Actions():

    CurrentAction = input("What would you like to do? ")

    if CurrentAction == "describe":
        print(DescribeCurrentRoom(CurrentRoom))
    if CurrentAction == "items":
        print(DescribeCurrentRoomItems(CurrentRoom))
    if CurrentAction == "inventory":
        print(PlayerItems(player))
    if CurrentAction == "score":
        print(player.score)

player.name = input("What is your name? ")


while CurrentRoom == Room1:
    Room1Actions()
