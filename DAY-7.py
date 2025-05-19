#Merge the lists and sort it- Time Complexity:O(n+m)
a=[3,5,6,8]
b=[2,4,7]
res=[]
i=0
j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        res.append(a[i])
        i+=1
    else:
        res.append(b[j])
        j+=1
while i<len(a):
    res.append(a[i])
    i+=1
while j<len(b):
    res.append(b[j])
    j+=1
print(res)


#Merge Sort-Time Complexity: O(nlogn)+n  [n can be ignored]
def div(a):               #Time Complexity: O(nlogn)
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=div(a[:mid])
    right=div(a[mid:])
    return merge(left,right)
def merge(l,r):          # Time Complexity: O(n+m)
    res=[]
    i=0
    j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
    while i<len(l):
        res.append(l[i])
        i+=1
    while j<len(r):
        res.append(r[j])
        j+=1
    return res
l=[3,2,1,5,4,6]
print(div(l))


#K-th largest number using Bucket Sort approach
l=[2,7,3,1,5,4]
k=3
res=[0]*(max(l)+1)
for i in l:
    res[i]=1
for i in range(len(res)-1,-1,-1):
    if res[i]==1:
        k-=1
    if k==0:
        print(i)
        break


#K-th largest element having dupicate elements
l=[5,3,6,2,2,1,1,8,7,3,1,12]
k=4
res=[0]*(max(l)+1)
for i in l:
    res[i]=1
c=0
for i in range(len(res)):
    if res[i]>0:
        c+=1
    if c==k:
        print(i)
        
        
#K-th minimum element in a list having duplicate elements using bucket sort
a=[5,3,3,5,2,2,2,1,1,4,4,3,1]
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
m=max(dict.values())
b=[[] for i in range(m+1)]
for i in dict:
    b[dict[i]].append(i)
res=[]
for i in range(1,len(b)):
    for j in b[i]:
        res.extend([j]*i)
print(res)


#Majority Element: The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
a=[3,2,2,2,1]
c=-1
v=0
for i in a:
    if v==0:
        c=i
        v=1
    elif i==c:
        v+=1
    else:
        v-=1
print(c)


#Linear Search: Time Complexity-O(n)
a=[1,4,6,3,5,9]
k=6
for i in range(len(a)):
    if a[i]==k:
        print(i)


#Binary Search
def bi(l,s,e,k):
    if s>e:
        return -1  
    mid=(s+e)//2
    if l[mid]==k:
        return mid
    elif k<l[mid]:
        return bi(l,s,mid-1,k)  
    else:
        return bi(l,mid+1,e,k)  
a=[1, 3, 4, 5, 6, 9, 11]
k=9
s=0
e=len(a)-1
print(bi(a,s,e,k))



#Search Insert Position: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.
def bi(a,k):
    l=0
    r=len(a)-1
    while l<=r:
        mid = l+(r-l)//2
        if a[mid]==k:
            return mid
        elif a[mid]<k:
            l=mid+1
        else:
            r=mid-1
    return l
l=[1,3,5,6]
k=4
print(bi(l,k))


#Find First and Last Position of Element in a Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
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
        return [left,right] if left<=right and 0<=left<len(nums) and nums[left]==target else [-1, -1]
 