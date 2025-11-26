def isValidSubsequence(array, sequence):
    i = 0
    
    for n in array:
        n_from_sequence = sequence[i]
        if n_from_sequence == n:
            i += 1
        if i == len(sequence):
            return True
            
    return False
