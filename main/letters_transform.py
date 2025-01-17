import string

def get_key(dictionary, val): 
    for key, value in dictionary.items(): 
         if val == value: 
             return key 
  
    return "Error: key doesn't exist"

def get_val(dictionary, k):
    for key, value in dictionary.items():
        if k == key:
            return value

    return "Error: value doesn't exist"

def dots_spaces(lettergrid):
    for row in range(len(lettergrid)):
        for column in range(len(lettergrid)):
            if lettergrid[row][column] == '.':
                return True
            elif lettergrid[row][column] == ' ':
                return False

def check_if_letters(grid):
    for row in range(len(grid)):
        for column in range(len(grid)):
            if isinstance(grid[row][column],str):
                return True 
            #else:
                #return False

def to_numbers(lettergrid):

    gridSize = len(lettergrid) + 1
    numKeys = [num for num in range(1,gridSize)]
    letterValues = list(map(chr, range(ord('A'), ord('A')+gridSize)))
    alphanumDict = dict(zip(numKeys, letterValues))
    if dots_spaces(lettergrid) == True:
        alphanumDict[0] = '.'
    elif dots_spaces(lettergrid) == False:
        alphanumDict[0] = ' '

    numbergrid = [[] for new_list in range(len(lettergrid))]    
    blanklist = []
    for row in range(len(lettergrid)):
        for column in range(len(lettergrid)):
            blanklist.append(get_key(alphanumDict, lettergrid[row][column]))
        numbergrid[row].extend(blanklist)
        blanklist.clear()
    return numbergrid

def to_letters(numbergrid):
    
    gridSize = len(numbergrid) + 1
    numKeys = [num for num in range(1,gridSize)]
    letterValues = list(map(chr, range(ord('A'), ord('A')+gridSize)))
    alphanumDict = dict(zip(numKeys, letterValues))
    alphanumDict[0] = '.'

    lettergrid = [[] for new_list in range(len(numbergrid))]
    blanklist = []
    for row in range(len(numbergrid)):
        for column in range(len(numbergrid)):
            blanklist.append(get_key(alphanumDict, numbergrid[row][column]))
        lettergrid[row].extend(blanklist)
        blanklist.clear()
    return lettergrid

grid = [['D','A','.','.','.','G','.','.','E'],
        ['.','.','C','B','.','I','.','.','H'],
        ['.','.','H','.','E','A','I','D','.'],
        ['F','C','E','.','.','.','.','G','.'],
        ['.','.','B','.','.','.','A','.','.'],
        ['.','D','.','.','.','.','H','E','B'],
        ['.','I','D','G','C','.','F','.','.'],
        ['C','.','.','D','.','F','B','.','.'],
        ['H','.','.','I','.','.','.','C','D']]

print(to_numbers(grid))
print(to_letters(grid))
print(check_if_letters(grid))