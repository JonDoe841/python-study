actor_name = input()
actor_points = float(input())
num_ppl = int(input())
for num in range(num_ppl):
    name_jury = input()
    jury_points = float(input())
    name_num = len(name_jury)
    actor_points += ((name_num * jury_points)/2)
    if actor_points > 1250.5:
        break
points_needed = abs(actor_points - 1250.5)
if actor_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
elif actor_points < 1250.5:
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")
