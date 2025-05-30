# SEARCH KEY ELEMENT IN BST

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def search(root,key):
    if root is None:
        return False
    if root.data==key:
        return True
    elif root.data>key:
        return search(root.left,key)
    else:
        return search(root.right,key)
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(search(root,key=3))

# SEARCH KEY ELEMENT IN BINARY TREE

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def search_bi(root,key):
    if root is None:
        return False
    if root.data==key:
        return True
    return search_bi(root.left,key) or search_bi (root.right,key)
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(search_bi(root,key=3))

# PRINT ALL THE PATHS OF A TREE FROM THE ROOT TO THE LEAF NODE

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def path(root,p=[]):
    if root is None:
        return
    p.append(str(root.data))
    if root.left is None and root.right is None:
        print(" ".join(p))  
    path(root.left,p)  
    path(root.right,p)
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
path(root)

# Max SUM OF THE PATH

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def max_sum(root):
    if root is None:
        return 0
    left_sum=max_sum(root.left)
    right_sum=max_sum(root.right)
    return root.data+max(left_sum,right_sum)
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
path(root)
print(max_sum(root))

#--------------------------------------------------------------------------------
#                                  GRAPHS
 
#  Graph is a non linear data structure consisting of nodes(vertices)and edges.
 
# TYPES OF GRAPHS
 
# 1.Directed Graph--Edges have a direction (one-way connection).
# 2.Undirected Graph--Edges have no direction (bi-directional connection).
# 3.Weighted Graph--Edges have associated weights (e.g., road distances).
# 4.Unweighted Graph--Edges do not have weights.
# 5.Cyclic Graph--Contains at least one cycle.
# 6.Acyclic Graph--No cycles exist.
# 7.Connected Graph--All nodes are reachable from any other node.
# 8.Disconnected Graph--Some nodes are not reachable from others.
 
# We can represent graphs in two ways
# 1.Adjecency List
# 2.Adjecency Matrix
  
# ADJECENCY LIST
 
#  A:[B,C]
#  B:[A,C,D,E]
#  C:[A,B,E]
#  D:[B,E,F]
#  E:[B,C,D,F]
#  F:[D,E]

#ADJECENCY MATRIX
'''
  A  B  C  D  E  F
  
A 0  1  1  0  0  0

B 1  0  1  1  1  0

C 1  1  0  0  1  0

D 0  1  0  0  1  1

E 0  1  1  1  0  1

F 0  0  0  1  1  0

- Adjacency List → Best for large graphs with few connections (saves space).
- Adjacency Matrix → Best for dense graphs with many connections (fast lookups).
If your graph is huge but mostly empty, use a list. If your graph is full of connections,use a matrix.

*BFS IS EQUAL TO LEVEL ORDER TRAVERSAL'''

# DFS

def dfs(graph,n,visited=set()):
    if n not in visited:
        print(n,end=" ")
        visited.add(n)
        for i in graph[n]:
            dfs(graph,i,visited)
    
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
dfs(graph,n='A')

# BFS

def bfs(graph,start):
    visited=set()
    q=[start]
    while q:
        n=q.pop(0)
        if n not in visited:
            print(n,end=" ")
            visited.add(n)
            q.extend(graph[n])
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
print()
bfs(graph,start='A')
    
# 547. Number of Provinces-----LEET CODE

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor]==1 and neighbor not in visited:
                    dfs(neighbor)
        if not isConnected:
            return 0
        n=len(isConnected)
        visited=set() 
        provinces=0
        for city in range(n):
            if city not in visited:
                provinces+=1
                dfs(city)
        return provinces

#UNDIRECTED GRAPH:PRINT IF PATH IS THERE OR NOT
    
from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
def path(graph,start,end):
    visited=set() 
    def dfs(val):
        if val==end:
            return True
        visited.add(val)
        for n in graph[val]:
            if n not in visited:
                if dfs(n):
                    return True
        return False
    return dfs(start)
start,end=0,5
print(path(graph,start,end))

#DIRECTED GRAPH: BFS TRAVERSAL

from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
def path(graph,start,end):
    v=set()
    q=[]
    q.append(start)
    v.add(start)
    while q:
        node=q.pop(0)
        if node==end:
            return True
        for i in graph[node]:
            if i not in v:
                v.add(i)
                q.append(i)
    return False
start,end=0,5
print(path(graph,start,end))

#PRINT ALL THE PATHS

from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
def path(start,end,p=[]):
    p.append(start)
    if start==end:
        print(p)
    else:
        for n in graph[start]:
            if n not in p:
                path(n,end,p)
    p.pop()
start,end=0,5
path(start,end)

# 1791. Find Center of Star Graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if (edges[0][0] in edges[1]):
            return edges[0][0]
        else:
            return edges[0][1]