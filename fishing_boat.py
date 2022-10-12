budget = int(input())
season = input()
buddies = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Winter":
    boat_rent = 2600
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200

if buddies <= 6:
    boat_rent = boat_rent * 0.90
elif 7 <= buddies <= 11:
    boat_rent = boat_rent * 0.85
elif buddies >= 12:
    boat_rent = boat_rent * 0.75

if buddies % 2 == 0 and season != "Autumn":
    boat_rent = boat_rent * 0.95

rest = abs(budget - boat_rent)
if budget >= boat_rent:
    print(f"Yes! You have {rest:.2f} leva left.")
elif budget < boat_rent:
    print(f"Not enough money! You need {rest:.2f} leva.")
