opp = {
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
    'EAST': 'WEST',
    'WEST': 'EAST'
}

print(opp['NORTH'])

def dirReduc(arr):
    i = 1
    while i < len(arr):
        if arr[i] == opp[arr[i-1]]:
            arr.pop(i)
            arr.pop(i-1)
            i -= 1
        else:
            i += 1
    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))