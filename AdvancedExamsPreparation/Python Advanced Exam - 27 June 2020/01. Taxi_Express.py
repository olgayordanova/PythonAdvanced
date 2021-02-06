from collections import deque

customers_time = deque([int(x) for x in input().split(', ')])
taxi_drivers_time = deque([int(x) for x in input().split(', ')])
total_time =0

while customers_time:
    customer=customers_time.popleft()
    if len(taxi_drivers_time)>0:
        driver= taxi_drivers_time.pop()
        if driver<customer:
            customers_time.appendleft(customer)
        else:
            total_time+=customer
    else:
        customers_time.appendleft ( customer )
        break

if len(customers_time)==0:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el) for el in customers_time])}")
