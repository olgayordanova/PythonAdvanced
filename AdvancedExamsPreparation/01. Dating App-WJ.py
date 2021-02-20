from collections import deque

males = deque([int(x) for x in input().split(' ')])
females = deque([int(x) for x in input().split(' ')])
matches = 0

while females:
    female=females.popleft()
    if female <= 0:
        continue
    elif female%25 == 0:
        if females:
            female = females.popleft ()
        continue

    if len ( males ) == 0:
        females.appendleft ( female )

    if len(males)>0:
        male= males.pop()
        if male <= 0:
            females.appendleft(female)
            continue
        elif male % 25 == 0:
            if males:
                male = males.pop()
                females.appendleft ( female )
                continue
        if female!= male:
            male = male-2
            males.append(male)
        else:
            matches+=1
    else:
        break

print(f'Matches: {matches}')
if males:
    print(f"Males left: {', '.join ( [str ( el ) for el in males])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join ( [str ( el ) for el in females])}")
else:
    print("Females left: none")