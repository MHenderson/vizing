# Matthew Henderson, 2010.12.23 (Chandlers Ford)

import networkx
import unittest

from vizing.test_functions import is_independent
from vizing.test_functions import is_proper
from vizing.test_functions import is_proper_list_colouring

class TestIsIndependent(unittest.TestCase):
    """Testing of independent set decision."""
    
    def setUp(self):
        """docstring for setup"""
        self.positive = {networkx.empty_graph(3):[0,1,2],
                         networkx.empty_graph(4):[0,1,2,3],}
        self.negative = {networkx.complete_graph(3):[0,1,2],
                         networkx.complete_graph(4):[0,1,2,3,4],}

    def test_is_independent(self):
        """Test positive cases."""
        map(self.assertTrue, [is_independent(G, self.positive[G]) for G in 
                              self.positive])

    def test_is_independent_f(self):
        """Test negative cases."""
        map(self.assertFalse, [is_independent(G, self.negative[G]) for G in 
                               self.negative])

class TestIsProper(unittest.TestCase):
    """Testing of proper vertex colouring decision."""
    
    def setUp(self):
        """docstring for setUp"""
        pass    

    def test_is_proper(self):
        """docstring for test_is_proper"""
        G = networkx.complete_graph(3)
        C = {0:[0], 1:[1], 2:[2]}
        self.assertTrue(is_proper(G,C))

    def test_is_proper_f(self):
        """docstring for test_is_proper_f"""
        G = networkx.complete_graph(3)
        C = {0:[0], 1:[1,2]}
        self.assertFalse(is_proper(G,C))

class TestIsProperListColouring(unittest.TestCase):
    """Testing of proper list colouring test function."""

    def setUp(self):
        self.G = networkx.complete_bipartite_graph(2,2)
        self.L = {0: [1, 2], 1: [2,3], 2: [1,3], 3: [1,2,3]}
        self.C = {1: [2, 3], 2: [0, 1]}

    def test_is_proper_list_colouring(self):
        assert is_proper_list_colouring(self.G, self.L, self.C)

