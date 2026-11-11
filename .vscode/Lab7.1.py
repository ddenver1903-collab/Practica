"""class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self,value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[idx]
                idx = parent_idx
            else:
                break
    def peek(self):
        return self.heap[0]
    def is_empty(self):
        return len(self.heap) == 0
min_heap = MinHeap()
numbers = [50,30,70,20,40,60,80,10,15,67]
for num in numbers:
    min_heap.insert(num)
print("Heap:",min_heap.heap)
print("Smallest number:",min_heap.peek())
print("Empty?:",min_heap.is_empty())"""
"""class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self,value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent_idx]:
                self.heap[idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[idx]
                idx = parent_idx
            else:
                break
    def peek(self):
        return self.heap[0]
    def is_empty(self):
        return len(self.heap) == 0
max_heap = MaxHeap()
numbers = [50,-30,70,20,-40,60,-80,10,15,67]
for num in numbers:
    max_heap.insert(num)
print("Heap:",max_heap.heap)
print("Biggest number:",max_heap.peek())
print("Empty?:",max_heap.is_empty())"""
"""class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self,value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        self.heapify_up(idx)
    def heapify_up(self,idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[idx]
                idx = parent_idx
            else:
                break
min_heap = MinHeap()
numbers = [40,25,30,10,15,5]
for num in numbers:
    min_heap.insert(num)
    print(min_heap.heap)"""
"""class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self,value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[idx]
                idx = parent_idx
            else:
                break
    def heapify_down(self,idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx],self.heap[smallest] = self.heap[smallest],self.heap[idx]
    def replace(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
min_heap = MinHeap()
numbers = [5,15,10,40,25,67]
for num in numbers:
    min_heap.insert(num)
print("Before:",min_heap.heap)
min_heap.replace()
print("After:",min_heap.heap)"""
"""class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self,value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[idx]
                idx = parent_idx
            else:
                break
    def heapify_down(self,idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx],self.heap[smallest] = self.heap[smallest],self.heap[idx]
    def is_empty(self):
        return len(self.heap) == 0
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        smallest = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 0:
            self.heapify_down(0)
        return smallest
min_heap = MinHeap()
numbers = [5,15,10,40,25,67]
for num in numbers:
    min_heap.insert(num)
print(min_heap.heap)
while not min_heap.is_empty():
    print("Removed:",min_heap.extract_min())
    print(min_heap.heap)"""
"""class MinHeap:
    def __init__(self):
        self.heap = []
    def heapify_down(self,idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx],self.heap[smallest] = self.heap[smallest],self.heap[idx]
            self.heapify_down(smallest)
    def built_heap(self,arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1,-1,-1):
            self.heapify_down(i)
min_heap = MinHeap()
arr = [60,5,15,30,80,10,40,25,67,35,50,90,65,45,85]
min_heap.built_heap(arr)
print(min_heap.heap)"""
"""class MaxHeap:
    def __init__(self):
        self.heap = []
    def peek(self):
        return self.heap[0]
    def heapify_down(self,idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            self.heap[idx],self.heap[largest] = self.heap[largest],self.heap[idx]
            self.heapify_down(largest)
    def built_heap(self,arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1,-1,-1):
            self.heapify_down(i)
max_heap = MaxHeap()
arr = [5,25,10,30,35,15,40,60,67,80,50,90,65,45,85]
max_heap.built_heap(arr)
print(max_heap.heap)
print("Biggest number:",max_heap.peek())"""
"""class MaxHeap:
    def __init__(self):
        self.heap = []
    def heapify_down(self,n,idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            self.heap[idx],self.heap[largest] = self.heap[largest],self.heap[idx]
            self.heapify_down(n,largest)
    def built_heap(self,arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1,-1,-1):
            self.heapify_down(n,i)
        for i in range(n - 1,0,-1):
            self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
            self.heapify_down(i,0)
        return arr
max_heap = MaxHeap()
arr1 = [40,10,30,50,20]
arr2 = [10,20,30,40,50]
arr3 = [50,40,30,20,10]
arr4 = [30,10,30,20,10,40]
print("Unsorted:",max_heap.built_heap(arr1))
print("Sorted:",max_heap.built_heap(arr2))
print("Reverse sorted:",max_heap.built_heap(arr3))
print("Duplicates:",max_heap.built_heap(arr4))"""
"""class MaxHeap:
    def __init__(self):
        self.heap = []
    def peek(self):
        return self.heap[0]
    def heapify_down(self,idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            self.heap[idx],self.heap[largest] = self.heap[largest],self.heap[idx]
            self.heapify_down(largest)
    def built_heap(self,arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1,-1,-1):
            self.heapify_down(i)
    def replace(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
max_heap = MaxHeap()
arr = [5,25,10,30,35,15,40,60,67,80,50,90,65,45,85]
max_heap.built_heap(arr)
print(max_heap.heap)
k = 3
for i in range(k):
    print(max_heap.peek())
    max_heap.replace()"""
"""class MinHeap:
    def __init__(self):
        self.heap = []
    def peek(self):
        return self.heap[0]
    def heapify_down(self,idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx],self.heap[smallest] = self.heap[smallest],self.heap[idx]
            self.heapify_down(smallest)
    def built_heap(self,arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1,-1,-1):
            self.heapify_down(i)
    def replace(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
min_heap = MinHeap()
arr = [60,5,15,30,80,10,40,25,67,35,50,90,65,45,85]
min_heap.built_heap(arr)
print(min_heap.heap)
k = 3
for i in range(k):
    print(min_heap.peek())
    min_heap.replace()"""
"""class MedianFinder: 
    def __init__(self): 
        self.lower = []
        self.upper = [] 
    def heapify_up_max(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.lower[idx] > self.lower[parent_idx]:
                self.lower[idx], self.lower[parent_idx] = self.lower[parent_idx], self.lower[idx]
                idx = parent_idx
            else:
                break
    def heapify_up_min(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.upper[idx] < self.upper[parent_idx]:
                self.upper[idx], self.upper[parent_idx] = self.upper[parent_idx], self.upper[idx]
                idx = parent_idx
            else:
                break
    def insert(self, value):
        if not self.lower or value <= self.lower[0]:
            self.lower.append(value)
            self.heapify_up_max(len(self.lower) - 1)
        else:
            self.upper.append(value)
            self.heapify_up_min(len(self.upper) - 1)
        if len(self.lower) > len(self.upper) + 1:
            num = self.lower[0]
            self.lower[0] = self.lower[-1]
            self.lower.pop()
            self.heapify_down_max(0)
            self.upper.append(num)
            self.heapify_up_min(len(self.upper) - 1)
        elif len(self.upper) > len(self.lower):
            num = self.upper[0]
            self.upper[0] = self.upper[-1]
            self.upper.pop()
            self.heapify_down_min(0)
            self.lower.append(num)
            self.heapify_up_max(len(self.lower) - 1)
    def heapify_down_max(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.lower) and self.lower[left] > self.lower[largest]:
            largest = left
        if right < len(self.lower) and self.lower[right] > self.lower[largest]:
            largest = right
        if largest != idx:
            self.lower[idx], self.lower[largest] = self.lower[largest], self.lower[idx]
            self.heapify_down_max(largest)
    def heapify_down_min(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.upper) and self.upper[left] < self.upper[smallest]:
            smallest = left
        if right < len(self.upper) and self.upper[right] < self.upper[smallest]:
            smallest = right
        if smallest != idx:
            self.upper[idx], self.upper[smallest] = self.upper[smallest], self.upper[idx]
            self.heapify_down_min(smallest)
    def find_median(self):
        if len(self.lower) > len(self.upper):
            return self.lower[0]
        return (self.lower[0] + self.upper[0]) / 2
median_finder = MedianFinder()
numbers = [5, 2, 10, 4, 8, 1]
for num in numbers: 
    median_finder.insert(num) 
    print("Inserted:",num,"Median:",median_finder.find_median())"""
"""class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self,value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[idx]
                idx = parent_idx
            else:
                break
    def heapify_down(self,idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx],self.heap[smallest] = self.heap[smallest],self.heap[idx]
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        smallest = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 0:
            self.heapify_down(0)
        return smallest
class MergeArrays:
    def __init__(self):
        self.min_heap = MinHeap()
    def merge(self, arrays):
        result = []
        for i in range(len(arrays)):
            if len(arrays[i]) > 0:
                self.min_heap.insert((arrays[i][0], i, 0))
        while self.min_heap.heap:
            value, array_idx, element_idx = self.min_heap.extract_min()
            result.append(value)
            next_idx = element_idx + 1
            if next_idx < len(arrays[array_idx]):
                next_value = arrays[array_idx][next_idx]
                self.min_heap.insert((next_value, array_idx, next_idx))
        return result
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
merger = MergeArrays()
print("Merged array:", merger.merge(arrays))"""
"""class MinHeap:
    def __init__(self,arr):
        self.heap = arr
    def is_min_heap(self):
        n = len(self.heap)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self.heap[i] > self.heap[left]:
                return False
            if right < n and self.heap[i] > self.heap[right]:
                return False
        return True
arrays = [
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    [1, 2, 3, 4, 5, 6],
    [5, 5, 6, 7, 8],
    [1, 1, 1, 1, 1],
    [10, 5, 15, 20],
    [1, 5, 2, 3, 4],
    [3, 2, 5, 7, 8],
    [1, 2, 0, 4, 5],
    [5, 6, 3, 8, 9]
]
for arr in arrays:
    min_heap = MinHeap(arr)
    print(arr,"is",min_heap.is_min_heap())"""
"""class MaxHeap:
    def __init__(self):
        self.heap = []
    def peek(self):
        return self.heap[0]
    def heapify_down(self,idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            self.heap[idx],self.heap[largest] = self.heap[largest],self.heap[idx]
            self.heapify_down(largest)
    def built_heap(self,arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1,-1,-1):
            self.heapify_down(i)
    def replace(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
max_heap = MaxHeap()
arr = [5,25,10,30,35,15,40,60,67,80,50,90,65,45,85]
max_heap.built_heap(arr)
k = 3
for i in range(k - 1):
    max_heap.replace()
print(max_heap.peek())"""
"""class Hospital:
    def __init__(self):
        self.heap = []
    def heapify_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx][1] > self.heap[parent_idx][1]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break
    def heapify_down(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left][1] > self.heap[largest][1]:
            largest = left
        if right < len(self.heap) and self.heap[right][1] > self.heap[largest][1]:
            largest = right
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self.heapify_down(largest)
    def add_patient(self, patient_id, urgency):
        self.heap.append((patient_id, urgency))
        self.heapify_up(len(self.heap) - 1)
    def peek_patient(self):
        if not self.heap:
            return None
        return self.heap[0]
    def treat_patient(self):
        if not self.heap:
            return None
        patient = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self.heapify_down(0)
        return patient
    def display(self):
        print("Patient queue:")
        for patient in self.heap:
            print("Patient id:",patient[0],"Urgency:",patient[1])
hospital = Hospital()
patients = [
    (101, 5),
    (102, 8),
    (103, 3),
    (104, 10),
    (105, 7),
    (106, 8),
    (107, 2),
    (108, 9),
    (109, 5),
    (110, 10)
]
for patient_id, urgency in patients:
    hospital.add_patient(patient_id, urgency)
hospital.display()
print("Next patient:",hospital.peek_patient())
print("Treating patient:",hospital.treat_patient())
print("After treatment:")
hospital.display()"""
"""class minh():
    def __init__(self):
        self.heap = []
    def insert(self,value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx],self.heap[parent] = self.heap[parent],self.heap[parent]
                idx = parent
            else:
                break
    def h_down(self,idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx],self.heap[smallest] = self.heap[smallest],self.heap[idx]
            self.h_down(smallest)
    def replace(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.h_down(0)
    def h_up(self,idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx],self.heap[parent] = self.heap[parent],self.heap[parent]
                idx = parent
            else:
                break
    def extract(self):
        smallest = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 0:
            self.h_down(0)
        return smallest  
    def empty(self):
        return len(self.heap) == 0
    def peek(self):
        return self.heap[0]
    def built(self,arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1,-1,-1):
            self.h_down(i)"""








class min_heap():
    def __init__(self):
        self.heap = []
    def h_down(self,idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx +2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[smallest],self.heap[idx] = self.heap[idx],self.heap[smallest]
            self.h_down(smallest)
    def peek(self):
        return self.heap[0]
    def built(self,arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1,-1,-1):
            self.h_down(i)
    def replace(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.h_down(0)
minh = min_heap()
arr = [5,4,8,9,2,3,7]
minh.built(arr)
k = 3
for i in range(k):
    print(minh.peek())
    minh.replace()
    