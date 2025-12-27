with open("input.txt", "r") as file:
    lines = file.read().splitlines()

values = [list(line)[::-1] for line in lines[:-1]]
operations = list(lines[-1])[::-1]

digits_count = len(values)

skip_next = False
problem_numbers = []
grand_total = 0

for i, operation in enumerate(operations):
    if skip_next:
        skip_next = False
        continue

    new_number = ""
    for j in range(digits_count):
        new_number += values[j][i]
    problem_numbers.append(int(new_number))
    
    if operation == "*":
        result = problem_numbers[0]
        for number in problem_numbers[1:]:
            result *= number

        skip_next = True
        grand_total += result
        problem_numbers = []

    elif operation == "+":
        result = sum(problem_numbers)

        skip_next = True
        grand_total += result
        problem_numbers = []

print(grand_total)
