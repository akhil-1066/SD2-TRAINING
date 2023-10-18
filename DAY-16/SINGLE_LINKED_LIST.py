class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class List:
    def __init__(self):
        self.head=None
    def insertAtBegin(self,val):
        if not self.head:
            self.head=node(val)
        else:
            new=node(val)
            new.next=self.head
            self.head=new
    def insertAtEnd(self,val):
        if not self.head:
            self.head=node(val)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node(val)
    def display(self):
        temp=self.head
        while temp:
            print(temp.val,end='->')
            temp=temp.next
        print('None')
    def deleteAtBegin(self):
        if not self.head:
            return 'List is empty'
        else:
            val=self.head.val
            self.head=self.head.next
            return val
    def deleteAtEnd(self):
        if not self.head:
            return 'List is empty'
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            val=temp.next.val
            temp.next=None
            return val
l=List()
lst=[9,4,1,6,2,8,6,1,3]
for i in lst:
    l.insertAtEnd(i)
l.display()
temp=l.head
while temp.next:
    t=temp.next
    while t:
        if temp.val>t.val:
            temp.val,t.val=t.val,temp.val
        t=t.next
    temp=temp.next
l.display()