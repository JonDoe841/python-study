num_of_pencil_bags = int(input())
num_of_markers_bags = int(input())
litres_of_detergent = int(input())
percent_discount = int(input())
# logic
price_for_pencils = num_of_pencil_bags * 5.80
price_for_markers = num_of_markers_bags * 7.20
price_for_detergent = litres_of_detergent * 1.20
price_for_all = price_for_detergent + price_for_markers + price_for_pencils
price_with_discount = price_for_all - (price_for_all * (percent_discount /100))
print(price_with_discount)
