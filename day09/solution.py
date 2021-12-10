import numpy as np
from numpy.core.defchararray import multiply

with open("input.txt", 'r') as f:
    heatmap = np.array([[int(h) for h in line] for line in f.read().splitlines()])

heatmap = np.pad(heatmap, [(1,), (1,)], 'constant', constant_values=9)

def find_lowest_points(map):
    lowest_points = []
    for i in range(1, len(map)-1):
        for j in range(1, len(map[0])-1):
            point = map[i,j]
            neighbours = [map[i-1,j], map[i+1,j], map[i,j-1], map[i,j+1]]
            if all([point < n for n in neighbours]):
                lowest_points.append((i,j))
    return lowest_points

lowest_points = find_lowest_points(heatmap)

def solution_part1():
    return sum(heatmap[coord]+1 for coord in lowest_points)

def explore_basin(map,start,basin_points):
    if map[start] == 9 or start in basin_points:
        return
    
    basin_points.append(start)
        
    i,j = start
    
    # explore upwards
    if i-1 > 0:
        explore_basin(map, (i-1,j), basin_points)
    # explore downwards
    if i+1 < len(map):
        explore_basin(map, (i+1,j), basin_points)
    # explore left
    if j-1 > 0:
        explore_basin(map, (i,j-1), basin_points)
    # explore right
    if j+1 < len(map[0]):
        explore_basin(map, (i,j+1), basin_points)
    
    return basin_points

def find_all_basins(map):
    return [explore_basin(map, low_point, []) for low_point in lowest_points]

def solution_part2():
    all_basins = sorted([len(basin) for basin in find_all_basins(heatmap)])
    return np.prod(all_basins[-3:])
        

if __name__ == "__main__":
    print(solution_part1())
    print(solution_part2())