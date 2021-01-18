import itertools

def validate_position(row, col, size):
    return 0 <= row < size and 0 <= col < size


def explode(matrix, x , y, n):
    bomb_value = matrix[x][y]
    if matrix[x][y]<=0:
        return matrix
    matrix[x][y] = 0
    for i in range(x-1,x+2):
        for j in range ( y-1,y+2):
            if validate_position(i, j, n) and matrix[i][j]>0:
                matrix[i][j] -=bomb_value
    return matrix


n = int ( input () )
matrix = [[int(el) for el in input().split()] for _ in range(n)]
coordinates = input().split()
row_mines = list(map(int, list(zip(*coordinates))[0]))
col_mines = list(map(int, list(zip(*coordinates))[2]))

for i in range (len(row_mines)):
    matrix = explode(matrix,row_mines[i] , col_mines[i],n)

count_alive =len([el for el in list( itertools.chain ( *matrix ) ) if el>0])
sum_alive = sum([el for el in list( itertools.chain ( *matrix ) ) if el>0])

print(f'Alive cells: {count_alive}')
print(f'Sum: {sum_alive}')
print ('\n'.join( ' '.join(map(str, el)) for el in matrix))