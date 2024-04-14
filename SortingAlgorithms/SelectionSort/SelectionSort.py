import random


def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


n = int(input("Enter the number of elements in the list: "))
my_list = random.sample(range(1, 101), n)
print(f"The list before sorting is: \n{my_list}")
SelectionSort(my_list)
print(f"The list after sorting using Selection Sort is: \n{my_list}")
