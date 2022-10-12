from math import pi
figure = input()
if figure == "square":
    num = float(input())
    result = num * num
elif figure == "rectangle":
    num1 = float(input())
    num2 = float(input())
    result = num1 * num2
elif figure == "circle":
    num = float(input())
    result = pi * (num ** 2)
elif figure == "triangle":
    num1 = float(input())
    num2 = float(input())
    result = num1 * num2 / 2
print(format(result, ".3f"))
