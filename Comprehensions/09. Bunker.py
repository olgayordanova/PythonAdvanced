def get_count(d):
    return  sum([d[key][0][0] for key, value in d.items ()])

def get_average(d, length):
    return  sum([d[key][0][1] for key, value in d.items ()])/length

def get_list_items(d, type):
    l=[]
    for key, value in d.items():
        key_type, key_item  = key.split('@')
        if key_type == type:
            l.append(key_item)
    return l

types = input().split(', ')
n = int(input())
d= {}

for _ in range(n):
    category, item_name, meashures = input().split(' - ')
    m = meashures.replace('quantity:', '')
    m = m.replace ( 'quality:', '' )
    quantity, quality = m.split(';')
    dict_key =category+'@'+ item_name
    if dict_key not in d:
        d[dict_key] = [(int(quantity), int(quality))]

print(f'Count of items: {get_count(d)}')
print(f'Average quality: {(get_average(d, len(types))):.2f}')
for type in types:
    print ( f"{type} -> {', '.join ( get_list_items ( d, type ) )}" )
