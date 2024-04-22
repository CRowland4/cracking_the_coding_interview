import random


class SingleNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def print_list(head: SingleNode):
    main = head
    while main:
        print(main.val, end=" -> ")
        main = main.next

    print()
    return


def create_singly_linked_list(length: int) -> SingleNode:
    """Creates a singly-linked list of length <length> and returns the head"""
    head = SingleNode(random.randint(1, 15))
    cur = head
    for _ in range(length - 1):
        cur.next = SingleNode(random.randint(1, 15))
        cur = cur.next

    return head
