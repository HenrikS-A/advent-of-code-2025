with open("input.txt", "r") as file:
    lines = file.read().splitlines()

dial = 50
zero_count = 0
for line in lines:
    direction, distance = line[0], int(line[1:])

    if direction == "L":
        if dial-(distance%100) < 0 and dial != 0:
            zero_count += 1

        dial -= distance
    elif direction == "R":
        if dial+(distance%100) > 100:
            zero_count += 1

        dial += distance
    dial %= 100

    zero_count += distance//100
    if dial == 0:
        zero_count += 1

print(zero_count)
