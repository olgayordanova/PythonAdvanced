from itertools import chain

def get_possition(matrix):
    pos = [(row, col) for col in range ( len(matrix) ) for row in range ( len(matrix) ) if matrix[row][col] == "K"]
    row = pos[0][0]
    col = pos[0][1]
    return row, col

def horisontals(coord, size, matrix):
    x, y = coord
    h_1 = [(x, y) for y in range ( y + 1, size, 1 )]
    h_2 = [(x, y) for y in range ( y - 1, -1, -1 )]
    v_1 = [(x, y) for x in range ( x + 1, size, 1 )]
    v_2 = [(x, y) for x in range (  x - 1, -1, -1  )]
    d = []
    for el in h_1:
        if matrix[el[0]][el[1]] == "Q":
            d.append ( el )
            break
    for el in h_2:
        if matrix[el[0]][el[1]] == "Q":
            d.append ( el )
            break
    for el in v_1:
        if matrix[el[0]][el[1]] == "Q":
            d.append ( el )
            break
    for el in v_2:
        if matrix[el[0]][el[1]] == "Q":
            d.append ( el )
            break
    return d


def diagonals(coord, size, matrix ):
    x, y = coord
    d_1= list(chain([(x, y)],zip(range(x - 1, -1, -1), range(y - 1, -1, -1)),))
    d_2 = list(chain([(x, y)], zip(range(x + 1, size, 1), range(y + 1, size, 1)),))
    d_3 = list(chain([(x, y)],zip(range(x + 1, size, 1), range(y - 1, -1, -1)),))
    d_4 = list(chain([(x, y)],zip(range(x - 1, -1, -1), range(y + 1, size, 1)),))
    d=[]
    for el in d_1:
        if matrix[el[0]][el[1]]=="Q":
            d.append(el)
            break
    for el in d_2:
        if matrix[el[0]][el[1]]=="Q":
            d.append(el)
            break
    for el in d_3:
        if matrix[el[0]][el[1]]=="Q":
            d.append(el)
            break
    for el in d_4:
        if matrix[el[0]][el[1]]=="Q":
            d.append(el)
            break
    return d


matrix = [ list(input().split(' ')) for _ in range(8)]
king_row, king_col = get_possition ( matrix )
coordinates = []

flat = horisontals((king_row, king_col), 8, matrix)
diag_coord = diagonals((king_row, king_col), 8, matrix )

m_d = flat+diag_coord

if len(m_d) == 0:
    print("The king is safe!")
else:
    for el in m_d:
        l_el = list(el)
        print(l_el)