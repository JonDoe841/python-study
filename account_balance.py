num = input()
total = 0
while num != "NoMoreMoney":
    num = float(num)
    if num < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {num:.2f}")
    total += num
    num = input()
print(f"Total: {total:.2f}")