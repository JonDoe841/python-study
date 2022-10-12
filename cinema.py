type = input()
rows = int(input())
colons = int(input())
price = 0
if type == "Premiere":
    price = (rows * colons) * 12.00
elif type == "Normal":
    price = (rows * colons) * 7.50
else:
    price = (rows * colons) * 5.00

print(f"{price:.2f} leva")

