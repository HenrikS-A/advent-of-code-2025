from itertools import combinations

with open("input.txt", "r") as file:
    lines = file.read().splitlines()


def extract_machine_data(line: str) -> tuple[ list[str], list[list[int]] ]:
    line = line.replace("] ", ":").replace(" {", ":")
    diagram_str, buttons_str, joltage_str = line.split(":")

    diagram = list(diagram_str.replace("[", ""))

    raw_buttons = buttons_str.replace("(", "").replace(")", "").split()
    buttons = [
        [int(light) for light in button.split(",")]
        for button in raw_buttons
    ]
    return diagram, buttons

def button_press(n_lights: int, buttons: tuple[list[int], ...]) -> list[int]:
    new_lights = ["." for _ in range(n_lights)]
    for button in buttons:
        for light_index in button:
            new_lights[light_index] = "." if new_lights[light_index] == "#" else "#"
    return new_lights


total_presses = 0

for line in lines:
    diagram, buttons = extract_machine_data(line)

    n_lights = len(diagram)
    fewest_presses = len(buttons) + 1

    for num_presses in range(len(buttons) + 1):
        for combination in combinations(buttons, num_presses):

            lights = button_press(n_lights, combination)
            if lights == diagram:
                if num_presses < fewest_presses:
                    fewest_presses = num_presses
    
    total_presses += fewest_presses

print(total_presses)
