from collections import defaultdict
import re

def parse_input():
    res = []
    
    for line in open("input.txt"):
        line_info = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line)
        
        pipe_start = (int(line_info.group(1)), int(line_info.group(2)))
        pipe_end = (int(line_info.group(3)), int(line_info.group(4)))
        
        res.append([pipe_start[0], pipe_start[1], pipe_end[0], pipe_end[1]])
    return res

def solution_part1():
    grid = defaultdict(int)
    pipes = parse_input()
    
    for start_x, start_y, end_x, end_y in pipes:
        x_direction = end_x > start_x and 1 or -1
        y_direction = end_y > start_y and 1 or -1
        
        if start_x == end_x:
            for y in range(start_y, end_y + y_direction, y_direction):
                grid[(start_x, y)] += 1
                
        elif start_y == end_y:
            for x in range(start_x, end_x + x_direction, x_direction):
                grid[(x, start_y)] += 1
    
    print(sum([1 for loc in grid if grid[loc] >= 2]))
    
def solution_part2():
    grid = defaultdict(int)
    pipes = parse_input()
    
    for start_x, start_y, end_x, end_y in pipes:
        x_direction = end_x > start_x and 1 or -1
        y_direction = end_y > start_y and 1 or -1
        
        if start_x == end_x:
            for y in range(start_y, end_y + y_direction, y_direction):
                grid[(start_x, y)] += 1
                
        elif start_y == end_y:
            for x in range(start_x, end_x + x_direction, x_direction):
                grid[(x, start_y)] += 1
            
        else:
            x_locs = range(start_x, end_x + x_direction, x_direction)
            y_locs = range(start_y, end_y + y_direction, y_direction)
            
            for x,y in zip(x_locs, y_locs):
                grid[(x,y)] += 1
        
    print(sum([1 for loc in grid if grid[loc] >= 2]))
    
if __name__ == "__main__":
    solution_part1()
    solution_part2()