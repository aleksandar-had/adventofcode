### Needed only for the timer wrapper
import sys
sys.path.append('../')
from timer import timer
###

##
# Solution begins here
##
def parse_input():
    res = []
    for line in open("input.txt"):
        res.extend([int(timer) for timer in line.split(',')]) 
    return res

@timer
def solution_part1(days):
    fish = parse_input()    
        
    for day in range(days):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
        
    print(len(fish))
    
# Solution to part1 was very brute-force (tracking each individual fish)
# Instead track the number of fish in each individual day
@timer
def solution_part2(days):
    fish = parse_input()
    
    fish_at_day = [0]*9
    
    for day in fish:
        fish_at_day[day] += 1
    
    for _ in range(days):
        fish_at_zero = fish_at_day[0]
        for fish_day in range(8):
            fish_at_day[fish_day] = fish_at_day[fish_day + 1]
        fish_at_day[6] += fish_at_zero
        fish_at_day[8] = fish_at_zero
    
    print(sum(fish_at_day))
    
    
if __name__ == "__main__":
    solution_part1(80)
    solution_part2(256)