samples = {
    'ABAB' : 2,
    'AAAB' : 1,
    'BAAA' : 4,
    'QUESTION' : 24572,
    'BOOKKEEPER' : 10743
}

def rank(word):
    letters = list(word)
    prime = sorted(letters)

    print(letters, prime)

rank('DEAB')