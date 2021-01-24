def add_to_list (lst, added_part, start_index):
    result = lst
    if start_index == 0:
        ll = lst[::-1]+added_part[::-1]
        result = ll[::-1]
    elif start_index == -1:
        result = lst[::] + added_part[::]
    return result

def remove_list (lst, remove_count, start_index):
    result = lst
    if start_index==0:
        if remove_count:
            result = lst[remove_count[0]:]
        else:
            result = lst[1:]
    elif start_index == -1:
        if remove_count:
            result = lst[:len ( lst ) - remove_count[0]]
        else:
            result = lst[0:len ( lst )-1]
    return result

def list_manipulator(numbers, command1, command2, *args):
    num_lst = [int(el) for el in args]
    manipulated_numbers = numbers
    if command1=="add" and command2=="beginning":
        manipulated_numbers= add_to_list ( numbers, num_lst, 0 )
    elif command1=="add" and command2=="end":
        manipulated_numbers= add_to_list ( numbers, num_lst, -1 )
    elif command1=="remove" and command2=="beginning":
        manipulated_numbers = remove_list (numbers, num_lst, 0)
    elif command1=="remove" and command2=="end":
        manipulated_numbers = remove_list (numbers, num_lst, -1)
    return manipulated_numbers



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
