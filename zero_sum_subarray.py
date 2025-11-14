def sum_values(nums):
    if len(nums) == 0:
        return -1
    sum = 0
    for n in nums:
        sum += n
        print(sum)
    return sum

def zeroSumSubarray(nums):
    length = len(nums)
    if length == 0:
        return False

    for i in range(length):
        for j in range(length):
            sum = sum_values(nums[i:j+1])
            if sum == 0:
                print(f"True Sum = {sum}")
                return True
    return False

