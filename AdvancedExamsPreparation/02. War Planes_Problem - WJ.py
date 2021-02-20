import itertools

def get_count_killed_targets(count_all_targets,matrix):
    return count_all_targets- list(itertools.chain ( *matrix )).count('t')


def validate_position(row, col, size, step, direction):
    row, col = get_coord ( row, col, step, direction )
    return 0 <= row < size and 0 <= col < size


def get_possition(matrix):
    pos = [(row, col) for col in range ( len(matrix) ) for row in range ( len(matrix) ) if matrix[row][col] == "p"]
    row = pos[0][0]
    col = pos[0][1]
    return row, col


def get_coord(row, col, step, direction):
    directions = ['up', 'down', 'left', 'right']
    direction_steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range ( 4 ):
        if direction == directions[i]:
            row += direction_steps[i][0] * step
            col += direction_steps[i][1] * step
    return row, col


def make_shoot(matrix, row, col, step, direction):
    row, col = get_coord ( row, col, step, direction )
    matrix[row][col] = 'x'
    return matrix


def make_move(matrix, row, col, step, direction):
    row_n, col_n = get_coord ( row, col, step, direction )
    if matrix[row_n][col_n] == '.':
        matrix[row_n][col_n] = 'p'
        matrix[row][col] = '.'
    return matrix


n = int(input())
matrix = [ list(input().split(' ')) for _ in range(n)]
m = int(input())

count_all_targets = list(itertools.chain ( *matrix )).count('t')
count_killed_targets = 0
flag_all = False

for _ in range (m):
    command, direction, step_s = input().split(' ')
    step = int(step_s)
    plane_row, plane_col = get_possition ( matrix )
    if not validate_position(plane_row, plane_col, n, step, direction):
        continue
    if command=='shoot':
        matrix = make_shoot(matrix, plane_row, plane_col, step, direction)
        count_killed_targets = get_count_killed_targets(count_all_targets,matrix)
    elif command=='move':
        matrix = make_move(matrix, plane_row, plane_col, step, direction)
    if count_killed_targets == count_all_targets:
        flag_all = True
        break

if flag_all:
    print(f"Mission accomplished! All {count_killed_targets} targets destroyed.")
else:
    print(f"Mission failed! {count_all_targets-count_killed_targets} targets left.")
print ('\n'.join( ' '.join(map(str, el)) for el in matrix))