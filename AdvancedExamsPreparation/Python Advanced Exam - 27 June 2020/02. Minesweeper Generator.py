def get_sum (i, j, matrix, size):
    count = 0
    x_poss= [-1, -1, -1, 0, 0, 1, 1, 1]
    y_poss = [-1, 0, 1, -1, 1, -1, 0, 1]
    for k in range ( 8 ):
        x = i + x_poss[k]
        y = j + y_poss[k]
        if (x >= 0 and y >= 0 and x < size and
                y < size and matrix[x][y] == '*'):
            count += 1
    return count

def get_pos_t(el):
    el = el.replace('(', '')
    el = el.replace ( ')', '' )
    out_el = (int(el) for el in el.split(', '))
    return out_el

size = int(input())
n = int(input())

bombs_position =[]
for _ in range (n):
    el = input()
    out_el = get_pos_t(el)
    bombs_position.append(out_el)

matrix = [["0" for _ in range(size)] for _ in range(size)]
for k in range (n):
    i, j = bombs_position[k]
    matrix[i][j] = "*"

for a in range(size):
    for b in range ( size ):
        if  matrix[a][b] !='*':
            matrix[a][b]= get_sum(a,b,matrix, size)

print ('\n'.join( ' '.join(map(str, el)) for el in matrix))