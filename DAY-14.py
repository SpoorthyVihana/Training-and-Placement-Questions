#Intersection of two linked lists
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         i=headA
#         j=headB
#         while i!=j:
#             if i:
#                 i=i.next
#             else:
#                 i=headB
#             if j:
#                 j=j.next
#             else:
#                 j=headA
#         return i
    
    
#Reverse a linked list
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         pre=None
#         c=head
#         while c!=None:
#             nn=c.next
#             c.next=pre
#             pre=c
#             c=nn
#         return pre
    

#Plaindrome in linked list
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         slow,fast=head,head
#         while (fast!=None and fast.next!=None):
#             slow=slow.next
#             fast=fast.next.next
#         pre=None
#         c=slow
#         while c!=None:
#             temp=c.next
#             c.next=pre
#             pre=c
#             c=temp
#         l,r=head,pre
#         while r!=None:
#             if l.val!=r.val:
#                 return False
#             l=l.next
#             r=r.next
#         return True


#Bubble Sort in linked list
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
    def bubble(self):
        e=None  
        while self.head.next!=e:
            c=self.head
            while c.next!=e:  
                if c.data>c.next.data:
                    c.data,c.next.data=c.next.data,c.data  
                c=c.next
            e=c  
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
l1=Linked_list()
l1.head=Node(10)
l1.append(20)
l1.append(30)
l1.append(5)
l1.display()
l1.bubble()
l1.display()


#Add two numbers using a linked list
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         temp2=ListNode()
#         temp=temp2
#         c=0
#         while l1 or l2 or c:
#             s=c
#             if l1:
#                 s+=l1.val
#                 l1=l1.next
#             if l2:
#                 s+=l2.val
#                 l2=l2.next
#             c=s//10
#             temp.next=ListNode(s%10)
#             temp=temp.next
#         return temp2.next
    

# Merge Sort in linked list
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
    def merge(self):
        e=None  
        while self.head.next!=e:
            c=self.head
            while c.next!=e:  
                if c.data>c.next.data:
                    c.data,c.next.data=c.next.data,c.data  
                c=c.next
            e=c  
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
l1=Linked_list()
l1.head=Node(4)
l1.append(6)
l1.append(3)
l1.append(1)
l1.display()
l1.merge()
l1.display()


#Valid Parentheses
def isValid(s):
    st=[]
    for i in s:
        if i in "({[":
            st.append(i)
        else:
            if not st:
                return False
            l=st.pop()
            if l=='(':
                if i!=')':
                    return False
            elif l=='{':
                if i!='}':
                    return False
            elif l=='[':
                if i!=']':
                    return False
    return not st
s="()[]{}"
print(isValid(s))


#Removing stars from a string
def removeStars(s):
    st=[]
    for i in s:
        if i=="*":
            st.pop()
        else:
            st.append(i)
    return "".join(st)
s="leet**cod*e"
print(removeStars(s))


#Number of students unable to eat lunch
def countStudents(students,sandwiches):
    c=len(students)
    while students and sandwiches and sandwiches[0] in students:
        if students[0]!=sandwiches[0]:
            students.append(students[0])
            students.pop(0)
        else:
            students.pop(0)
            sandwiches.pop(0)
            c-=1
    return c
students=[1,1,1,0,0,1]
sandwiches=[1,0,0,0,1,1]
print(countStudents(students,sandwiches))