from collections import deque

green_time = int(input())
window_time = int(input())
crashed = False

line = input()

cars = deque()
counter = 0

while line != "END":
    if line == "green":
        green_timer = green_time
        if cars:
            copy = cars.popleft()
            current_car = deque(copy)
            while green_timer:
                if not current_car:
                    if cars:
                        copy = cars.popleft()
                        current_car = deque(copy)
                    else:
                        break
                current_car.popleft()
                green_timer -= 1

            if current_car:
                window_timer = window_time
                while window_timer and current_car:
                    current_car.popleft()
                    window_timer -= 1

            if current_car:
                crashed = True
                print("A crash happened!")
                print(f"{copy} was hit at {current_car.popleft()}.")
                break

    else:
        cars.append(line)
        counter += 1

    line = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{counter - len(cars)} total cars passed the crossroads.")