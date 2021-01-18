import itertools

rows, cols = map(int, input().split(' '))
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

size = 3
total_sumatrix = []
total_sum = []


for i in range(rows-size+1):
    submatrix = []
    for j in range(cols-size+1):
        submatrix = [
            matrix[i+n][j:j+size]
            for n in range (size)
        ]
        total_sum.append ( sum ( itertools.chain ( *submatrix ) ) )
        total_sumatrix.append ( submatrix )

max_sum = max(total_sum)
ind = total_sum.index(max_sum)
max_submatrix = total_sumatrix[ind]
print(f'Sum = {max_sum}')
print ('\n'.join( ' '.join(map(str, el)) for el in max_submatrix))

