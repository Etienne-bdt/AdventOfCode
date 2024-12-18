import networkx as nx
import matplotlib.pyplot as plt
def main():
    with open('./Day18/file.txt') as f:
        lines = f.readlines()

    positions = [(int(line.split(",")[0]), int(line.split(",")[1].strip('\n'))) for line in lines]
    fallen_blocks = set(positions[:1024])

    G = nx.grid_2d_graph(71,71)
    G.remove_nodes_from(fallen_blocks)
    path = nx.shortest_path(G, (0, 0), (70,70))    
    print("Answer to part 1: ", len(path)-1)

    for j in range(1024, len(positions)):
        G.remove_node(positions[j])
        if positions[j] in path:
            try:
                path = nx.shortest_path(G, (0, 0), (70,70))
                print(len(path)-1)
            except nx.NetworkXNoPath:
                print("No path left after removing position:", positions[j])
                break

if __name__ == "__main__":
    main()
