import random


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


n = int(input("Nhập số lượng phần tử trong danh sách: "))
my_list = random.sample(range(1, 101), n)
print(f"Danh sách trước khi sắp xếp là: {my_list}")
selection_sort(my_list)
print(f"Danh sách sau khi sắp xếp là: {my_list}")
