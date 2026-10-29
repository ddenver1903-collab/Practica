"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)
bst = BinarySearchTree()
keys = [50,30,70,20,40,60,80]
for key in keys:
    bst.insert(key)
bst.inorder(bst.root)"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def search(self,key):
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)
bst = BinarySearchTree()
keys = [50,30,70,20,40,60,80]
for key in keys:
    bst.insert(key)
bst.inorder(bst.root)
print(bst.search(50))
print(bst.search(90))"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key)
bst = BinarySearchTree()
keys = [45,25,65,15,35,55,75]
for key in keys:
    bst.insert(key)
print("Inorder:")
bst.inorder(bst.root)
print("Preorder:")
bst.preorder(bst.root)
print("Postorder:")
bst.postorder(bst.root)"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key
    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key
bst = BinarySearchTree()
keys = [45,25,65,15,35,55,75]
for key in keys:
    bst.insert(key)
print("Min:",bst.find_min())
print("Max:",bst.find_max())"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def height(self,root):
        if root is None:
            return -1
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        return 1 + max(l_height,r_height)
bst1 = BinarySearchTree()
keys1 = [50,30,70,20,40,60,80]
for key in keys1:
    bst1.insert(key)
print("Balanced-looking tree height:",bst1.height(bst1.root))
bst2 = BinarySearchTree()
keys2 = [10,20,30,40,50,60,70]
for key in keys2:
    bst2.insert(key)
print("Screwed tree height:",bst2.height(bst2.root))"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def total(self,root):
        if root is None:
            return 0
        return 1 + self.total(root.left) + self.total(root.right)
    def leaves(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.leaves(root.left) + self.leaves(root.right)
    def internal(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return 1 + self.internal(root.left) + self.internal(root.right)
bst = BinarySearchTree()
keys = [45,25,65,15,35,55,75]
for key in keys:
    bst.insert(key)
print("Total nodes:",bst.total(bst.root))
print("Leaf nodes:",bst.leaves(bst.root))
print("Internal nodes:",bst.internal(bst.root))"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def delete(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)
        return root
    def remove(self, key):
        self.root = self.delete(self.root, key)
    def is_bst(self, root, min_key=None, max_key=None):
        if root is None:
            return True
        if min_key is not None and root.key <= min_key:
            return False
        if max_key is not None and root.key >= max_key:
            return False
        return self.is_bst(root.left, min_key, root.key) and self.is_bst(root.right, root.key, max_key)
bst = BinarySearchTree()
keys = [45,25,65,15,35,55,75]
for key in keys:
    bst.insert(key)
bst.remove(15)
print(bst.is_bst(bst.root))
bst.remove(25)
print(bst.is_bst(bst.root))
bst.remove(45)
print(bst.is_bst(bst.root))"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def kth(self, k):
        if k < 1:
            return None
        count = 0
        result = None
        def inorder(node):
            nonlocal count, result
            if node is None or result is not None:
                return
            inorder(node.left)
            count += 1
            if count == k:
                result = node.key
                return
            inorder(node.right)
        inorder(self.root)
        return result
bst = BinarySearchTree()
keys = [10,5,15,3,7,12,18]
for key in keys:
    bst.insert(key)
print("1st:",bst.kth(1))
print("3rd:",bst.kth(3))
print("Invalid:",bst.kth(0))"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def is_bst(self, root, min_key=None, max_key=None):
        if root is None:
            return True
        if min_key is not None and root.key <= min_key:
            return False
        if max_key is not None and root.key >= max_key:
            return False
        return self.is_bst(root.left, min_key, root.key) and self.is_bst(root.right, root.key, max_key)
bst = BinarySearchTree()
keys = [45,25,65,15,35,55,75]
for key in keys:
    bst.insert(key)
print(bst.is_bst(bst.root))"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def lca(self, key1, key2):
        current = self.root
        while current is not None:
            if key1 < current.key and key2 < current.key:
                current = current.left
            elif key1 > current.key and key2 > current.key:
                current = current.right
            else:
                return current.key
        return None
bst = BinarySearchTree()
keys = [20, 10, 30, 5, 15, 25, 35]
for key in keys:
    bst.insert(key)
print("LCA of 5 and 15:", bst.lca(5, 15))
print("LCA of 5 and 30:", bst.lca(5, 30))"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def bst_insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.bst_insert(root.left,key)
        elif key > root.key:
            root.right = self.bst_insert(root.right,key)
        return root
    def insert(self,key):
        self.root = self.bst_insert(self.root,key)
    def height(self,root):
        if root is None:
            return -1
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        return 1 + max(l_height,r_height)
    def balance_factor(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return left_height - right_height
    def display(self, root):
        if root is not None:
            self.display(root.left)
            bf = self.balance_factor(root)
            print("Node:",root.key,"Balance factor:",bf)
            self.display(root.right)
bst = BinarySearchTree()
keys = [50,30,70,20,40,60,80]
for key in keys:
    bst.insert(key)
bst.display(bst.root)"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class AVLTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        return x
    def display(self, node, level=0):
        if node is not None:
            self.display(node.right, level + 1)
            print("     "* level + str(node.key))
            self.display(node.left, level + 1)
avl = AVLTree()
keys = [30,20,10]
for key in keys:
    avl.insert(key)
print("Before rotation:")
avl.display(avl.root)
avl.root = avl.right_rotate(avl.root)
print("After rotation:")
avl.display(avl.root)"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class AVLTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        return y
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left),self.height(node.right))
    def balanced(self, node):
        if node is None:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.balanced(node.left) and self.balanced(node.right)
    def display(self, node, level=0):
        if node is not None:
            self.display(node.right, level + 1)
            print("     "* level + str(node.key))
            self.display(node.left, level + 1)
avl = AVLTree()
keys = [30,20,10]
for key in keys:
    avl.insert(key)
print("Before rotation:")
avl.display(avl.root)
avl.balanced(avl.root)
avl.root = avl.left_rotate(avl.root)
print("After rotation:")
avl.display(avl.root)
avl.balanced(avl.root)"""
"""class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class AVLTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        return y
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        return x
    def fix_LR(self, root):
        root.left = self.left_rotate(root.left)
        return self.right_rotate(root)
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left),self.height(node.right))
    def balanced(self, node):
        if node is None:
           return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.balanced(node.left) and self.balanced(node.right)
    def display(self, node, level=0):
        if node is not None:
            self.display(node.right, level + 1)
            print("    "* level + str(node.key))
            self.display(node.left, level + 1)
avl = AVLTree()
keys = [30,20,10]
for key in keys:
    avl.insert(key)
print("Before rotations:")
avl.display(avl.root)
print("Balanced:",avl.balanced(avl.root))
avl.root = avl.fix_LR(avl.root)
print("After rotations:")
avl.display(avl.root)
print("Balanced:",avl.balanced(avl.root))"""
"""class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class AVLTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        return y
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        return x
    def fix_RL(self, root):
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)    
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left),self.height(node.right))
    def balanced(self, node):
        if node is None:
           return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.balanced(node.left) and self.balanced(node.right)
    def display(self, node, level=0):
        if node is not None:
            self.display(node.right, level + 1)
            print("    "* level + str(node.key))
            self.display(node.left, level + 1)
avl = AVLTree()
keys = [30,20,10]
for key in keys:
    avl.insert(key)
print("Before rotations:")
avl.display(avl.root)
print("Balanced:",avl.balanced(avl.root))
avl.root = avl.fix_RL(avl.root)
print("After rotations:")
avl.display(avl.root)
print("Balanced:",avl.balanced(avl.root))"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __init__(self):
        self.root = None
    def get_height(self, root):
        if root is None:
            return 0
        return root.height
    def balance(self,root):
        if root is None:
            return 0
        return (self.get_height(root.left) - self.get_height(root.right))
    def right_rotate(self,y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        return x
    def left_rotate(self,x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y
    def insert_node(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left,key)
        elif key > root.key:
            root.right = self.insert_node(root.right,key)
        else:
            return root
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        bf = self.balance(root)
        if bf > 1 and key < root.left.key:
            return self.right_rotate(root)
        if bf < -1 and key > root.right.key:
            return self.left_rotate(root)
        if bf > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if bf < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def insert(self, value):
        self.root = self.insert_node(self.root,value)
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.key, end= " ")
            self.inorder(root.right)
    def display_balance_factors(self,root):
        if root is not None:
            self.display_balance_factors(root.left)
            print("Node:",root.key,"Height:",root.height,"Balance Factor:",self.balance(root))
            self.display_balance_factors(root.right)
    def is_balanced(self, root):
        if root is None:
            return True
        if abs(self.balance(root)) > 1:
            return False
        return (self.is_balanced(root.left) and self.is_balanced(root.right))
avl = AVLTree()
keys = [10,20,30,40,50,25,5,15,35,45,60,1,8,22,28]
for key in keys:
    avl.insert(key)
print("Inorder traversal:")
avl.inorder(avl.root)
print("Height and balance factors:")
avl.display_balance_factors(avl.root)
print("Tree is balanced:", avl.is_balanced(avl.root))"""
"""class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __init__(self):
        self.root = None
    def get_height(self,root):
        if root is None:
            return 0
        return root.height
    def balance(self,root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def right_rotate(self,y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        return x
    def left_rotate(self,x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y
    def insert_node(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left,key)
        elif key > root.key:
            root.right = self.insert_node(root.right,key)
        else:
            return root
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        bf = self.balance(root)
        if bf > 1 and key < root.left.key:
            return self.right_rotate(root)
        if bf < -1 and key > root.right.key:
            return self.left_rotate(root)
        if bf > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if bf < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def insert(self,value):
        self.root = self.insert_node(self.root,value)
    def find_min(self,root):
        while root.left:
            root = root.left
        return root
    def delete_node(self,root, alue):
        if root is None:
            return None
        if value < root.key:
            root.left = self.delete_node(root.left, value)
        elif value > root.key:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = self.find_min(root.right)
            root.key = successor.key
            root.right = self.delete_node(root.right,successor.key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        bf = self.balance(root)
        if bf > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)
        if bf > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if bf < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)
        if bf < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def delete(self,value):
        self.root = self.delete_node(self.root,value)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
avl = AVLTree()
keys = [20, 10, 30, 5, 15, 25, 35, 13]
for key in keys:
    avl.insert(key)
avl.delete(5)
avl.inorder(avl.root)
avl.delete(15)
avl.inorder(avl.root)
avl.delete(20)
avl.inorder(avl.root)"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        self.root = self.insert_node(self.root,key)
    def insert_node(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left,key)
        elif key > root.key:
            root.right = self.insert_node(root.right,key)
        return root
    def get_height(self,root):
        if root is None:
            return -1
        return 1 + max(self.get_height(root.left),self.get_height(root.right))
class AVLTree:
    def __init__(self):
        self.root = None
    def get_height(self,root):
        if root is None:
            return 0
        return root.height
    def balance(self,root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def right_rotate(self,y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        return x
    def left_rotate(self,x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y
    def insert(self,key):
        self.root = self.insert_node(self.root,key)
    def insert_node(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left,key)
        elif key > root.key:
            root.right = self.insert_node(root.right,key)
        else:
            return root
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        bf = self.balance(root)
        if bf > 1 and key < root.left.key:
            return self.right_rotate(root)
        if bf < -1 and key > root.right.key:
            return self.left_rotate(root)
        if bf > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if bf < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
def compare_trees(keys):
    bst = BST()
    avl = AVLTree()
    for key in keys:
        bst.insert(key)
        avl.insert(key)
    bst_height = bst.get_height(bst.root)
    avl_height = avl.root.height if avl.root else -1
    print("Input:",keys)
    print("BST height:",bst_height)
    print("AVL height:",avl_height)
    print()
ascending = list(range(1, 13))
descending = list(range(12, 0, -1))
random_values = [7, 2, 11, 4, 9, 1, 12, 5, 8, 3, 10, 6]
print("Ascending order:")
compare_trees(ascending)
print("Descending order:")
compare_trees(descending)
print("Random order:")
compare_trees(random_values)"""
"""class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def get_height(self,root):
        if root is None:
            return 0
        return root.height
    def balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def right_rotate(self,root):
        new_root = root.left
        temp = new_root.right
        new_root.right = root
        root.left = temp
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
    def left_rotate(self,root):
        new_root = root.right
        temp = new_root.left
        new_root.left = root
        root.right = temp
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
    def insert_node(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left,key)
        elif key > root.key:
            root.right = self.insert_node(root.right,key)
        else:
            return root
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance = self.balance(root)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def insert(self, key):
        self.root = self.insert_node(self.root,key)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
    def display(self,root):
        if root:
            self.display(root.left)
            print("Node:",root.key,"Balance factor:",self.balance(root))
            self.display(root.right)
avl = AVLTree()
avl.root = None
keys = [10, 20, 30, 40, 50, 25, 30, 20]
for key in keys:
    avl.insert(key)
print("Inorder traversal:")
avl.inorder(avl.root)
print("Final height:",avl.get_height(avl.root))
print("Balance factors:")
avl.display(avl.root)"""
"""class Node:
    def __init__(self,id,score):
        self.id = id
        self.score = score
        self.key = (score, -id)
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def get_height(self,root):
        if root is None:
            return 0
        return root.height
    def balance(self,root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def right_rotate(self,root):
        new_root = root.left
        temp = new_root.right
        new_root.right = root
        root.left = temp
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root
    def left_rotate(self,root):
        new_root = root.right
        temp = new_root.left
        new_root.left = root
        root.right = temp
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root
    def insert_node(self,root,id,score):
        if root is None:
            return Node(id,score)
        key = (score,-id)
        if key < root.key:
            root.left = self.insert_node(root.left,id,score)
        elif key > root.key:
            root.right = self.insert_node(root.right,id,score)
        else:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        b = self.balance(root)
        if b > 1 and key < root.left.key:
            return self.right_rotate(root)
        if b < -1 and key > root.right.key:
            return self.left_rotate(root)
        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def insert(self,id,score):
        if self.search(self.root,id):
            print("Student ID already exists")
            return
        self.root = self.insert_node(self.root,id,score)
    def search(self,root,id):
        if root is None:
            return None
        if root.id == id:
            return root
        result = self.search(root.left,id)
        if result:
            return result
        return self.search(root.right,id)
    def find_min(self,root):
        while root.left:
            root = root.left
        return root
    def delete_node(self,root,key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left,key)
        elif key > root.key:
            root.right = self.delete_node(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.find_min(root.right)
            root.id = temp.id
            root.score = temp.score
            root.key = temp.key
            root.right = self.delete_node(root.right,temp.key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        b = self.balance(root)
        if b > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)
        if b > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)
        if b < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def remove(self, id):
        student = self.search(self.root, id)
        if student is None:
            print("Student not found")
            return
        self.root = self.delete_node(self.root,(student.score,-student.id))
        print("Student removed:", id)
    def update_score(self,id,new_score):
        student = self.search(self.root,id)
        if student is None:
            print("Student not found")
            return
        self.root = self.delete_node(self.root,(student.score,-student.id))
        self.root = self.insert_node(self.root,id,new_score)
        print("Score updated")
    def display(self,root):
        if root:
            self.display(root.right)
            print("ID:",root.id,"Score:",root.score)
            self.display(root.left)
    def highest_score(self):
        if self.root is None:
            print("No students")
            return
        root = self.root
        while root.right:
            root = root.right
        print("Highest score:",root.score,"Student ID:",root.id)
avl = AVLTree()
avl.root = None
students = [(101, 85),(102, 92),(103, 78),(104, 95),(105, 88),(106, 92),(107, 73),(108, 95),(109, 81),(110, 67)]
for id, score in students:
    avl.insert(id, score)
print("Students ranked by score:")
avl.display(avl.root)
print("Search for student 105:")
student = avl.search(avl.root, 105)
if student:
    print("ID:",student.id,"Score:",student.score)
print("Update student 103:")
avl.update_score(103, 90)
print("Remove student 107:")
avl.remove(107)
print("Updated ranking:")
avl.display(avl.root)
print()
avl.highest_score()"""