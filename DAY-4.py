# SUM OF N NATURAL NUMBERS USING RECURSION


# def fun(n):
#     if n==0:
#         return 0
#     return n+fun(n-1)
# n=5
# print(fun(5))


#PARAMETERIZED RECURSSION


# def fun(n,sum):
#     if n<1:
#         print(sum)
#         return
#     fun(n-1,sum+n)
# n=5 
# fun(n,sum=0)


# write a code to find all the subset of a list[1,2,3,4,5] and pass the list to the function


# def fun(arr,i=0,res=[]):
#     if sum(res)==k:
#         print(res)
#         return
#     if i==len(arr):
#         return
#     fun(arr,i+1,res+[arr[i]])   # TAKE----ADDING ELEMENT TO THE LIST 
#     fun(arr,i+1,res)     # NOT TAKE
# l=[1,2,3,4,8]
# k=8
# fun(l)



# def fun(arr,i,k):
#     if k==0:
#         return True
#     if i==0:
#         return False
#     if arr[i-1]>k:
#         return fun(arr,i-1,k)
#     return fun(arr,i-1,k) or fun(arr,i-1,k-arr[i-1])
# l=[1,2,3,8]
# k=7
# print(fun(l,len(l),k))


#FIND FREQUENCY OF ELEMENTS IN THE LIST [1,3,5,1,2,2,3,3,5,2,1]
    
        
# def fun(a,k,i=0):
#     if i==len(a):
#         return 0
#     if a[i]==k:
#         return 1+fun(a,k,i+1)
#     else:
#         return fun(a,k,i+1)
# l=[1,2,3,3,4]
# k=3
# print(fun(l,k))


# def freq(l,t,i=0):
#     if i==len(l):
#         return 0
#     if l[i]==t:
#         return 1+freq(l,t,i+1)
#     return freq(l,t,i+1)
# 
# l=[1,1,1,1,2,2,2,3]
# target=2
# print(freq(l,target))




# Dislike of Threes-----1560
#INPUT:
10
1
2
3
4
5
6
7
8
9
1000


t=int(input())
for _ in range(t):
    i=1
    count=0
    k=int(input())
    while(1):
        if i%3!=0 and i%10!=3:
            count+=1
            if count==k:
                print(i)
                break
        i+=1



   
