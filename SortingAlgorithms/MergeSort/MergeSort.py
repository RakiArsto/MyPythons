import random


def Merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result


def MergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = MergeSort(left_half)
    right_half = MergeSort(right_half)

    return Merge(left_half, right_half)
    
    
n = int(input("Enter the number of elements in the list: "))
my_list = random.sample(range(1, 101), n)
print(f"The list before sorting is: \n{my_list}")
SortedList = MergeSort(my_list)
print(f"The list after sorting using Merge Sort is: \n{SortedList}")
