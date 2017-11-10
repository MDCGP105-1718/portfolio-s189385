import sys,time
""" these are data types which store information such as the room desriptions, score and player inventory"""
Room1 = "You are in a small room with no windows and a flickering light above you"
Room1Items = ['bed' , 'table']
Room2 = "room 2"
Room3 = "room 3"
Room4 = "room 4"
Room5 = "room 5"
PlayerInventory = []

""" These are a list of functions i have created which allow me to save time by not having to re-write code"""

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


def CurrentAction():

	Action = input("What would you like to do? ")

	if Action == "Describe":
		DescribeRoom(CurrentRoom)
	elif Action == "Items":
		RoomItems(CurrentRoom)


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def RoomItems(CurrentRoom):
	if CurrentRoom == Room1:
		print(f"Around the room there lies {Room1Items}")

	

""" This is where the game code begins"""

#CurrentRoom must be defined in order for the Describe room function to work

CurrentRoom = Room1

print_slow("'Well hello there, whats your name?' ")

Name = input("")

print_slow(f"'well {Name} I am your keeper and you\'re stuck with me now'\n")

print("The unknown man pulls the sack that has been covering your head and walks away laughing leaving you in an locked cell")

while CurrentRoom == Room1:
	CurrentAction()

