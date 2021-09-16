import sys

def selection_sort(arr):
    for i in range(len(arr)):
	    minimum = i
	    for j in range(i+1, len(arr)):
		    if arr[minimum] > arr[j]:
			    minimum = j
	    arr[i], arr[minimum] = arr[minimum], arr[i]

A = [5,2,3,1]
B = [5,1,1,2,0,0]

selection_sort(A)
selection_sort(B)

print ("Sorted array A")
for i in range(len(A)):
	print("%d" %A[i]),

print ("Sorted array B")
for i in range(len(B)):
	print("%d" %B[i]),
#best case complexity O(n^2)
#average case complexity O(n^2)
#worst case complexity O(n^2)
#space complexity O(1)