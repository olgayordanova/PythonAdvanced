def rotate_list(l, y=1):
    y = y % len ( l )
    return l[y:] + l[:y]

def reverce_list(l):
    return l[::-1]


rows, cols = map(int, input().split())
snake=[ch for ch in input()]
matrix = [ [] for _ in range(rows)]

while len ( snake ) <=cols:
    snake +=snake

for i in range (rows):
    matrix[i] = snake[:cols]
    snake= rotate_list(snake, cols)
    if i%2!=0:
        matrix[i] = reverce_list(matrix[i])

print ('\n'.join( ''.join(map(str, el)) for el in matrix))