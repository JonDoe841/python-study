num_chicken_menu = int(input())
num_fish_menu = int(input())
num_veg_menu = int(input())
# logic
chicken_price = num_chicken_menu * 10.35
fish_price = num_fish_menu * 12.40
veg_price = num_veg_menu * 8.15
price_for_all = chicken_price + fish_price + veg_price
dessert_price = price_for_all * 0.20
delivery = 2.50
final_price = price_for_all + dessert_price + delivery
print(final_price)