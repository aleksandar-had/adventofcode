def solution_part1():
    measures = [int(num) for num in open("input.txt")]
    res = 0
    for i in range(1, len(measures)):
        res += 1 if measures[i] > measures[i-1] else 0
    print(res)
    
def solution_part2():
    measures = [int(num) for num in open("input.txt")]
    res = 0
    old_sum = sum(measures[:3])
    for i in range (3, len(measures)):
        new_sum = old_sum + measures[i] - measures[i-3]
        res += 1 if new_sum > old_sum else 0
        old_sum = new_sum
    print(res)
    
if __name__ == "__main__":
    solution_part1()
    solution_part2()
    