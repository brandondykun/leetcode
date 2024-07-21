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

print("Tests - 19. Remove Nth Node From End of List: ")


def test_runner(
    input: Optional[List[int]], index: int, expected: Optional[List[int]]
) -> Optional[ListNode]:
    """Helper function to test different inputs/outputs.
    Convert input list to linked list, remove node at index,
    convert back to list and compare to expected list.
    """
    linked_list = sol.build_list(input)  # build input list
    removed = sol.removeNthFromEnd(linked_list, index)  # remove node
    output = sol.print_list(removed)  # convert linked list to list
    print(output == expected)  # assert correct output


#### Example 1:
input = [1, 2, 3, 4, 5]
n = 2
expected = [1, 2, 3, 5]
test_runner(input, n, expected)

#### Example 2:
input = [1]
n = 1
expected = []
test_runner(input, n, expected)

#### Example 3:
input = [1, 2]
n = 1
expected = [1]
test_runner(input, n, expected)

#### Example 4 (extra):
input = [1, 2, 3, 4, 5, 6, 7]
n = 4
expected = [1, 2, 3, 5, 6, 7]
test_runner(input, n, expected)

#### Example 5 (extra):
input = [1, 2]
n = 2
expected = [2]
test_runner(input, n, expected)

#### Example 6 (extra):
input = [1, 2, 3]
n = 3
expected = [2, 3]
test_runner(input, n, expected)
