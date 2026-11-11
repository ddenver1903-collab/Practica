"""table_size = 10
hash_table = [None] * table_size
def my_hash(key):
    return key % table_size
keys = [41,37,89,17,52,67,29,33,101,63]
for key in keys:
    index = my_hash(key)
    hash_table[index] = key
    print("Index:",index,"Key:",key)"""
"""table_size = 10
hash_table = [None] * table_size
def my_hash(key):
    total = 0
    for char in key:
        total += ord(char)
    return total % table_size
keys = ["word","task","cow","cat","dog","hope","job","key","hash","snake"]
for key in keys:
    index = my_hash(key)
    print("Index:",index,"Word:",key)"""
"""class hash_table:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    def my_hash(self,key):
        return key % self.size
    def insert(self,key,value):
        index = self.my_hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key,value])
    def search(self,key):
        index = self.my_hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
    def delete(self,key):
        index = self.my_hash(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return
    def display(self):
        for i in range(self.size):
            print(i,":",self.table[i])
ht = hash_table()
ht.insert(67,"Snake")
ht.insert(51,"Apple")
ht.insert(15,"Table")
ht.insert(25,"Cat")
ht.display()
print("51:",ht.search(51))
ht.delete(51)
ht.display()"""
"""text = "cat dog cat word word cat dog dog"
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word,count in word_count.items():
    print(word,":",count)"""
"""arr = [6,4,3,2,1,1,9,4]
hash_table = {}
for numb in arr:
    if numb in hash_table:
        hash_table[numb] += 1
    else:
        hash_table[numb] = 1
for numb in hash_table:
    if hash_table[numb] > 1:
        print(numb)"""
"""class hash_table:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    def my_hash(self,key):
        return key % self.size
    def insert(self,key):
        index = self.my_hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)
    def search(self,key):
        index = self.my_hash(key)
        if key in self.table[index]:
            return True
        return False
    def delete(self,key):
        index = self.my_hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)
    def display(self):
        for i in range(self.size):
            print(i,":",self.table[i])
ht = hash_table()
keys = [41,37,89,17,52,67,29,33,101,63]
for key in keys:
    ht.insert(key)
ht.display()
print("52",ht.search(52))
ht.delete(52)
ht.display()"""
"""class hash_table:
    def __init__(self):
        self.size = 11
        self.table = [None] * self.size
    def my_hash(self,key):
        return key % self.size
    def insert(self,key):
        index = self.my_hash(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key
    def search(self,key):
        index = self.my_hash(key)
        start = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
            if index == start:
                break
        return False
    def display(self):
        for i in range(self.size):
            print(i,":",self.table[i])
ht = hash_table()
keys = [41,37,89,17,52,67,29,33,101,63,11]
for key in keys:
    ht.insert(key)
ht.display()
print("11",ht.search(11))"""
"""class hash_table:
    def __init__(self):
        self.size = 13
        self.quadratic = [None] * self.size
        self.linear = [None] * self.size
    def my_hash(self, key):
        return key % self.size
    def insert_quadratic(self, key):
        index = self.my_hash(key)
        i = 0
        probes = 0
        while i < self.size:
            new_index = (index + i ** 2) % self.size
            probes += 1
            if self.quadratic[new_index] is None:
                self.quadratic[new_index] = key
                print(key, "Probes:", probes)
                return
            i += 1
    def insert_linear(self, key):
        index = self.my_hash(key)
        probes = 0
        while self.linear[index] is not None:
            index = (index + 1) % self.size
            probes += 1
        self.linear[index] = key
        probes += 1
        print(key, "Probes:", probes)
    def display(self, table):
        for i in range(self.size):
            print(i, ":", table[i])
ht = hash_table()
keys = [41,37,89,17,52,67,29,33,101,63,11,30,55]
print("Quadratic Probing:")
for key in keys:
    ht.insert_quadratic(key)
print("Quadratic Hash Table:")
ht.display(ht.quadratic)
print("Linear Probing:")
for key in keys:
    ht.insert_linear(key)
print("Linear Hash Table:")
ht.display(ht.linear)"""
"""class hash_table:
    def __init__(self):
        self.size = 11
        self.table = [None] * self.size
        self.collisions = 0
    def hash1(self, key):
        return key % self.size
    def hash2(self, key):
        return 1 + (key % (self.size - 1))
    def insert(self, key):
        index1 = self.hash1(key)
        index2 = self.hash2(key)
        i = 0
        while i < self.size:
            index = (index1 + i * index2) % self.size
            if self.table[index] is None:
                self.table[index] = key
                return
            self.collisions += 1
            i += 1
    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])
ht = hash_table()
keys = [41,37,89,17,52,67,29,33,101,63,11]
for key in keys:
    ht.insert(key)
ht.display()
print("Total collisions:", ht.collisions)"""
"""class hash_table:
    def __init__(self):
        self.size = 11
    def hash1(self, key):
        return key % self.size
    def hash2(self, key):
        return 1 + (key % (self.size - 1))
    def insert(self, keys, method):
        table = [None] * self.size
        collisions = 0
        probes = 0
        for key in keys:
            index = self.hash1(key)
            step = self.hash2(key)
            i = 0
            while i < self.size:
                if method == "Linear":
                    new_index = (index + i) % self.size
                elif method == "Quadratic":
                    new_index = (index + i ** 2) % self.size
                else:
                    new_index = (index + i * step) % self.size
                probes += 1
                if table[new_index] is None:
                    table[new_index] = key
                    break
                collisions += 1
                i += 1
        print(method)
        print("Table:", table)
        print("Collisions:", collisions)
        print("Probes:", probes)
keys = [41,37,89,17,52,67,29,33,101,63,11]
ht = hash_table()
ht.insert(keys, "Linear")
ht.insert(keys, "Quadratic")
ht.insert(keys, "Double")"""
"""def two_sum(arr,target):
    hash_table = {}
    for i in range(len(arr)):
        num = arr[i]
        targ = target - num
        if targ in hash_table:
            return hash_table[targ],i
        hash_table[num] = i
    return None
arr = [11,15,2,7]
target = 9
result = two_sum(arr,target)
print("Indexes:",result[0],",",result[1])"""
text = "swiss"
words = text.split()
word_count = {}
"""def first(text):
    hash_table = {}
    for ch in text: 
        if ch in hash_table:
            hash_table[ch] += 1
        else:
            hash_table[ch] = 1
    for ch in text:
        if hash_table[ch] == 1:
            return ch
    return None
print(first(text))"""
"""def anagrams(words):
    hash_table = {}
    for word in words:
        key = "".join(sorted(word))
        if key in hash_table:
            hash_table[key].append(word)
        else:
            hash_table[key] = [word]
    for group in hash_table.values():
        print(group)
words = ["eat","tea","win","hop","tab","bat"]
anagrams(words)"""
"""def common(A, B):
    hash_table = {}
    for numb in A:
        hash_table[numb] = True
    result = []
    for numb in B:
        if numb in hash_table:
            if numb not in result:
                result.append(numb)
    return result
A = [1, 2, 3, 4, 5, 6]
B = [4, 5, 6, 7, 8]
print(common(A, B))"""
"""def longest_s(arr):
    hash_set = set(arr)
    longest = 0
    best_sequence = []
    for numb in hash_set:
        if numb - 1 not in hash_set:
            current = numb
            sequence = []
            while current in hash_set:
                sequence.append(current)
                current += 1
            if len(sequence) > longest:
                longest = len(sequence)
                best_sequence = sequence
    print("Length:", longest)
    print("Sequence:", best_sequence)
arr = [100,4,200,1,3,2,5]
longest_s(arr)"""
"""def sum(arr):
    hash_set = set()
    prefix_sum = 0
    for numb in arr:
        prefix_sum += numb
        if prefix_sum == 0:
            return True
        if prefix_sum in hash_set:
            return True
        hash_set.add(prefix_sum)
    return False
arr = [4, 2, -3, 1, 6]
print(sum(arr))"""
"""def longest_s(text):
    hash_table = {}
    start = 0
    longest = 0
    best_substring = ""
    for i in range(len(text)):
        char = text[i]
        if char in hash_table and hash_table[char] >= start:
            start = hash_table[char] + 1
        hash_table[char] = i
        if i - start + 1 > longest:
            longest = i - start + 1
            best_substring = text[start:i + 1]
    print("Length:", longest)
    print("Substring:", best_substring)
text = "abcabcbb"
longest_s(text)"""
"""class student_database:
    def __init__(self):
        self.students = {}
    def add_student(self,student_id,name,group,gpa):
        if student_id in self.students:
            print("Student ID already exists")
            return
        self.students[student_id] = {
            "name": name,
            "group": group,
            "gpa": gpa
        }
        print("Student added")
    def search_student(self,student_id):
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print("Student not found")
    def update_gpa(self,student_id,gpa):
        if student_id in self.students:
            self.students[student_id]["gpa"] = gpa
            print("GPA updated")
        else:
            print("Student not found")
    def delete_student(self,student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted")
    def display(self):
        for student_id, info in self.students.items():
            print(student_id,info)
db = student_database()
db.add_student(101,"Biba","101SE",3.5)
db.add_student(102,"Danik","102SE",3.8)
db.add_student(103,"Yelaman","103SE",3.2)
db.add_student(104,"Alan","104SE",4.0)
db.search_student(102)
db.update_gpa(101,3.9)
db.delete_student(103)
db.display()"""
"""def repeated(words):
    hash_table = {}
    for word in words:
        if word in hash_table:
            hash_table[word] += 1
        else:
            hash_table[word] = 1
    result = []
    for word, count in hash_table.items():
        if count > 1:
            result.append((word,count))
    result.sort(key=lambda x: (-x[1],x[0]))
    for word, count in result:
        print(word,":",count)
words = ["cat","dog","cat","bird","dog","cat"]
repeated(words)"""
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRU:
    def __init__(self,capacity):
        self.capacity = capacity
        self.hash_table = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def add_front(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def get(self,key):
        if key not in self.hash_table:
            return -1
        node = self.hash_table[key]
        self.remove(node)
        self.add_front(node)
        return node.value
    def put(self,key,value):
        if key in self.hash_table:
            node = self.hash_table[key]
            node.value = value
            self.remove(node)
            self.add_front(node)
        else:
            node = Node(key,value)
            self.hash_table[key] = node
            self.add_front(node)
        if len(self.hash_table) > self.capacity:
            old_node = self.tail.prev
            self.remove(old_node)
            del self.hash_table[old_node.key]
cache = LRU(2)
cache.put(1, 10)
cache.put(2, 20)
print(cache.get(1))
cache.put(3, 30)
print(cache.get(2))