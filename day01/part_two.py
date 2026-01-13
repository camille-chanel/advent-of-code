#
#    Advent of Code 2025
#    Day 1, Part 2: Secret Entrance
#

from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
position = 50
times_passed_zero = 0

with open(file_path, "r") as file:
    for line in file: 
        rotation_num = int(line[1:])
        if line[0] == 'R':
            times_passed_zero += (position + rotation_num) // 100 
            position = (position + rotation_num) % 100
        else:                  
            times_passed_zero += (((position - rotation_num) // 100) * -1) - 1
            position = (position - rotation_num) % 100
            #if position == 0:
                #times_passed_zero += 1

print(times_passed_zero)
