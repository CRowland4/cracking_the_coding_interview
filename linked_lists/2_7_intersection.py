# Given two singly-linked lists, determine if the two lists intersect. Return the intersecting node. Note that the
#   intersection is based on reference, not value.
from data_structure_classes.singly_linked_list import SingleNode


def intersection(head1: SingleNode, head2: SingleNode) -> SingleNode | None:
    """First thought method, works"""
    nodes = set()

    cur1 = head1
    cur2 = head2
    while cur1 or cur2:
        if cur1 in nodes:
            return cur1
        else:
            nodes.add(cur1)
            cur1 = cur1.next

        if cur2 in nodes:
            return cur2
        else:
            nodes.add(cur2)
            cur2 = cur2.next

    return None


def intersection_no_node_set(head1: SingleNode, head2: SingleNode) -> SingleNode | None:
    """The idea here is that intersected singly-linked lists will share the same tail."""
    length1 = 0
    length2 = 0

    cur1 = head1
    cur2 = head2
    # Traverse to the end of each list and remember the lengths
    while cur1 or cur2:
        if cur1:
            length1 += 1
            cur1 = cur1.next
        if cur2:
            length2 += 1
            cur2 = cur2.next

    # If they don't end with the same tail, we know the two linked lists don't intersect
    if cur2 != cur1:
        return

    # Reset the head pointers
    cur1 = head1
    cur2 = head2

    length_difference = abs(length1 - length2)
    if length1 > length2:
        for _ in range(length_difference):
            cur1 = cur1.next
    if length2 > length1:
        for _ in range(length_difference):
            cur2 = cur2.next

    # Since we know there's an intersection, this can be an "infinite" loop
    while True:
        if cur1 is cur2:
            return cur1

        cur1 = cur1.next
        cur2 = cur2.next
