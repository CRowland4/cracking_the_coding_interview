# Write code to remove duplicates from an unsorted linked list.
from data_structure_classes.singly_linked_list import SingleNode


def remove_dups(head: SingleNode):
    """This solution uses a buffer"""
    dummy = SingleNode(nxt=head)
    prv = dummy
    cur = head

    vals = {}
    while cur:
        if cur.val in vals:
            prv.next = cur.next
        else:
            vals.add(cur.val)
            prv = cur

        cur = cur.next

    return


def remove_dups_no_buffer(head: SingleNode):
    """This solution doesn't use a buffer"""
    cur = head

    while cur:
        runner = cur.next
        while runner:
            if cur.val == runner.val:
                cur.next = runner.next

            runner = runner.next

        cur = cur.next

    return

