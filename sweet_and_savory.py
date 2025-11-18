def sweetAndSavory(dishes, target):
    # Write your code here.
    count = len(dishes)
    answer = [0,0]
    best = None
    i = 0
    j = 1
    for i in range(count - 1):
        for j in range(1, count):
            if i == j:
                continue
            first = dishes[i]
            second = dishes[j]
            if (first < 0 and second < 0) or (first > 0 and second > 0):
                continue
            current = first + second
            if current <= target:
                if best == None or current > best:
                    if first < 0:
                        answer = [first, second]
                    else:
                        answer = [second, first]
                    best = current
    return answer
