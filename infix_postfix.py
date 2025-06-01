def precedance(op):
    if op in ('+','-') :
        return 1
    if op in ('*','/'):
        return 2
    if op in ('^'):
        return 3
    return 0

def infix_postfix(expression):
    stack =[]
    postfix = []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char ==')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedance(stack[-1])>=precedance(char):
                postfix.append(stack.pop())
            stack.append(char)
            
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)


def infix_prefix(expression):
    expression = expression[::-1]
    stack = []
    prefix = []
    for char in expression:
        if char.isalnum():
            prefix.append(char)
        
        elif char == ')':
            stack.append(char)
        elif char=="(":
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedance(stack[-1])>precedance(char):
                prefix.append(stack.pop())
            stack.append(char)
    
    while stack:
        prefix.append(stack.pop())
    return ''.join(prefix[::-1])

expression ="(a+b)-c"
print("Postfix expression:",infix_postfix(expression))
print("Prefix expression:",infix_prefix(expression))