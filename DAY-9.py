#Capacity to ship Packages within D Days
def shipWithinDays(weights,days):
    def canship(k):
        cc=0
        n=1
        for i in weights:
            if cc+i>k:
                n+=1
                cc=0
            cc+=i
        return n<=days
    l=max(weights)
    r=sum(weights)
    while l<=r:
        mid=(l+r)//2
        if canship(mid):
            r=mid-1
        else:
            l=mid+1
    return l
weights=[1,2,3,4,5,6,7,8,9,10]
days=5
print(shipWithinDays(weights,days))


#Search a 2D Matrix
def searchMatrix(matrix,target):
    m=len(matrix)
    n=len(matrix[0])
    l=0
    r=m*n-1
    while l<=r:
        mid=(l+r)//2
        i=mid//n
        j=mid%n
        mid_val=matrix[i][j]
        if mid_val==target:
            return True
        elif mid_val<target:
            l=mid+1
        else:
            r=mid-1
    return False
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(searchMatrix(matrix,target))


#Agressive Cows: You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.
def cankeep(stalls,k,d):
    c=1
    lp=stalls[0]
    for i in range(1,len(stalls)):
        if stalls[i]-lp>=d:
            c+=1
            lp=stalls[i]
            if c==k:
                return True
    return False
def aggressiveCows(stalls,k):
    l=1
    r=stalls[-1]-stalls[0]
    bd=0
    while(l<=r):
        mid=(l+r)//2
        if cankeep(stalls,k,mid):
            bd=mid
            l=mid+1
        else:
            r=mid-1
    return bd
stalls=[1, 2, 4, 8, 9]
k=3
print(aggressiveCows(stalls,k))


#Nim Game: You are playing the following Nim Game with your friend:Initially, there is a heap of stones on the table.You and your friend will alternate taking turns, and you go first. On each turn, the person whose turn it is will remove 1 to 3 stones from the heap. The one who removes the last stone is the winner. Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
def canWinNim(n):
        return n%4!=0
n=4
print(canWinNim(n))


#Candies and Two Sisters: There are two sisters Alice and Betty. You have n candies. You want to distribute these n candies between two sisters in such a way that: Alice will get a (a>0 ) candies; Betty will get b b>0 ) candies; each sister will get some integer number of candies Alice will get a greater amount of candies than Betty (i.e. a>b ); all the candies will be given to one of two sisters (i.e. a+b=n ). Your task is to calculate the number of ways to distribute exactly n candies between sisters in a way described above. Candies are indistinguishable. Formally, find the number of ways to represent n as the sum of n=a+b where a and b are positive integers and a>b You have to answer t independent test cases.
# t=int(input())
# for i in range(t):
#     n=int(input())
#     if n<3:
#         print("0")
#     else:
#         print((n-1)//2)
#         
        
#Remove Smallset: You are given the array a consisting of n positive (greater than zero) integers. In one move, you can choose two indices i and j (i≠j ) such that the absolute difference between ai and aj is no more than one (|ai−aj|≤1 ) and remove the smallest of these two elements. If two elements are equal, you can remove any of them (but exactly one). Your task is to find if it is possible to obtain the array consisting of only one element using several (possibly, zero) such moves or not. You have to answer t independent test cases.
t=int(input())  
for i in range(t):  
    n=int(input())  
    arr=list(map(int,input().split()))  
    arr.sort()  
    for j in range(n-1):  
        if abs(arr[j]-arr[j+1])>1:  
            print("NO")  
            break  
        else:  
            print("YES")