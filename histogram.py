num_of_nums = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for num in range(num_of_nums):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    elif number >= 800:
        p5 += 1
percents_p1 = p1 / num_of_nums * 100
percents_p2 = p2 / num_of_nums * 100
percents_p3 = p3 / num_of_nums * 100
percents_p4 = p4 / num_of_nums * 100
percents_p5 = p5 / num_of_nums * 100
print(f"{percents_p1:.2f}%\n{percents_p2:.2f}%\n{percents_p3:.2f}%\n"
      f"{percents_p4:.2f}%\n{percents_p5:.2f}%")