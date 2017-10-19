semi_annual_raise = 0.7
annual_interest_rate = 0.04
cost_of_house = 1000000
down_payment = cost_of_house * 0.25
annual_salary = 150000
months_to_save = 36
current_savings = 0
portion_saved = 0.10
number_of_months = 0
low = 0 
high = 10000
epsilon = 100
monthly_salary = annual_salary / 12

while current_savings < down_payment: 
    current_savings = current_savings + current_savings * annual_interest_rate /12
    current_savings += monthly_salary * portion_saved
    number_of_months += 1
    if number_of_months % 6 == 0:
    	annual_salary += annual_salary * semi_annual_raise
    	monthly_salary = annual_salary / 12
    	
print(number_of_months)

