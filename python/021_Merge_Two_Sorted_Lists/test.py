"""Merge Two Sorted Lists Tests

This file is to test the functionality of the Solution.mergeTwoLists() method.

A helper class (TestHelper) has been defined to facilitate testing.

TestHelper class adds methods to the Solution class to build and print linked lists.
It does not modify the mergeTwoLists method, and is only used for testing.
"""

from typing import List
from solution import Solution, ListNode


class TestHelper(Solution):
    def build_list(self, lst: list) -> ListNode:
        """Build a linked list from a list input."""
        head = None
        curr = None

        if len(lst):
            for item in lst:
                if not head:
                    head = ListNode(val=item)
                    curr = head
                else:
                    new_node = ListNode(val=item)
                    curr.next = new_node
                    curr = new_node

        return head

    def print_list(self, head: ListNode) -> List:
        """Convert linked list to a list by passing the linked list head node."""
        curr = head
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next

        return output


sol = TestHelper()

print("Tests - 21. Merge Two Sorted Lists: ")

#### Example 1:
output = [1, 1, 2, 3, 4, 4]  # expected output
list1 = sol.build_list([1, 2, 4])  # build first linked list
list2 = sol.build_list([1, 3, 4])  # build second linked list
merged = sol.mergeTwoLists(list1, list2)  # merge the lists
print(sol.print_list(merged) == output)  # assert correct output

#### Example 2:
output = []  # expected output
list1 = sol.build_list([])  # build first linked list
list2 = sol.build_list([])  # build second linked list
merged = sol.mergeTwoLists(list1, list2)  # merge the lists
print(sol.print_list(merged) == output)  # assert correct output

#### Example 3:
output = [0]  # expected output
list1 = sol.build_list([])  # build first linked list
list2 = sol.build_list([0])  # build second linked list
merged = sol.mergeTwoLists(list1, list2)  # merge the lists
print(sol.print_list(merged) == output)  # assert correct output
