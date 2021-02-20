def numbers_searching(*arg):
    l=[]
    input_numbers = arg
    calibrating_set = set([el for el in range(min(input_numbers),max(input_numbers) +1)])
    my_set = set(input_numbers)

    diff = list((calibrating_set-my_set))[0]
    l.append(diff)

    dupl = sorted(list(set([el for el in arg if arg.count(el)>1])))
    l.append ( dupl )

    return l





# if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number
# and 2, 4 as duplicate numbers in the following format: [3, [2, 4]]

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
