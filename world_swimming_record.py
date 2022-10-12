record_sec = float(input())
meters = float(input())
meters_moved_for_sec = float(input())
delay = (meters // 15) * 12.5
final_time = (meters * meters_moved_for_sec) + delay
if final_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    seconds = abs(final_time - record_sec)
    print(f"No, he failed! He was {seconds:.2f} seconds slower.")