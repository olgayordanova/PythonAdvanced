import re
pattern = r'(\d+,\d+)-(\d+,\d+)'
n = int(input())
intersections = []
lengths = []
for i in range(n):
    line = input()
    matches = re.findall(pattern, line)
    start1,end1 = map(int,  matches[0][0].split(','))
    start2,end2 = map(int, matches[0][1].split(','))
    set1 = set([el for el in range (start1,end1+1)])
    set2 = set([el for el in range ( start2, end2+1  )])
    intersection = (set1&set2)
    intersections.append(intersection)
    lengths.append(len(intersection))

long_intersection = max(lengths)
ind = lengths.index(long_intersection)

print(f'Longest intersection is {list(intersections[ind])} with length {lengths[ind]}')



