budget = float(input())
season = input()
where = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
        where = "Camp"
    else:
        price = budget * 0.70
        where = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
        where = "Camp"
    else:
        price = budget * 0.80
        where = "Hotel"
elif budget > 1000:
    destination = "Europe"
    price = budget * 0.90
    where = "Hotel"
print(f"Somewhere in {destination}")
print(f" {where} - {price:.2f}")

