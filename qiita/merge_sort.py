from random import sample

def mergeLst(left, right):
    merged_lst = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged_lst.append(left[l])
            l += 1
        else:
            merged_lst.append(right[r])
            r += 1
    if l < len(left):
        merged_lst += left[l:]
    elif r < len(right):
        merged_lst += right[r:]

    return merged_lst

def mergeSort(lst):
    if len(lst) <= 1: return lst
    if len(lst) == 2:
        if lst[0] >= lst[1]:
            lst = [lst[1], lst[0]]
        return lst

    middle = len(lst) //2
    left = mergeSort(lst[:middle])
    right = mergeSort(lst[middle:])
    return mergeLst(left, right)

# ランダムな配列を作成
lst = sample(range(100), k=16)
print(mergeSort(lst))