import itertools

def is_valid_position (row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def get_possition(matrix, str):
    pos = [(row, col) for col in range ( len(matrix) ) for row in range ( len(matrix) ) if matrix[row][col] == str]
    row = pos[0][0]
    col = pos[0][1]
    return row, col


def get_next_move(position, dir):
    dir_deltas = {
        'up': (-1, 0),
        'down': (+1, 0),
        'left': (0, -1),
        'right': (0, +1),
    }
    (row_index, column_index) = position
    (row_delta, column_delta) = dir_deltas[dir]
    return row_index + row_delta, column_index + column_delta


def make_move(r,c,rn,cn, matrix):
    matrix[r][c] = '*'
    matrix[rn][cn] = 's'
    return matrix


size= int(input())
commands  = list(map(str, input().split()))
matrix = [[el for el in input().split()] for _ in range(size)]

flag_end =False

count_coal =list(itertools.chain ( *matrix )).count('c')
miner_position = get_possition ( matrix, 's' )
miner_row, miner_col = miner_position[0],miner_position[1]

for comand in commands:
    miner_next_row, miner_next_col = get_next_move(miner_position, comand)
    if not is_valid_position ( miner_next_row, miner_next_col, size ):
        continue
    if matrix[miner_next_row][miner_next_col]=='c':
        matrix = make_move(miner_row, miner_col,miner_next_row, miner_next_col, matrix)
        miner_row, miner_col = miner_next_row, miner_next_col
        miner_position = (miner_row, miner_col)
        count_coal-=1
        if count_coal == 0:
            print(f"You collected all coals! ({miner_next_row}, {miner_next_col})")
            break
    elif matrix[miner_next_row][miner_next_col]=='e':
        print(f"Game over! ({miner_next_row}, {miner_next_col})")
        flag_end =True
        break
    elif matrix[miner_next_row][miner_next_col]=='*':
        matrix = make_move ( miner_row, miner_col, miner_next_row, miner_next_col, matrix )
        miner_row, miner_col = miner_next_row, miner_next_col
        miner_position = (miner_row, miner_col)

miner_position = get_possition ( matrix, 's' )
if count_coal == 0 or flag_end:
    pass
else:
    print(f"{count_coal} coals left. ({miner_position[0]}, {miner_position[1]})")

