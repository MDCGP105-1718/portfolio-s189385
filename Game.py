import sys,time
""" these are data types which store information such as the room desriptions, score and player inventory"""
Room1 = "You are in a small room with no windows and a flickering light above you"
CurrentRoomItems = []
Room2 = "room 2"
Room3 = "room 3"
Room4 = "room 4"
Room5 = "room 5"
PlayerInventory = []


""" These are a list of functions i have created which allow me to save time by not having to re-write code"""

# The below function takes the argument of CurrentRoom to print the user a description of the room. 
def DescribeRoom(CurrentRoom):
	if CurrentRoom == Room1:
		print(Room1)
	elif CurrentRoom == Room2:
		print(Room2)
	elif CurrentRoom == Room3:
		print(Room3)
	elif CurrentRoom == Room4:
		print(Room3)
	elif CurrentRoom == Room5:
		print(Room3)

# The current action functions allow the user to interact with the game by inputting commands such as Describe and Items. 
def CurrentActionRoom1():
	Action = input("What would you like to do? ")
	MoveTable = False

	if Action == "describe":
		DescribeRoom(CurrentRoom)
	elif Action == "items":
		print(f"In this room there is {CurrentRoomItems}")
	elif Action == "inventory":
		print(PlayerInventory)
	elif Action == "take bed":
		print("You cannot be serious...")
	elif Action == "take table":
		print("Seriously?")
	elif Action == "move bed":
		print("It is attached to the wall")
	elif Action == "move table" and MoveTable == False:
		MoveTable()
	else:
		print(f"You cant do that {Name}")

def MoveTable():
	x = 1
	
	while x == 1:
		print("You slide the table away from the wall to reveal a paperclip")
		CurrentRoomItems.append(['paperclip'])
		x =+ 1
	
	

# This function prints text slowly in order to make the game more emmersive. 

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)




""" This is where the game code begins"""

#CurrentRoom must be defined in order for the Describe room function to work

CurrentRoom = Room1
CurrentRoomItems.append(['bed' , 'table'])

print_slow("'Well hello there, whats your name?' ")

# The user inputs their name here, this is referenced throughout the game. 

Name = input("")

print_slow(f"'well {Name} I am your keeper and you\'re stuck with me now'\n")

print("The unknown man pulls the sack that has been covering your head and walks away laughing leaving you in an locked cell")

while CurrentRoom == Room1:
	CurrentActionRoom1()

