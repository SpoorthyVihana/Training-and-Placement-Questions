#Count of Prime
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)




w=int(input())
if w%2!=0:
    print("No")
else:
    x=w//2
    if x%2==0:
        print(x,x)
    else:
        print(x-1,x+1)


x=int(input())
s=0
if x<5:
    print("1")
elif x%5==0:
    print(x//5)
else:
    print((x//5)+1)



n,m=map(int,input().split())
if n%m==0:
    print(n//m)
else:
    print((n//m)+(n%m))



a,b=map(int,input().split())
y=0
while a<=b:
    a*=3
    b*=2
    y+=1
print(y)



n,m,a,b=map(int,input().split())
if m*a<b:
    print(a*n)
else:
    print(((n//m)*b) + min((n%m)*a,b))

#Bitwise Operator
a=5
b=7
print(a^b)