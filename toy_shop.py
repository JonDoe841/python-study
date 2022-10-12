trip_prize = float(input())
num_jigsaw = int(input())
num_talking_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

price_jigsaw = num_jigsaw * 2.60
price_talking_doll = num_talking_dolls * 3
price_teddy_bear = num_teddy_bears * 4.10
price_minions = num_minions * 8.20
price_truck = num_trucks * 2

num_of_toys = num_trucks + num_minions + num_jigsaw + num_teddy_bears + num_talking_dolls
all_price = price_truck + price_minions + price_jigsaw + price_teddy_bear + price_talking_doll
money_left = all_price
if num_of_toys >= 50:
    discount = all_price * 0.25
    money_left = all_price - discount
rent = money_left * 0.10
final_sum = money_left - rent
if float(final_sum) >= trip_prize:
    final_sum = format(float(final_sum) - trip_prize, ".2f")
    print(f"Yes! {final_sum} lv left.")
else:
    not_enough = format(trip_prize - final_sum, ".2f")
    print(f"Not enough money! {not_enough} lv needed.")
