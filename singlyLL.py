
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singly:
    def __init__(self):
        self.head= None
    
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            trv = self.head
            while trv is not None:
                print(trv.data,end="-> ")
                trv= trv.next 
    
    def insertfirst(self,data):
        temp = Node(data)
        temp.next =  self.head
        self.head = temp
        
    def insertlast(self,data):
        temp = Node(data)
        trv = self.head
        if trv is None:
            self.head = temp
        else:
            while trv.next is not None:
                trv = trv.next
            trv.next=temp
            
    def deletefirst(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head = self.head.next
            
    def deletelast(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            trv = self.head
            while trv.next.next is not None :
                trv= trv.next
            trv.next = None
                         
    def reverse(self):
        prev = None
        trv = self.head
        while trv is not None:
            temp = trv.next  
            trv.next = prev       
            prev = trv            
            trv = temp 
        self.head = prev  
        print("\nReversed List:")
        self.display()    
        
obj = singly()
obj.insertfirst(10)
obj.insertfirst(55)
obj.insertfirst(30)
print("Linked List :")
obj.display()
obj.reverse()
# obj.display()