import itertools
def equal_chars(submatrix):
    my_set = set(itertools.chain(*submatrix))
    if len(my_set)==1:
        return True
    return False

rows, cols = map(int, input().split(' '))
matrix = [[(el) for el in input().split(' ')] for _ in range(rows)]

submatrix = []
count_equal_chars = 0

for i in range(rows-1):
    for j in range(cols-1):
        submatrix=[
            [matrix[i][j],matrix[i][j+1]],
            [matrix[i+1][j],matrix[i+1][j+1]]
        ]
        if equal_chars(submatrix):
            count_equal_chars+=1

print(count_equal_chars)
