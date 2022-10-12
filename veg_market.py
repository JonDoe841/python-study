price_for_veg = float(input())
price_for_fruit = float(input())
kg_veg = int(input())
kg_fruit = int(input())
final_veg_price = price_for_veg * kg_veg
final_fruit_price = price_for_fruit * kg_fruit
final_price = final_fruit_price + final_veg_price
bgn_to_euro = final_price / 1.94
print(format(bgn_to_euro, ".2f"))
