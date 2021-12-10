def parse_input():
    directions = []
    for line in open('input.txt'):
        temp = line.split(' ')
        directions.append((temp[0], int(temp[1])))
    return directions
    
def solution_part1():
    dirs = parse_input()
    horiz = depth = 0
    for move in dirs:
        if move[0] == "forward":
            horiz += move[1]
        elif move[0] == "down":
            depth += move[1]
        elif move[0] == "up":
            depth = max(depth - move[1], 0)
    print(depth*horiz)
    
def solution_part2():
    dirs = parse_input()
    horiz = depth = aim = 0
    for move in dirs:
        if move[0] == "forward":
            horiz += move[1]
            depth += move[1] * aim
        elif move[0] == "down":
            aim += move[1]
        elif move[0] == "up":
            aim = max(aim - move[1], 0)
    
    print(horiz*depth)
            
        
if __name__ == "__main__":
    solution_part1()
    solution_part2()