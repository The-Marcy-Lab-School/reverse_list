import pytest

from exercise import Node, reverse #"*" means import everything

#@pytest.mark.skip(reason="not implemented yet")
def test_reverse():
    llist = Node(1, Node(2, Node(3, Node(4))))
    reversed_list = reverse(llist)
    assert reversed_list.data == 4
    assert reversed_list.next.data == 3
    assert reversed_list.next.next.data == 2
    assert reversed_list.next.next.next.data == 1
    