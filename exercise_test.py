import pytest
from exercise import Node, reverse

@pytest.mark.skip(reason="not implemented yet")
def test_reverse():
    llist = Node(1, Node(2, Node(3, Node(4))))
    reverse_list = reverse(llist)
    assert reverse_list.data == 4
    assert reverse_list.next.data == 3
    assert reverse_list.next.next.data == 2
    assert reverse_list.next.next.next.data == 1
    
    