# In this section i will be defining classes and thir methods and attributes.

# Here is the player class.

class Player():

    def __init__(self, items, score, name):

        self.items = items
        self.score = score
        self.name = name

    def PrintItems(self):

        if len(player.items) > 0:
            return str(items)
        else:
            return "You dont have any items"

    def PrintScore(self):
        return self.score

# This is the room class, it contains information surrounding the room and its items.

class Room:

    def __init__(self, description, items):

        self.items = items
        self.description = description

    def DescribeRoom(self):
        return self.description

    def DescribeItems(self):
        return "In this room there is" + str(self.items)

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

# My game code starts here

CurrentRoom = Room1
TableMoved = False


# This function allows the player to interact with the game

def Actions(TableMoved):



    Action = input("What would you like to do ? ")

    if Action == "describe":
        print(Room1.DescribeRoom())
    elif Action == "score":
        print(player.PrintScore())
    elif Action == "inventory":
        print(player.PrintItems())
    elif Action == "items":
        print(Room1.DescribeItems())
    elif Action == "describe bed":
        print(bed.DescribeItem())
    elif Action == "describe table":
        print(table.DescribeItem())
    elif Action == "bed actions":
        print(bed.PrintActions())
    elif Action == "table actions":
        print(table.PrintActions())
    elif Action == "move table":
        while TableMoved == False:
                Room1.items.append('paperclip')
                print("You moved the table to reveal a paperclip, it is added to you inventory")
                
        else:
            print("You already did that")
    else:
        print("You cant do that")

while CurrentRoom == Room1:
    Actions(TableMoved)
