import sys
nums = int(input())
min_num = sys.maxsize
max_num = -sys.maxsize
for num in range(nums):
    number = int(input())
    if number > max_num:
        max_num = number
    elif number < min_num:
        min_num = number
print(f"Max number: {max_num}\nMin number: {min_num}")