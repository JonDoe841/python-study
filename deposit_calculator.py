deposit_num = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())

# logic

math_part1 = deposit_num * (annual_interest_rate / 100)
math_part2 = math_part1 / 12
math_final = deposit_num + term_of_the_deposit * math_part2

print(math_final)
