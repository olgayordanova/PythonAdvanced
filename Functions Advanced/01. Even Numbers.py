def get_even(numbers):
    return [el for el in numbers if el%2==0]

numbers =[int(el) for el in input().split(' ')]
print(get_even(numbers))
