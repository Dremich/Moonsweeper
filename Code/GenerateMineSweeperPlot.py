import random

def generateMap(size, numMines):
    map = [[0] * size for _ in range(size)]
    rng = random.Random()
    
    for mines in range(numMines):
        row = rng.randint(0, size-1)
        col = rng.randint(0, size-1)
        if map[row][col] == -1:
            mines -= 1 #If index already is a mine run loop again
        else:
            map[row][col] = -1
    
    minesAdjacent = 0
    for i in range(size):
        for j in range(size): #Iterate through 2D array and set elements to the # of bombs touching
            if map[i][j] != -1:
                list = getAdjacent(map, i, j)
                for x in range(len(list)):
                    if list[x] == -1:
                        minesAdjacent += 1
                map[i][j] = minesAdjacent
                minesAdjacent = 0
            else:
                map[i][j] = -1
    
    return map

def isValidPos(i, j, n, m):
    if i < 0 or j < 0 or i > n - 1 or j > m - 1:
        return False
    return True

def getAdjacent(arr, i, j):
    n = len(arr)
    m = len(arr[0])
    
    v = []
    
    if isValidPos(i - 1, j - 1, n, m):
        v.append(arr[i - 1][j - 1])
    if isValidPos(i - 1, j, n, m):
        v.append(arr[i - 1][j])
    if isValidPos(i - 1, j + 1, n, m):
        v.append(arr[i - 1][j + 1])
    if isValidPos(i, j - 1, n, m):
        v.append(arr[i][j - 1])
    if isValidPos(i, j + 1, n, m):
        v.append(arr[i][j + 1])
    if isValidPos(i + 1, j - 1, n, m):
        v.append(arr[i + 1][j - 1])
    if isValidPos(i + 1, j, n, m):
        v.append(arr[i + 1][j])
    if isValidPos(i + 1, j + 1, n, m):
        v.append(arr[i + 1][j + 1])
    
    return v
#Test
size = 4
map = generateMap(size, 4)
for i in range(size):
    print()
    for j in range(size):
        print("{:2d}".format(map[i][j]), end="")
