#Find First and Last Position of Element in a Sorted Array
def searchRange(nums,target):
    l=0
    h=len(nums)-1
    while l<=h:
        mid=(l+h)//2
        if nums[mid]<target:
            l=mid+1
        else:
            h=mid-1
    left=l
    l=0
    h=len(nums)-1
    while l<=h:
        mid=(l+h)//2
        if nums[mid]<=target:
            l=mid+1
        else:
            h=mid-1
    right=h
    if left<=right and 0<=left<len(nums) and nums[left]==target:
        return [left,right]
    else:
        return [-1, -1]
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))


#Left and Right Rotation in a list
a=[1,2,3,4,5,6,7]
k=3
res1=a[k:]+a[:k]       #Left Rotation
print(res1)
res2=a[-k:]+a[:-k]     #Right Rotation
print(res2)


#Find the index where the rotation starts in a list
a=[4,5,6,1,2,3]
l=0
h=len(a)-1
while l<=h:
    mid=(l+h)//2
    if mid<len(a)-1 and a[mid]>a[mid+1]:
        res=mid
        break
    if a[mid]<a[mid-1]:
        res=mid-1
        break
    if a[l]>=a[mid]:
        h=mid-1
    else:
        l=mid+1
print(res)


#Peak Element in a list
a=[1,2,3,4,5,3,2]
l=0
r=len(a)-1
while l<r:
    mid=(l+r)//2
    if a[mid]>a[mid+1]:
        r=mid
    else:
        l=mid+1
print(l)

def findPeakElement(a):
    n=len(a)
    if len(a)==1:
        return 0
    if a[0]>a[1]:
        return 0
    if a[n-1]>a[n-2]:
        return n-1
    l=1
    r=n-2
    while l<=r:
        mid=(l+r)//2
        if a[mid-1]<a[mid] and a[mid]>a[mid+1]:
            return mid
        if a[mid]>a[mid-1]:
            l=mid+1
        else:
            r=mid-1
    return -1
a=[1,2,3,4,5,3,2]
print(findPeakElement(a))


#Sqrt(x)
def mySqrt(x):
    l=0
    r=x
    while l<=r:
        mid=(l+r)//2
        if mid*mid==x:
            return mid
        elif mid*mid>x:
            r=mid-1
        else:
            l=mid+1
    return r
x=4
print(mySqrt(x))


#Search in Rotated Sorted Array
def search(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(r+l)//2
        if nums[mid]==target:
            return mid
        if nums[l]<=nums[mid]:
            if nums[l]<=target<=nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if nums[r]>=target>=nums[mid]:
                l=mid+1
            else:
                r=mid-1
    return -1
nums=[4,5,6,7,0,1,2]
target=3
print(search(nums,target))


#Koko Eating Bananas
from math import ceil
def minEat(piles,h):
    l,r=1,max(piles)
    def caneat(k):
        res=0
        for p in piles:
            res+=ceil(p/k)
        if res<=h:
            return True
        else:
            return False
    while l<=r:
        mid=(l+r)//2
        if caneat(mid):
            r=mid-1
        else:
            l=mid+1
    return l
piles=[3,6,7,11]
h=8
print(minEat(piles,h))