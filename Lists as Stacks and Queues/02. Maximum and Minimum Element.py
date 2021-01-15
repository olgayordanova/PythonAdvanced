n=int(input())
stack =[]
for i in range (n):
    command = input().split(' ')
    action = int(command[0])
    if action == 1:
        element = int(command[1])
        stack.append(element)
    elif action == 2:
        if len(stack)>0:
            stack.pop()
    elif action == 3:
        if len ( stack ) > 0:
            print(f"{max(stack)}")
    elif action == 4:
        if len ( stack ) > 0:
            print(f"{min(stack)}")

reverced_stack = reversed(stack)
print(', '.join([str(i) for i in reverced_stack]))
