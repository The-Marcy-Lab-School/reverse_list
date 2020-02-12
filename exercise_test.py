import pytest
from exercise import Node, reverse

# @pytest.mark.skip(reason="Not implemented")
def test_reverse():
	l_list = Node(1, Node(2, Node(3, Node(4))))
	reversed_list = reverse(l_list)
	assert reversed_list.data == 4
	assert reversed_list.next.data == 3
	assert reversed_list.next.next.data == 2
	assert reversed_list.next.next.next.data == 1