# COIN CHANGE
'''
STEP-1-- Create the 2D matrix
STEP-2-- Keep True for all the 0 values
STEP-3-- Create a Tree Traverse
'''

'''
CASE-1

arr[i-1]>j
3>1
3>2
3>3

CASE-2

dp[i-1][j] or dp[i-1][j-arr[i-1]

TARGET=11 
                      j
i  0  1  2  3  4  5  6  7  8  9  10  11

2  0  0  1  0  0  0  0  0  0  0   0   0

3  1  0  1  1  0  1  0  0  0  0   0   0  

5  1  0  1  1  0  1  0  1  1  0   1   0

TARGET=12
                      j
i  0  1  2  3  4  5  6  7  8  9  10  11  12

1  1  1  0  0  0  0  0  0  0  0  0   0   0

2  1  1  1  1  0  0  0  0  0  0  0   0   0

5  1  1  1  1  0  1  1  1  1  0  0   0   0

10 1  1  1  1  0  1  1  1  1  0  1   1   1 

'''
arr=[1,2,5,10]
target=12
n=len(arr)
dp=[[False]*(target+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=True
for i in range(1,n+1):
    for j in range(1,target+1):
        if arr[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
if dp[n][target]:
    print("Yes")
else:
    print("No")


# ---------------------------------------------------------------------------------------

# LONGEST COMMOM SUBSEQUENCE UING RECURSION

def lcs(s1,s2,i,j):
    if i==0 or j==0:
        return 0
    if s1[i-1]==s2[j-1]:
        return 1+lcs(s1,s2,i-1,j-1)
    else:
        return max(lcs(s1,s2,i-1,j),lcs(s1,s2,i,j-1))
s1="abcd"
s2="abce"
print(lcs(s1,s2,len(s1),len(s2)))


# USING TABULATION

'''
#S1=abaaba
#S2=babbab

   0  b  a  b  b  a  b

0  0  0  0  0  0  0  0

a  0  0  1  1  1  1  1

b  0  1  1  2  2  2  2

a  0  1  2  2  2  3  3 

a  0  1  2  2  2  3  3

b  0  1  2  3  3  3  4

a  0  1  2  3  3  4  4
'''

s1="abaaba"
s2="babbab"
n,m=len(s1),len(s2)
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])

# PRINT LENGTH OF LARGEST COMMEM SUBSEQUENCE

s1="abaaba"
s2="babbab"
n,m=len(s1),len(s2)
dp=[[""]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+s1[i-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(len(dp[n][m]))
print(dp[n][m])

# INFINITE COIN
'''
(2,5)----TARGET=11
  
   0  1  2  3  4  5  6  7  8  9  10  11
  
0  1  0  0  0  0  0  0  0  0  0  0   0

2  1  0  1  0  1  0  1  0  1  0  1   0

5  1  0  1  0  1  1  0  1  0  1  1   0

(2,3,5)----TARGET=13

   0  1  2  3  4  5  6  7  8  9  10  11  12  13

0  0  0  0  0  0  0  0  0  0  0  0   0   0   0

2  0  0  1  0  2  0  3  0  4  0  5   0   6   0

3  0  0  1  1  2  2  2  0  3  3  5   4   4   5

5  0  0  1  1  2  1  2  2  2  3  2   3   3   3 
'''

coins=[1,2,5]
amount=11
dp=[float('inf')]*(amount+1)
dp[0]=0
for coin in coins:
    for i in range(coin,amount+1):
        dp[i]=min(dp[i],dp[i-coin]+1)
if dp[amount]!=float('inf'):
    print(dp[amount])
else:
    print(-1)
    
# TRIES

class Node:
    def __init__(self,data):
        self.data={}
        self.next=None


