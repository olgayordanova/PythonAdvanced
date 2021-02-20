import math
import itertools
def is_valid_position (pos, n):
    row, col = pos
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

def is_not_wall(pos, matrix):
    row, col = pos
    if matrix[row][col]=='X':
        return False
    return True

def get_sum(pos, matrix, coinsum):
    row, col = pos
    coinsum = int(matrix[row][col])
    return coinsum

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


size= int(input())
matrix = [[el for el in input().split()] for _ in range(size)]
player_position = get_possition ( matrix, 'P' )

coins = 0
player_path=[]

command = input ()
while command:
    if command not in  {'up', 'down', 'left', 'right'}:
        continue

    player_next_position = get_next_move(player_position, command)
    if is_valid_position((player_next_position), size) and is_not_wall(player_next_position, matrix):
        player_path.append(player_next_position)
        coins += get_sum ( player_next_position, matrix, coins )

        player_position = player_next_position
        if coins >= 100:
            break
    else:
        if coins==0:
            coins=0
        else:
            coins=math.floor(coins/2)
        break
    command = input ()

if coins>=100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print(f"Your path:")
for el in player_path:
    n_el= list(itertools.chain(el))
    print(f"{n_el}")


