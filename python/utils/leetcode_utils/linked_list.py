from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class LinkedListUtil:
    @staticmethod
    def build_list(lst: list[int]) -> Optional[ListNode]:
        """Build a linked list from a list input."""
        if not lst:
            return None

        head = ListNode(val=lst[0])
        curr = head
        for item in lst[1:]:
            new_node = ListNode(val=item)
            curr.next = new_node
            curr = new_node

        return head

    @staticmethod
    def to_list(head: Optional[ListNode]) -> List[int]:
        """Convert linked list to a list by passing the linked list head node."""
        if not head:
            return []

        curr = head
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next

        return output
