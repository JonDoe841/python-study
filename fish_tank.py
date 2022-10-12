long = int(input())
wide = int(input())
tall = int(input())
percent_taken = float(input())
# logic
size = long * wide * tall
size_in_lt = size / 1000
lt_needed = size_in_lt*(1-(percent_taken * 0.01))
print(lt_needed)