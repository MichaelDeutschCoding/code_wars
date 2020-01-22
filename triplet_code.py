from collections import defaultdict

def recoverSecret(triplets):
    d = defaultdict(set)
    for line in triplets:
        for i in range(3):
            d[line[i]].update(line[:i])
    
    result = ''
    while d:
        c = next(k for k, v in d.items() if not v)
        result += c      
        del d[c]
        for letters in d.values():
            if c in letters:
                letters.remove(c)
    return result


secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]


print(recoverSecret(triplets))
