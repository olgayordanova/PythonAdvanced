def odd_sum (numbers):
    return sum(el for el in numbers if el%2!=0)

def even_sum(numbers):
    return sum(el for el in numbers if el%2==0)

command = input()
numbers =[int(el) for el in input().split(' ')]
if command=='Odd':
    print(odd_sum(numbers)*len(numbers))
elif command=='Even':
    print(even_sum(numbers)*len(numbers))
