import pytest

import tree


@pytest.fixture
def bin_tree():
    return tree.BinaryTree(1989)


def test_insert_left(bin_tree):
    bin_tree.insert_left(1990)
    assert bin_tree.left_child.key == 1990
