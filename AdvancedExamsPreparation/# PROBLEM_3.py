def add_to_list (lst, added_part):
    result = lst
    for el in added_part:
        result.append(el)
    return result

def remove_s (lst, remove_count, start_index):
    result = lst
    for i in range(remove_count):
        if lst[i]:
            result =lst[remove_count:]
    return result


def remove_list ( lst,new_boxes):
    result = lst
    for el in new_boxes:
       result =  [value for value in result if value != el]
    return result


def stock_availability(lst, command, *args):
    # new_boxes = [str ( el ) for el in args]
    boxes = lst
    if command == "delivery":
        new_boxes = [str ( el ) for el in args]
        boxes = add_to_list ( boxes, new_boxes)
    elif command == "sell":
        try:
            n=int(*args)
            boxes= remove_s(boxes, n, 0)
        except:
            pass
        if not args:
            boxes = boxes[1:]
        else:
            new_boxes = [str ( el ) for el in args]
            boxes = remove_list ( boxes, new_boxes)
    return boxes


print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie","chocolate","vanilla"))
# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
