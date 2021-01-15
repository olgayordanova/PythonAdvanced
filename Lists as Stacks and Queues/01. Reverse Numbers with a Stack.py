number = input().split(' ')
reverser_number=[]
for i in range(len(number)):
    reverser_number.append(number.pop())
print(' '.join(reverser_number))