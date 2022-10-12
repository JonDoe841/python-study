num_groups = int(input())
musala = 0
monblan = 0
kilimindjaro = 0
k2 = 0
everest = 0
ppl = 0
for groups in range(num_groups):
    num_ppl = int(input())
    ppl += num_ppl
    if num_ppl <= 5:
        musala += num_ppl
    elif num_ppl <= 12:
        monblan += num_ppl
    elif num_ppl <= 25:
        kilimindjaro += num_ppl
    elif num_ppl <= 40:
        k2 += num_ppl
    elif num_ppl >= 41:
        everest += num_ppl
musala = (musala / ppl) * 100
monblan = (monblan / ppl) * 100
kilimindjaro = (kilimindjaro / ppl) * 100
k2 = (k2 / ppl) * 100
everest = (everest / ppl) * 100
print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimindjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")