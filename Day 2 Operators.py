def total_cost_cal():

    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    tip_amount = meal_cost * tip_percent / 100
    tax_amount = meal_cost * tax_percent / 100

    total_cost = round(meal_cost + tip_amount + tax_amount)

    return str(total_cost)



# Print result
print(total_cost_cal())


#Method 2. We can use one line to get the total coast of a meal
'''
print(round (float(input()) * (1+int(input())*.01+int(input())*.01)))

#the first input: meal cost
#the second input: tip percent
#the third input: tax percent
'''

