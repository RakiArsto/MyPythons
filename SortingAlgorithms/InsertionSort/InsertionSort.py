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


n = int(input("Enter the number of elements in the list: "))
my_list = random.sample(range(1, 101), n)
print(f"The list before sorting is: \n{my_list}")
InsertionSort(my_list)
print(f"The list after sorting using Insertion Sort is: \n{my_list}")
