def find_trail_start(lines):
    table = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '0':
                table.append((i, j))
    return table

def find_next_step(lines, start, ending_list=None):
    possible_branches = []
    if lines[start[0]][start[1]] == '0':
        ending_list = []

    if lines[start[0]][start[1]] == '9':
        ending_list.append((start[0], start[1]))

        
    try:
        if int(lines[start[0] + 1][start[1]]) == int(lines[start[0]][start[1]]) + 1:
            possible_branches.append((start[0] + 1, start[1]))
    except IndexError:
        pass
    try:
        if start[0] != 0 and int(lines[start[0] - 1][start[1]]) == int(lines[start[0]][start[1]]) + 1:
            possible_branches.append((start[0] - 1, start[1]))
    except IndexError:
        pass
    try:
        if int(lines[start[0]][start[1] + 1]) == int(lines[start[0]][start[1]]) + 1:
            possible_branches.append((start[0], start[1] + 1))
    except IndexError:
        pass
    try:
        if start[1] != 0 and int(lines[start[0]][start[1] - 1]) == int(lines[start[0]][start[1]]) + 1:
            possible_branches.append((start[0], start[1] - 1))
    except IndexError:
        pass

    for branch in possible_branches:
        next_step = branch
        result = find_next_step(lines, next_step, ending_list)

    return ending_list
    """try:
        if int(lines[start[0] + 1][start[1]]) == int(lines[start[0]][start[1]]) + 1:
            return find_next_step(lines, (start[0] + 1, start[1]), ending_list)
    except IndexError:
        pass
    try:
        if start[0] != 0 and int(lines[start[0] - 1][start[1]]) == int(lines[start[0]][start[1]]) + 1:
            return find_next_step(lines, (start[0] - 1, start[1]), ending_list)
    except IndexError:
        pass
    try:
        if int(lines[start[0]][start[1] + 1]) == int(lines[start[0]][start[1]]) + 1:
            return find_next_step(lines, (start[0], start[1] + 1), ending_list)
    except IndexError:
        pass
    try:
        if start[1] != 0 and int(lines[start[0]][start[1] - 1]) == int(lines[start[0]][start[1]]) + 1:
            return find_next_step(lines, (start[0], start[1] - 1), ending_list)
    except IndexError:
        pass

    return None"""
def main():
    with open('./Day10/file.txt') as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')

    start = find_trail_start(lines)

    trail_dict = {}
    sum =0
    sum2 = 0
    for point in start:
        trails = find_next_step(lines, point)
        ends = []
        idx = point[0] * len(lines[0]) + point[1]
        for trail in trails:
            if trail not in ends:
                ends.append(trail)
        for _ in ends:
            trail_dict[idx] = trail_dict.get(idx, 0) + 1
            sum += 1

        for _ in trails:
            sum2 += 1

    print("Answer to part 1: ", sum) 
    print("Answer to part 2: ", sum2)



    

        


if __name__ == '__main__':
    main()