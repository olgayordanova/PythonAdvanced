def is_valid_position (pos, n):
    row, col = pos
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

def get_letter(str, pos, matrix):
    i,j =pos
    if matrix[i][j]!='-':
        str+=matrix[i][j]
    return str


def make_move(old_pos,new_pos, matrix):
    r,c = old_pos
    rn, cn = new_pos
    matrix[r][c] = '-'
    matrix[rn][cn] = 'P'
    return matrix

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


initial_string  = input()
size = int(input())
matrix = [[char for char in input()] for _ in range(size)]

m = int(input())
player_position = get_possition ( matrix, 'P' )

for i in range(m):
    command = input().strip()
    player_next_position = get_next_move(player_position, command)
    if is_valid_position((player_next_position), size):
        initial_string=get_letter(initial_string, player_next_position, matrix)
        matrix = make_move(player_position,player_next_position, matrix)
    else:
        if initial_string:
            initial_string=initial_string[:len(initial_string)-1]
    player_position = (get_possition ( matrix, 'P' ))

print(initial_string)
print ('\n'.join( ''.join(map(str, el)) for el in matrix))