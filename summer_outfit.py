temp = int(input())
time = input()
drip = ""
shoes = ""
if time == "Morning":
    if 10 <= temp <= 18:
        drip = "Sweatshirt"
        shoes = "Sneakers"
    if 18 <= temp <= 24:
        drip = "Shirt"
        shoes = "Moccasins"
    if temp >= 25:
        drip = "T-Shirt"
        shoes = "Sandals"
elif time == "Afternoon":
    if 10 <= temp <= 18:
        drip = "Shirt"
        shoes = "Moccasins"
    if 18 <= temp <= 24:
        drip = "T-Shirt"
        shoes = "Sandals"
    if temp >= 25:
        drip = "Swim Suit"
        shoes = "Barefoot"
elif time == "Evening":
    if 10 <= temp <= 18:
        drip = "Shirt"
        shoes = "Moccasins"
    if 18 <= temp <= 24:
        drip = "Shirt"
        shoes = "Moccasins"
    if temp >= 25:
        drip = "Shirt"
        shoes = "Moccasins"
print(f"It's {temp} degrees, get your {drip} and {shoes}.")