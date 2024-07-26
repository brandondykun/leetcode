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

print("Tests - 61. Rotate List: ")


def test_runner(
    input: Optional[List[int]], k: int, expected: Optional[List[int]]
) -> Optional[ListNode]:
    """Helper function to test different inputs/outputs.
    Convert input list to linked list, rotate list,
    convert back to list and compare to expected list.
    """
    linked_list = sol.build_list(input)  # build input list
    removed = sol.rotateRight(linked_list, k)  # rotate list
    output = sol.print_list(removed)  # convert linked list to list
    print(output == expected)  # assert correct output


#### Example 1:
input = [1, 2, 3, 4, 5]
k = 2
expected = [4, 5, 1, 2, 3]
test_runner(input, k, expected)

#### Example 2:
input = [0, 1, 2]
k = 4
expected = [2, 0, 1]
test_runner(input, k, expected)

#### Example 3 (extra):
input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 7
expected = [3, 4, 5, 6, 7, 8, 9, 1, 2]
test_runner(input, k, expected)

#### Example 4 (extra):
input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 0
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_runner(input, k, expected)

#### Example 5 (extra):
input = [1]
k = 4
expected = [1]
test_runner(input, k, expected)

#### Example 6 (extra):
input = []
k = 4
expected = []
test_runner(input, k, expected)

#### Example 7 (extra):
input = [1, 2]
k = 7
expected = [2, 1]
test_runner(input, k, expected)

#### Example 8 (extra):
input = [1]
k = 0
expected = [1]
test_runner(input, k, expected)

#### Example 9 (extra):
input = [1, 2, 3, 4, 5]
k = 1
expected = [5, 1, 2, 3, 4]
test_runner(input, k, expected)
