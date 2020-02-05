from pprint import pprint
import numpy as np


# Example from https://en.wikipedia.org/wiki/Knapsack_problem
# capacity = 67
weights = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]
values = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]

test_weight = [1, 5, 3, 4]
test_value = [15, 10, 9, 5]

guru_w = [3, 4, 5, 9, 4]
guru_v = [3, 4, 4, 10, 4]

guru2_w = [12, 2, 1, 1, 4]
guru2_v = [4, 2, 1, 2, 10]

def solve(weight_list, value_list, capacity):
    assert(len(weight_list) == len(value_list))
    w = [0] + weight_list
    v = [0] + value_list
    n = len(w)

    table = np.zeros((n, capacity +1 ), dtype=np.int16)
    
    for i in range(1, n):
        for capacity_remaining in range(capacity + 1):
            if w[i] <= capacity_remaining:
                table[i, capacity_remaining] = max(
                    table[i-1, capacity_remaining],     # don't take it
                    v[i] + table[i -1, capacity_remaining - w[i]] # take it
                )
            else:
                table[i, capacity_remaining] = table[i-1, capacity_remaining]
    print(table)
    take = []
    j = capacity
    for i in range(n-1, 0, -1):
        if table[i, j] != table[i-1, j]:
            take.append(i)
            j -= w[i]

    return table[-1, -1], take

print(solve(weights, values, 67))
