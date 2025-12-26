with open("input.txt", "r") as file:
    ranges, ids = file.read().split("\n\n")

ids = [int(id) for id in ids.split()]

id_ranges = []
for range_str in ranges.split():
    start, end = range_str.split("-")
    id_ranges.append( range(int(start), int(end) + 1) )

fresh_ingredients = 0
for id in ids:
    for id_range in id_ranges:
        if id in id_range:
            fresh_ingredients += 1
            break

print(fresh_ingredients)
