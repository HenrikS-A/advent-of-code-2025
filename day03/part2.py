with open("input.txt", "r") as file:
    battery_banks = file.read().splitlines()

total_joltage = 0
for bank in battery_banks:

    bank_joltage = ""
    start_index = 0

    for remaining in range(12, 0, -1):
        end_index = len(bank) - remaining + 1
        sequence = bank[start_index : end_index]
        joltage = max(sequence) 

        start_index += sequence.index(joltage) + 1
        bank_joltage += joltage

    total_joltage += int(bank_joltage)

print(total_joltage)
