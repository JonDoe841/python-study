num = input()

first_digit = int(num[2])
second_digit = int(num[1])
third_digit = int(num[0])
for number1 in range(1, first_digit + 1):
    for number2 in range(1, second_digit + 1):
        for number3 in range(1, third_digit + 1):
            result = number1 * number2 * number3
            print(f"{number1} * {number2} * {number3} = {result};")