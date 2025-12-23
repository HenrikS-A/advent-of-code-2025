with open("input.txt", "r") as file:
    ranges = file.read().strip("\n").split(",")

invalid_total = 0
for id_range in ranges:
    first_id, last_id = id_range.split("-")

    for current_id in range(int(first_id), int(last_id)+1):
        id_str = str(current_id)
        first_half, second_half = id_str[:len(id_str)//2], id_str[len(id_str)//2:]
        if first_half == second_half:
            invalid_total += current_id

print(invalid_total)
