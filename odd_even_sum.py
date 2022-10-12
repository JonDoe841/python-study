num_of_loops = int(input())
even_num = 0
odd_num = 0
for num in range(1, num_of_loops +1):
    nums = int(input())
    if num % 2 == 0:
        even_num += nums
    elif num % 2 != 0:
        odd_num += nums
diff = abs(even_num - odd_num)
if even_num == odd_num:
    print(f"Yes\nSum = {even_num}")
elif even_num != odd_num:
    print(f"No\nDiff = {diff}")