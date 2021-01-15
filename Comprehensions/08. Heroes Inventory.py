def get_count_items(name, d):
    return len([value for key, value in d.items ()if key.startswith ( name )])


def get_sum_costs(name, d):
    return sum([value for key, value in d.items ()if key.startswith ( name )])


names= input().split(', ')
d={}
while True:
    comand = input()
    if comand == "End":
        break
    name, item,cost =comand.split('-')
    dict_key = name+'@'+item
    if dict_key not in d:
        d[dict_key]=int(cost)
for name in names:
    print(f'{name} -> Items: {get_count_items(name, d)}, Cost: {get_sum_costs(name, d)}')
