import networkx as nx
from tqdm import tqdm

def main():
    with open('./Day23/file.txt') as f:
        lines = f.readlines()

    G = nx.Graph()
    for connections_l in tqdm(lines):
        connections = connections_l.strip('\n').split('-')
        G.add_edge(connections[0], connections[1])

    # Find all triangles in the graph
    triangles = []
    for node in tqdm(G.nodes):
        neighbors = set(G.neighbors(node))
        for neighbor in neighbors:
            common_neighbors = neighbors.intersection(G.neighbors(neighbor))
            for common in common_neighbors:
                triangle = sorted([node, neighbor, common])  # Sort to avoid duplicates
                if triangle not in triangles:
                    triangles.append(triangle)

    # Filter triangles with at least one node starting with 't'
    triangles_with_t = [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]
    print("Answer to part 1 : ", len(triangles_with_t))
    
    #Find most common occurence of a node in the graph
    cliques = list(nx.find_cliques(G))
    largest_clique = max(cliques, key=len)  # Find the largest clique

    password = ','.join(sorted(largest_clique))
    print("Answer to part 2 : ", password)
if __name__ == "__main__":
    main()
