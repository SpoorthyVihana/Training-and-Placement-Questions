
#                                             RECURSION


# PRINT 123454321


def recurssion(n, i=1):
    if i>n:
        return
    print(i,end=" ")
    recurssion(n,i+1)
    if i<n:
        print(i,end=" ")
recurssion(5)


#5 4 3 2 1


def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n,end=" ")
n=5
fun(n)


# 1 2 3 4


def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
n=5
fun(n)


def fun(n):
    if n==0:
        return 200
    print(n,end=" ")
    return fun(n-1)

n = 5
result = fun(n)
print(result)

# PRINT 5 4 3 2 1 1 2 3 4 5 

    
def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
    print(n,end="  ")
n=int(input())
fun(n)


# PRINT 5 4 3 2 1 2 3 4 5

def fun(n):
    if n==0:
        return
    print(n, end=" ")
    fun(n-1)
    if n!=1:
        print(n,end=" ")
n=int(input())
fun(n)

#PRINT ODD AND EVEN NUMBERS

def fun(n):
    if n==0:
        return
    if n%2!=0:
        print(n,end=" ")  
    fun(n-1)
    if n!=1:
        if n%2!=0:
            print(n,end=" ") 
n = int(input())
fun(n)


# PRINT 1 2 3 4 5 5  4  3  2  1

def fun(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    fun(n,m+1)
    print(m+1,end="  ")
n=5
fun(n)


# FACTORIAL USING RECURSSION


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
x=int(input())
print(fact(x))
 
 
# GIVEN NUMBER IS PRIME OR NOT


def is_prime(num, i=2):
    if i * i > n:
        return True
    if num % i==0:
        return False
    return is_prime(num, i+1)
n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime Number")
else:
    print("Not a Prime Number")
     
     
# FIBONACCI SERIES
 
 
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
x=int(input())
print(fib(x))
 
 
# REVERSE OF A NUMBER


def reverse(n,res=0):
    if n==0:
        return res
    else:
        d=n%10
        res=res*10+d
        return reverse(n//10,res)
n=int(input())
print(reverse(n))


#PALINDROME


def is_palindrome(n, rev=0):
    if n == 0:
        return rev
    rev = rev * 10 + n % 10
    return is_palindrome(n // 10, rev)

num = int(input("Enter a number: "))
if is_palindrome(num) == num:
    print(num, "is a Palindrome")
else:
    print(num, "is Not a Palindrome")


#OPTIMIZED PRIME OR NOT


n=int(input())
flag=0
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        flag+=1
        break
if flag==0:
        print("prime")
else:
        print("not prime")


# N=15 reduce the num to 1 if it is odd num add 1 or reduce 1 if it is even divide by 2 find the minimum steps to reach 1   


def min_steps(n):
    if n==1:
        return 0
    if n%2==0:
        return 1 + min_steps(n//2)
    return 1 + min(min_steps(n-1), min_steps(n+1))
n = 15
print("Minimum steps to reach 1:", min_steps(n))



#Sum of all the elements in a list using recurssion

 
def Sum(l,i=0):
    if i==len(l):
        return 0
    return l[i] + Sum(l,i+1)
l=[1, 2, 3, 4, 5]
print(Sum(l))

#count of all prime numbers using recursion


def prime(n,i=2):
    if i*i>n:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)

def fun(l,i=0):
    if i==len(l):
        return 0
    if prime(l[i]):
        return 1+fun(l,i+1)
    else:
        return fun(l,i+1)

l=[11,4,3,6,5]
print(fun(l))
            

#Reverse the list using recursion


def rev(l):
    if not l:
        return []
    return rev(l[1:]) + [l[0]]
n= [1, 2, 3, 4, 5]
print(rev(n))









