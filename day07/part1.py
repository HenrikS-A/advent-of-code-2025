with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def will_split(lines: list[str], y_pos: int, x_pos: int) -> bool:
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

split_count = 1 # First split at the top

for y in range(4, len(lines), 2):
    for x in range(len(lines[0])):
        if lines[y][x] == "^":
            split_count += 1 if will_split(lines, y, x) else 0

print(split_count)
