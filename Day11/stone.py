import numpy as np
from tqdm import tqdm
from functools import cache

@cache
def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            stone1 = stone[:len(stone)//2]
            stone2 = stone[len(stone)//2:]

            new_stones.append(str(int(stone1)))
            new_stones.append(str(int(stone2)))
        else:
            new_stones.append(str(int(stone) * 2024))

    return tuple(new_stones)

def blink_recursively(stones, iterations):
    if iterations == 0:
        return stones
    return blink_recursively(blink(stones), iterations - 1)

@cache
def blink2(stone, steps):
    if steps == 0:
        return 1
    if stone == '0':
        return blink2('1', steps - 1)
    length = len(stone)
    if length%2==0:
        return blink2(str(int(stone[:length//2])),steps-1) + blink2(str(int(stone[length//2:])), steps - 1)
    return blink2(str(int(stone) * 2024), steps - 1)
    
def main():
    with open('./Day11/file.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]    

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        lines[i] = lines[i].split(' ')
        to_blink = lines[i]
        to_blink = blink_recursively(tuple(to_blink), 3)


    print("Answer to part 1: ", len(to_blink))

    sum2 = sum(blink2(stone, 75) for stone in lines[0])
    print("Answer to part 2: ", sum2)

if __name__ == '__main__':
    main()