#Valid Palindrome II


def validPalindrome(s):
    def isPal(s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    l=0
    r=len(s)-1
    while(l<r):
        if s[l]!=s[r]:
            return isPal(s,l+1,r) or isPal(s,l,r-1)
        l+=1
        r-=1
    return True
s="abca"
print(validPalindrome(s))


#Check if the list is sorted and doesn't have any duplicate elements


l=[1,2,3,4,5,7]
f=0
for i in range(len(l)-1):
    if l[i]>=l[i+1]:
        f+=1
        break
if f==1:
    print("No")
else:
    print("Yes")
    
    
# Fixed Sliding Windows
    
    
l=[4,3,4,5,1,3,2,1,5,2,3,5]
k=4
sum=0
for i in range(k):
    sum+=l[i]
m=sum
for i in range(len(l)-k):
    sum=sum+l[i+k]-l[i]
    m=max(m,sum)
print(m)
    
    
# Dynamic Sliding Window

a=[2,5,1,7,10]
k=14
l,r,sum,m=0,0,0,0
while r<len(a):
    sum+=a[r]
    if sum>=k:
        sum-=a[l]
        l+=1
    if sum<k:
       m=max(m,(r-l)+1)
    r+=1
print(m)


#Maximum Points you can obtain from Cards: There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints. In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards. Your score is the sum of the points of the cards you have taken. Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
def maxScore(cardPoints,k):
    n=len(cardPoints)
    l_s=sum(cardPoints[:k])
    r_s=0
    m=l_s
    for i in range(k):
        l_s-=cardPoints[k-i-1]
        r_s+=cardPoints[n-i-1]
        m=max(m,l_s+r_s)
    return m
cardPoints=[1,2,3,4,5,6,1]
k=3
print(maxScore(cardPoints,k))


#Jump Game II: You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0]. Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where: 0 <= j <= nums[i] and i + j < n Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


def jump(nums):
    l,r,j=0,0,0
    while r<len(nums)-1:
        m=0
        for i in range(l,r+1):
            if i+nums[i]>m:
                m=i+nums[i]
        l=r+1
        r=m
        j=j+1
    return j
nums=[2,3,1,1,4]
print(jump(nums))