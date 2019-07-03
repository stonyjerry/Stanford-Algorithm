def merge_sort(data):
    if len(data) <= 1:
        return data
    index = len(data) // 2
    lst1 = data[:index]
    lst2 = data[index:]
    left = merge_sort(lst1)
    right = merge_sort(lst2)
    return merge(left, right)

def merge(lst1,lst2):
    list = []
    i = j =0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            list.append(lst1[i])
            i += 1
        else:
            global num
            num = num + len(lst1)-i
            list.append(lst2[j])
            j += 1
    if i == len(lst1):
        for h in lst2[j:]:
            list.append(h)
    elif j == len(lst2):
        for h in lst1[i:]:
            list.append(h)
    return list

##Data Processing
import numpy as np
file = np.loadtxt('/Users/jingweili/Documents/人工智能培训/斯坦福算法课/IntegerArray.txt')
num = 0
print(merge_sort(file))
print(num)
