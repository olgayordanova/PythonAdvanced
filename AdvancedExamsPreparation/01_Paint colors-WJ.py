from collections import deque

def insert_element(el, words):
    n= len(words)//2
    words.insert(n, el)
    return words


def is_all_main_colors (color_collection, color):
    d = {'orange': ('red', 'yellow'),
         'purple': ('red', 'blue'),
         'green': ('yellow', 'blue')
         }
    c1,c2 =  d[color]
    if c1 in color_collection and c2 in color_collection:
        return True
    return False


def get_colors(color_collection, secondary_colors):
    for color in color_collection:
        if color in secondary_colors:
            if is_all_main_colors (color_collection,color):
                continue
            else:
                del color_collection[color_collection.index(color)]
    return color_collection


words = deque(input().split())
main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}

color_collection=[]
n=len(words)
while words:
    first = words.popleft()
    if words:
        second = words.pop ()
    else:
        second=''
    if first == '' and second =='':
        break
    if first+second in main_colors.union(secondary_colors):
        color_collection.append(first+second)
    elif second+first in main_colors.union(secondary_colors):
        color_collection.append ( second+first )
    else:
        new_word_1 = first[0:-1]
        new_word_2 = second[0:-1]
        words = insert_element(new_word_1+new_word_2, words)

color_collection = get_colors(color_collection, secondary_colors)
print (color_collection)