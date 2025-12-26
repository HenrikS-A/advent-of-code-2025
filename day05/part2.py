with open("input.txt", "r") as file:
    ranges = file.read().split("\n\n")[0]

id_ranges = []
for range_str in ranges.split():
    start, end = range_str.split("-")
    id_ranges.append((int(start), int(end)))

id_ranges.sort()

fresh_ingredients = 0
current_start, current_end = id_ranges[0]

# After sorting, each new range can either start a new separate range
# or merge with the current range by (possibly) extending the current range end-point
for start, end in id_ranges[1:]:

    # New separate range, add up the previous range
    if start > current_end + 1:
        fresh_ingredients += current_end - current_start + 1
        current_start, current_end = start, end
    
    # The start-point is inside the current range.
    # Now we want the largest end-point. 
    # The intervall can be fully inside the current range, or extend the current range
    else:
        current_end = max(current_end, end)

# Add up the last range
fresh_ingredients += current_end - current_start + 1

print(fresh_ingredients)
