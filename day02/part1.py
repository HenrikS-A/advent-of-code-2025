with open("input.txt", "r") as file:
    ranges = file.read().strip("\n").split(",")

invalid_ids = []
for id_range in ranges:
    first_id, last_id = id_range.split("-")

    for id in range(int(first_id), int(last_id)+1):
        id_str = str(id)
        first_half, second_half = id_str[:len(id_str)//2], id_str[len(id_str)//2:]
        if first_half == second_half:
            invalid_ids.append(id)

print(sum(invalid_ids))
