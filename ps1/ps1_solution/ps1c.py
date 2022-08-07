# -*- coding: utf-8 -*-
# Housing Hunting: How much should you save each month to afford the down payment in three years?
# Finding the right amount to save away

# Initialize some sate variables
starting_annual_salary = float(input("Enter the starting salary: "))

semi_annual_raise = 0.07
annual_return = 0.04
portion_down_payment = 0.25
total_cost = 1000000
down_payment = total_cost * portion_down_payment
monthly_return  = annual_return / 12
current_savings = 0
low = 0
high =10000
epsilon = 100
steps = 0 

# e.g. Anything between 250000 and 250100---break loop and show result
while abs(current_savings - down_payment) >= epsilon:
    current_savings = 0
    guess_rate = (low + high) // 2
    rate = guess_rate / 10000
    print(rate)
    current_annual_salary = starting_annual_salary
    # Calculating savings
    for months in range(36):
        if months % 6 == 0 and months != 0:
            current_annual_salary += current_annual_salary * semi_annual_raise
        monthly_salary = current_annual_salary / 12       
        current_savings += rate * monthly_salary  + current_savings * monthly_return
    # Bisection search    
    if current_savings < down_payment:
        low = guess_rate
    else:
        high = guess_rate
    guess_rate = (low + high)//2
    steps += 1
    # log(2,100)> 13, when it reaches 14 guesses, it breaks out of the loop. 
    if steps > 13:
        break

# Output control:  
if steps > 13:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best saving rate: ", rate)            
    print("Steps in bisection search: ", steps)



