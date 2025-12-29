# After some research, I found that by adding just functools.lru_cache
# was enough to make the recursive function efficient and 
# return the correct answer.
# https://en.wikipedia.org/wiki/Memoization
# 
# This would probably also make my recursive function from 
# day 7 part 2 run efficiently as well.

from functools import lru_cache

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

@lru_cache(None)
def find_paths(device: str, fft: bool, dac: bool) -> int:
    specific_paths = 0

    if device == "fft":
        fft = True
    if device == "dac":
        dac = True

    if device == "out":
        if fft and dac:
            return 1
        else:
            return 0
    
    for output in devices[device]:
        specific_paths += find_paths(output, fft, dac)
    
    return specific_paths

devices = {}
for line in lines:
    device, outputs = line.split(": ")
    devices[device] = outputs.split(" ")

result = find_paths("svr", False, False)
print(result)
