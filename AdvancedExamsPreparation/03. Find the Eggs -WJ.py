def get_stronger(sublist):
    stronger_egg = -99999999
    k=len(sublist)//2
    midlle_egg = sublist[k]
    for i in range(k-1, -1, -1):
        if midlle_egg > sublist[i] and midlle_egg > sublist[k+i+1]:
            stronger_egg = midlle_egg
    return stronger_egg


def find_strongest_eggs (powers, count_lst):
    output_l =[]
    for j in range (count_lst):
        sublist = []
        for b in range(j, len(powers), count_lst):
            sublist.append(powers[b])
        stronger_egg = get_stronger (sublist)
        if stronger_egg!=-99999999:
            output_l.append ( stronger_egg )
    return output_l





test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
