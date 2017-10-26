number_of_nights = float(input("Please enter the number of nights you wish to stay "))
destination = float(input("Please select the number of your destination \n 1 : New York \n 2 : Auckland \n 3 : Venice \n 4 : Glasgow \n "))


def hotel_cost(nights):
	total_hotel_cost = nights * 70
	print(f"The total cost for your stay will be £{total_hotel_cost}")
	return total_hotel_cost

def plane_ticket_cost(flight_dest, ticket_class):
	NewYork = 2000
	Auckland = 790
	Venice = 154
	Glasgow = 65
	plane_ticket_price = 0
	if flight_dest == 1:
		plane_ticket_price = NewYork
	elif flight_dest == 2:
		plane_ticket_price = Auckland
	elif flight_dest == 3:
		plane_ticket_price = Venice
	elif flight_dest == 4:
		plane_ticket_price = Glasgow
	print(f"Your flights will cost you £{plane_ticket_price}")
	return(plane_ticket_price)

def car_hire_cost():
	days_rented = float(input("Please input the number of days you wish to rent the car "))
	cost_of_rental = days_rented * 30
	if days_rented >= 7:
		cost_of_rental = cost_of_rental - 50
	if days_rented >= 3 and days_rented < 7 :
		cost_of_rental = cost_of_rental - 30
	return(cost_of_rental)

total_cost = 0
total_cost += hotel_cost(number_of_nights)
total_cost += plane_ticket_cost(destination, 1)
total_cost += car_hire_cost()


print(total_cost)





