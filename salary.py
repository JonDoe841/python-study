num_tabs_open = int(input())
salary = int(input())
for num in range(num_tabs_open):
    tabs_open = input()
    if tabs_open == "Facebook":
        salary -= 150
    elif tabs_open == "Instagram":
        salary -= 100
    elif tabs_open == "Reddit":
        salary -= 50
if salary <= 0:
    print("You have lost your salary.")
elif salary > 0:
    print(salary)