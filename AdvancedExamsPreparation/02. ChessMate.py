def is_valid(r, c, ):
    if 0 <= r < 8 and 0 <= c < 8:
        return True
    return False


def count_queens(the_matrix, row_1, col_1, queens_count):
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queens_count = []
    curr_row = row_1
    curr_col = col_1
    for i in range ( len ( moves ) ):

        while True:
            curr_row += moves[i][0]
            curr_col += moves[i][1]
            if is_valid ( curr_row, curr_col ):
                if the_matrix[curr_row][curr_col] == 'Q':
                    queens_count.append ( [curr_row, curr_col] )
                    curr_row = row_1
                    curr_col = col_1
                    break
            else:
                curr_row = row_1
                curr_col = col_1
                break
    return queens_count


matrix = []
queens = []
kings_row = 0
kings_col = 0
for row_index in range ( 8 ):
    matrix.append ( [x for x in input ().split ()] )
for i in range ( len ( matrix ) ):
    for j in range ( len ( matrix[i] ) ):
        if matrix[i][j] == 'K':
            kings_row = i
            kings_col = j
current_row = kings_row
current_col = kings_col

queens = count_queens ( matrix, current_row, current_col, queens )
if len ( queens ) > 0:
    for queen in queens:
        print ( queen )
else:
    print ( "The king is safe!" )