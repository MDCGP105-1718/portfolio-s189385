import sys,time,random

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

Room2 = Room( "A narrow corridor with a door on the south , east and west wall" , [''])

Room3 = Room(  "You are in what seems to be a staff room" , ['wall safe' , 'lockers'])

Room4 = Room( "You find yourself in a glass room surrounded by thousands of people" , ['keypad' , 'painting'])

# Here are all of the item instances

table = Item("A solid oak table, looks like it can be moved" , ['describe' , 'move'])

bed = Item("A metal framed bed, its attached to the wall" , ['describe'])

paperclip = Item("A small paperclip, maybe you can pick a lock with that" , ['describe' , 'pick lock'])

wallsafe = Item("A locked wall safe, maybe the code is around here somewhere..." , ['describe', 'open'])

lockers = Item("A set of lockers, all of which are open." , ['describe', 'search'])

keypad = Item("A keypad, it must open the doors to this place." , ['use', 'describe'])

painting = Item("an exact replica of the Mona Lisa" , ['take', 'describe' ])

# Below are all the functions used within the game

# This function is used to navigate through the game.

def Walk():

    global CurrentRoom


    Direction = input("Which direction would you like to move? ")

    if Direction == "n" and CurrentRoom == Room1:
        if Door1Locked == True:
            return "This door is locked"
        else:
            CurrentRoom = Room2
            return "You walk through the door"
    elif Direction == "s" and CurrentRoom == Room2:
        CurrentRoom = Room1
        return "You walk back into the starting room"
    elif Direction == "w" and CurrentRoom == Room2:
        CurrentRoom = Room3
        return "You open the door and walk through. "
    elif Direction == "e" and CurrentRoom == Room3:
        CurrentRoom = Room2
        return "You walk back into the corridor"
    elif Direction == "e" and CurrentRoom == Room2:
        CurrentRoom = Room4
        return "You push open the heavy door and walk through"
    elif Direction == "w" and CurrentRoom == Room4:
        CurrentRoom = Room2
        return "You walk back into the corridor"
    else:
        return "You cant go that way"

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
        return "There are no items in this room"
    elif CurrentRoom == Room3:
        return Room3.items
    elif CurrentRoom == Room4:
        return Room4.items


# This function is used to describe an item

def ItemDescription():

    SelectedItem = input("What item would you like to describe? " )

    if SelectedItem == "table" and CurrentRoom == Room1:
        return table.description
    elif SelectedItem == "bed" and CurrentRoom == Room1:
        return bed.description
    elif SelectedItem == "paperclip" and "paperclip" in player.items:
        return paperclip.description
    elif SelectedItem == "wall safe" and CurrentRoom == Room3:
        return wallsafe.description
    elif SelectedItem == "lockers" and CurrentRoom == Room3:
        return lockers.description
    elif SelectedItem == "keypad" and CurrentRoom == Room4:
        return keypad.description
    elif SelectedItem == "painting" and CurrentRoom == Room4:
        return painting.description
    elif SelectedItem == "painting" and 'painting' in player.items:
        return painting.description
    else:
        return "There is no such item in this room"

# This functions prints the description of an item

def AvailibleActions():

    SelectedItem = input("Which item would you like to know the actions for? ")

    if SelectedItem == "table" and CurrentRoom == Room1:
        return table.actions
    elif SelectedItem == "bed" and CurrentRoom == Room1:
        return bed.actions
    elif SelectedItem == "paperclip" and "paperclip" in player.items:
        return paperclip.actions
    elif SelectedItem == "wall safe" and CurrentRoom == Room3:
        return wallsafe.actions
    elif SelectedItem == "lockers" and CurrentRoom == Room3:
        return lockers.actions
    elif SelectedItem == "keypad" and CurrentRoom == Room4:
        return keypad.actions
    elif SelectedItem == "painting" and CurrentRoom == Room4:
        return painting.actions
    else:
        return "There is no such item"


# This fucntion allows the player to move the table

def MoveTable():

    global TableMoved

    if TableMoved == False:
        player.items.append('paperclip')
        TableMoved = True
        return "You move the table to find a paperclip, it is added to your inventory"
    else:
        return "You already did that"

 # This function allows the player to pick the lock in room 1

# this contains the logic behind the picking a locked

def PickLock():

    global Door1Locked

    if Door1Locked == True:
        if 'paperclip' in player.items:
            Door1Locked = False
            return "You pick the lock and the door creeks open slowly"
        else:
            return "You need something to pick the lock with"
    else:
        return "You already did this"

# Room1Actions defines what the player can do in room 1.

# The logic behind cracking the safe

def OpenSafe():

    global SafeOpened

    if SafeOpened == False:
        CorrectCode = ['1','2','3','4']
        currentGuess = []
        Digit1 = input("please input digit 1 ")
        currentGuess.append(Digit1)
        Digit2 = input("please input digit 2 ")
        currentGuess.append(Digit2)
        Digit3 = input("please input digit 3 ")
        currentGuess.append(Digit3)
        Digit4 = input("please input digit 4 ")
        currentGuess.append(Digit4)
        if currentGuess == CorrectCode:
            SafeOpened = True
            return "The safe opened, scratched into the back are the numbers 2418"
        else:
            return "Nothing happend"
    else:
        return "You already opened the safe"

# The logic for searching the lockers

def SearchLockers():

    return "You find a piece of paper saying 1-2-3-4, maybe its the safe code ..."

# logic for using the UseKeypad function

def UseKeypad():

    global KeypadUsed
    global GameCompleted

    if KeypadUsed == False:
        CorrectCode = ['2','4','1','8']
        currentGuess = []
        Digit1 = input("please input digit 1 ")
        currentGuess.append(Digit1)
        Digit2 = input("please input digit 2 ")
        currentGuess.append(Digit2)
        Digit3 = input("please input digit 3 ")
        currentGuess.append(Digit3)
        Digit4 = input("please input digit 4 ")
        currentGuess.append(Digit4)
        if currentGuess == CorrectCode:
            KeypadUsed = True
            GameCompleted = True
            return "The floor collapses around you, you black out."
        else:
            return "Nothing happend"

# This function allows the player to take the painting

def TakePainting():

    global PaintingTaken

    if PaintingTaken == False:
        player.items.append('painting')
        PaintingTaken = True
        Room4.items.remove('painting')
        player.score += 1000
        return "You strap the painting to your back"
    else:
        print("You already did that")


def GameHelp():

    print("The aim of the game is to escape the building that you are stuck in.")
    print("When asked by the game input one of the following commands")
    print("'describe room' To describe the room ")
    print("'items' To print the room items ")
    print("'describe item' To select and item you would like to know more about")
    print("'item actions' To see what an item can do ")
    print("'inventory' To list currently held items ")
    print("'Walk' this will then prompt you to input a direction ")
    print("'score' this will then print your score ")
    print("If an item has a specific actions for example move, type 'move' followed by the name of the item")







def Actions():

    CurrentAction = input("What would you like to do? ")

    if CurrentAction == "walk":
        print(Walk())
    elif CurrentAction == "describe room":
        print(DescribeRoom())
    elif CurrentAction == "items":
        print(RoomItems())
    elif CurrentAction == "describe item":
        print(ItemDescription())
    elif CurrentAction == "item actions":
        print(AvailibleActions())
    elif CurrentAction == "inventory":
        if len(player.items) > 0:
            print(player.items)
        else:
            print("You dont have any items")
    elif CurrentAction == "move table" and CurrentRoom == Room1:
        print(MoveTable())
    elif CurrentAction == "pick lock paperclip" and CurrentRoom == Room1:
        print(PickLock())
    elif CurrentAction == "open wall safe" and CurrentRoom == Room3:
        print(OpenSafe())
    elif CurrentAction == "search lockers":
        print(SearchLockers())
    elif CurrentAction == "use keypad":
        print(UseKeypad())
    elif CurrentAction == "take painting" and CurrentRoom == Room4:
        print(TakePainting())
    elif CurrentAction == "score":
        print(player.score)
    elif CurrentAction == "help":
        GameHelp()
    else:
        print("You cant do that")

# This function prints the text slowly

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)






# These are some variables used within the game

CurrentRoom = Room1
Door1Locked = True
TableMoved = False
GameCompleted = False
SafeOpened = False
KeypadUsed = False
PaintingTaken = False



# The game starts here

print_slow("You awaken to find yourself in what appears to be a prison cell \n")

print_slow("A man appears from another room and walks slowly upto you \n")

player.name = input("'Well what is your name?' ")

print_slow(f"'Well {player.name}, you are stuck with me now.' \n")

print_slow("The unknown man walks away leaving you in a locked cell \n")

GameHelp()

while GameCompleted == False:
    Actions()

print_slow("You awaken in your beedroom \n")

if 'painting' in player.items:
    print_slow("You glance at the wall see the Mona Lisa \n")
    print_slow(f"Your score was {player.score}\n")
    print_slow("Thanks for playing \n")
else:
    print_slow(f"Your score was {player.score}\n")
    print_slow("Thanks for playing \n")
