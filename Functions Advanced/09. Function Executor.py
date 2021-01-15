def sum_numbers(num1, num2):
    return (num1) + (num2)

def multiply_numbers(num1, num2):
    return (num1) * (num2)

def func_executor(*args):
    l=[]
    for el in args:
        res = el[0](*el[1])
        l.append(res)
    return l
#
# print(func_executor((sum_numbers, (15, 80))))
#
# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))