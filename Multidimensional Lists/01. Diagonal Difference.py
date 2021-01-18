def rotate_matrix(matrix):
    rot_matrix = []
    for j in range (len(matrix)-1,-1,-1):
        rot_matrix.append(matrix[j])
    return rot_matrix

size = int(input())
matrix = [[int(el) for el in input().split(' ')] for _ in range(size)]
primary_diagonal = sum([matrix[i][i] for i in range (size)] )

new_matrix = rotate_matrix(matrix)
secondary_diagonal = sum([new_matrix[k][k] for k in range (size)] )

print(abs(primary_diagonal-secondary_diagonal))


