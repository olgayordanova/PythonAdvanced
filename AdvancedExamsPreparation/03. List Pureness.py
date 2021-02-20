def get_sum(l):
    sum_p =0
    for i in range (len(l)):
        sum_p+=i*l[i]
    return sum_p


def rotate(l, n):
    return l[-n:] + l[:-n]

# max(n, len(l))
def best_list_pureness (*args):
    n=args[-1]
    l = list(args[0])
    best_pureness = []
    for _ in range (0, n+1):
        best_pureness.append ( get_sum ( l ) )
        l=l[-1:] + l[:-1] #rotate(l, 1)
    result = f'Best pureness {max(best_pureness)} after {best_pureness.index(max(best_pureness))} rotations'
    return result



test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

