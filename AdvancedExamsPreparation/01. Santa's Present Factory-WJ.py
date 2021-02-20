from collections import deque

def getKey(dct, value):
    for key in dct.keys ():
        if value == dct[key]:
            return ( key )

def sucsses(dict):
    if dict['Doll'] >0 and dict['Wooden train']>0:
        return True
    if dict['Teddy bear'] >0 and dict['Bicycle']>0:
        return True
    return False


materials = deque([int(x) for x in input().split(' ')])
magic_levels = deque([int(x) for x in input().split(' ')])

maked_toys = {'Doll': 0, 'Wooden train': 0,'Teddy bear': 0, 'Bicycle': 0}
point_needs = {'Doll': 150, 'Wooden train': 200,'Teddy bear': 300, 'Bicycle': 400}

while materials:
    material = materials.pop()
    if magic_levels:
        magic_level = magic_levels.popleft()
        value = material * magic_level
        if material == 0 and magic_level!=0:
            magic_levels.appendleft(magic_level)
            continue
        elif magic_level==0 and material != 0:
            materials.append(material)
            continue
        elif material == 0 and magic_level==0:
            continue

        if value in point_needs.values():
            key = getKey(point_needs, value)
            maked_toys[key] +=1
        else:
            if value<0:
                value = material + magic_level
                materials.append(value)
            else:
                materials.append(material+15)
    else:
        materials.append ( material )
        break

print(materials)

if sucsses(maked_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if len(materials)>0:
    print(f"Materials left: {', '.join ( [str ( el ) for el in materials])}")

if len(magic_levels)>0:
    print(f"Magic left: {', '.join ( [str ( el ) for el in magic_levels])}")

for toys, count in sorted(maked_toys.items()):
    if count>0:
        print(f"{toys}: {count}")







