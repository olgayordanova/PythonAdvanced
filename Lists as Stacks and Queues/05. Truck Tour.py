from collections import deque
count_station = int(input())
pumps = deque()

for _ in range (count_station):
    amount, distance = map(int,input().split(' '))
    pumps.append([amount,distance])

for i in range (count_station):
    is_valid = True
    total_fuel = 0

    for _ in range(count_station):
        current = pumps.popleft ()
        total_fuel += current[0]-current[1]

        if total_fuel<0:
            is_valid = False
        pumps.append ( current )

    if is_valid:
        print(i)
        break
    pumps.append ( pumps.popleft() )
