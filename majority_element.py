def majorityElement(array):
    dict = {}

    for i in array:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    majority = None
    for i in dict:
        n = dict[i]
        if majority == None or n > dict[majority]:
            majority = i
    
    return majority
