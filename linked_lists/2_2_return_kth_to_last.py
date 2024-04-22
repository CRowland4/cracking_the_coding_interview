# Implement an algorithm to find the kth to last element of a singly linked list
from data_structure_classes.singly_linked_list import SingleNode


def kth_to_last(head: SingleNode, k: int) -> SingleNode:
    """Using a buffer, not really optimal and kinda defeats the purpose of the linked list"""
    node_pointers = {}
    next_num = 1

    current = head
    while current:
        node_pointers[next_num] = current
        current = current.next
        next_num += 1

    return node_pointers[max(node_pointers.keys()) - (k - 1)]


def kth_to_last_no_buffer(head: SingleNode, k: int) -> SingleNode | None:
    first_counter = 0
    cur = head
    while cur:
        first_counter += 1
        cur = cur.next

    second_counter = 0
    cur = head
    while cur:
        second_counter += 1
        if second_counter == first_counter - k + 1:
            return cur

    return  # This would mean k was greater than the length of the list
