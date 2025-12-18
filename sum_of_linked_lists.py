# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sum = linkedListOne.value + linkedListTwo.value
    next_one = linkedListOne.next
    next_two = linkedListTwo.next
    carry_one = sum > 9
    next_value = sum % 10
    sum_list = LinkedList(next_value)
    head_sum_list = sum_list
    while next_one != None or next_two != None:
        if next_one != None and next_two:
            sum = next_one.value + next_two.value
            next_one = next_one.next
            next_two = next_two.next
        elif next_one != None:
            sum = next_one.value
            next_one = next_one.next
        else:
            sum = next_two.value
            next_two = next_two.next
        if carry_one:
            sum += 1
        carry_one = sum > 9
        next_value = sum % 10
        sum_list.next = LinkedList(next_value)
        sum_list = sum_list.next

    if carry_one:
        sum_list.next = LinkedList(1)
        sum_list = sum_list.next
    
    return head_sum_list
