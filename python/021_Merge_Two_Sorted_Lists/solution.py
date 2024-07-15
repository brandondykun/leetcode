from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None and list2 != None:
            return list2
        if list2 == None and list1 != None:
            return list1

        list1_curr = list1
        list2_curr = list2
        head = None
        tail = None

        if list2_curr.val <= list1_curr.val:
            head = list2_curr
            tail = list2_curr
            list2_curr = list2_curr.next
        else:
            head = list1_curr
            tail = list1_curr
            list1_curr = list1_curr.next

        while list1_curr != None and list2_curr != None:
            if list2_curr.val <= list1_curr.val:
                tail.next = list2_curr
                tail = list2_curr
                list2_curr = list2_curr.next
            else:
                tail.next = list1_curr
                tail = list1_curr
                list1_curr = list1_curr.next

        if list1_curr == None:
            tail.next = list2_curr
        else:
            tail.next = list1_curr

        return head
