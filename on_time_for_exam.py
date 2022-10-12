exam_hour = int(input())
exam_minute = int(input())
arrived_hour = int(input())
arrived_minute = int(input())

exam_time = (exam_hour * 60) + exam_minute
arrived = (arrived_hour * 60) + arrived_minute
dif = abs(exam_time - arrived)

if arrived > exam_time:
    if dif < 60:
        print(f"Late\n{dif} minutes after the start")
    elif dif >= 60:
        hour = dif // 60
        minute = dif % 60
        if minute < 10:
            print(f"Late\n{hour}:0{minute} hours after the start")
        elif minute >= 10:
            print(f"Late\n{hour}:{minute} hours after the start")

elif exam_time == arrived or dif <= 30:
    print("On time")
    if 1 <= dif <= 30:
        print(f"{dif} minutes before the start")
elif exam_time > arrived or dif > 30 or exam_time != arrived:
    if dif < 60:
        print(f"Early\n{dif} minutes before the start")
    elif dif >= 60:
        hour = dif // 60
        minute = dif % 60
        if minute < 10:
            print(f"Early\n{hour}:0{minute} hours before the start")
        elif minute >= 10:
            print(f"Early\n{hour}:{minute} hours before the start")

