import random


def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input("Enter the number of elements in the list: "))
my_list = random.sample(range(1, 101), n)
print(f"The list before sorting is: \n{my_list}")
BubbleSort(my_list)
print(f"The list after sorting using Bubble Sort is: \n{my_list}")
