cel = float(input())
if cel <= 5.00:
    print("unknown")
elif cel <= 11.9:
    print("Cold")
elif cel <= 14.9:
    print("Cool")
elif cel <= 20.00:
    print("Mild")
elif cel <= 25.9:
    print("Warm")
elif cel <= 35.00:
    print("Hot")
else:
    print("unknown")
