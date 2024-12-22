from math import floor
from tqdm import tqdm
import numpy as np

def mixing(a, b):
    return a ^ b

def prunning(a):
    return a % 16777216

def secret(a):
    secretv = a * 64
    mixed = mixing(secretv, a)
    prunned = prunning(mixed)
    divided = prunned // 32
    mixed2 = mixing(divided, prunned)
    prunned2 = prunning(mixed2)
    mul2 = prunned2 * 2048
    mixed3 = mixing(mul2, prunned2)
    prunned3 = prunning(mixed3)
    return prunned3

def main():
    with open('./Day22/file.txt') as f:
        lines = f.readlines()
    
    lines = [int(line.strip()) for line in lines]
    num_lines = len(lines)
    res = np.zeros((2000, num_lines), dtype=int)
    sum1 = 0
    
    for i in tqdm(range(num_lines)):
        secretv = lines[i]
        for j in range(2000):
            secretv = secret(secretv)
            res[j, i] = secretv % 10
        sum1 += secretv
    
    print("Answer to part 1:", sum1)
    
    diffs = np.diff(res, axis=0)
    seqs = {}
    
    for buyer in tqdm(range(diffs.shape[1])):
        for i in range(diffs.shape[0] - 3):
            sub = tuple(diffs[i:i + 4, buyer])
            if sub not in seqs:
                seqs[sub] = np.zeros(num_lines, dtype=int)
            if seqs[sub][buyer] == 0:
                seqs[sub][buyer] = res[i + 4, buyer]
    
    best = max(sum(v) for v in tqdm(seqs.values()))
    print(best)

if __name__ == "__main__":
    main()