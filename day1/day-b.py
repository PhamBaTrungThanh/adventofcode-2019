import math


def fuel_for_fuel(fuel):
    fuel_to_add = math.floor(int(fuel) / 3) - 2
    if (fuel_to_add > 0):
        fuel_to_add += fuel_for_fuel(fuel_to_add)
    if (fuel_to_add < 0):
        return 0
    return fuel_to_add


DAY_1_OUTPUT = 3256114

input_file = open('./day1_input.txt', 'r')

day1_input = input_file.read()

fuel_input = day1_input.split("\n")

total = 0
for fuel in fuel_input:
    if '' == fuel:
        continue
    fuel = math.floor(int(fuel) / 3) - 2
    total = total + fuel + fuel_for_fuel(fuel)


print(total)
