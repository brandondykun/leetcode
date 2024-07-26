from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        nodes: List[ListNode] = []

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        rotations = k % len(nodes)

        if rotations == 0:
            return head

        new_head_index = len(nodes) - rotations
        new_tail_index = new_head_index - 1

        nodes[new_tail_index].next = None
        nodes[-1].next = nodes[0]

        return nodes[new_head_index]
