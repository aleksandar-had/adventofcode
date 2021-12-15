import numpy as np

with open("input.txt") as f:
    octi_map = np.array([[int(h) for h in line] for line in f.read().splitlines()])
    
    
class OctoPIE:
    def __init__(self, octopus_map):
        self.map = octopus_map.copy()
        self.flashes = 0
        self.day = 0
        self.m, self.n = octopus_map.shape
        
    def pass_days(self, total_days):
        for _ in range(total_days):
            flashing = set()
            self.map += 1
            self.day += 1
            new_flashes = True if np.count_nonzero(self.map > 9) > 0 else False
            self.flashes += np.count_nonzero(self.map > 9)
            self.map = np.where(self.map > 9, 0, self.map)
            
            while new_flashes:
                iterate_flashes(self.map, flashing)
                
                new_flashes = True if np.count_nonzero(self.map > 9) > 0 else False
            
                self.flashes += np.count_nonzero(self.map > 9)
                flashing.update([f for f in zip(np.where(self.map == 0)[0], np.where(self.map == 0)[1])])
                self.map = np.where(self.map > 9, 0, self.map)
    
    def get_zero_levels(self):
        while np.count_nonzero(self.map > 0) > 0:
            self.pass_days(1)
        return self.day
    
def get_neighbours(octopus_map, curr_pos):
    i, j = curr_pos
    m, n = octopus_map.shape
    neighbours = set()
    
    if i > 0:
        neighbours.add((i-1, j))
        if j > 0:
            neighbours.add((i-1, j-1))
    if i < m - 1:
        neighbours.add((i+1, j))
        if j < n - 1:
            neighbours.add((i+1, j+1))
    if j > 0:
        neighbours.add((i, j-1))
        if i < m - 1:
            neighbours.add((i+1, j-1))
    if j < n - 1:
        neighbours.add((i, j+1))
        if i > 0:
            neighbours.add((i-1, j+1))
    
    return neighbours

def iterate_flashes(octopus_map, flashing):
    m, n = octopus_map.shape
    for i in range(m):
        for j in range(n):
            neighbours = get_neighbours(octopus_map, (i,j))
            for neighb in neighbours - flashing:
                if octopus_map[i,j] != 0 and octopus_map[neighb] == 0:
                   octopus_map[i,j] += 1

if __name__ == "__main__":
    print(octi_map)
    octo = OctoPIE(octi_map)
    octo.pass_days(100)
    
    print(f"Flashes in 100 days: {octo.flashes}")
    
    octo = OctoPIE(octi_map)
    days = octo.get_zero_levels()
    
    print(f"Days for all 0 levels: {days}")