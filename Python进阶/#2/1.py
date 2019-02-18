list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 3, 1, 5, 5, 3, 1]
list3 = [23, 456, 134, 45]

max_num = list1[0]
for i in list1:
    if max_num < i:
        max_num = i
print(max_num)


max_num = list2[0]
for i in list2:
    if max_num < i:
        max_num = i
print(max_num)

max_num = list3[0]
for i in list3:
    if max_num < i:
        max_num = i
print(max_num)
