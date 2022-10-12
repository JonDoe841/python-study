import sys
max_num = - sys.maxsize
numbers = 0
loops = int(input())
for num in range(loops):
    number = int(input())
    if number > max_num:
        max_num = number
    numbers += number
diff = abs(numbers - max_num)
if diff == max_num:
    print(f"Yes\nSum = {diff}")
elif diff != max_num:
    diff -= max_num
    print(f"No\nDiff = {abs(diff)}")
