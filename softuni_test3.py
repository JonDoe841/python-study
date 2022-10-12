num_days = int(input())
temp_l = 0
rakiq = 0
for num in range(num_days):
    rakiq_amount = float(input())
    rakiq += rakiq_amount
    rakiq_temp = float(input())
    temp_l += rakiq_amount * rakiq_temp
final_temp = temp_l / rakiq
print(f"Liter: {rakiq:.2f}")
print(f"Degrees: {final_temp:.2f}")
if final_temp < 38:
    print("Not good, you should baking!")
elif final_temp <= 42:
    print("Super!")
elif final_temp > 42:
    print("Dilution with distilled water!")