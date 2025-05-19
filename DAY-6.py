#Bubble Sort
arr=[5,1,4,9,2,6,8]
for i in range(len(arr)):
    flag=False
    for j in range(i+1,len(arr)):
        if arr[j]<arr[i]:
            arr[i],arr[j]=arr[j],arr[i]
            flag=True
    if not flag:
        break
print(arr)


#Insertion Sort
arr=[3,6,1,5,9,2]
min_ind=arr[0]
for i in range(0,len(arr)):
    min_ind=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_ind]:
            min_ind=j
    arr[i],arr[min_ind]=arr[min_ind],arr[i]
print(arr)


#Selection sort
arr=[10,40,30,20,50]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)


#Input:[3,6,1,7,4,2,5] Output:[6,4,2,1,3,5,7]            
a = [3, 6, 1, 7, 4, 2, 5]
a.sort()
b=[]
for i in a:
    if i%2!=0:
        b.append(i)
    else:
        b.insert(0,i)
print(b)


#Largest Number in a list
a=[7,2,3,6,1]     #Bruteforce approach
a.sort()
print(a[-1])
a=[7,2,3,6,1]     #Optimized code
m=a[0]
for i in a:
    if i>m:
        m=i
print(m)


#Second Largest element in a list
a=[7,2,3,6,1]
l=sl=0
for i in a:
    if i>l:
        sl,l=l,i
    elif i>sl and i!=l:
        sl=i
print(sl)


#K-th Largest Number in a list
l=[7,2,3,6,1]
k=3
for i in range(k):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l[-k])


#Input:[2,3,5,1,6,9,8] Output:[2,3,1,5,6,9,8]
a=[2,3,5,6,7,9,8]
k=2
for i in (k,len(a)):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)


#Input:[[1,2],[5,1],[2,4],[6,3]] Output:[[5,1],[1,2],[6,3],[2,4]]
a=[[1,2],[5,1],[2,4],[6,3]]
for i in range(len(a)):
    for j in range(0,len(a)-1-i):
        if a[j][1]>a[j+1][1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)


#Input:[[20,12,11],[10,5,22],[16,7,30]]
def pri(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
            return i
    return None
a=[[20,12,11],[10,5,22],[16,7,30]]
b=[]
n=len(a)
for i in a:
    b.append(pri(i))
for i in range(n):
    for j in range(0,len(a)-1-i):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
print(a)


#Sorting strings based on length 
a=["abc","hsahjhd","ha","hjajh"]
res=sorted(a,key=len)
print(res)


#Sorting based on frequency
a="baabaaccc"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
sc=sorted(b.items(),key=lambda item:item[1])
res=""
for c,count in sc:
    res+=c*count
print(res)


#Input:[[1,0,0,1],[1,0,0,0],[0,0,1,0],[0,1,1,0]] Output:[9,5,3,13]
a=[[1,0,0,1],[1,0,0,0],[0,0,1,0],[0,1,1,0]]
b=[5,10,3,4]
for i in a:
    s=0
    for j in range(len(i)):
        if i[j]==1:
            s+=b[j]
    print(s)