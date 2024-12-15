import numpy as np

def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i][0])):
            if lines[i][0][j] == "@":
                return j,i
    return 0, 0
def move_boxes_in_line(robot, boxes, walls, direction):
    xr, yr = robot
    can_it = False
    try:
        if direction == "U":
            if (xr, yr-1) in boxes:
                can_it,_ = move_boxes_in_line((xr, yr-1), boxes, walls, direction)
            elif (xr, yr-1) in walls:
                return False, robot
            else: 
                robot = (xr, yr-1)
                index = boxes.index((xr, yr))
                boxes[index] = (xr, yr-1)
                return True, robot
            if can_it:
                robot = (xr, yr-1)
                #find index of box in boxes
                index = boxes.index((xr, yr))
                boxes[index] = (xr, yr-1)
                return True, robot
        elif direction == "D":
            if (xr, yr+1) in boxes:
                can_it,_ = move_boxes_in_line((xr, yr+1), boxes, walls, direction)
            elif (xr, yr+1) in walls:
                return False, robot
            else:
                robot = (xr, yr+1)
                #find index of box in boxes
                index = boxes.index((xr, yr))
                boxes[index] = (xr, yr+1)
                return True, robot
            if can_it:
                robot = (xr, yr+1)
                #find index of box in boxes
                index = boxes.index((xr, yr))
                boxes[index] = (xr, yr+1)
                return True, robot
        elif direction == "L":
            if (xr-1, yr) in boxes:
                can_it,_ = move_boxes_in_line((xr-1, yr), boxes, walls, direction)
            elif (xr-1, yr) in walls:
                return False, robot
            else:
                robot = (xr-1, yr)
                #find index of box in boxes
                index = boxes.index((xr, yr))
                boxes[index] = (xr-1, yr)
                return True, robot
            if can_it:
                robot = (xr-1, yr)
                #find index of box in boxes
                index = boxes.index((xr, yr))
                boxes[index] = (xr-1, yr)
                return True, robot
        elif direction == "R":
            if (xr+1, yr) in boxes:
                #print("Found a box at ", xr+1, yr)
                can_it,_ = move_boxes_in_line((xr+1, yr), boxes, walls, direction)
                #print("Can it move? ", can_it)
            elif (xr+1, yr) in walls:
                return False, robot
            else:
                #find index of box in boxes
                robot = (xr+1, yr)
                index = boxes.index((xr, yr))
                boxes[index] = (xr+1, yr)
                return True, robot
            if can_it:
                #find index of box in boxes
                robot = (xr+1, yr)
                index = boxes.index((xr, yr))
                boxes[index] = (xr+1, yr)
                return True, robot
    except ValueError:
        return True, robot
    return False, robot

def modern_slavery(robot, move, boxes ,walls, it_could=None, previous_move=None):
    x, y = robot
    #print(move)
    if move == "^":
        direction = "U"
    elif move == ">":
        direction = "R"
    elif move == "<":
        direction = "L"
    elif move == "v":
        direction = "D"



    if previous_move == None:
        could_it, robot = move_boxes_in_line(robot, boxes, walls, direction)
    elif it_could == False and previous_move == move:
        return False, robot
    else:
        could_it, robot = move_boxes_in_line(robot, boxes, walls, direction)
    """
        if could_it:
            if direction == "U":
                robot = (x, y-1)
            elif direction == "D":
                robot = (x, y+1)
            elif direction == "L":
                robot = (x-1, y)
            elif direction == "R":
                robot = (x+1, y)
    """

    return could_it, robot

def serialize(maze):
    walls= set()
    boxes = []
    for i in range(len(maze)):
        for j in range(len(maze[i][0])):
            if maze[i][0][j] == "#":
                walls.add((j,i))
            if maze[i][0][j] == "O":
                boxes.append((j,i))
    return walls, boxes

def reconstruct(robot,maze, walls, boxes):
    new_maze = np.zeros((len(maze), len(maze[0][0])), dtype=str)
    for i in range(len(maze)):
        for j in range(len(maze[i][0])):
            if (j,i) in walls:
                new_maze[i][j] = "#"
            if (j,i) in boxes:
                new_maze[i][j] = "O"
            if (j,i) not in walls and (j,i) not in boxes:
                new_maze[i][j] = "."
    x, y = robot
    new_maze[y][x] = "@"
    return new_maze
    
def reconstruct_huge(robot, maze, walls, boxes):
    new_maze = np.zeros((len(maze), len(maze[0][0])*2), dtype=str)
    for i in range(len(maze)):
        for j in range(len(maze[0][0])*2):
            if (j,i) in walls:
                new_maze[i][j] = "#"
            if [(j,i),(j+1,i)] in boxes:
                print("Found a box at ", j, i)
                new_maze[i][j] = "["
                new_maze[i][j+1] = "]"
            if (j,i) not in walls and ([(j,i),(j+1,i)] not in boxes and [(j-1,i),(j,i)] not in boxes):
                new_maze[i][j] = "."
    x, y = robot
    new_maze[y][x] = "@"
    return new_maze

def transform(maze):
    walls = set()
    boxes = []
    for i in range(len(maze)):
        for j in range(0,len(maze[0][0]) * 2,2):
            if maze[i][0][j // 2] == "#":
                walls.add((j, i))
                walls.add((j+1, i))
            if maze[i][0][j // 2] == "O":
                boxes.append([(j, i), (j+1, i)])
    return walls, boxes

def modern_slavery_huge(robot, move, boxes ,walls, it_could=None, previous_move=None):
    x, y = robot
    if move == "^":
        direction = "U"
    elif move == ">":
        direction = "R"
    elif move == "<":
        direction = "L"
    elif move == "v":
        direction = "D"

    if previous_move is None:
        could_it, robot = move_boxes_in_line_huge(robot, boxes, walls, direction)
    elif it_could is False and previous_move == move:
        return False, robot
    else:
        could_it, robot = move_boxes_in_line_huge(robot, boxes, walls, direction)

    return could_it, robot
def move_boxes_in_line_huge(robot, boxes, walls, direction):
    xr, yr = robot
    can_it = False
    try:
        if direction == "U":
            if (xr, yr-1) in [coord for box in boxes for coord in box]:
                can_it, _ = move_boxes_in_line_huge((xr, yr-1), boxes, walls, direction)
            elif (xr, yr-1) in walls:
                return False, robot
            else:
                robot = (xr, yr-1)
                for box in boxes:
                    if (xr, yr) in box:
                        index = box.index((xr, yr))
                        box[index] = (xr, yr-1)
                return True, robot
            if can_it:
                robot = (xr, yr-1)
                for box in boxes:
                    if (xr, yr) in box:
                        index = box.index((xr, yr))
                        box[index] = (xr, yr-1)
                return True, robot
        elif direction == "D":
            if (xr, yr+1) in [coord for box in boxes for coord in box]:
                can_it, _ = move_boxes_in_line_huge((xr, yr+1), boxes, walls, direction)
            elif (xr, yr+1) in walls:
                return False, robot
            else:
                robot = (xr, yr+1)
                for box in boxes:
                    if (xr, yr) in box:
                        index = box.index((xr, yr))
                        box[index] = (xr, yr+1)
                return True, robot
            if can_it:
                robot = (xr, yr+1)
                for box in boxes:
                    if (xr, yr) in box:
                        index = box.index((xr, yr))
                        box[index] = (xr, yr+1)
                return True, robot
        elif direction == "L":
            if (xr-1, yr) in [coord for box in boxes for coord in box]:
                can_it, _ = move_boxes_in_line_huge((xr-1, yr), boxes, walls, direction)
            elif (xr-1, yr) in walls:
                return False, robot
            else:
                robot = (xr-1, yr)
                for box in boxes:
                    if (xr, yr) in box:
                        index = box.index((xr, yr))
                        box[index] = (xr-1, yr)
                return True, robot
            if can_it:
                robot = (xr-1, yr)
                for box in boxes:
                    if (xr, yr) in box:
                        index = box.index((xr, yr))
                        box[index] = (xr-1, yr)
                return True, robot
        elif direction == "R":
            if (xr+1, yr) in [coord for box in boxes for coord in box]:
                can_it, _ = move_boxes_in_line_huge((xr+1, yr), boxes, walls, direction)
            elif (xr+1, yr) in walls:
                return False, robot
            else:
                robot = (xr+1, yr)
                for box in boxes:
                    if (xr, yr) in box:
                        index = box.index((xr, yr))
                        box[index] = (xr+1, yr)
                return True, robot
            if can_it:
                robot = (xr+1, yr)
                for box in boxes:
                    if (xr, yr) in box:
                        index = box.index((xr, yr))
                        box[index] = (xr+1, yr)
                return True, robot
    except ValueError:
        return True, robot
    return False, robot

def main():
    with open('./Day15/file.txt') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
        #find index of '' in the list
        moves =''
        
        for i in range(len(lines)):
            if lines[i] == []:
                maze = lines[:i]
                moves = lines[i+1:]


    new_moves = ''
    for i in range(len(moves)):
        new_moves += ''.join(moves[i])
        
    moves = [new_moves]
    #print(new_moves)

    walls, boxes = serialize(maze)
    start = find_start(maze)
    for i in range(len(moves[0])):
        could_it,start = modern_slavery(start, moves[0][i], boxes=boxes, walls=walls, it_could=(could_it if i>0 else None), previous_move=(moves[0][i-1] if i>0 else None)) 
    new_maze = reconstruct(start,maze, walls, boxes)
    print(new_maze)


    sum=0
    for box in boxes:
        sum+= box[0] + 100*box[1]
    print("Answer to part 1: ", sum)

    #Boxes now transform from O to [] which take up 2 spaces walls also take up two spaces horizontally
    walls2, boxes2 = transform(maze) 
    start = find_start(maze)
    print("Start: ", start)
    start = (start[0]*2, start[1])
    print("Start: ", start)
    for i in range(len(moves[0])):
        could_it,start = modern_slavery_huge(start, moves[0][i], boxes=boxes2, walls=walls2, it_could=(could_it if i>0 else None), previous_move=(moves[0][i-1] if i>0 else None))   
        new_maze_huge = reconstruct_huge(start, maze, walls2, boxes2)
        print(new_maze_huge)





if __name__=='__main__':
    main()