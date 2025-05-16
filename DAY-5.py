1.CREATE A 2D MATRIX AND FIND THE SUM OF ALL THE 2D MATRIX


M=[
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
 ]
 .................................................
S=sum(sum(row) for row in M)
print("Matrix:")
for row in M:
    print(row)
print("\nSum of all elements:",S)
 ..................................................
rows=len(M)
cols=len(M[0])
 S=0
 for i in range(rows):
     for j in range(cols):
         
        S+=M[i][j]
print(S)


2.FIND THE COUNT OF ALL THE PRIME NUMBERS IN THIS 2X2 MATRIX


def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
matrix=[[3, 4], [5, 6]]
C=sum(is_prime(n)
      for row in matrix for n in row)
print(C)



3.BACK TRACKING
PATH TO REACH THE EXIT


def path(m,i,j,p,n):
    if i==n-1 and j==n-1:
        print(p)
        return
    if i+1<n and m[i+1][j]==1:
        path(m,i+1,j,p+"D",n)
    if j+1<n and m[i][j+1]==1:
        path(m,i,j+1,p+"R",n)   
m=[[1,1,1,0],
    [0,1,1,0],
    [0,1,1,1],
    [0,0,0,1]]
path(m,0,0,"",len(m))

4.RECURSIVE FUNCTION


def fire(m,i,j):
    c=0
    if not m:
        return 
    if i<0 or i>=len(m) or j<0 or j>=len(m) or m[i][j]!=1:
        return
    m[i][j]=2
    fire(m,i+1,j)
    fire(m,i-1,j)
    fire(m,i,j+1)
    fire(m,i,j-1)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==1:
                c+=1
    return c
m=[[1,1,1,0,1],
   [0,1,1,1,0],
   [0,0,0,1,0],
   [1,1,0,0,1]]
print(fire(m,0,1))


5.PROBLEM ON ISLAND


def island(m,i,j):
    if not m:
        return 
    if i<0 or i>=len(m) or j<0 or j>=len(m) or m[i][j]!=1:
        return
    m[i][j]=2
    island(m,i+1,j)
    island(m,i-1,j)
    island(m,i,j+1)
    island(m,i,j-1)
m=[[1,1,1,0,1],
   [0,1,1,1,0],
   [0,0,0,1,0],
   [1,1,0,0,1]]
c=0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j]==1:
             island(m,i,j)
             c+=1
print(c)


6.POSSIBLE BINARY NUMBERS


def binary(n,s):
    if n==0:
        print(s)
        return
    binary(n-1,s+"0")
    binary(n-1,s+"1")
n=int(input())
binary(n,"")
n=int(input())


7.COUNT OF VALID PARANTHESIS


def par(n,s=0,e=0,p=""):
    if s==n and e==n:
        return [p]
    res=[]
    if s<n:
        res+=par(n,s+1,e,p+"(")
    if e<s:
        res+=par(n,s,e+1,p+")")
    return res
n=int(input())
print(par(n))

def binary(n,res="",o=0,c=0):
    if o==n and c==n:
        print(res)
        return
    if o<n:
        binary(n,res+"(",o+1,c)
    if c<o:
        binary(n,res+")",o,c+1)
n=2
binary(n)


121. Best Time to Buy and Sell Stock---LEETCODE


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for price in prices[1:]:
            max_profit=max(max_profit,price-min_price)
            min_price=min(min_price,price)
        return max_profit

172. Factorial Trailing Zeroes


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if(n<5):
            return 0;
        sum=0
        while(n>=5):
          sum=sum+n//5
          n//=5
        return sum




