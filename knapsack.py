from pprint import pprint
import numpy as np

w = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]
v = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]

test_weight = [1, 5, 3, 4]
test_value = [15, 10, 9, 5]

def solve(weight_list, value_list, capacity):
    assert(len(weight_list) == len(value_list))
    w = [0] + weight_list
    v = [0] + value_list
    n = len(w)

    table = np.zeros((n, capacity), dtype=np.int16)
    
    for i in range(1, n):
        for capacity_remaining in range(capacity):
            if w[i] <= capacity_remaining:
                table[i, capacity_remaining] = max(
                    table[i-1, capacity_remaining],     # don't take it
                    v[i] + table[i, capacity_remaining - w[i]] # take it
                )
            else:
                table[i, capacity_remaining] = table[i-1, capacity_remaining]

    return table

results = solve(test_weight, test_value, 8)
print(results)