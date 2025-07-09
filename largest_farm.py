# given a AxB matrix of 1s and 0s, where 1 is good farm land and 0 is bad farm land,
# identify the largest sqaure of good farm land

from pprint import pprint

input = [
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 0],
]

def find_largest_farm(input_matrix):    
    dp_matrix = [[0] * len(input_matrix[0]) for _ in range(len(input_matrix))]
    max_size = -1

    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[0])):
            if input_matrix[i][j] == 0:
                continue

            left = dp_matrix[i][j-1] if j > 0 else 0
            top = dp_matrix[i-1][j] if i > 0 else 0
            diagonal = dp_matrix[i-1][j-1] if i > 0 and j > 0 else 0

            dp_matrix[i][j] = min(left, top, diagonal) + 1
            max_size = max(max_size, dp_matrix[i][j])

    pprint(dp_matrix)
    return max_size

print(find_largest_farm(input) ** 2)
