class Node:
    def __init__(self,data):
        self.prev =None
        self.data = data
        self.next =None
        
class double:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            trv =  self.head
            while trv is not None:
                print(trv.data,end= " -> ")
                trv = trv.next
    
    def insertfirst(self,data):
        temp = Node(data)
        if self.head is None:
            self.head= temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            
    def insertlast(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            trv = self.head
            while trv.next is not None:
                trv= trv.next
            trv.next = temp
            temp.prev = trv
            
    def deletefirst(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head =None
        else:
            self.head= self.head.next
            self.head.prev =None
            
    def deletelast(self):
        if self.head is None:
            print("List is Empty")
        else:
            if self.head.next is None:
                self.head = None
                return
            
            trv = self.head
            while trv.next is not None:
                trv = trv.next
            trv.prev.next = None
            
    def sort(self):
        if self.head is None:  # If the list is empty
            return

        trv = self.head
        while trv is not None:
            index = trv.next
            while index is not None:
                if trv.data > index.data:
                    temp = trv.data
                    trv.data = index.data
                    index.data = temp
                index = index.next
            trv = trv.next
        
obj = double()
# obj.deletefirst()
obj.insertfirst(20)
obj.insertfirst(20)
obj.insertlast(50)
obj.insertlast(69)
obj.insertlast(920)
obj.insertlast(30)
# obj.deletefirst()
# obj.deletefirst()
# obj.deletelast()
obj.sort()
obj.display()