from functools import lru_cache
from tqdm import tqdm

@lru_cache(None)
def is_doable(available_patterns, wanted_pattern):
    # Base case
    if len(wanted_pattern) == 0:
        return True
    
    # Recursive case
    for p in available_patterns:
        if wanted_pattern.startswith(p):
            if is_doable(available_patterns, wanted_pattern[len(p):]):
                return True
    return False

@lru_cache(None)
def all_cases(available_patterns, wanted_pattern):
    # Base case
    if len(wanted_pattern) == 0:
        return 1
    
    # Recursive case
    sum = 0
    for p in available_patterns:
        if wanted_pattern.startswith(p):
            sum += all_cases(available_patterns, wanted_pattern[len(p):])
    return sum

def main():
    with open('./Day19/file.txt') as f:
        lines = f.readlines()
    available_patterns = tuple(lines[0].strip('\n').split(', '))
    wanted_patterns = [line.strip('\n') for line in lines[2:]]

    sum = 0
    sum2 = 0
    # Find all combinations of elements of available patterns to match all wanted patterns individually
    # If a pattern is doable using available patterns increment sum by 1
    for wanted_pattern in tqdm(wanted_patterns):
        if is_doable(available_patterns, wanted_pattern):
            sum += 1
        sum2 += all_cases(available_patterns, wanted_pattern)
    
    print("Answer to part 1: ", sum)
    print("Answer to part 2: ", sum2)

if __name__ == "__main__":
    main()