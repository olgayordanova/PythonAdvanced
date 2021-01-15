line = [int(el)  for el in input().split(', ')]
print(f'Positive: {", ".join([str(el) for el in line if el>=0])}')
print(f'Negative: {", ".join([str(el) for el in line if el<0])}')
print(f'Even: {", ".join([str(el) for el in line if el%2==0])}')
print(f'Odd: {", ".join([str(el) for el in line if el%2!=0])}')