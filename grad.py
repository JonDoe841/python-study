name = input()
grade = 0
current_grade = 0
all_nums = 0
times_failed = 0
while grade <= 11:
    current_grade = float(input())
    all_nums += current_grade
    if current_grade < 4.00:
        times_failed += 1
        if times_failed > 1:
            break
    grade += 1
av_grade = all_nums / grade
if times_failed < 2:
    print(f"{name} graduated. Average grade: {av_grade:.2f}")
elif times_failed > 1:
    print(f"{name} has been excluded at {grade} grade")
