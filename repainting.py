nylon = int(input())
paint = int(input())
thinner = int(input())
hours_for_painter = int(input())
nylon_price = (nylon + 2) * 1.50
paint_price = (paint * 1.1) * 14.50
thinner_price = thinner * 5.00
price_for_bag = 0.40
price_for_all = nylon_price + paint_price + thinner_price + price_for_bag
price_for_painter = (price_for_all * 0.30) * hours_for_painter
final_price = price_for_all + price_for_painter
print(final_price)

