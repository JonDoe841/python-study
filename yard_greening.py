num_of_square_meters = float(input())
price_for_square_meters = num_of_square_meters * 7.61
discount = price_for_square_meters * 0.18
final_price_for_square_meters = price_for_square_meters - discount
print(f"The final price is: {final_price_for_square_meters} lv.")
print(f"The discount is: {discount} lv.")
