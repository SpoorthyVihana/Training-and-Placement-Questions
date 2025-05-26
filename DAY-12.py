# Minimum number of doctors required at any time
arr=[900,945,955,1100,1500,1800]
dep=[920,1200,1130,1150,1900,2000]
arr.sort()
dep.sort()
i,j,doct,m=1,0,1,0
while i<len(arr) and j<len(dep):
    if arr[i]<=dep[j]:
        doct+=1
        i+=1
    else:
        doct-=1
        j+=1
    m=max(m,doct)
print(m)


# Find the length of the longest palindromic substring
s="ababab"
m=0
for i in range(len(s)):
    # Odd length palindrome
    l=i
    r=i
    while l>=0 and r<len(s) and s[l]==s[r]:
        m=max(m,(r-l)+1)
        l-=1
        r+=1
    # Even length palindrome
    l=i
    r=i+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        m=max(m,(r-l)+1)
        l-=1
        r+=1
print(m)


#Longest Substring without repeating characters 
def lengthofLongestSubstring(s):
    l,m,d=0,0,{}
    for r in range(len(s)):
        v=s[r]
        if v in d and d[v]>=l:
            l=d[v]+1
        d[v]=r
        m=max(m,r-l+1)
    return m
s="abcabcbb"
print(lengthofLongestSubstring(s))


#Fruits into Basket: You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces. You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow: You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold. Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets. Once you reach a tree with fruit that cannot fit in your baskets, you must stop. Given the integer array fruits, return the maximum number of fruits you can pick.
def totalFruit(fruits):
    n=len(fruits)
    l,m=0,0
    dict={}
    k=2
    for i in range(n):
        r=fruits[i]
        if r in  dict:
            dict[r]+=1
        else:
            dict[r]=1
        while len(dict)>k:
            v=fruits[l]
            dict[v]-=1
            if dict[v]==0:
                dict.pop(v)
            l+=1
        m=max(m,(i-l)+1)
    return m
fruits=[1,2,1]
print(totalFruit(fruits))