import pytest
from exercise import Node, reverse

# @pytest.mark.skip(reason="Finish the problem before you run this!")
def test_reverse():
    llist = Node(1, Node(2, Node(3, Node(4))))
    assert reverse(llist).data == 4
    assert reverse(llist).next.data == 3
    assert reverse(llist).next.next.data == 2
    assert reverse(llist).next.next.next.data == 1