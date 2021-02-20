import itertools

def validate_position(row, col, size):
    return 0 <= row < size and 0 <= col < size

def santa_happy(matrix, i, j, count_presents):
    x_poss=[-1,0,1,0]
    y_poss=[0,1,0,-1]
    for k in range ( 4 ):
        x = i + x_poss[k]
        y = j + y_poss[k]
        if validate_position(x,y,len(matrix)):
            count_presents-=1
            matrix[x][y] ="-"
    return count_presents

def santa_move ( matrix, row, col, count_presents ):
    if matrix[row][col]=="V":
        count_presents-=1
    elif matrix[row][col]=="C":
        count_presents= santa_happy(matrix, row, col, count_presents)
    return count_presents

count_presents  = int(input())
size = int(input())
matrix = [ list(input().split(' ')) for _ in range(size)]
count_nice_presents_before_tour =list(itertools.chain ( *matrix )).count('V')

while True:
    if count_presents<=0:
        print("Santa ran out of presents!")
        break
    command = input()
    if command=="Christmas morning":
        break
    santa_pos = [(row,col) for col in range ( size ) for row in range ( size ) if matrix[row][col]=="S"]
    row = santa_pos[0][0]
    col=santa_pos[0][1]
    matrix[row][col] = "-"

    if command == 'up':
        if validate_position(row-1, col, size):
            row , col = row-1, col
    elif command == 'down':
        if validate_position(row+1, col, size):
            row , col = row+1, col
    elif command == 'left':
        if validate_position(row, col-1, size):
            row , col = row, col-1
    elif command == 'right':
        if validate_position(row, col+1, size):
            row , col = row, col+1

    count_presents = santa_move ( matrix, row, col, count_presents )
    matrix[row][col] = "S"


print ('\n'.join( ' '.join(map(str, el)) for el in matrix))


count_nice_presents_after_tour =list(itertools.chain ( *matrix )).count('V')

if count_nice_presents_after_tour ==0:
    print(f"Good job, Santa! {count_nice_presents_before_tour} happy nice kid/s.")
else:
    print(f"No presents for {count_nice_presents_after_tour} nice kid/s.")
