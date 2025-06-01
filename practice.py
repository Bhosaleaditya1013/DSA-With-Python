class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singly:
    def __init__(self):
        self.head = None

    def display(self):
        trv  = self.head
        if trv is None:
            print("Linked List Is Empty")
        else:
            while trv is not None:
                print(trv.data,end = "-> ")
                trv = trv.next

    def insertfirst(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def delfirst(self):
        if self.head is None:
            print("List is Empty")
        else:
            self.head = self.head.next

    def insertlast(self,data):
        temp = Node(data)
        trv = self.head
        if trv.next is None:
            self.head = temp
        else:
            while trv.next is not None:
                trv = trv.next
            trv.next = temp

    def deletelast(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            trv = self.head
            if trv.next is None:
                self.head = None
            else:
                while trv.next.next is not None:
                    trv = trv.next
                trv.next = None           
                

obj = singly()
obj.insertfirst(45)
obj.insertfirst(15)
obj.insertfirst(20)
obj.insertlast(12)
obj.delfirst()
obj.deletelast()
obj.deletelast()
obj.display()