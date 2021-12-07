### Needed only for the timer wrapper
import sys
sys.path.append('../')
from timer import timer
###

import statistics

def parse_input():
    return [*map(int, open('input.txt').read().split(','))]

@timer
def solution_part1():
    coords = parse_input()
    med = int(statistics.median(coords))
    
    min_fuel = sum([abs(pos - med) for pos in coords])
    print(min_fuel)
    
    
def arithmetic_sum(n):
    return sum(i for i in range(n+1))

# computing the arithmetic sum on each iter of the for loop was slow
# therefore, went for a caching approach
@timer
def solution_part2():
    coords = parse_input()
    single_coords = set(coords)
    fuel_costs = []
    cache = {}
    
    for pos1 in single_coords:
        fuel_cost = 0
        for pos2 in coords:
            diff = abs(pos1 - pos2)
            if diff not in cache:
                diff_arithm_sum = arithmetic_sum(diff)
                cache[diff] = diff_arithm_sum
            fuel_cost += cache[diff]
 
        fuel_costs.append(fuel_cost)
    
    print(min(fuel_costs))

if __name__ == "__main__":
    solution_part1()
    solution_part2()