class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class cirularLL:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("Linked List Is empty")
        else:
            trv = self.head
            while trv.next is not self.head:
                print(trv.data,end="-> ")
                trv = trv.next
            print(trv.data)
                
    def insertfirst(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            temp.next = self.head
        else:
            trv =self.head
            while trv.next is not self.head:
                trv= trv.next
            temp.next = self.head
            self.head = temp
            trv.next = self.head
            
    def insertlast(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            temp.next = self.head
        else:
            trv = self.head
            while trv.next is not self.head:
                trv = trv.next
            trv.next = temp
            temp.next = self.head
            
    def deletefirst(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            trv = self.head
            while trv.next is not self.head:
                trv= trv.next
            trv.next = self.head.next
            self.head = self.head.next
            
    def deletelast(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            trv = self.head
            while trv.next.next is not self.head:
                trv= trv.next
            trv.next =self.head

obj = cirularLL()
obj.insertfirst(20)
obj.insertfirst(40)
obj.insertfirst(50)
obj.deletefirst()
obj.deletelast()
obj.display()              