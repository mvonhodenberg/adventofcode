import numpy as np
from scipy.signal import convolve2d

#This mostly isn't my code, I just wanted to include this day for the sake of completeness; it was a boring and annoying task.

data=open('2021/input/day11input.txt').read()


def flash(arr):
    arr += 1
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    flashed = np.zeros(arr.shape, dtype=bool)
    while np.any(flashing := arr > 9):
        flashed |= flashing
        arr += convolve2d(flashing, mask, mode='same')
        arr[flashed] = 0
    return flashed

def part1(data, steps=100):
    arr = np.array([[*line] for line in data.splitlines()], dtype=int)
    return sum(flash(arr).sum() for _ in range(steps))

def part2(data):
    arr = np.array([[*line] for line in data.splitlines()], dtype=int)
    
    step = 0
    while np.any(arr):
        flash(arr)
        step += 1
    return step

print('Part 1:', part1(data))
print('Part 2:', part2(data))
