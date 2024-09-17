import pytest

import tree


@pytest.fixture
def bin_tree():
    return tree.BinaryTree(1989)


def test_insert_left(bin_tree):
    bin_tree.insert_left(1990)
    assert bin_tree.left_child.key == 1990


def test_insert_right(bin_tree):
    bin_tree.insert_right(1999)
    assert bin_tree.right_child.key == 1999


def test_breadth_first_search_found(bin_tree):
    bin_tree.insert_left(2000)
    assert bin_tree.breadth_first_search(2000)


def test_breadth_first_search_not_found(bin_tree):
    bin_tree.insert_left(2000)
    assert not bin_tree.breadth_first_search(20001)
