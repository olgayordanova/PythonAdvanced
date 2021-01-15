def rotate_matrix(matrix):
    rot_matrix = []
    for j in range (len(matrix)-1,-1,-1):
        rot_matrix.append(matrix[j])
    return rot_matrix

size = int(input())
matrix = [[int(el) for el in input().split(', ')] for _ in range(size)]

first_diagonal = [matrix[i][i] for i in range(size)]
first_diagonal_sum= sum(first_diagonal)

new_matrix = rotate_matrix(matrix)
secondary_diagonal = [new_matrix[k][k] for k in range (size)]
secondary_diagonal_sum = sum(secondary_diagonal)

print(f'First diagonal: {", ".join([str(el) for el in first_diagonal])}. Sum: {first_diagonal_sum}')
print(f'Second diagonal: {", ".join([str(el) for el in secondary_diagonal[::-1]])}. Sum: {secondary_diagonal_sum}')