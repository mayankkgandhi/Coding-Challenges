def get_total_cost_of_meal():
    meal_cost = float(raw_input())
    tip_percent = int(raw_input())
    tax_percent = int(raw_input())
    
    tip =(meal_cost * tip_percent)/100
    tax =(meal_cost * tax_percent)/100
    total_cost = int(round(meal_cost+tip+tax))
    return str(total_cost)

print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")
