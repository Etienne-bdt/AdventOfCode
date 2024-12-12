def find_regions(lines):
    # Regions are adjacent same letters
    # OOOOO
    # OXOXO
    # OOOOO
    # OXOXO
    # OOOOO
    # Will return 5 regions, 4 X and 1 O
    # Find this region

    region = {}
    visited = set()
    coordinates_to_explore = set([(0, 0)])
    other_regions_to_explore = set()
    region_index = 0
    region[region_index] = []

    while coordinates_to_explore or other_regions_to_explore:

        if not coordinates_to_explore:
            region_index += 1
            region[region_index] = []
            i, j = other_regions_to_explore.pop()
            exploring_letter = lines[i][j]
        else:
            i, j = coordinates_to_explore.pop()
            exploring_letter = lines[i][j]
        if (i, j) not in visited:
            visited.add((i, j))
        if (i, j) not in region:
            region[region_index].append((i, j))
            # Look around
            if i > 0 and (i - 1, j) not in visited:
                if lines[i - 1][j] == exploring_letter:
                    coordinates_to_explore.add((i - 1, j))
                    other_regions_to_explore.discard((i - 1, j))
                else:
                    other_regions_to_explore.add((i - 1, j))
            if j > 0 and (i, j - 1) not in visited:
                if lines[i][j - 1] == exploring_letter:
                    coordinates_to_explore.add((i, j - 1))
                    other_regions_to_explore.discard((i, j - 1))
                else:
                    other_regions_to_explore.add((i, j - 1))
            if j < len(lines[0]) - 1 and (i, j + 1) not in visited:
                if lines[i][j + 1] == exploring_letter:
                    coordinates_to_explore.add((i, j + 1))
                    other_regions_to_explore.discard((i, j + 1))
                else:
                    other_regions_to_explore.add((i, j + 1))
            if i < len(lines) - 1 and (i + 1, j) not in visited:
                if lines[i + 1][j] == exploring_letter:
                    coordinates_to_explore.add((i + 1, j))
                    other_regions_to_explore.discard((i + 1, j))
                else:
                    other_regions_to_explore.add((i + 1, j))

    return region


def calculate_price(region):
    perimeter = 0
    area = 0
    #Region is a list of coordinates present in the region
    #Region is not square, so we need to calculate the area and perimeter accordingly
    for i, j in region:
        if (i - 1, j) not in region:
            perimeter += 1
        if (i + 1, j) not in region:
            perimeter += 1
        if (i, j - 1) not in region:
            perimeter += 1
        if (i, j + 1) not in region:
            perimeter += 1
        area += 1

    return area * perimeter
def calculate_discounted_price(region):
    area = 0
    for i, j in region:
        area += 1
    
    sides = 0
    for i, j in region:
        neighbors = 0
        if (i-1, j) in region: neighbors += 1
        if (i+1, j) in region: neighbors += 1
        if (i, j-1) in region: neighbors += 1
        if (i, j+1) in region: neighbors += 1
        # No neighbors = 4 corners
        if neighbors == 0:
            sides += 4
        # One neighbor = 2 corners on the end
        elif neighbors == 1:
            sides += 2
        # Two neighbors in a corner = 1 corner
        elif neighbors == 2:
            # Check if opposing
            if not ((i-1,j) in region and (i+1,j) in region) and \
               not ((i,j-1) in region and (i,j+1) in region):
                if (i-1,j) in region and (i,j-1) in region and (i-1,j-1) not in region:
                    sides += 1
                if (i-1,j) in region and (i,j+1) in region and (i-1,j+1) not in region:
                    sides += 1
                if (i+1,j) in region and (i,j-1) in region and (i+1,j-1) not in region:
                    sides += 1
                if (i+1,j) in region and (i,j+1) in region and (i+1,j+1) not in region:
                    sides += 1    
                sides += 1
        # Three neighbors (T-shape) or four neighbors (cross)
        # Count corners where diagonally adjacent cell is not in region
        elif neighbors >= 3:
            if (i-1,j) in region and (i,j-1) in region and (i-1,j-1) not in region:
                sides += 1
            if (i-1,j) in region and (i,j+1) in region and (i-1,j+1) not in region:
                sides += 1
            if (i+1,j) in region and (i,j-1) in region and (i+1,j-1) not in region:
                sides += 1
            if (i+1,j) in region and (i,j+1) in region and (i+1,j+1) not in region:
                sides += 1
        

    return area * sides

def main():
    with open('./Day12/file.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    
    regions = find_regions(lines)
    price = 0
    discounted_price=0
    for region in regions:
        price += calculate_price(regions[region]) 

    print("Answer to part1: ", price)

    for region in regions:
        discounted_price += calculate_discounted_price(regions[region])

    print("Answer to part2: ", discounted_price)
if __name__ == '__main__':
    main()
