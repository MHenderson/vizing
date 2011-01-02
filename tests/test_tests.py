# Matthew Henderson, 2010.12.23 (Chandlers Ford)

import networkx
import unittest

from vizing.test_functions import is_proper_list_colouring

class TestIsProperListColouring(unittest.TestCase):
    """Testing of proper list colouring test function."""

    def setUp(self):
        self.G = networkx.complete_bipartite_graph(2,2)
        self.L = {0: [1, 2], 1: [2,3], 2: [1,3], 3: [1,2,3]}
        self.C = {1: [2, 3], 2: [0, 1]}

    def test_is_proper_list_colouring(self):
        assert is_proper_list_colouring(self.G, self.L, self.C)

