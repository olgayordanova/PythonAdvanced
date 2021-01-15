def valid(col, row, size):
    if 0<=col<size and 0<=row<size:
        return True

size = int(input())
matrix = [[int(el) for el in input().split(' ')] for _ in range(size)]

while True:
    line = input()
    if line == 'END':
        break
    action, row, col, val = line.split(' ')
    row = int(row)
    col = int ( col )
    val = int ( val )
    if valid(col, row, size):
        if action == 'Add':
            matrix[row][col]+=val
        elif action == 'Subtract':
            matrix[row][col] -= val
    else:
        print('Invalid coordinates')
print ( '\n'.join ( ' '.join ( map ( str, el ) ) for el in matrix ) )
