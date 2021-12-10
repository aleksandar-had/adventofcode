with open("input.txt", 'r') as f:
    codes = [[set(c) for c in line.split(" ")] for line in f.read().splitlines()]

def solution_part1():
    count = 0
    for code in codes:
        count += sum(len(digit) in (2,3,4,7) for digit in code[-4:])
    return count
    
def solution_part2():
    count = 0
    for code in codes:
        # lengths 2,3,4,7 will be at ind 0,1,2,9
        # numbers 1,7,4,8 will be at ind 0,1,2,9
        sorted_input = sorted(code[:10], key=len)
        # [1, 7, 4, ..., 8]
        
        # length 5 will be at ind 3,4,5
        # numbers 2,3,5 will be at ind [3:6]
        # number 7 is fully contained only in number 3
        # number 4 shares 3 sides with number 5
        # number 4 shares 2 sides with number 2
        sorted_input[3:6] = sorted(sorted_input[3:6], key=lambda f: (sorted_input[1].issubset(f), len(sorted_input[2] & f)))
        # [1, 7, 4, 2, 5, 3, ..., 8]
        
        # length 6 will be at ind 6,7,8
        # numbers 0,6,9 will be at ind [6:9]
        # numbers 4 and 7 are fully contained only in number 9
        # number 7 and not 4 is fully contained only in number 0
        # numbers 4 and 7 are not fully contained in number 6
        sorted_input[6:9] = sorted(sorted_input[6:9], key=lambda f: (sorted_input[2].issubset(f), sorted_input[1].issubset(f)))
        # [1, 7, 4, 2, 5, 3, 6, 0, 9, 8]
        # ind of correct ordering: [7, 0, 3, 5, 2, 4, 6, 1, 9, 8]
        correct_input = [sorted_input[i] for i in [7, 0, 3, 5, 2, 4, 6, 1, 9, 8]]
        
        four_digits = ""
        for digit in code[-4:]:
            for i, input in enumerate(correct_input):
                if input == digit:
                    four_digits += str(i)
        count += int(four_digits)
                    
    return count
    
if __name__ == "__main__":
    print(solution_part1())
    print(solution_part2())