# Implement a function to check if a linked list is a palindrome
from data_structure_classes.singly_linked_list import SingleNode
from io import StringIO


def palindrome(head: SingleNode) -> bool:
    string_builder = StringIO()
    cur = head
    while cur:
        string_builder.write(str(cur.val))
        cur = cur.next

    value = string_builder.getvalue()
    return value == value[::-1]


if __name__ == "__main__":
    yes = SingleNode(1, SingleNode(2, SingleNode(3, SingleNode(2, SingleNode(1)))))
    no = SingleNode(1, SingleNode(7, SingleNode(3, SingleNode(2, SingleNode(1)))))
    print(palindrome(yes))
    print(palindrome(no))
