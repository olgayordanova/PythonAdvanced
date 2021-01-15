clotes = [int(el) for el in input().split(' ')]
capacity = int(input())
count_racks = 0

while len(clotes)>0:
    sum_of_current_clotes = 0
    l= len(clotes)
    for i in range (l-1,-1,-1):
        if capacity >= sum_of_current_clotes+clotes[-1]:
            if i < len(clotes):
                sum_of_current_clotes += clotes.pop ()
    count_racks+=1

print(count_racks)

