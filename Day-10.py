#Lemonade Change
def lemonadeChange(bills):
    f=0
    t=0
    tw=0
    for i in bills:
        if i==5:
            f+=1
        elif i==10:
            if f==0:
                return False
            f-=1
            t+=1
        elif i==20:
            if t>0 and f>0:
                t-=1
                f-=1
                tw+=1
            elif f>=3:
                f-=3
                tw+=1
            else:
                return False
        else:
            if tw>0 and f>0:
                tw-=1
                f-=1
            elif f>=5:
                f-=5
            else:
                return False
    return True
bills=[5,5,5,10,20,30]
print(lemonadeChange(bills))


#Jump Game: You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
def canJump(nums):
    p=0
    for i in nums:
        if p<0:
            return False
        elif i>p:
            p=i
        p-=1
    return True
nums=[3,2,1,0,4]
print(canJump(nums))


#Shortest Job First
def solve(bt):
    bt.sort()
    n=len(bt)
    wt=[0]*n
    for i in range(1,n):
        wt[i]=wt[i-1]+bt[i-1]
    return int(sum(wt)/n)
bt=[4,3,7,1,2]
print(solve(bt))


#Assign Cookies: Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
def findContentChildren(g,s):
    g.sort()
    s.sort()
    i,j=0,0
    c=0
    while i<len(g) and j<len(s):
        if s[j]>=g[i]:
            c+=1
            i+=1
        j+=1
    return c
g=[1,2]
s=[1,2,3]
print(findContentChildren(g,s))


#N Meeting in one room: You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 
def maximumMeetings(start,end):
    m=list(zip(start,end))
    m.sort(key=lambda x:x[1])
    c=0
    l=-1
    for s,e in m:
        if s>l:
            c+=1
            l=e
    return c
start=[1, 3, 0, 5, 8, 5]
end=[2, 4, 6, 7, 9, 9]
print(maximumMeetings(start,end))


#Your task is to modify and print the given string in such a way that the adjacent characters in the string don't repeate themselves more than twice.
s="aabbbc"
res=[]
n=len(s)
for i in range(n):
    if i>=2 and s[i]==s[i-1]==s[i-2]:
        continue
    res.append(s[i])
print("".join(res))


#Your task is it reduce the string to the minimum length where no two adjacent letters can be same.
n="abba"
st=[]
for i in n:
    if st and st[-1]==i:
        st.pop()
    else:
        st.append(i)
print("".join(st))


#Length of the longest palindromic subsequence

#String Compression: Input- "aaaabbbc" Output- "a4b3c1"
s="aaaabbbc"
res=[]
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        res.append(s[i-1]+str(c))
        c=1
print("".join(res))
#Reverse Vowels of a String
def reverseVowels(s):
    v=set("aeiouAEIOU")
    s=list(s)
    l=0
    r=len(s)-1
    while l<r:
        if s[l] not in v:
            l+= 1
        elif s[r] not in v:
            r-= 1
        else:
            s[l],s[r]=s[r],s[l]
            l+= 1
            r-= 1
    return "".join(s)
s="IceCreAm"
print(reverseVowels(s))