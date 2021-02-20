def is_valid_position (row, col, n, m):
    if 0 <= row < n and 0 <= col < m:
        return True
    return False

def make_move(matrix, flower_row, flower_col, n,m):
    for j in range(m):
        matrix[flower_row][j] +=1
    for i in range (n):
        matrix[i][flower_col] += 1
    matrix[flower_row][flower_col] -= 1
    return matrix

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

flowers_position = []
while True:
    commmand = input()
    if commmand=='Bloom Bloom Plow':
        break
    flowers_position.append(tuple(map(int,commmand.split())))

for flower in flowers_position:
    flower_row, flower_col = flower[0],flower[1]
    if is_valid_position(flower_row, flower_col, n,m ):
        matrix = make_move(matrix, flower_row, flower_col,n,m)
    else:
        print("Invalid coordinates.")
        continue

print ( '\n'.join ( ' '.join ( map ( str, el ) ) for el in matrix ) )