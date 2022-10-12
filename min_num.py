num = input()
smallest_num = +100000000
while num != "Stop":
    num = int(num)
    if num < smallest_num:
        smallest_num = num
    elif num > smallest_num:
        pass
    num = input()
print(smallest_num)