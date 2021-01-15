n = int(input())
odds = set()
evens = set()
for i in range (1,n+1):
    name = input()
    sum_ascii_number = sum ([ord(ch) for ch in name])//i
    if sum_ascii_number%2==0:
        evens.add(sum_ascii_number)
    else:
        odds.add(sum_ascii_number)

if sum(odds)==sum(evens):
    result_set = odds|evens
    print(', '.join([str(el) for el in result_set]))
elif sum(odds)>sum(evens):
    result_set = odds- evens
    print(', '.join([str(el) for el in result_set]))
elif sum(odds)<sum(evens):
    result_set = odds^evens
    print(', '.join([str(el) for el in result_set]))

