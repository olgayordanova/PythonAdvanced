def positive_sum (numbers):
    return sum(el for el in numbers if el>=0)

def negative(numbers):
    return sum(el for el in numbers if el <0)

numbers =[int(el) for el in input().split(' ')]
print (negative(numbers))
print(positive_sum (numbers))
if positive_sum (numbers)>abs(negative(numbers)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
