def merge_sort(lst):
    n = len(lst)

    if n > 1:
        mid = n//2
        left = lst[0:mid]
        right = lst[mid:n]
        # sort the left side
        merge_sort(left)
        #sort the right side
        merge_sort(right)
        # merge the sorted left and right sides together
        merge(left, right, lst)


def merge(left, right, lst):
    i = 0
    j = 0
    k = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        for i in range(k, len(lst)):
            lst[k] = right[j]
            j += 1
    else:
        for j in range(k, len(lst)):
            lst[k] = left[i]
            i += 1


lst = [8, 4, 23, 42, 16, 15]
merge_sort(lst)
for i in range(len(lst)):
    print( lst[i])
