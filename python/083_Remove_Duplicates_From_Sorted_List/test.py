"""Remove Duplicates From Sorted List Tests

This file is to test the functionality of the Solution.deleteDuplicates() method.

A helper class (TestHelper) has been defined to facilitate testing.

TestHelper class adds methods to the Solution class to build and print linked lists.
It does not modify the deleteDuplicates method, and is only used for testing.
"""

from typing import List, Optional
from solution import Solution, ListNode


class TestHelper(Solution):
    def build_list(self, lst: list) -> ListNode:
        """Build a linked list from a list input."""
        head = None
        curr = None

        if lst and len(lst):
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
        if not head:
            return None

        curr = head
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next

        return output


sol = TestHelper()

print("Tests - 83. Remove Duplicates From Sorted List: ")


def test_runner(
    input: Optional[List[int]], expected: Optional[List[int]]
) -> Optional[ListNode]:
    """Helper function to test different inputs/outputs.
    Convert input list to linked list, remove duplicates,
    convert back to list and compare to expected list.
    """
    linked_list = sol.build_list(input)  # build input list
    removed = sol.deleteDuplicates(linked_list)  # remove duplicates
    output = sol.print_list(removed)  # convert linked list to list
    print(output == expected)  # assert correct output


#### Example 1:
input = [1, 1, 2]  # input to build list
expected = [1, 2]  # expected output
test_runner(input, expected)

#### Example 2:
input = [1, 1, 2, 3, 3]  # input to build list
expected = [1, 2, 3]  # expected output
test_runner(input, expected)

#### Example 3 (extra):
input = None  # input to build list
expected = None  # expected output
test_runner(input, expected)

#### Example 4 (extra):
input = [-10, -4, -4, -4, -1, 0, 1, 4, 6, 8, 8, 9, 9, 10, 10]  # input to build list
expected = [-10, -4, -1, 0, 1, 4, 6, 8, 9, 10]  # expected output
test_runner(input, expected)

#### Example 5 (extra):
input = [1, 1, 1, 1, 1, 1, 1, 1, 1]  # input to build list
expected = [1]  # expected output
test_runner(input, expected)

#### Example 6 (extra):
input = [1]  # input to build list
expected = [1]  # expected output
test_runner(input, expected)
