skumriq = float(input())
cacata = float(input())
kolichestvo_palamud = float(input())
kolichestvo_safrid = float(input())
kolichestvo_midi = float(input())
math_for_palamud = kolichestvo_palamud * (skumriq * 1.6)
math_for_safrid = kolichestvo_safrid * (cacata * 1.8)
math_for_midi = kolichestvo_midi * 7.50
final_price = math_for_safrid + math_for_midi + math_for_palamud
print(format(final_price, ".2f"))
