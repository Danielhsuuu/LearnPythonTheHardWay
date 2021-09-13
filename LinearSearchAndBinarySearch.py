import time
def linear_search(arr, x):
    value_found_at = []
    for i in range(len(arr)):
        if arr[i] == x:
            value_found_at.append(i)
    return value_found_at

def duplicates(arr):
    list_of_duplicates = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                list_of_duplicates.append(j)
                break
    return list_of_duplicates

def binary_Search (arr, left, right, value):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return binary_Search(arr, left, mid - 1, value)
        else:
            return binary_Search(arr, mid + 1, right, value)
    else:
        return -1


arr = [1, 8, 3, 5, 8, 5, 0, 6, 2, 7]
print("Looking for 8: ")
start = time.time()
print("8 is at position", linear_search(arr, 8))
end = time.time()
print(end - start)
print("Looking for 3: ")
start = time.time()
print("3 is at position", linear_search(arr, 3))
end = time.time()
print(end - start)
print("Looking for 0: ")
print("0 is at position", linear_search(arr, 0))

print("Looking for 9: ")
print("9 is at position", linear_search(arr, 9))

start = time.time()
print(duplicates(arr))
end = time.time()
print(end - start)

arr.sort()
print(arr)

start = time.time()
print("looking for 1 in the list using binary:", binary_Search(arr, 0, len(arr)-1, 1))
end = time.time()
print(end - start)