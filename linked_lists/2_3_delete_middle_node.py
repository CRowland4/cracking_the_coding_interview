# Implement an algorithm to delete a node in the middle (i.e, any node but the first and last node, not necessarily the
#   exact middle) of a singly linked list, given only access to that node
from data_structure_classes.singly_linked_list_node import SingleNode


def delete_middle(node: SingleNode):
    node.val = node.next.val
    node.next = node.next.next
    return


# NOTE: This problem would be impossible if we were supposed to delete the last node while only having access to the
#           last node
