with open("input.txt", "r") as file:
    ranges = file.read().strip("\n").split(",")

invalid_total = 0
for id_range in ranges:
    first_id, last_id = id_range.split("-")

    for current_id in range(int(first_id), int(last_id)+1): 
        id_str = str(current_id)

        # A sequence cannot repeat at least twice if its lenght 
        # is more than half of the lenght of the full id
        for sequence_len in range(1, len(id_str)//2 + 1):
            sequence = id_str[:sequence_len]
            expected_repetitions = len(id_str) / len(sequence)
            actual_repetitions = id_str.count(sequence)

            if actual_repetitions == expected_repetitions:
                invalid_total += current_id
                break

print(invalid_total)
