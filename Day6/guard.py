import polars as pl
import numpy as np
import multiprocessing as mp
from tqdm import tqdm

def find_start(map):
    for i in range(len(map)):
        for j in range(len(map[i][0])):
            if map[i][0][j] == "^":
                return i, j
    return 0, 0

def check_direction(map, posx, posy, direction):
    if direction == "up":
        if map[posx-1][0][posy] == "#" or map[posx-1][0][posy] == "O":
            return "right", False
    elif direction == "right":
        if map[posx][0][posy+1] == "#" or map[posx][0][posy+1] == "O":
            return "down", False
    elif direction == "down":
        if map[posx+1][0][posy] == "#" or map[posx+1][0][posy] == "O":
            return "left", False
    elif direction == "left":
        if map[posx][0][posy-1] == "#" or map[posx][0][posy-1] == "O":
            return "up", False
    return direction, True

def walk(map, posx, posy, direction):
    initialpath = [(posx, posy, direction)]
    while True:
        try:
            direction, can_move = check_direction(map, posx, posy, direction)
            if can_move:
                map[posx][0] = map[posx][0][:posy] + "X" + map[posx][0][posy+1:]
                if direction == "up":
                    posx -= 1
                elif direction == "down":
                    posx += 1
                elif direction == "left":
                    posy -= 1
                elif direction == "right":
                    posy += 1
                initialpath.append((posx, posy, direction))
                map[posx][0] = map[posx][0][:posy] + "^" + map[posx][0][posy+1:]
        except IndexError:
            map[posx][0] = map[posx][0][:posy] + "X" + map[posx][0][posy+1:]
            return map, initialpath

def check_direction_loop(currentpath, previouspos, posx, posy):
    if len(currentpath) > 3:
        try:
            for idx in range(len(currentpath[:-2])):
                x, y, _ = currentpath[idx]
                x1, y1, _ = currentpath[idx+1]
                if [(x, y), (x1, y1)] == [previouspos, (posx, posy)]:
                    return True
        except ValueError:
            pass
    return False

def walk_in_loops(map, initialmap, initialpath, posx, posy, direction):
    currentpath = initialpath.copy()
    previouspos = (posx, posy)
    while True:
        lenx, leny = len(map), len(map[0][0])
        if posx < 0 or posx >= lenx-1 or posy < 0 or posy >= leny-1:
            return False
        if check_direction_loop(currentpath, previouspos, posx, posy):
            return True
        direction, can_move = check_direction(map, posx, posy, direction)
        if can_move:
            previouspos = (posx, posy)
            if direction == "up":
                posx -= 1
            elif direction == "down":
                posx += 1
            elif direction == "left":
                posy -= 1
            elif direction == "right":
                posy += 1

            if posx < 0 or posx >= lenx-1 or posy < 0 or posy >= leny-1:
                return False
        
            currentpath.append((posx, posy, direction))

def find_loop(args):
    map, initialmap, initialpath, candidate, wall_list = args
    posx, posy, direction = initialpath[candidate-1]
    wall_pos = (initialpath[candidate][0], initialpath[candidate][1])
    
    if wall_pos in wall_list:
        return 0
    wall_list.add(wall_pos)
    if initialmap[wall_pos[0]][0][wall_pos[1]] not in ["#", "^"]:
        map[wall_pos[0]][0] = map[wall_pos[0]][0][:wall_pos[1]] + "O" + map[wall_pos[0]][0][wall_pos[1]+1:]
        if (walk_in_loops(map, initialmap, initialpath[:candidate], posx, posy, direction)):
            return 1
    return 0

def main():
    map = pl.read_csv("./Day6/file.txt", has_header=False).to_numpy()
    posx, posy = find_start(map.copy())
    direction = "up"
    map, initialpath = walk(map.copy(), posx, posy, direction)
    
    total = sum(1 for i in range(len(map)) for j in range(len(map[i][0])) if map[i][0][j] == "X")
    print("Answer to part 1:", total)
    
    candidates = [(x, y) for x, y, _ in initialpath]
    wall_list = set()
    args = [(map.copy(), map.copy(), initialpath, i, wall_list) for i in range(1, len(candidates))]
    
    with mp.Pool() as pool:
        results = list(tqdm(pool.imap(find_loop, args), total=len(args)))
    
    num_loops = sum(results)
    print("Answer to part 2:", num_loops)

if __name__ == "__main__":
    main()
