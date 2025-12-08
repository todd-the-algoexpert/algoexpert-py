def minNumberOfCoinsForChange(n, denoms):
    if n == 0:
        return 0
    if len(denoms) == 0:
        return -1
    denoms.sort(reverse=True)
    coin = denoms[0]
    answer = -1
    if coin > n:
        answer = minNumberOfCoinsForChange(n, denoms[1:])
    elif coin <= n:
        included = minNumberOfCoinsForChange(n - coin, denoms)
        if included != -1:
            included += 1
        skipped = minNumberOfCoinsForChange(n, denoms[1:])
        if included == -1:
            answer = skipped
        elif skipped == -1:
            answer = included
        else:
            if included < skipped:
                return included
            else:
                return skipped
    return answer
