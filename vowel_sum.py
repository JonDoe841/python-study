text = input()
a = 1
e = 2
i = 3
o = 4
u = 5
points = 0
for letters in text:
    if letters == "a":
        points += a
    elif letters == "e":
        points += e
    elif letters == "i":
        points += i
    elif letters == "o":
        points += o
    elif letters == "u":
        points += u
print(points)