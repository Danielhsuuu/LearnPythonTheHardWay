def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
arr = [1] 
 
bubbleSort(arr)

for i in range(len(arr)):
    print("% d" % arr[i])

#best case complexity O(n)
#average case complexity O(n^2)
#worst case complexity O(n^2)
#space complexity O(1)