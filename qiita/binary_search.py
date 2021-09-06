array = [1,2,3,4,5,6,7,8,9]
target = 9

top = len(array) - 1
bottom = 0

while top >= bottom:
    middle = (top + bottom) // 2
    if array[middle] < target:
        bottom = middle + 1
    elif array[middle] > target:
        top = middle - 1
    elif array[middle] == target:
        print(f'{middle + 1}番目に発見！')
        break
else:
    print('存在しない')
