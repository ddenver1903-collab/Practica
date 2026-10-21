"""def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
n = int(input("Number:"))
print(factorial(n))"""
"""def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)
n = int(input("Number:"))
print(sum(n))"""
"""def power(a,n):
    if n == 1:
        return a
    return a * power(a,n - 1)
a = int(input("Number:"))
n = int(input("Power:"))
print(power(a,n))"""
"""def count(n):
    if n == 0:
        return 0
    return 1 + count(n // 10)
n = int(input("Number:"))
print(count(n))"""
"""def sumd(n):
    if n == 0:
        return 0
    return n % 10 + sumd(n // 10)
n = int(input("Number:"))
print(sumd(n))"""
"""def reverse(n, rev = 0):
    if n == 0:
        return rev
    return reverse(n // 10, rev * 10 + n % 10)
n = int(input("Number:"))
print(reverse(n))"""
"""def fibanachi(n):
    if n < 2:
        return n
    return fibanachi(n - 1) + fibanachi(n - 2)
n = int(input("Number:"))
print(fibanachi(n))"""
"""def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b,a % b)
a = int(input("Number:"))
b = int(input("Number:"))
print(gcd(a,b))"""
"""arr = [2,4,6,8]
def arrsum(arr,i = 0):
    if i == len(arr):
        return 0
    return arr[i] + arrsum(arr,i + 1)
print(arrsum(arr))"""
"""arr = [4,8,2,15,7]
def max(arr,i = 0,m = arr[0]):
    if i == len(arr):
        return m
    if m < arr[i]:
        m = arr[i]
    return max(arr,i + 1,m)
print(max(arr))"""
"""arr = [2,5,2,8,2,9]
def target(arr,x,i = 0):
    if i == len(arr):
        return x
    if x == arr[i]:
        x+=1
    return target(arr,x,i + 1)
x = int(input("Target:"))
print(target(arr,x))"""
"""def palidrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return palidrome(string[1:-1])
string = input("String:")
print(palidrome(string))"""
"""def reverse(string, rev = ""):
    if string == "":
        return rev
    return reverse(string[:-1],rev = rev + string[-1])
string =input("String:")
print(reverse(string))"""
"""arr = [2,4,7,10,15,21]
def target(arr,x,i = 0):
    if i == len(arr):
        return "Not found"
    if x == arr[i]:
        return "Index " + str(i)
    return target(arr,x,i + 1)
x = int(input("Target:"))
print(target(arr,x))"""
"""def hanoi(n, source, aux, target): 
    if n == 1: 
        print(f"Move disk 1 from {source} to {target}") 
        return
    hanoi(n - 1, source, target, aux)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, aux, source, target)
n = int(input("Number of disks: "))
hanoi(n, "A", "B", "C")
print("Total moves:", 2 ** n - 1)"""
"""arr = [1,2,3]
def subset(arr,i = 0,sub = []):
    if i == len(arr):
        print(sub)
        return
    subset(arr,i + 1,sub)
    sub.append(arr[i])
    subset(arr,i + 1,sub)
    sub.pop()
subset(arr)"""
"""def permutation(string,st = ""):
    if len(string) == 0:
        print(st)
        return
    for i in range(len(string)):
        permutation(string[:i] + string[i + 1:],st + string[i])
string =input("String:")
print(permutation(string))"""
"""maze = [
    [0,1,0,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,0,0,0]
]
n = len(maze)
path = []
def find(r,c):
    if r < 0 or c < 0 or r >=n or c >=n or maze[r][c] == 1:
        return False
    path.append((r,c))
    if r == n - 1 and c == n - 1:
        return True
    maze[r][c] = 1
    if (find(r + 1,c) or find(r,c + 1) or find(r - 1,c) or find(r,c - 1)):
        return True
    path.pop()
    return False
if find(0,0):
    print("Path found:")
    for cell in path:
        print(cell)
else:
    print("Path not found")"""
"""def solve_n_queens(n): 
    board = [-1] * n 
    solutions = []
    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            safe = True
            for prev_row in range(row):
                if (board[prev_row] == col or
                    abs(board[prev_row] - col) == abs(prev_row - row)):
                    safe = False
                    break
            if safe:
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    backtrack(0)
    for solution in solutions:
        for row in range(n):
            line = ""
            for col in range(n):
                if solution[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()
    print("Total solutions:", len(solutions))
n = int(input("Number:"))
solve_n_queens(n)"""
"""class Node: 
    def __init__(self, value): 
        self.value = value 
        self.left = None 
        self.right = None
root = Node(10) 
root.left = Node(5) 
root.right = Node(15)
root.left.left = Node(2) 
root.left.right = Node(7) 
root.right.right = Node(20)
def preorder(node): 
    if node is None: 
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)
def inorder(node): 
    if node is None: 
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)
def postorder(node): 
    if node is None: 
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")
print("Preorder: ", end="") 
preorder(root)
print("\nInorder:  ", end="") 
inorder(root)
print("\nPostorder:", end=" ") 
postorder(root)"""