import math

input_file = open('./day1_input.txt', 'r')

day1_input = input_file.read()

fuel_input = day1_input.split("\n")

total = 0
for fuel in fuel_input:
    if '' == fuel:
        continue
    total += math.floor(int(fuel) / 3) - 2

print(total)
