year_tax = int(input())
shoes_price = year_tax - (year_tax * 0.4)
uniform_price = shoes_price - (shoes_price * 0.2)
ball_price = uniform_price / 4
accessories_price = ball_price / 5
final_price = year_tax + shoes_price + uniform_price + ball_price + accessories_price
print(final_price)