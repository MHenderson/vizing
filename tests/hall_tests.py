# Matthew Henderson, 2010.12.30 (Chandler's Ford)

import networkx
import unittest

from vizing.hall import halls_condition
from vizing.hall import hall_number
from vizing.hall import hall_sum
from vizing.hall import hall_inequality
from vizing.hall import hall_inequality_induced_by

E1 = networkx.empty_graph(1)
K33 = networkx.complete_bipartite_graph(3,3)
K23pE = networkx.complete_bipartite_graph(2,3)
K23pE.add_edge(0,1)
C4 = networkx.cycle_graph(4)

L1 = {0:[1]}
L2 = {0:[2,3], 1:[1,3], 2:[1,2], 3:[2,3], 4:[1,3], 5:[1,2]}
L3 = {0:['a','b','c'], 1:['a','b','c'], 2:['a','b'], 3:['a','c'], 4:['b','c']}
L4 = {0:[1], 1:[], 2:[2], 3:[]}

class TestHallNumber(unittest.TestCase):
    """
    Testing of Hall number function.
    """

    def setUp(self):
        pass

    def test_hall_number(self):
        self.assertEqual(hall_number(E1, L1, 1), 1)

class TestHallSum(unittest.TestCase):
    """
    Testing of Hall sum function.
    """

    def setUp(self):
        pass

    def test_hall_sum(self):
        pass
       
class TestHallInequality(unittest.TestCase):
    """
    Testing of Hall inequality function.
    """

    def setUp(self):
        pass

    def test_hall_inequality(self):
        pass

class TestHallInequalityInducedBy(unittest.TestCase):
    """
    Testing of Hall inequality on induced subgraph function.
    """

    def setUp(self):
        pass

    def test_hall_inequality_induced_by(self):
        pass

class TestHallsCondition(unittest.TestCase):
    """
    Testing of Hall's condition.
    """

    def setUp(self):
        pass

    def test_halls_condition(self):
        self.assertTrue(halls_condition(K33, L2, [1,2,3]))
        self.assertTrue(halls_condition(K23pE, L3, ['a','b','c']))
        self.assertFalse(halls_condition(C4, L4, [1,2]))
