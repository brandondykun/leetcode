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

    def print_list(self, head: Optional[ListNode]) -> List:
        """Convert linked list to a list by passing the linked list head node."""
        if not head:
            return []

        curr = head
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next

        return output


sol = TestHelper()

print("Tests - 206. Reverse Linked List: ")


def test_runner(
    input: Optional[List[int]], expected: Optional[List[int]]
) -> Optional[ListNode]:
    """Helper function to test different inputs/outputs.
    Convert input list to linked list, reverse the linked list,
    convert back to list and compare to expected list.
    """
    linked_list = sol.build_list(input)  # build input list
    reversed = sol.reverseList(linked_list)  # reverse list
    output = sol.print_list(reversed)  # convert linked list to list
    print(output == expected)  # assert correct output


#### Example 1:
input = [1, 2, 3, 4, 5]
expected = [5, 4, 3, 2, 1]
test_runner(input, expected)

#### Example 2:
input = [1, 2]
expected = [2, 1]
test_runner(input, expected)

#### Example 3:
input = []
expected = []
test_runner(input, expected)

#### Example 4 (extra):
input = [1, 2, 3, 4, 5, 6, 7]
expected = [7, 6, 5, 4, 3, 2, 1]
test_runner(input, expected)

#### Example 5 (extra):
input = [1]
expected = [1]
test_runner(input, expected)
