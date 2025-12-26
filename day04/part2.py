with open("input.txt", "r") as file:
    lines = file.read().splitlines()

lines = [list(line) for line in lines]

change = True
removable_rolls = 0

while change:

    change = False
    new_diagram = [line.copy() for line in lines]

    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):

            if symbol != "@":
                continue
            
            adjacent_rolls = 0

            # Above
            if y > 0:
                # Above
                if lines[y-1][x] == "@":
                    adjacent_rolls += 1


                # Above left
                if x > 0:
                    if lines[y-1][x-1] == "@":
                        adjacent_rolls += 1

                # Above right
                if x < len(line) - 1:
                    if lines[y-1][x+1] == "@":
                        adjacent_rolls += 1

            # Left
            if x > 0:
                if line[x-1] == "@":
                    adjacent_rolls += 1

            # Right
            if x < len(line) - 1:
                if line[x+1] == "@":
                    adjacent_rolls += 1

            # Bellow
            if y < len(lines) - 1:
                # Bellow
                if lines[y+1][x] == "@":
                    adjacent_rolls += 1
                
                # Bellow left
                if x > 0:
                    if lines[y+1][x-1] == "@":
                        adjacent_rolls += 1

                # Bellow right
                if x < len(line) - 1:
                    if lines[y+1][x+1] == "@":
                        adjacent_rolls += 1

            
            if adjacent_rolls < 4:
                new_diagram[y][x] = "x"

                removable_rolls += 1
                change = True
    
    lines = new_diagram

print(removable_rolls)
