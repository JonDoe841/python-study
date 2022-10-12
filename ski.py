day_stayed = int(input())-1
type_room = input()
positive_negative = input()
price = 0
if type_room == "room for one person":
    price = 18.00 * day_stayed
elif type_room == "apartment":
    price = 25.00 * day_stayed
    if day_stayed < 10:
        price *= 0.70
    elif 10 <= day_stayed <= 15:
        price *= 0.65
    elif day_stayed > 15:
        price *= 0.50
elif type_room == "president apartment":
    price = 35.00 * day_stayed
    if day_stayed < 10:
        price *= 0.90
    elif 10 <= day_stayed <= 15:
        price *= 0.85
    elif day_stayed > 15:
        price *= 0.80
if positive_negative == "positive":
    price *= 1.25
elif positive_negative == "negative":
    price *= 0.90
print(f"{price:.2f}")