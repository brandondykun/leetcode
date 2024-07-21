from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes: list[ListNode] = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        index_to_remove = len(nodes) - n
        node_to_remove = nodes[index_to_remove]
        prev_node_index = index_to_remove - 1

        if prev_node_index >= 0:
            prev_node = nodes[prev_node_index]
            next_node = node_to_remove.next
            prev_node.next = next_node
        else:
            head = node_to_remove.next

        return head
