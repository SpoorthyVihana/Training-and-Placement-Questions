# Lowest Common Ancestor-----HACKER RANK

def lca(root, v1, v2):
    if(v1<root.info and v2<root.info):
        return lca(root.left,v1,v2)
    elif(v1>root.info and v2>root.info):
        return lca(root.right,v1,v2)
    else:
        return root
    
#SOME OF ALL THE NODES IN THE BST

class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
    def sum1(self):
        t=self.data
        if self.left:
            t+=self.left.sum1()
        if self.right:
            t+=self.right.sum1()
        return t
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.sum1())

# Sum of even Nodes in BST

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def even_sum(self):
        t=0
        if self.data%2==0:
            t=self.data
        if self.left is not None:
            t+=self.left.even_sum()
        if self.right is not None:
            t+=self.right.even_sum()
        return t
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.even_sum())
 
# SUM OF ODD NODES IN BST

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def odd_sum(self):
        t=0
        if self.data%2!=0:
            t=self.data
        if self.left is not None:
            t+=self.left.odd_sum()
        if self.right is not None:
            t+=self.right.odd_sum()
        return t
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.odd_sum())


# PRINT ALL LEAF NODES IN BST

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def print_leaf(self):
        if self.left is None and self.right is None:
            print(self.data,end=" ")
        if self.left:
            self.left.print_leaf()
        if self.right:
            self.right.print_leaf()
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.print_leaf())

#  WRITE A FUNCTION TO FIND SUM OF PRIME NUMBERS IN THE NODE

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def prime(self):
        def is_prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        t=0
        if is_prime(self.data):
            t=self.data
        if self.left is not None:
            t+=self.left.prime()
        if self.right is not None:
            t+=self.right.prime()
        return t
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.prime())

#Kth LARGEST

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def klargest(self,k):
        def inorder(node,l):
            if node is None:
                return
            inorder(node.right,l)
            l.append(node.data)
            inorder(node.left,l)
        l=[]
        inorder(self,l)
        return l[k-1]
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.klargest(3))
 
# Kth SMALLEST
 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def ksmallest(self,k):
        def inorder(node,l):
            if node is None:
                return
            inorder(node.left,l)
            l.append(node.data)
            inorder(node.right,l)
        l=[]
        inorder(self,l)
        return l[k-1]
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.ksmallest(3))
 
# 100. Same Tree-----LEET CODE
 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True  
        if not p or not q:
            return False  
        if p.val!=q.val:
            return False 
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
#     
# 226. Invert Binary Tree-----LEET CODE
 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root
# 
#  FIND COUNT OF LEAF NODE IN A TREE
# 
class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
    def count_leaf(self):
        if self.left is None and self.right is None:
            return 1
        c=0
        if self.left:
            c+=self.left.count_leaf()
        if self.right:
            c+=self.right.count_leaf()
        return c
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.count_leaf())

# TOP VIEW

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def top_view(root):
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,val=q.pop(0)
        if val not in d:
            d[val]=node.data
        if node.left:
            q.append((node.left,val-1))
        if node.right:
            q.append((node.right,val+1))
    for key in sorted(d):
        print(d[key],end=" ") 
root=Node(5)  
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
top_view(root)

#BOTTOM VIEW

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def bottom_view(root):
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,val=q.pop(0)
        d[val]=node.data
        if node.left:
            q.append((node.left,val-1))
        if node.right:
            q.append((node.right,val+1))
    for key in sorted(d):
        print(d[key],end=" ") 
root=Node(5)  
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
bottom_view(root)

# LEFT VIEW

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def left_view(root):
    if not root:
        return
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,val=q.pop(0)
        if val not in d:
            d[val]=node.data
        if node.left:
            q.append((node.left,val+1))
        if node.right:
            q.append((node.right,val+1))
    for key in sorted(d):
        print(d[key],end=" ") 
root = Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
left_view(root)

#RIGHT VIEW

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def right_view(root):
    if not root:
        return
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,val=q.pop(0)
        d[val]=node.data
        if node.left:
            q.append((node.left,val+1))
        if node.right:
            q.append((node.right,val+1))
    for key in sorted(d):
        print(d[key],end=" ") 
root = Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
right_view(root)

# Huffman Decoding-----HACKER RANK
def decodeHuff(root, s):
    temp=root
     res=[]
     for ch in s:
        if ch=='0':
            temp=temp.left
        else:
            temp=temp.right
        if temp.left is None and temp.right is None:
            res.append(temp.data)
            temp=root
     print("".join(res))
        





    

    