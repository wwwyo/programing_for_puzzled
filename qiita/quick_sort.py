from random import sample

def divided(lst, start, end):
    pivot = lst[end]
    # startを3個目のループで使いたいので最初に-1をする
    start -= 1
    done = False

    while not done:
        while not done:
            start += 1
            if start >= end:
                done = True
                break

            if lst[start] > pivot:
                lst[end] = lst[start]
                break
        while not done:
            end -= 1
            if start >= end:
                done = True
                break

            if lst[end] < pivot:
                lst[start] = lst[end]
                break

    lst[end] = pivot
    return end

def quickSort(lst, start, end):
    if start >= end:
        return lst

    pivot_idx = divided(lst, start, end)
    quickSort(lst, start, pivot_idx - 1)
    quickSort(lst, pivot_idx + 1, end)
    return lst



# ランダムな配列を作成
lst = sample(range(100), 15)
print(quickSort(lst, 0, len(lst)-1))
