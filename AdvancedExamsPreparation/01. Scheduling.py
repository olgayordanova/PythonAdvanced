jobs = [int(x) for x in input().split(', ')]
index = int(input())
job = jobs[index]
sum_out=0
for j in range (0, job):
    sum_out += sum([el for el in jobs if el==j])
for i in range (0, index+1):
    if jobs[i] ==job:
        sum_out += jobs[i]
print ( sum_out )

# prioritetna opashka heep_sort
# from heapq import heappush, heappushpop, heapify

