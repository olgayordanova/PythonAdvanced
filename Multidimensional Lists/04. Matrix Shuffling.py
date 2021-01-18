rows, cols = map(int, input().split(' '))
matrix = [[(el) for el in input().split(' ')] for _ in range(rows)]

while True:
    command =input()
    if command=='END':
        break
    try:
        action, *data = command.split(' ')
        x1, y1,x2,y2   = [int ( el ) for el in data]
        matrix[x1][y1],matrix[x2][y2]= matrix[x2][y2],matrix[x1][y1]
        print ( '\n'.join ( ' '.join ( map ( str, el ) ) for el in matrix ) )
    except:
        print('Invalid input!')

