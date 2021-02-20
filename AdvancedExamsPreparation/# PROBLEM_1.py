#for correction - 60/100 points

from collections import deque

def get_sucsses(output_firework):
    if output_firework['Palm Fireworks']>=3 and output_firework['Willow Fireworks']>=3 and output_firework['Crossette Fireworks']>=3 :
        return True
    return False


firework_effect = deque([int(x) for x in input().split(', ')])
explosive_power = deque([int(x) for x in input().split(', ')])

output_firework={'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}

while True:
    if not firework_effect:
        break
    first_item=firework_effect.popleft()
    if first_item <= 0:
        continue
    if  explosive_power:
        second_item= explosive_power.pop()
        if second_item <= 0:
            firework_effect.appendleft ( first_item )
            continue
        sum_all = first_item+second_item
        if sum_all%3==0 and sum_all%5!=0:
            output_firework['Palm Fireworks']+=1
        elif sum_all%3!=0 and sum_all%5==0:
            output_firework['Willow Fireworks']+=1
        elif sum_all%3==0 and sum_all%5==0:
            output_firework['Crossette Fireworks']+=1
        else:
            first_item-=1
            firework_effect.append(first_item)
            explosive_power.append (second_item)
    else:
        # if first_item:
        #     firework_effect.appendleft ( first_item )
        break


if get_sucsses(output_firework):
    print('Congrats! You made the perfect firework show!')
else:
    print('Sorry. You can’t make the perfect firework show.')

if firework_effect:
    print(f"Firework Effects left: {', '.join ( [str ( el ) for el in firework_effect])}")

if explosive_power:
    print ( f"Explosive Power left: {', '.join ( [str ( el ) for el in explosive_power] )}" )

for key, value in output_firework.items ():
    print(f"{key}: {value}")


