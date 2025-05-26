#SUM OF ALL THE ELEMENTS IN A LINKED LIST


# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
# class Linked_list:
#     def _init_(self):
#         self.head=None
#     def append(self,val):
#         temp=self.head
#         while temp.next!=None:
#             temp=temp.next
#         temp.next=Node(val)
#     def k_from_last(self,k):
#         slow=self.head
#         fast=self.head
#         for i in range(k):
#             fast=fast.next
#         while fast!=None:
#             fast=fast.next
#             slow=slow.next
#         print(slow.data)
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")
#     def sum1(self):
#         temp=self.head
#         t=0
#         while temp!=None:
#             t+=temp.data
#             temp=temp.next
#         return t
#     def count(self):
#         temp=self.head
#         c=0
#         while temp!=None:
#             c+=1
#             temp=temp.next
#         return c
#     def evensum(self):
#         temp=self.head
#         t=0
#         while temp!=None:
#             if temp.data%2==0:
#                 t+=temp.data
#             temp=temp.next
#         return t
#     def oddsum(self):
#         temp=self.head
#         t=0
#         while temp!=None:
#             if temp.data%2!=0:
#                 t+=temp.data
#             temp=temp.next
#         return t
#     def even_insum(self):
#         temp=self.head
#         i=0
#         t=0
#         while temp:
#             if i%2==0:  
#                 t+=temp.data
#             temp=temp.next
#             i+=1
#         return t
#     def odd_insum(self):
#         temp=self.head
#         i=0
#         t=0
#         while temp:
#             if i%2!=0:  
#                 t+=temp.data
#             temp=temp.next
#             i+=1
#         return t
#     def largest(self):
#         temp=self.head
#         m=temp.data
#         while temp is not None:
#             if temp.data>m:
#                 m=temp.data
#             temp=temp.next
#         return m
#     def second_largest(self):
#         temp=self.head
#         m=temp.data
#         sl=None
#         temp=temp.next
#         while temp:
#             if temp.data>m:
#                 sl=m
#                 m=temp.data
#             elif sl is None or temp.data>sl:
#                 sl=temp.data
#             temp=temp.next
#         return sl
#     def mid(self):
#         temp=self.head
#         temp2=self.head
#         c=0
#         while temp!=None:
#             c+=1
#             temp=temp.next
#         m=c//2
#         for i in range(m):
#             temp2=temp2.next
#         return temp2.data
# l1=Linked_list()
# l1.head=Node(10)
# l1.append(20)
# l1.append(30)
# l1.append(5)
# l1.display()
# print(l1.sum1())
# print(l1.count())
# print(l1.evensum())
# print(l1.oddsum())
# print(l1.even_insum())
# print(l1.odd_insum())
# print(l1.largest())
# print(l1.second_largest())
# print(l1.mid())
# 

#  Remove Nth Node From End of List


class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def append(self,val):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(val)
    def klast(self,k):
        temp=Node(0)
        temp.next=self.head
        fast=temp
        slow=temp
        for i in range(k+1):
            if fast:
                fast=fast.next
            else:
                return self.head
        while fast!=None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return temp.next
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
l2=Linked_list()
l2.head=Node(3)
l2.append(2)
l2.append(0)
l2.append(-4)
k=2
l2.klast(k)
l2.display()


#Find if k is the sum of two consecutive nodes in the linked list


class Node:
    def _init_(self,val):
        self.data=val
        self.next=None
class Linked_list:
    def _init_(self):
        self.head=None
    def append(self,val):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(val)
    def sum1(self,k):
        temp=self.head
        s=0
        flag=0
        while temp.next!=None:
            if temp.data+temp.next.data==k:
                flag=1
            temp=temp.next
        if flag==1:
            return True
        return False
l2=Linked_list()
l2.head=Node(3)
l2.append(2)
l2.append(0)
l2.append(4)
k=5
print(l2.sum1(k))


#Find if k is the sum of any two nodes in the linked list


class Node:
    def _init_(self,val):
        self.data=val
        self.next=None
class Linked_list:
    def _init_(self):
        self.head=None
    def append(self,val):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(val)
    def sum1(self,k):
        s=set()
        temp=self.head
        while temp!=None:
            if k-temp.data in s:
                return True
            s.add(temp.data)
            temp=temp.next
        return False
l2=Linked_list()
l2.head=Node(3)
l2.append(2)
l2.append(0)
l2.append(4)
k=6
print(l2.sum1(k))



   

