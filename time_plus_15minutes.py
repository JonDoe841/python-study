hour = int(input())
minutes = int(input())
hour_passed = hour
minutes_pass = minutes + 15
if minutes_pass >= 60:
    minutes_pass = minutes_pass - 60
    hour_passed = hour + 1
if hour_passed >= 24:
    hour_passed = hour_passed % 24
if minutes_pass < 10:
    print(f"{hour_passed}:0{minutes_pass}")
else:
    print(f"{hour_passed}:{minutes_pass}")