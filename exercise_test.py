import pytest 
from exercise import Node, reverse

# @pytest.mark.skip(reason= "not made yet")
def test_reverse():
    llist = Node(1,Node(2,Node(3,Node(4))))
    reversed_llist = reverse(llist)
    assert reversed_llist.value == 4
    assert reversed_llist.next.value == 3
    assert reversed_llist.next.next.value == 2
    assert reversed_llist.next.next.next.value == 1