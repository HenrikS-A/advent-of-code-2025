with open("input.txt", "r") as file:
    lines = file.read().splitlines()

red_tiles = [[int(value) for value in line.split(",")] for line in lines]

max_area = 0
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]

        # Add 1 because the area is measured in grid tiles and includes
        # both corner tiles, not just the geometric area
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > max_area:
            max_area = area

print(max_area)
