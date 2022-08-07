# -*- coding: utf-8 -*-
# Housing Hunting:determing how long it will take you to save enough money to make the down payment
# Saving, with a raise every six months

# Initialize some sate variables
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

r = 0.04
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

monthly_salary = annual_salary / 12
monthly_return  = r/12

current_savings = 0
months = 0

while current_savings <= down_payment:  
    if months % 6 == 0 and months != 0:
        monthly_salary += monthly_salary * semi_annual_raise
    current_savings += portion_saved * monthly_salary  + current_savings * monthly_return
    months += 1
    
print("Number of months: ", months)