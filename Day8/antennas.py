import numpy as np

def unique_antennas(lines):
    antennas = set()
    for line in lines:
        #Find unique letters uppercase or lowercase or digits in the line and list them in a set
        #Filter list of string line to remove . and \n
        line = list(filter(lambda x: x.isalnum(), line))
        antennas.update(set(line))
    return antennas

def get_antinodes(coord1, coord2, num_lines, width_line):
    #Get the coordinates of the antinodes of the line between coord1 and coord2
    x1, y1 = coord1
    x2, y2 = coord2

    #Get difference in x and y
    dx1 = x2 - x1
    dy1 = y2 - y1

    list_an=[]
    if x2+dx1 >=0 and x2+dx1 < num_lines and y2+dy1 >= 0 and y2+dy1 < width_line:
        list_an.append((x2+dx1, y2+dy1))

    if x1-dx1 >=0 and x1-dx1 < num_lines and y1-dy1 >= 0 and y1-dy1 < width_line:
        list_an.append((x1-dx1, y1-dy1))
    #print(x2+dx1, y2+dy1, x1-dx1, y1-dy1)
    return list_an

def get_antinodes_with_harmonics(coord1, coord2, num_lines, width_line):
    #Get the coordinates of the antinodes of the line between coord1 and coord2
    x1, y1 = coord1
    x2, y2 = coord2

    #Get difference in x and y
    dx1 = x2 - x1
    dy1 = y2 - y1

    list_an=[]
    if x2+dx1 >=0 and x2+dx1 < num_lines and y2+dy1 >= 0 and y2+dy1 < width_line:
        list_an.append((x2+dx1, y2+dy1))

    if x1-dx1 >=0 and x1-dx1 < num_lines and y1-dy1 >= 0 and y1-dy1 < width_line:
        list_an.append((x1-dx1, y1-dy1))

    max_harmonics_forward = int(max((width_line-x2)/dx1, (num_lines-y2)/dy1))+3

    max_harmonics_backward = int(max(x2/dx1, y2/dy1))+3

    for i in range(2,max_harmonics_forward):
        if x2+i*dx1 >=0 and x2+i*dx1 < num_lines and y2+i*dy1 >= 0 and y2+i*dy1 < width_line:
            list_an.append((x2+i*dx1, y2+i*dy1))

    for i in range(2,max_harmonics_backward):
        if x2-i*dx1 >=0 and x2-i*dx1 < num_lines and y2-i*dy1 >= 0 and y2-i*dy1 < width_line:
            list_an.append((x2-i*dx1, y2-i*dy1))

    list_an.append(coord1)
    list_an.append(coord2)
    list_an = list(set(list_an))
    return list_an

def antenna_matrix(lines, antennas, num_lines, width_line):
    unique_antinodes = set()
    for antenna in antennas:
        #Find the coordinates of the antenna in the
        coordinates = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])-1) if lines[i][j] == antenna]
        for i in range(len(coordinates)):
            for j in range(i+1, len(coordinates)):
                #Get the antinodes of the line between the two coordinates
                antinodes = get_antinodes(coordinates[i], coordinates[j], num_lines, width_line)
                if len(antinodes) > 0:
                    unique_antinodes.update(antinodes)
                    #print(unique_antinodes)

    """for antinode in unique_antinodes:
        if lines[antinode[0]][antinode[1]] == ".":
            lines[antinode[0]] = lines[antinode[0]][:antinode[1]] + "#" + lines[antinode[0]][antinode[1]+1:]
    """
    return unique_antinodes
    
def antenna_matrix_with_harmonics(lines, antennas, num_lines, width_line):
    unique_antinodes = set()
    for antenna in antennas:
        #Find the coordinates of the antenna in the
        coordinates = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])-1) if lines[i][j] == antenna]
        for i in range(len(coordinates)):
            for j in range(i+1, len(coordinates)):
                #Get the antinodes of the line between the two coordinates
                antinodes = get_antinodes_with_harmonics(coordinates[i], coordinates[j], num_lines, width_line)
                if len(antinodes) > 0:
                    unique_antinodes.update(antinodes)
                    #print(unique_antinodes)

    for antinode in unique_antinodes:
        if lines[antinode[0]][antinode[1]] == ".":
            lines[antinode[0]] = lines[antinode[0]][:antinode[1]] + "#" + lines[antinode[0]][antinode[1]+1:]
    
    return unique_antinodes

def main():
    # Read the input
    with open("./Day8/file.txt") as f:
        lines = f.readlines()
    # Parse the input
    num_lines = len(lines)
    width_line = len(lines[0])-1
    antennas = unique_antennas(lines)
    unique_antinodes = antenna_matrix(lines, antennas, num_lines, width_line)
    print("Answer to part1 : ", len(unique_antinodes))
    unique_antinodes_with_harmonics = antenna_matrix_with_harmonics(lines, antennas, num_lines, width_line)

    for line in lines:
        print(line, end="")


    print("\nAnswer to part2 : ", len(unique_antinodes_with_harmonics))

if __name__ == "__main__":
    main()