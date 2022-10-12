film_budget = float(input())
num_statist = int(input())
price_for_costumes = float(input())
decor_price = film_budget * 0.10
costume_price = num_statist * price_for_costumes
if num_statist > 150:
    costume_price *= 0.9
film_price = costume_price + decor_price
money_left = format(abs(film_budget - film_price), ".2f")
if film_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {money_left} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left} leva left.")