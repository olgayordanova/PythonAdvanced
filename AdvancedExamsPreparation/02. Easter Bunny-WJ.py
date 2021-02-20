def get_steps(direction, matrix,bunny_row, bunny_col):
    steps =[]
    if direction == 'up':
        for i in range (bunny_row-1,-1,-1):
            if matrix[i][bunny_col]!='X':
                steps.append([i,bunny_col])
            else:
                break
    elif direction == 'down':
        for i in range (bunny_row+1,len (matrix)):
            if matrix[i][bunny_col]!='X':
                steps.append([i,bunny_col])
            else:
                break
    elif direction == 'right':
        for j in range (bunny_col+1,len (matrix)):
            if matrix[bunny_row][j]!='X':
                steps.append([bunny_row, j])
            else:
                break
    elif direction == 'left':
        for j in range (bunny_col-1,-1,-1):
            if matrix[bunny_row][j]!='X':
                steps.append([bunny_row, j])
            else:
                break
    return steps

def get_key(val, d):
   for key, value in d.items():
      if val == value:
         return key

def get_possition(matrix):
    pos = [(row, col) for col in range ( size ) for row in range ( size ) if matrix[row][col] == "B"]
    row = pos[0][0]
    col = pos[0][1]
    return row, col


def until_not_x(lst):
    for i in lst:
        if i != "X":
            yield int(i)
        else:
            break


def get_direction_sums(hor, ver, d, bunny_row, bunny_col):
    d['right'] = sum(until_not_x(hor[bunny_col+1: len(hor)]))
    d['down'] = sum ( until_not_x ( ver[bunny_row + 1: len ( ver )] ) )
    hor = list(reversed(hor))
    ver = list(reversed(ver))
    bunny_col = hor.index('B')
    bunny_row = ver.index('B')
    if bunny_row ==0:
        bunny_row = 1
    if bunny_col ==0:
        bunny_col = 1
    d['left'] = sum(until_not_x(hor[bunny_col+1: len(hor)]))
    d['up'] = sum ( until_not_x ( ver[bunny_row+1: len ( ver )] ) )
    return d


size = int(input())
matrix = [ list(input().split(' ')) for _ in range(size)]
direction_sums = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
max_sum = 0

bunny_row, bunny_col = get_possition(matrix)
hor = [matrix[row][col] for col in range (size) for row in range (size) if row == bunny_row]
ver = [matrix[row][col] for col in range (size) for row in range (size) if col == bunny_col]
direction_sums = get_direction_sums(hor, ver, direction_sums,bunny_row, bunny_col)

max_value = max(direction_sums.values())
direction = get_key(max_value,direction_sums)

print(direction)
steps = get_steps(direction, matrix, bunny_row, bunny_col )
for el in steps:
    print( el)
print(max_value)


