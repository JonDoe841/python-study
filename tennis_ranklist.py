num_tournament = int(input())
starting_tournament_points = int(input())
tournament_points = 0
percent_num = 0
for num in range(num_tournament):
    tournament_place = input()
    if tournament_place == "W":
        tournament_points += 2000
        percent_num += 1
    elif tournament_place == "F":
        tournament_points += 1200
    elif tournament_place == "SF":
        tournament_points += 720
average_points = tournament_points / num_tournament
percent = (percent_num / num_tournament) * 100
tournament_points = tournament_points + starting_tournament_points
print(f"Final points: {tournament_points}")
print(f"Average points: {int(average_points)}")
print(f"{percent:.2f}%")