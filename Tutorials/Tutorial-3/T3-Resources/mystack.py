def push(stack, value):
    stack.append(value)

def pop(stack):
    if isempty(stack):
        return None
    return stack.pop()

def isempty(stack):
    return len(stack) == 0

def peek(stack):
    if isempty(stack):
        return None
    return stack[len(stack) - 1]