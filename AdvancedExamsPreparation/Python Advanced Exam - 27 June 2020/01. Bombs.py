from collections import deque

def add_bomb_to_pouch(bombs, val,bomb_pouch):
    for key, value in bombs.items():
        if value == val:
            bomb_pouch[key] +=1
    return bomb_pouch

def bomb_pouch_is_full(bomb_pouch):
    if bomb_pouch['Datura Bombs']>=3 and bomb_pouch['Cherry Bombs']>=3 and bomb_pouch['Smoke Decoy Bombs']>=3:
        return True
    return False


def print_output(bomb_effects, bomb_casings, bomb_pouch, is_full):
    res_str = ""
    if is_full:
        res_str+= "Bene! You have successfully filled the bomb pouch!"+"\n"
    else:
        res_str+="You don't have enough materials to fill the bomb pouch."+"\n"

    if len(bomb_effects)==0:
        res_str+= ( "Bomb Effects: empty" )+"\n"
    else:
        res_str+=(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")+"\n"

    if len(bomb_casings)==0:
        res_str+= ( "Bomb Casings: empty" )+"\n"
    else:
        res_str+=(f"Bomb Casings: {', '.join([str(el) for el in bomb_casings])}")+"\n"

    for key,value in sorted(bomb_pouch.items()):
        res_str+= (f"{key}: {value}")+"\n"
    return res_str



bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]
bombs = {'Datura Bombs':40, 'Cherry Bombs': 60, 'Smoke Decoy Bombs': 120}
bomb_pouch ={"Datura Bombs":0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
is_full = False

while bomb_effects:
    current_bomb_effect = bomb_effects[0]
    if bomb_casings:
        current_bomb_casings = bomb_casings[-1]
        if current_bomb_casings+current_bomb_effect in bombs.values():
            bomb_pouch = add_bomb_to_pouch(bombs, current_bomb_casings+current_bomb_effect,bomb_pouch)
            bomb_effects.popleft()
            bomb_casings.pop()
            if bomb_pouch_is_full(bomb_pouch):
                is_full = True
                break
        else:
            bomb_casings[-1]-=5
    else:
        break

print(print_output(bomb_effects, bomb_casings, bomb_pouch, is_full))
