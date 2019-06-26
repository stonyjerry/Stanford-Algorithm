### divide & conquer strategy

### Here is the conquer part:
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    elif h==len(b):
        for i in a[j:]:
            c.append(i)

    return c

### Here is the divide part
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = int(len(lists)/2)
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

### Testing
a = [4, 2, 8, 10, 5, 9]
print(merge_sort(a))
