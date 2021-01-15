country = input().split(', ')
capitals = input().split(', ')
print('\n'.join([str(f'{country[i]} -> {capitals[i]}')for i in range (len(country))]))