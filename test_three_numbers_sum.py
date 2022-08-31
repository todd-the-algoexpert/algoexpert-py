def three_number_sum(array, targetSum):
    size = len(array)
    if size < 3:
        return []
    triplets = []
    for i in range(0, len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                if (array[i] + array[j] + array[k]) == targetSum:
                    triplet = [array[i], array[j], array[k]]
                    triplet.sort()
                    triplets.append(triplet)
    triplets.sort()
    return triplets


def test_base_case():
    assert three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
