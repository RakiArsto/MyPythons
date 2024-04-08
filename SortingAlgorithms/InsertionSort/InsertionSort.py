import random


def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


n = int(input("Nhập số lượng phần tử trong danh sách: "))
my_list = random.sample(range(1, 101), n)
print(f"Danh sách trước khi sắp xếp là: {my_list}")
InsertionSort(my_list)
print(f"Danh sách sau khi sắp xếp bằng Insertion Sort là: {my_list}")
