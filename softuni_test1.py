import math
num_missing = int(input())
food_kg = int(input())
first_deer_food_kg = float(input())
second_deer_food_kg = float(input())
third_deer_food_kg = float(input())
first_deer_food = num_missing * first_deer_food_kg
second_deer_food = num_missing * second_deer_food_kg
third_deer_food = num_missing * third_deer_food_kg
food_needed = first_deer_food + second_deer_food + third_deer_food
food_left = abs(food_needed - food_kg)
if food_needed <= food_kg:
    print(f"{math.floor(food_left):.0f} kilos of food left.")
elif food_needed > food_kg:
    print(f"{math.ceil(food_left):.0f} more kilos of food are needed.")