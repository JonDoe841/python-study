num = input()
highest_num = -100000000
while num != "Stop":
    if int(num) > int(highest_num):
        highest_num = num
    num = input()
print(highest_num)