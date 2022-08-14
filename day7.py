# merge sort
def sort(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    return res


def divide(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        arr1 = divide(arr[0: mid])
        arr2 = divide(arr[mid:])
        return sort(arr1, arr2)

print(divide([1, 9, 25, 4, 3]))

#insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        while arr[i - 1] > arr[i] and i > 0:
            arr[i],arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

arr = [1, -25, 5, 4]
print(insertion_sort(arr))

#bubble sort 1
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


print(bubble_sort([1, 5, -5, 2]))

#bubble sort 2
def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            if not swapped:
                break
    return arr


print(bubble_sort([1, 5, -5, 2]))

#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
