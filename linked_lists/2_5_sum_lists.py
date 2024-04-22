# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in
#   reverse order, such that the 1s digit is at the head of the list. Write a function that adds the two numbers and
#   returns the sum as a linked list
from data_structure_classes.singly_linked_list import SingleNode, print_list


def sum_lists(num1: SingleNode, num2: SingleNode) -> SingleNode:
    result = SingleNode()
    result_head = result

    carry = 0
    one = num1
    two = num2
    while one and two:
        place = one.val + two.val + carry
        carry = 0
        if place >= 10:
            carry = 1
            result.next = SingleNode(place - 10)
        else:
            result.next = SingleNode(place)

        one = one.next
        two = two.next
        result = result.next

    last = None
    if one:
        last = one
    elif two:
        last = two

    while last:
        place = last.val + carry
        carry = 0
        if place >= 10:
            carry = 1
            result.next = SingleNode(place - 10)
        else:
            result.next = SingleNode(place)

        last = last.next
        result = result.next

    if carry:
        result.next = SingleNode(1)

    return result_head.next


if __name__ == "__main__":
    first = SingleNode(7, SingleNode(1, SingleNode(6, SingleNode(4, SingleNode(8, SingleNode(9))))))
    second = SingleNode(5, SingleNode(9, SingleNode(2)))
    print_list(first)
    print_list(second)
    print()
    print_list(sum_lists(first, second))
