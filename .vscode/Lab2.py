import time
arr = [23,56,81,67,14]
a = 67
l_it = 0
start = time.perf_counter()
for i in range(len(arr)):
    l_it += 1
    if arr[i] == a:
        print("Target:",a,"Position:",i,"Iterations:",l_it)
        break
end = time.perf_counter()
print("Linear search time:",(end - start) * 1000,"ms")

arrr = [14,23,56,67,81]
niz = 0
verx = len(arrr) - 1
b_it = 0
start = time.perf_counter()
while niz <= verx:
    mid = niz + (verx - niz)//2
    if arrr[mid] > a:
        b_it += 1
        verx = mid - 1
    elif arrr[mid] < a:
        b_it += 1
        niz = mid + 1
    elif arrr[mid] == a:
        b_it += 1
        print("Target:",a,"Position:",mid,"Iterations:",b_it)
        break
end = time.perf_counter()
print("Binary search time:",(end - start) * 1000,"ms")

if l_it == b_it:
    print("Linear and Binary search are equal")
elif l_it > b_it:
    print("Binary search is faster than Linear by",l_it - b_it,"iterations")
elif l_it < b_it:
    print("Lineary search is faster than Binary by",b_it - l_it,"iterations")