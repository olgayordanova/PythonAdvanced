from collections import deque

def get_sucsses(output_foods):
    if output_foods['Bread']>=1 and output_foods['Cake']>=1 and output_foods['Pastry']>=1 and output_foods['Fruit Pie']>=1:
        return True
    return False

def get_key(dct, value):
    for key in dct.keys ():
        if value == dct[key]:
            return ( key )


liquids = deque([int(x) for x in input().split(' ')])
ingredients = deque([int(x) for x in input().split(' ')])

foods = {'Bread':25, 'Cake': 50, 'Pastry': 75, 'Fruit Pie': 100}
output_foods={'Bread':0, 'Cake': 0, 'Pastry': 0, 'Fruit Pie': 0}
while True:
    if not liquids:
        break
    first_item=liquids.popleft()
    if len(ingredients)>0:
        second_item= ingredients.pop()
        if (first_item+second_item) in foods.values():
            key= get_key(foods, first_item+second_item )
            output_foods[key]+=1
        else:
            ingredients.append ( second_item+3 )

sucsses = get_sucsses(output_foods)
if sucsses:
    print("Wohoo! You succeeded in cooking all the food!" )
else:
    print("Ugh, what a pity! You didn't have enough materials to cook everything.")

if len(liquids)==0:
    print( "Liquids left: none" )
else:
    print(f"Liquids left: {', '.join([str(el) for el in liquids])}")

if len(ingredients)==0:
    print( "Ingredients left: none" )
else:
    print(f"Ingredients left: {', '.join([str(el) for el in ingredients])}")

for key, value in sorted ( output_foods.items () ):
    print(f"{key}: {value}")


