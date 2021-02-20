from collections import deque

first_loot_box = deque([int(x) for x in input().split(' ')])
second_loot_box  = deque([int(x) for x in input().split(' ')])
collection =[]

while True:
    if not first_loot_box:
        print("First lootbox is empty")
        break
    first_item=first_loot_box.popleft()
    if len(second_loot_box)>0:
        second_item= second_loot_box.pop()
        if (first_item+second_item)%2==0:
            collection.append(first_item+second_item)
        else:
            first_loot_box.appendleft ( first_item )
            first_loot_box.append ( second_item )
    else:
        first_loot_box.appendleft ( first_item )
        print(f"Second lootbox is empty")
        break


collection_sum = sum(collection)
if collection_sum>=100:
    print(f"Your loot was epic! Value: {collection_sum}")
else:
    print(f"Your loot was poor... Value: {collection_sum}")

