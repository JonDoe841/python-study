num_of_pages = int(input())
pages_for_one_hour = int(input())
days_needed = int(input())
# logic
time_to_read_book = num_of_pages / pages_for_one_hour
hours_for_day = time_to_read_book / days_needed
print(int(hours_for_day))
