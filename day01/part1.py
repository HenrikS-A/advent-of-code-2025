with open("input.txt", "r") as file:
    lines = file.read().splitlines()

dial = 50
zero_count = 0
for line in lines:
    direction, distance = line[0], int(line[1:])
    
    if direction == "L":
        dial -= distance
    elif direction == "R":
        dial += distance
    dial %= 100
    
    if dial == 0:
        zero_count += 1

print(zero_count)
