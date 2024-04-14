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


n = int(input("Enter the number of elements in the list: "))
my_list = random.sample(range(1, 101), n)
print(f"The list before sorting is: \n{my_list}")
QuickSort(my_list, 0, len(my_list) - 1)
print(f"The list after sorting using Quick Sort is: \n{my_list}")
