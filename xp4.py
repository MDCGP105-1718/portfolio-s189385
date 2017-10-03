
my_name = 'Alex Jacobs'
my_age = 19 
my_height = 73 # inches
my_weight = 14 # Stone
my_eyes = 'blue'
my_hair = 'Blonde'
is_heavy = my_weight > 3000
print(f"Let's talk about {my_name}.")
print(f"He is {my_height} inches tall.")
print(f"He's {my_weight} stone in weight.")
print(f"It is {is_heavy} that he is overweight.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}")

#inches to centimeters

inches = 2

print(inches * 2.54) 

#pounds into kilograms

pounds = 1

print(pounds / 2.2)

"""The "is heavy variable" works by calculating if the weight is larger than 3000 regardless of unit of measurement
if the test returns true than the variable is equal to true when it is called later on in the code. the same is true if the code returns false"""