n = int(input())
elements = set()

for _ in range (n):
    elements.update(input().split(' '))
print('\n'.join(elements))