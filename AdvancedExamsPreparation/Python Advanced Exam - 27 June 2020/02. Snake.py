def make_jump (r, c, mtr):
    for i in range (len(mtr)):
        for j in range (len(mtr)):
            if mtr[i][j]=="B" and (i!=r and j!=c):
                return i,j

def is_valid_position (row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

n = int(input())
matrix = [ list(input()) for _ in range(n)]
move_dict = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}
coord = [(x,y) for x in range(0,n) for y in range(0,n) if matrix[x][y]=="S"]
current_r, current_c =coord[0][0], coord[0][1]
food_quantity=0

command = input()
while command!="":
    move_r, move_c = move_dict[command]
    if is_valid_position (current_r+move_r, current_c+move_c, n):
        move_position = matrix[current_r+move_r][current_c+move_c]
        matrix[current_r + move_r][current_c + move_c] ="S"
        matrix[current_r][current_c] = "."
        if move_position =="-":
            current_r, current_c = current_r + move_r, current_c + move_c
        elif move_position =="*":
            food_quantity+=1
            current_r, current_c = current_r + move_r, current_c + move_c
            if food_quantity>=10:
                print("You won! You fed the snake.")
                break
        elif move_position =="B":
            matrix[current_r + move_r][current_c + move_c] = "."
            current_r, current_c = make_jump (current_r, current_c, matrix)
    else:
        matrix[current_r][current_c] = "."
        print("Game over!")
        break
    command = input ()
print(f"Food eaten: {food_quantity}")
print ('\n'.join( ''.join((el)) for el in matrix))