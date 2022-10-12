w = float(input())
h = float(input())
num_of_seats_in_lines = int((h * 100 - 100) / 70)
num_of_lines = int(w * 100 / 120)
num_of_seats = num_of_lines * num_of_seats_in_lines - 3
print(num_of_seats)
