num1 = int(input())
num2 = int(input())
operator = input()
result = 0
even_odd = 0
if operator == "-" or operator == "+" or operator == "*":
    if operator == "-":
        result = num1 - num2
    elif operator == "+":
        result = num1 + num2
    elif operator == "*":
        result = num1 * num2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{num1} {operator} {num2} = {result} - {even_odd}")
if operator == "/":
    if num1 == 0 or num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
if operator == "%":
    if num1 == 0 or num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")