from random import randint

number = randint(1,10)
guess = int(input("please enter a guess between 1 and 10 "))
number_of_guesses = 0

while number != guess:
	if number > guess:	
		print("Your guess was too small")
	elif number < guess:
		print("Your guess was too big")
	guess = int(input("please enter a guess between 1 and 10 "))
	number_of_guesses = number_of_guesses + 1	
else:
	print("your guess was correct !")
	print(f"you took {number_of_guesses} guesses")




