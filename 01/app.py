import numpy as np
from collections import Counter

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        data = np.array([list(map(int, line.split())) for line in lines])
        column1, column2 = data.T
    return column1, column2

def part1(column1,column2):
    deltas = 0
    column1.sort()
    column2.sort()
    for i in range(len(column1)):
        column_delta = column1[i] - column2[i]
        deltas += abs(column_delta)
    return deltas

def part2(column1, column2):
    score = 0
    count2_dict = Counter(column2)
    for key in column1:
        score += key * count2_dict[key]
    return score

if __name__ == '__main__':
    column1, column2 = read_file('input.txt')
    answer_part1 = part1(column1,column2)
    answer_part2 = part2(column1,column2)

    print(f"Total Distance: {answer_part1}")
    print(f"Similarity score: {answer_part2}")