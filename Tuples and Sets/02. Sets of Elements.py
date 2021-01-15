n,m = map(int, input().split(' '))
n_set=set()
m_set=set()

for _ in range (n):
    n_set.add(int(input()))
for _ in range (m):
    m_set.add ( int ( input () ) )

print('\n'.join(str(el) for el in (n_set&m_set)))