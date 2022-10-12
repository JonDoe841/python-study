product = input()
city = input()
num = float(input())
price = 0
if city == "Sofia":
    if product == "coffee":
        price = num * 0.50
    elif product == "water":
        price = num * 0.80
    elif product == "beer":
        price = num * 1.20
    elif product == "sweets":
        price = num * 1.45
    elif product == "peanuts":
        price = num * 1.60
if city == "Plovdiv":
    if product == "coffee":
        price = num * 0.40
    elif product == "water":
        price = num * 0.70
    elif product == "beer":
        price = num * 1.15
    elif product == "sweets":
        price = num * 1.30
    elif product == "peanuts":
        price = num * 1.50
if city == "Varna":
    if product == "coffee":
        price = num * 0.45
    elif product == "water":
        price = num * 0.70
    elif product == "beer":
        price = num * 1.10
    elif product == "sweets":
        price = num * 1.35
    elif product == "peanuts":
        price = num * 1.55
print(price)
