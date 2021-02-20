# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
def validate_position(row, col,n):
    return 0 <= row < n and 0 <= col < n

def get_magic_triangle (n):
    triangle = [[0] * n for _ in range(n)]

    for i in range ( 0, n):
        triangle[i][0] = 1
        triangle[i][i] = 1

    for i in range (2,n):
        for j in range ( 0, i+1):
            if validate_position(i-1,j-1,n) :
                triangle[i][j] =triangle[i-1][j-1]+triangle[i-1][j]

    out_triangle = []
    for el in triangle:
        el_out = [i for i in el if i>0]
        out_triangle.append(el_out)

    return out_triangle

get_magic_triangle(6)


# def get_magic_triangle(rows_count):
#     triangle = [[1 for _ in range(row)] for row in range(1, rows_count + 1)]
#
#     for row in range(2, rows_count):
#         for col in range(1, row):
#             triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
#
#     return triangle
#
#
# print(get_magic_triangle(10))