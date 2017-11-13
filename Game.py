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
		print(CurrentRoomItems)
	elif Action == "Interact":
		ItemSelector()
	elif Action == "Inventory":
		print(PlayerInventory)
	else:
		print(f"You cant do that {Name}")

def ItemSelector():
	n = 0
while n <= 7:
	x = input("What would you like to Interact with?")
	n = n+1
	if x in CurrentRoomItems:
		print("ok")
	if x not in CurrentRoomItems:
		print("ValueError: ",x, "is not in list")



	

	





def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)




""" This is where the game code begins"""

#CurrentRoom must be defined in order for the Describe room function to work

CurrentRoom = Room1
CurrentRoomItems.append(['Bed' , 'Table'])

print_slow("'Well hello there, whats your name?' ")

Name = input("")

print_slow(f"'well {Name} I am your keeper and you\'re stuck with me now'\n")

print("The unknown man pulls the sack that has been covering your head and walks away laughing leaving you in an locked cell")

while CurrentRoom == Room1:
	CurrentAction()

