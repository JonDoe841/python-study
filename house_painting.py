x_tall = float(input())
y_long = float(input())
h_tall = float(input())
windows = 1.5 * 1.5
door = 1.2 * 2
both_sides = ((x_tall * y_long) * 2) - windows * 2
back_and_front = ((x_tall * x_tall) * 2) - door
area_of_walls = both_sides + back_and_front
lt_green = area_of_walls / 3.4
print(format(lt_green, ".2f"))
roof_both_sides = (x_tall * y_long) * 2
roof_math = 2 * (x_tall * h_tall / 2)
area_of_roof = roof_math + roof_both_sides
lt_red = area_of_roof / 4.3
print(format(lt_red, ".2f"))
