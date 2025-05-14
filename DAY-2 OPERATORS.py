# l=[10,10,10]
# print(id(l[0]))
# print(id(l[1]))
# print(id(l[2]))


# finding the even numbers in odd set (this is for finding the index values)
# l=[2,3,7,5,1,4,6,8,9]
# sum=0
# for i in range(len(l)):
#     if i%2!=0 and l[i]%2==0:
#         sum+=l[i]
# print(sum)

# finding the elements in the list
# l=list(map(int,input().split()))
# sum=0
# for i in l:
#     sum+=i
# print(sum)

# Finding the max numbers in the list
# l=list(map(int,input().split()))
# max=0
# count=0
# for i in l:
#     if i>max:
#         max=i
#         count+=1
# print(count)

# CodeForce4A problem 427A problem
# n=int(input())
# police=0
# unsolved=0
# event=list(map(int,input().split()))
# for e in event:
#     if e==-1:
#         if police>0:
#             police-=1
#         else:
#             unsolved+=1
#     else:
#         police+=e
# print(unsolved)

# Problem that the which candicate is ot the more votes (should consider the including no of voters and there ages and candicates#
#n=int(input())
#vote=list(map(int,input().split()))
#age=list(map(int,input().split()))
#c=max(vote)*[0]
#for i in range(n):
#   if age[i]>=18:
#        c[vote[i]-1]+=1
#m=max(c)
## print(max(c)) ## optional
# print(c.index(m)+1)
     ####### OR ##########
# n=int(input())
# vote=list(map(int,input().split()))
# age=list(map(int,input().split()))
# c=max(vote)*[0]
# for i in range(n):
#     if age[i]>=18:
#         c[vote[i]-1]+=1
# m=max(c)
# temp=sorted(c,reverse=True)
# if temp[0]==temp[1]:
#     print(-1)
# else:
#     print(c.index(temp[0])+1)

# Swaping two numbers without using temp and using AND , OR #
# a=6
# b=9
# a=a^b
# b=a^b
# a=a^b
# print("a =", a)
# print("b =", b)

### find even or odd using XOR and AND ###
# num=int(input("Enter a number: "))
# if (num&1)==0:  #if num ^ 1 == num + 1:
#     print("Even")
# else:
#     print("Odd")

#
# l=[1,2,3,4,5,6,7]
# for i in l:
#     l.remove(i)
# print(l)

######### Or #########

# l=[1,2,3,4,5,67,7]
# l.apend([1,2,3])
# l.extend(1,2)
# l.append(1)
# l.extend()
# print(l)

# 1^2^3^4^5
# n=int(input())
# if n%4==1:
#     print(1)
# if n%3==2:
#     print(n+1)
# if n%4==3:
#     print(0)
# if n%4==0:
#     print(n)


#1^2^3^4^5 without using for condition
# def XoR(n):
#     if n%4==1:
#         return 1
#     if n%4==2:
#         return n+1
#     if n%4==3:
#         return 0
#     if n%4==0:
#         return n
#         
# l=int(input())
# r=int(input())
# a=XoR(r)
# b=XoR(l-1)
# print(a^b)
