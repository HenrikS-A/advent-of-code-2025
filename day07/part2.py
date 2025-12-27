# My attemt at recursion failed.
# Therefore this monstrosity was created

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def will_split(lines: list[list], y_pos: int, x_pos: int) -> bool:
    # Goes upwards through previous rows and looks for splitters on each side
    for y in range(y_pos - 2, 1, -2):

        if lines[y][x_pos - 1] == "^":
            return True
        if lines[y][x_pos + 1] == "^":
            return True

        # A splitter above in the same x position blocks the current splitter,
        # so no tachyon will reach it
        if lines[y][x_pos] == "^":
            return False

lines = [list(line) for line in lines]

# Build up the number of paths by going through the manifold row by row
for y in range(2, len(lines), 2):
    for x in range(len(lines[y])):

        if lines[y][x] == "^":
            if will_split(lines, y, x) or lines[y - 2][x] == "S":

                above = lines[y - 1][x]
                if above != "." and above > 1:
                    paths_here = above
                else:
                    paths_here = 1

                # Left split
                if lines[y + 1][x - 1] != ".":
                    lines[y + 1][x - 1] += paths_here
                else:
                    lines[y + 1][x - 1] = above if above != "." else 1

                # Right split
                if lines[y + 1][x + 1] != ".":
                    lines[y + 1][x + 1] += paths_here
                else:
                    lines[y + 1][x + 1] = above if above != "." else 1

        elif lines[y][x] == ".":
            above = lines[y - 1][x]

            # Move the value along towards the bottom
            if above != ".":
                if lines[y + 1][x] != ".":
                    lines[y + 1][x] += above
                else:
                    lines[y + 1][x] = above

timeline = 0

for value in lines[-1]:
    if value != ".":
        timeline += value
    
print(timeline)
