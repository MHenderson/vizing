# Matthew Henderson, 2010.12.23 (Chandler's Ford)

import networkx
import unittest

from vizing.models import list_colouring
from vizing.test_functions import is_proper_list_colouring

class TestListColouring(unittest.TestCase):
    """Testing of list colouring."""

    def setUp(self):
        n = 3
        self.G = networkx.complete_graph(n)
        self.L = dict([(node, range(n)) for node in self.G.nodes()])

    def test_list_colouring(self):
        self.C = list_colouring(self.G, self.L, model = 'CP')
        assert is_proper_list_colouring(self.G, self.L, self.C)

