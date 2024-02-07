"""
Given a singly linked list, remove the nth last node from the end of the list and return its head.
"""
# from linked_list import LinkedList
# from linked_list_node import LinkedListNode

def remove_nth_last_node(head, n):
    left = right = head

    for i in range(n):
        right = right.next

    if not right:
        return left.next

    while right.next:
        left = left.next
        right = right.next

    left.next = left.next.next

    return head

