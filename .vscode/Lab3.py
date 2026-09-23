#Task1
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    cursor = head
    while cursor:
        print(cursor.data)
        cursor = cursor.next
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
traverse(node1)"""
#Task2
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    cursor = head
    while cursor:
        print(cursor.data)
        cursor = cursor.next
def insertAtBeginning(head,value):
    new_node = Node(value)
    new_node.next = head
    return new_node
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node1.next = node2
node2.next = node3
print("Before:")
traverse(node1)
head = insertAtBeginning(node1,10)
print("After:")
traverse(head)"""
#Task3
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    cursor = head
    while cursor:
        print(cursor.data)
        cursor = cursor.next
def insertAtEnd(head,value):
    new_node = Node(value)
    cursor = head
    while cursor.next:
        cursor = cursor.next
    cursor.next = new_node
    return head
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
print("Before:")
traverse(node1)
insertAtEnd(node1,40)
print("After:")
traverse(node1)"""
#Task4
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def getLenght(head):
    len = 0
    cursor = head
    while cursor:
        len+=1
        cursor = cursor.next
    print("Lenght of the list:",len)
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
getLenght(node1)"""
#Task5
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def search(head,value):
    cursor = head
    while cursor:
        if cursor.data == value:
            print(value,"is Found")
            return
        cursor = cursor.next
    print(value,"is Not Found")
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
search(node1,30)
search(node1,50)"""
#Task6
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    cursor = head
    while cursor:
        print(cursor.data)
        cursor = cursor.next
def deleteFirst(head):
    return head.next
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
print("Before:")
traverse(node1)
node1 = deleteFirst(node1)
print("After:")
traverse(node1)"""
#Task7
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    cursor = head
    while cursor:
        print(cursor.data)
        cursor = cursor.next
def deletelast(head):
    cursor = head
    while cursor.next.next:
        cursor = cursor.next
    cursor.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
print("Before:")
traverse(node1)
deletelast(node1)
print("After:")
traverse(node1)"""
#Task8
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    cursor = head
    while cursor:
        print(cursor.data)
        cursor = cursor.next
def deleteValue(head,value):
    if head.data == value:
        return head.next
    cursor = head
    while cursor.next:
        if cursor.next.data == value:
            cursor.next = cursor.next.next
            return head
        cursor = cursor.next
    print("Element not found")
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
print("Before:")
traverse(node1)
node1 = deleteValue(node1,30)
print("After:")
traverse(node1)"""
#Task9
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def Maximum(head):
    max = head.data
    cursor = head.next
    while cursor:
        if max < cursor.data:
            max = cursor.data
        cursor = cursor.next
    print("Maximum =",max)
node1 = Node(10)
node2 = Node(20)
node3 = Node(50)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
Maximum(node1)"""       
#Task10
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def Minimum(head):
    min = head.data
    cursor = head.next
    while cursor:
        if min > cursor.data:
            min = cursor.data
        cursor = cursor.next
    print("Minimum =",min)
node1 = Node(10)
node2 = Node(20)
node3 = Node(0)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
Minimum(node1)"""
#Task11
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def EvenNumbers(head):
    cursor = head
    ev = 0
    while cursor:
        if cursor.data % 2 == 0:
            ev+=1
        cursor = cursor.next
    print("Even numbers =",ev)
node1 = Node(10)
node2 = Node(23)
node3 = Node(37)
node4 = Node(40)
node5 = Node(50)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
EvenNumbers(node1)"""
#Task12
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    cursor = head
    while cursor:
        print(cursor.data)
        cursor = cursor.next
def Reverse(head):
    prev = None
    cursor = head
    while cursor:
        next_node = cursor.next
        cursor.next = prev
        prev = cursor
        cursor = next_node
    return prev
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
print("Before:")
traverse(node1)
node1 = Reverse(node1)
print("After:")
traverse(node1)"""
#Task13
"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def Middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print("Middle =",slow.data)
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
Middle(node1)"""
#Task14
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    cursor = head
    while cursor:
        print(cursor.data)
        cursor = cursor.next
    node1 = Node(10)
def RemoveDuplicates(head):
    numb = set()
    cursor = head
    numb.add(cursor.data)
    while cursor.next:
        if cursor.next.data in numb:
            cursor.next = cursor.next.next
        else:
            numb.add(cursor.next.data)
            cursor = cursor.next
node1 = Node(10)
node2 = Node(20)
node3 = Node(10)
node4 = Node(30)
node5 = Node(20)
node6 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5  
node5.next = node6
print("Before:")
traverse(node1)
RemoveDuplicates(node1)
print("After:")
traverse(node1)