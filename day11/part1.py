with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def find_paths(outputs: list[str]) -> int:
    paths = 0
    for output in outputs:
        if output != "out":
            paths += find_paths(devices[output])
        else:
            return 1
    return paths

devices = {}
for line in lines:
    device, outputs = line.split(": ")
    devices[device] = outputs.split(" ")

result = find_paths(devices["you"])
print(result)
