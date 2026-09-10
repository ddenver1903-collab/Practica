arr = [35,4,18,58,67,23]
print("Array before sorting:",arr)
n = len(arr)
for i in range(n):
    for j in range(n - i - 1):
        if arr[j]>arr[j+1]:
            a = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = a
print("Array after sorting:",arr)