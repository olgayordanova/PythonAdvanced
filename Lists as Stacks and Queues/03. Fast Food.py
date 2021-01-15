from collections import deque
flag = False
orders = deque()
quantity = int(input())
line = input().split(' ')

for el in line:
    orders.append(int(el))
print(max(orders))

while len(orders)>0:
    current_quantity=orders.popleft ()
    if quantity>=current_quantity:
        quantity-=current_quantity
    else:
        orders.appendleft(current_quantity)
        flag = True
        break

if flag == True:
    orders_left = [str(el) for el in orders]
    print(f"Orders left: {' '.join(orders_left)}")
else:
    print ( "Orders complete" )