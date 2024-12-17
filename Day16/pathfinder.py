import networkx as nx
from tqdm import tqdm



def get_neighbors(pos):
    x, y = pos
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


import matplotlib.pyplot as plt

def path_find(start, end, walls, width, height):
    G = nx.grid_2d_graph(width, height)
    G.remove_nodes_from(walls)

    print("Searching for paths")
    def custom_weight(u, v, d):
        if u[0] != v[0] and u[1] != v[1]:
            return 1001
        return 1

    print("Calculating shortest path")
    try:
        path = nx.shortest_path(G, source=start, target=end, weight=custom_weight)
        #Extract the path weights from the path
        path_weight = 0
        for i in range(1,len(path)-1):
            path_weight += custom_weight(path[i-1], path[i+1], 0)
    except nx.NetworkXNoPath:
        return float('inf')
    return path_weight

def main():
    with open('./Day16/file.txt') as f:
        lines = f.readlines()
        lines = [line.strip('\n') for line in lines]




    walls =[]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                walls.append((j, i))
            elif lines[i][j] == 'S':
                start = (j, i)
            elif lines[i][j] == 'E':
                end = (j, i)

    print(path_find(start, end, walls, len(lines[0]), len(lines)))



if __name__ == "__main__":
    main()
    #85396
    #428