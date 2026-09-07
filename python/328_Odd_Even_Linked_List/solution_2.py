from typing import Optional

from leetcode_utils.linked_list import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        even_head = head.next
        odd_curr = None
        even_curr = None
        index = 1

        while curr:
            if index % 2 == 0:
                if not even_curr:
                    even_curr = curr
                else:
                    even_curr.next = curr
                    even_curr = curr
            else:
                if not odd_curr:
                    odd_curr = curr
                else:
                    odd_curr.next = curr
                    odd_curr = curr

            curr = curr.next
            index += 1

        if odd_curr:
            odd_curr.next = even_head
        if even_curr:
            even_curr.next = None
        return head
