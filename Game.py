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

# Room take functions allow the user to interact with the items within the room

def Room1Take():
		
	SelectedItem = input("What item would you like to take? ")

	while SelectedItem in CurrentRoomItems:
		if SelectedItem == "bed":
			print("You cannot be serious...")
		elif SelectedItem == "table":
			print("Seriously?")
		elif SelectedItem == "paperclip":
			PlayerInventory.append(['paperclip'])
			print("hmmm maybe you could pick a lock with that...")
	else:
		print("There is no such item")

# The current action functions allow the user to interact with the game by inputting commands such as Describe and Items. 

def CurrentActionRoom1():
	Action = input("What would you like to do? ")

	if Action == "describe":
		DescribeRoom(CurrentRoom)
	elif Action == "items":
		print(f"In this room there is {CurrentRoomItems}")
	elif Action == "inventory":
		print(PlayerInventory)
	elif Action == "take":
		Room1Take()
	elif Action == "move":
		Room1Move()
	elif Action == "move n":
		print("You move to the north of the room, you come to a small locked door")
	elif Action == "move e":
		print("You move to the east of the room, there is a small bed in the right hand corner.")
	elif Action == "move s":
		print("You move to the south of the room, the only thing you see is a table pushed against the wall")
	elif Action == "move n":
		print("You move to the west of the room, there is nothing here.")
	else:
		print(f"You cant do that {Name}")
	







	
	
	

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

