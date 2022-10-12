days = 1
top = 8848
text = input()
goal = 5364
while goal < top or text == "END":
    climbed = int(input())
    if text == "Yes":
        days += 1
    if days > 5:
        break
    goal += climbed
    text = input()
if goal >= top:
    print(f"Goal reached for {days} days!")
elif goal < top:
    print("Failed!")
    print(f"{goal}")
