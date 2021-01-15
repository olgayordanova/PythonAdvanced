def odds(numbers):
    return list ( filter ( lambda x: x % 2 != 0, numbers ) )

def evens(numbers):
    return list ( filter ( lambda x: x % 2 == 0, numbers ) )

def even_odd (*line):
    command = line[-1]
    numbers =[int(line[i])for i in range(0, len(line)-1)]
    if command=='odd':
        return odds(numbers)
    elif command=='even':
        return evens(numbers)