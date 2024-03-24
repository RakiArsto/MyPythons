import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input("Nhập số lượng phần tử trong danh sách: "))
my_list = random.sample(range(1, 101), n)
print("Danh sách trước khi sắp xếp là:", my_list)
bubble_sort(my_list)
print("Danh sách sau khi sắp xếp bằng Bubble Sort là:", my_list)
