import numpy as np
from tqdm import tqdm
from multiprocessing import Pool


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone)%2 == 0:
            stone1 = stone[:len(stone)//2]
            stone2 = stone[len(stone)//2:]

            new_stones.append(str(int(stone1)))
            new_stones.append(str(int(stone2)))
        else:
            new_stones.append(str(int(stone)*2024))

    return new_stones

def blink_recursively(stones, i=0):
    print(i)
    if i == 50:
        return len(stones)
    
    total_len = 0
    new_stones = blink(stones)
    total_len = blink_recursively(new_stones, i + 1)
    return total_len

def main():
    with open('./Day11/file.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]    

    sum=0
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        lines[i] = lines[i].split(' ')
        to_blink = lines[i]
        for i in range(25):
            to_blink = blink(to_blink)

    print("Answer to part 1: ", len(to_blink))
    
    for b in to_blink:
        sum2 = blink_recursively(b)
    print("Answer to part 2: ", sum2)

if __name__ == '__main__':
    main()