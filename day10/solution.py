from collections import deque

with open("input.txt", 'r') as f:
    chunks = [line.strip() for line in f.read().splitlines()]
    
    
# DICT HELPERS
pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
bracket_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    # 
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def solution_part1_part2():
    corrupted_score = 0
    incomplete_scores = list()
    corrupted = False
    
    for chunk in chunks:
        incomplete = 0
        corrupted = False
        stack = deque()
        
        for c in chunk:
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            elif c in pairs:
                bracket_to_close = stack.pop()
                if bracket_to_close != pairs[c]:
                    corrupted_score += bracket_scores[c]
                    corrupted = True
                    break
        if not corrupted:
            while stack:
                bracket = stack.pop()
                incomplete = incomplete * 5 + bracket_scores[bracket]
            incomplete_scores.append(incomplete)
            
    incomplete_scores.sort()

    return corrupted_score, incomplete_scores[len(incomplete_scores) // 2]

if __name__ == "__main__":
    print(solution_part1_part2())