with open("input.txt", "r") as file:
    lines = file.read().splitlines()

values = [line.split() for line in lines[:-1]]
values = [[int(value) for value in sublist] for sublist in values]
operations = lines[-1].split()

grand_total = 0

for i, operation in enumerate(operations):
    problem_total = values[0][i]
    for value in values[1:]:
        if operation == "*":
            problem_total *= value[i]
        elif operation == "+":
            problem_total += value[i]

    grand_total += problem_total

print(grand_total)
