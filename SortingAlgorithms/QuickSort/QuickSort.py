import random


def Partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def QuickSort(arr, left, right):
    if left < right:
        pi = Partition(arr, left, right)
        QuickSort(arr, left, pi - 1)
        QuickSort(arr, pi + 1, right)


n = int(input("Nhập số lượng phần tử trong danh sách: "))
my_list = random.sample(range(1, 101), n)
print(f"Danh sách trước khi sắp xếp là: {my_list}")
QuickSort(my_list, 0, len(my_list) - 1)
print(f"Danh sách sau khi sắp xếp bằng Quick Sort là: {my_list}")
