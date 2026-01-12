def insert_to_sorted(value, sorted_stack):
    if len(sorted_stack) == 0:
        sorted_stack.append(value)
        return sorted_stack
    temp = []
    
    while len(sorted_stack) > 0:
        next = sorted_stack.pop()
        if value > next:
            sorted_stack.append(next)
            sorted_stack.append(value)
            break
        else:
            temp.append(next)
    if len(sorted_stack) == 0:
        sorted_stack.append(value)
    while len(temp) > 0:
        sorted_stack.append(temp.pop())
    return sorted_stack

def sortStack(stack):
    temp = []
    while len(stack) > 0:
        temp.append(stack.pop())
    while len(temp) > 0:
        value = temp.pop()
        insert_to_sorted(value, stack)
    return stack
