class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} - Enqueued")
            
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty !!")
        else:
            elt = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(f"\n{elt} - Dequeued")
    
    def peek(self):
        if self.is_empty():
            print("Queue is Empty !!")
        else:
            eltfront = self.front.data
            eltrear = self.rear.data 
            print(f"\n{eltfront} <- Front Element")
            print(f"{eltrear} <- Rear Element\n")
            
    def display(self):
        if self.is_empty():
            print("Queue is Empty !!")
        else:
            print("\nThe Queue is : ")
            temp = self.front
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print()
            
qll = Queue()
qll.enqueue(10)
qll.enqueue(20)
qll.enqueue(30)
qll.enqueue(40)
qll.dequeue()
qll.peek()
qll.display()

