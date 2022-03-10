def quick_sort(lst, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(lst)-1
    if left < right:
        position = partition(lst, left, right)
        quick_sort(lst, left, position - 1)
        quick_sort(lst, position + 1, right)


def partition(lst, left, right):
    pivot = lst[right]
    low = left - 1
    for i in range(left, right):
        if lst[i] <= pivot:
            low += 1
            swap(lst, i, low)
    swap(lst, right, low + 1)
    return low + 1


def swap(lst, i, low):
    temp = lst[i]
    lst[i] = lst[low]
    lst[low] = temp


lst = [8, 4, 23, 42, 16, 15]
quick_sort(lst)
for i in range(len(lst)):
    print( lst[i])
