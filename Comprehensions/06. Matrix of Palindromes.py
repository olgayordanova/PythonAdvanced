rows, cols = map(int, input().split(' '))
matrix=[[(chr(97+i)+chr(97+i+x)+chr(97+i)) for x in range (cols)] for i in range (rows)]
print ( '\n'.join ( ' '.join ( map ( str, el ) ) for el in matrix ) )