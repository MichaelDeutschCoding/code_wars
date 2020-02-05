from collections import defaultdict

sample_clues = ( 2, 2, 1, 3,  
  2, 2, 3, 1,  
  1, 2, 2, 3,  
  3, 2, 1, 3 )

print(sample_clues)



def solve_puzzle(clues):
    d = defaultdict(set)
    