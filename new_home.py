flower = input()
flower_num = int(input())
budget = int(input())
expenses = 0
if flower == "Roses":
    expenses = 5 * flower_num
    if flower_num > 80:
        expenses = expenses * 0.90
elif flower == "Dahlias":
    expenses = 3.80 * flower_num
    if flower_num > 90:
        expenses = expenses * 0.85
elif flower == "Tulips":
    expenses = 2.80 * flower_num
    if flower_num > 80:
        expenses = expenses * 0.85
elif flower == "Narcissus":
    expenses = 3 * flower_num
    if flower_num < 120:
        expenses = expenses * 1.15
elif flower == "Gladiolus":
    expenses = 2.50 * flower_num
    if flower_num < 80:
        expenses = expenses * 1.20
final_price = abs(expenses - budget)
if budget >= expenses:
    print(f"Hey, you have a great garden with {flower_num} {flower} and {final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price:.2f} leva more.")


