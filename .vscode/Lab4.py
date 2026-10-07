"""stack = []
def push(element,st):
    st.append(element)
def pop(st):
    st.pop()
def peek(st):
    print("Top element:",st[-1])
def isEmpty(st):
    if len(st) == 0:
        print("Stack is empty")
    else:
        print("Stack isn't empty")
def size(st):
    print("Size:",len(st))
for i in range(10):
    push(1 + i,stack)
print(stack)
pop(stack)
print(stack)
peek(stack)
isEmpty(stack)
size(stack)"""
"""string = "HELLO"
stack = []
for char in string:
    stack.append(char)
gnirts = ""
while stack:
    gnirts += stack.pop()
print(gnirts)"""
"""def balanced(expression):
    stack = []
    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                print("Not balanced")
                return
            if (char == ")" and stack.pop() != "(" or char == "]" and stack.pop() != "[" or char == "}" and stack.pop() != "{"):
                print("Not balanced")
                return
    print("Balanced")
expression1 = "{[()]}"
expression2 = "{[(])}"
balanced(expression1)
balanced(expression2)"""
"""string = "abbaca"
stack = []
for char in string:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)
print(stack)"""
"""stack = []
integer = 25
while integer > 0:
    binary = integer % 2
    stack.append(binary)
    integer = integer // 2
print(stack[::-1])"""
"""from collections import deque
q = deque()
def enqueue(element,queue):
    queue.append(element)
def dequeue(queue):
    queue.popleft()
def front(queue):
    print("Front:",queue[0])
def isEmpty(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue isn't empty")
def size(queue):
    print("Size:",len(queue))
for i in range(10):
    enqueue(1 + i,q)
print(q)
dequeue(q)
print(q)
front(q)
isEmpty(q)
size(q)"""
"""from collections import deque
q = deque([10,20,30,40,50])
stack = []
while q:
    stack.append(q.popleft())
while stack:
    q.append(stack.pop())
print(q)"""
"""from collections import deque
q = deque()
q.append("1")
n = 5
for i in range(n):
    binary = q.popleft()
    print(binary)
    q.append(binary + "0")
    q.append(binary + "1")"""
"""def arithmetic(expression):
    stack = []
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == "+":
                stack.append(a + b)
            if char == "-":
                stack.append(a - b)
            if char == "*":
                stack.append(a * b)
            if char == "/":
                stack.append(a / b)
    print(stack.pop())
expression1 = "5 3 + 2 *"
expression2 = "6 12 * 5 -"
arithmetic(expression1)
arithmetic(expression2)"""
"""def postfix(expression):
    stack1 = []
    stack2 = []
    for char in expression.split():
        if char in ("+-*/()"):
            stack2.append(char)
        else:
            stack1.append(char)
    while stack2:
        stack1.append(stack2.pop())
    print(stack1)
expression1 = "A + B * C"
expression2 = "( S - D ) / H"
postfix(expression1)
postfix(expression2)"""
"""class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self,element):
        self.stack1.append(element)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    def isEmpty(self):
        return not self.stack1 and not self.stack2
q = queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q.dequeue())
print(q.peek())
print(q.isEmpty())"""
"""from collections import deque
class stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    def push(self,element):
        self.queue2.append(element)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
    def pop(self):
        return self.queue1.popleft()
    def peek(self):
        return self.queue1[0]
    def isEmpty(self):
        return len(self.queue1) == 0
st = stack()
st.push(5)
st.push(6)
st.push(7)
print(st.pop())
print(st.peek())
print(st.isEmpty())"""
"""class browserhistory:
    def __init__(self, homepage):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []
    def visit(self, page):
        self.back_stack.append(self.current)
        self.current = page
        self.forward_stack.clear()
    def back(self):
        if not self.back_stack:
            print("Can't go back")
            return
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
    def forward(self):
        if not self.forward_stack:
            print("Can't go forward")
            return
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
    def currentpage(self):
        print("Current page:", self.current)
browser = browserhistory("Google")
browser.visit("Youtube")
browser.visit("GitHub")
browser.currentpage()
browser.back()
browser.currentpage()
browser.back()
browser.currentpage()
browser.forward()
browser.currentpage()"""
"""from collections import deque
queue = deque()
queue.append((1, "Biba", 5)) 
queue.append((2, "Danchic", 2)) 
queue.append((3, "Alan", 8))
total = 0
while queue: 
    task_id, student, pages = queue.popleft()
    print(f"Task {task_id}: {student} - {pages} pages")
    total += pages
print("Total number of pags printed:",total)"""
class editor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
    def write(self, text):
        self.undo_stack.append(self.text)
        self.text += text
        self.redo_stack.clear()
    def undo(self):
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
    def redo(self):
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
    def show(self):
        print("Text:", self.text)
edit = editor()
edit.write("Hello")
edit.write(" World")
edit.show()
edit.undo()
edit.show()
edit.redo()
edit.show()

