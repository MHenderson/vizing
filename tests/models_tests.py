# Matthew Henderson, 2010.12.23 (Chandler's Ford)

import networkx
import unittest

from vizing.models import list_colouring
from vizing.test_functions import is_proper_list_colouring

class TestListColouring(unittest.TestCase):
    """Testing of list colouring."""

    def setUp(self):
        pass

    def test_list_colouring(self):
        """With lists of integers."""
        n = 3
        G = networkx.complete_graph(n)
        L = dict([(node, range(n)) for node in G.nodes()])        
        C = list_colouring(G, L, model = 'CP')
        assert is_proper_list_colouring(G, L, C)
    
    def test_list_colouring_strings(self):
        """With lists of strings."""
        n = 3
        G = networkx.complete_graph(n)
        L = dict([(node,['a','b','c','d']) for node in G.nodes()])
        C = list_colouring(G, L, model = 'CP')
        assert is_proper_list_colouring(G, L, C)

