def bubbleSort(arr):
    n=len(arr)
    
    for i in range(n-1):

        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]

arr=[29, 39, 49, 95, 27, 36, 46, 50, 100, 25, 197, 120, 99, 156, 56, 195, 97]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])