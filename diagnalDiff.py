#/bin/python3

def diagonalDifference(arr):
    lastIndex = len(arr) - 1
    diagnal1, diagnal2 = 0, 0
    for n in range(0, lastIndex + 1):
        diagnal1 += arr[n][n]
        diagnal2 += arr[lastIndex - n][n]
    return abs(diagnal1-diagnal2)


test = [[0,1,2],[0,1,2],[0,1,2]]
assert(diagonalDifference(test) == 0)
print(diagonalDifference(test))
