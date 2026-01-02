def nextGreaterElement(array):
    result = []
    length = len(array)
    
    for i in range(length):
        j = i + 1
        if j == length:
            j = 0
        current = array[i]
        while j != i:
            next = array[j]
            if next > current:
                result.append(next)
                break
            j += 1
            if j == length:
                print(j)
                j = 0
        if j == i:
            result.append(-1)
        
    return result
