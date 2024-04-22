# Write code to partition a linked list around a value, x, such that all nodes less than x come before all noedes
#   greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements
#   less than x. The partition element x can appear anywhere in the "right partition"; it does not need to appear
#   between the left and the right partitions
from data_structure_classes.singly_linked_list import SingleNode, print_list, create_singly_linked_list


def partition(head: SingleNode, x: int) -> SingleNode:
    left = SingleNode()
    right = SingleNode()

    main = head
    curl = left
    curr = right
    while main:
        if main.val < x:
            curl.next = main
            curl = curl.next
            main = main.next
            curl.next = None
        else:
            curr.next = main
            curr = curr.next
            main = main.next
            curr.next = None

    curl.next = right.next
    return left.next


if __name__ == "__main__":
    start = create_singly_linked_list(15)
    print_list(start)
    print_list(partition(start, 9))
