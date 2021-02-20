def is_valid_position (pos, n):
    row, col = pos
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def get_pollinated(pollinated_flowers, pos, matrix):
    i,j =pos
    if matrix[i][j]=='f': #or matrix[i][j]=='O':
        pollinated_flowers+=1
    return pollinated_flowers


def make_move(old_pos,new_pos, matrix):
    r,c = old_pos
    rn, cn = new_pos
    matrix[r][c] = '.'
    matrix[rn][cn] = 'B'
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


size = int(input())
matrix = [[char for char in input()] for _ in range(size)]
pollinated_flowers = 0

bee_position = get_possition ( matrix, 'B' )
flag_bonus =False
while True:
    command = input().strip()
    if command == 'End':
        break
    bee_next_position = get_next_move(bee_position, command)
    if is_valid_position((bee_next_position), size):
        if matrix[bee_next_position[0]][bee_next_position[1]] == 'O':
            # pollinated_flowers+=1
            flag_bonus =True
        else:
            pollinated_flowers=get_pollinated(pollinated_flowers, bee_next_position, matrix)
            matrix = make_move(bee_position,bee_next_position, matrix)
    else:
        matrix[bee_position[0]][bee_position[1]] = '.'
        print("The bee got lost!")
        break
    if flag_bonus ==True:
        matrix = make_move ( bee_position, bee_next_position, matrix )
        bee_next_next_position = get_next_move(bee_next_position, command)
        if  is_valid_position((bee_next_next_position), size):
            pollinated_flowers = get_pollinated ( pollinated_flowers, bee_next_next_position, matrix )
            matrix = make_move ( bee_next_position, bee_next_next_position, matrix )
        bee_position = (get_possition ( matrix, 'B' ))
        flag_bonus = False
    else:
        bee_position = (get_possition ( matrix, 'B' ))


if pollinated_flowers<5:
    print(f"The bee couldn't pollinate the flowers, she needed {5-pollinated_flowers} flowers more")
else:
    print(f"Great job, the bee manage to pollinate {pollinated_flowers} flowers!")
print ('\n'.join( ''.join(map(str, el)) for el in matrix))