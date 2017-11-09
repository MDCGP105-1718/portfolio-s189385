low_value = int(input("please input the lowest value"))
high_value = int(input("please input the highest value"))

for i in range(low_value,high_value):
	if i % 3 == 0 and i % 5 == 0:
		print("FIZZBUZZ")
	elif i % 3 == 0:
		print("FIZZ")
	elif i % 5 == 0:
		print("BUZZ")
	else:
		print(i)

