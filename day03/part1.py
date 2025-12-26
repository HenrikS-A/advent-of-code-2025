with open("input.txt", "r") as file:
    battery_banks = file.read().splitlines()

total_joltage = 0
for bank in battery_banks:
    first_max = max(bank[:-1]) # exclude last element
    first_max_index = bank.index(first_max)

    second_max = max(bank[first_max_index + 1:])

    total_joltage += int(first_max + second_max)

print(total_joltage)
