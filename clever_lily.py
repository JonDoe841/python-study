years = int(input())
washing_machin_price = float(input())
toy_price = int((input()))
money_saved = 0
money = 0
toys = 0
num_year = 0
for year in range(1, years + 1):
    if year % 2 == 0:
        money += 10
        money_saved += money
        money_saved -= 1
    elif year % 2 != 0:
        toys += 1
money_saved = (toys * toy_price) + money_saved
rest = abs(money_saved - washing_machin_price)
if money_saved >= washing_machin_price:
    print(f"Yes! {rest:.2f}")
elif money_saved < washing_machin_price:
    print(f"No! {rest:.2f}")