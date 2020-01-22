def incrementing(s):
    for i in range(len(s) - 1):
        if s[i] == '0':
            return False
        if s[i] == '9' and s[i+1] == '0':
            continue
        if not ord(s[i]) + 1 == ord(s[i+1]):
            return False
    return True

def decrementing(s):
    for i in range(len(s) - 1):
        if not ord(s[i]) - 1 == ord(s[i+1]):
            return False
    return True

def zeros(s):
    for digit in s[1:]:
        if not digit == '0':
            return False
    return True


def check(number, awesome_phrases):
    if number < 100:
        return False
    if number in awesome_phrases:
        return True
    s = str(number)
    if incrementing(s):
        return True
    if decrementing(s):
        return True
    if zeros(s):
        return True
    if all(s[i] == s[0] for i in range(len(s))):
        return True
    if s == s[::-1]:
        return True
    return False

def is_interesting(number, awesome_phrases):
    if check(number, awesome_phrases):
        return 2
    if check(number+1, awesome_phrases):
        return 1
    if check(number+2, awesome_phrases):
        return 1        
    return 0
