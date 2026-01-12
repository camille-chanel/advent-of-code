#
#    Advent of Code 2025
#    Day 1, Part 1: Secret Entrance
#

from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
position = 50
count_at_zero = 0
# file = open(file_path, "r")
# then you would have to close manually
# file.close()

# this will automatically close the file outside the block
with open(file_path, "r") as file:
    for line in file: # each line is "L" or "R" then a number [1, 99]
        rotation_num = int(line[1:])
        if line[0] == 'R':
            position = (position + rotation_num) % 100
        else:                  # line[0] is 'L'
            position = (position - rotation_num) % 100
        
        if position == 0:
            count_at_zero += 1

print(count_at_zero)
