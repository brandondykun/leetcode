# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Accepted Solution
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        curr = head
        temp = None
        head = None
        if curr and curr.val == val:
            while curr and curr.val and curr.val == val:
                temp = curr.next
                curr.next = None
                curr = temp

        head = curr
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


# Example i/o

# head = [1, 2, 6, 3, 4, 5, 6]
# val = 6
# output = [1, 2, 3, 4, 5]

# head = []
# val = 1
# output = []

# head = [7, 7, 7, 7]
# val = 7
# output = []
