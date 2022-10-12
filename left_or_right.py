number = int(input())
left_sum = 0
right_sum = 0
for num in range(number):
    nums = int(input())
    left_sum += nums
for num in range(number):
    nums = int(input())
    right_sum += nums
if left_sum != right_sum:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
elif left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")