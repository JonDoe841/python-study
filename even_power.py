n = int(input())
for power_of in range(n + 1):
    if power_of % 2 == 0:
        result = 2 ** power_of
        print(result)