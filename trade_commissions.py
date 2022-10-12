city = input()
sales = float(input())
num = 0
if city == "Sofia":
    if 0 <= sales <= 500:
        num = sales * 0.05
    elif 500 < sales <= 1000:
        num = sales * 0.07
    elif 1000 < sales <= 10000:
        num = sales * 0.08
    elif sales > 10000:
        num = sales * 0.12
if city == "Varna":
    if 0 <= sales <= 500:
        num = sales * 0.045
    elif 500 < sales <= 1000:
        num = sales * 0.075
    elif 1000 < sales <= 10000:
        num = sales * 0.10
    elif sales > 10000:
        num = sales * 0.13
if city == "Plovdiv":
    if 0 <= sales <= 500:
        num = sales * 0.055
    elif 500 < sales <= 1000:
        num = sales * 0.08
    elif 1000 < sales <= 10000:
        num = sales * 0.12
    elif sales > 10000:
        num = sales * 0.145
if num > 0 and city == "Plovdiv" or city == "Varna" or city == "Sofia":
    print(f"{num:.2f}")
else:
    print("error")

