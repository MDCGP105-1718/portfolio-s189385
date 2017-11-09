current_savings = 0
total_cost = float(input ("Please enter the cost of your house: £"))
semi_annual_raise = float(input("please input the percentage amount of your semi annual raise as a decimal value "))
portion_deposit = total_cost * .20
print (f"Your need a 20% deposit of £{portion_deposit}")
annual_income = float(input ("Please enter your annual income: £"))
portion_saved = float(input("Please enter the proportion of salary to save in decimals) :"))
r = 0.04
monthly_salary = annual_income / 12
number_of_months = 0

while current_savings < portion_deposit: 
    current_savings = current_savings + current_savings * r /12
    current_savings += monthly_salary * portion_saved
    number_of_months += 1
    if number_of_months % 6 == 0:
    	annual_income += annual_income * semi_annual_raise
    	monthly_salary = annual_income / 12
    	
print(number_of_months)
