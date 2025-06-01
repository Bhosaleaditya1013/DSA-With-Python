class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{new_node.data} - Pushed")
    
    def pop(self):
        if self.is_empty():
            print("Stack is Empty !!")
        else:
            element = self.top.data
            self.top = self.top.next
            print(f"{element} - Poped")
    
    def peek(self):
        if self.is_empty():
            print("Stack is Empty !!")
        else:
            element = self.top.data
            print(f"\n{element} <- Top element")
            
    def display(self):
        if self.is_empty():
            print("Stack is Empty !!")
        else:
            print("\nStack from top to bottom are : ")
            temp = self.top
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
                
    def is_palindrome(self,string):
        stack = []
        for char in string:
            stack.append(char)
        reversed_str = ''.join(stack.pop() for _ in range(len(stack)))
        # if (string==reversed_str):
        #     print("\nIt is Palindrome")
        # else:
        #     print("\nIt is Not palindrome")
        print("\nReversed string:",reversed_str)
    
    def evaluate_postfix(expression):
        stack = []
        for char in expression:
            if char.isdigit():
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(a - b)
                elif char == '*':
                    stack.append(a * b)
                elif char == '/':
                    stack.append(a / b)
        return stack[0]
           
sll = Stack()
sll.push(10)
sll.push(20)
sll.push(30)
sll.push(140)
sll.pop()
sll.peek()
sll.display()
sll.is_palindrome("adi")
sll.evaluate_postfix()
