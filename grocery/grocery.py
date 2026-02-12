import numpy as np

grocery_list = []
while True:
    try:
        items = input().upper().strip()
        grocery_list.append(items)
    except EOFError:
        break
print()

item_counts = {}
for item in grocery_list:
   item_counts[item] = item_counts.get(item, 0) + 1


values, keys = np.unique(grocery_list, return_counts=True)
item_dict = {values[i]: keys[i] for i in range(len(values))}
for item in item_dict:
    print(item_dict[item], item)
