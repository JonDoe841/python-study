num_ppl = int(input())
season = input()
price = 0
if season == "spring":
    if num_ppl <= 5:
        price = 50.00
    elif num_ppl > 5:
        price = 48.00
elif season == "summer":
    if num_ppl <= 5:
        price = 48.50
    elif num_ppl > 5:
        price = 45.00
elif season == "autumn":
    if num_ppl <= 5:
        price = 60.00
    elif num_ppl > 5:
        price = 49.50
if season == "winter":
    if num_ppl <= 5:
        price = 86.00
    elif num_ppl > 5:
        price = 85.00
group_price = price * num_ppl
if season == "summer":
    group_price *= 0.85
elif season == "winter":
    group_price *= 1.08
print(f"{group_price:.2f} leva.")
