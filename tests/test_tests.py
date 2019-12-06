r"""
Testing of Python components for testing list colourings of graphs.

- Matthew Henderson (2011-1-2): initial version

EXAMPLES:
"""

#********************************************************************************
#       Copyright (C) 2010 Matthew Henderson <matthew.james.henderson@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#********************************************************************************

import networkx
import unittest

from vizing.test_functions import is_independent
from vizing.test_functions import is_exact
from vizing.test_functions import is_proper
from vizing.test_functions import has_colour
from vizing.test_functions import is_list_colouring
from vizing.test_functions import is_proper_list_colouring

class TestIsIndependent(unittest.TestCase):
    """Testing of independent-set decision."""
    
    def setUp(self):
        """Some graphs and vertex-sets used in testing."""
        self.E3 = networkx.empty_graph(3)
        self.E4 = networkx.empty_graph(4)
        self.K3 = networkx.complete_graph(3)
        self.K4 = networkx.complete_graph(4)
        self.petersen = networkx.petersen_graph()
        self.S3 = [0,1,2]
        self.S4 = [0,1,2,3]
        self.PT = [2,4,5,6]
        self.PF = [0,3,4,5,9]

    def test_is_independent(self):
        """Test positive cases."""
        self.assertTrue(is_independent(self.E3, self.S3))
        self.assertTrue(is_independent(self.E4, self.S4))
        self.assertTrue(is_independent(self.petersen, self.PT))
    
    def test_is_independent_f(self):
        """Test negative cases."""
        self.assertFalse(is_independent(self.K3, self.S3))
        self.assertFalse(is_independent(self.K4, self.S4))
        self.assertFalse(is_independent(self.petersen, self.PF))

class TestIsExact(unittest.TestCase):
    """Testing exactness of vertex colourings."""
                
    def setUp(self):
        """Graphs and colourings used in tests."""
        self.K3 = networkx.complete_graph(3)
    
    def test_is_exact(self):
        """Positive cases."""
        #self.assertTrue(is_exact(self.K3, {0:[0,1,2]}))
        #self.assertTrue(is_exact(self.K3, {0:[0], 1:[1,2]}))
        #self.assertTrue(is_exact(self.K3, {0:[0], 1:[1], 2:[2]}))
        pass

    def test_is_exact_f(self):
        """Negative cases."""
        self.assertFalse(is_exact(self.K3, {}))                                 
        self.assertFalse(is_exact(self.K3, {0:[0,1]}))                                 
        self.assertFalse(is_exact(self.K3, {0:[0], 1:[1]}))                                 

class TestIsProper(unittest.TestCase):
    """Testing of proper vertex colouring decision."""
    
    def setUp(self):
        """Some graphs and colourings which are used throughout testing."""
        self.K3 = networkx.complete_graph(3)
        self.K4 = networkx.complete_graph(4)
        self.C3T1 = {0:[0], 1:[1], 2:[2]}
        self.C3T2 = {'a':[0], 'b':[1], 'c':[2]}
        self.C4T1 = {'a':[0], 'b':[1], 'c':[2], 'd':[3]}
        self.C3F1 = {0:[0], 1:[1,2]}
        self.C3F2 = {}
        self.C4F1 = {'a':[0,1], 'b':[2], 'c':[3]}

    def test_is_proper(self):
        """Test positive cases."""
        #self.assertTrue(is_proper(self.K3, self.C3T1))
        #self.assertTrue(is_proper(self.K3, self.C3T2))
        #self.assertTrue(is_proper(self.K4, self.C4T1))
        pass

    def test_is_proper_f(self):
        """Test negative cases"""
        self.assertFalse(is_proper(self.K3, self.C3F1))
        self.assertFalse(is_proper(self.K3, self.C3F2))
        self.assertFalse(is_proper(self.K4, self.C4F1))

class TestHasColour(unittest.TestCase):
    """Testing colour membership decision."""
                
    def setUp(self):
        """Some list assignments used in testing."""
        self.L1 = {0: [1,2], 1: [3]}

    def test_has_colour(self):
        """Test positive cases."""
        self.assertTrue(has_colour(self.L1, 0, 2))

    def test_has_colour_f(self):
        """docstring for test_has_colour_f"""
        self.assertFalse(has_colour(self.L1, 0, 3))

class TestIsListColouring(unittest.TestCase):
    """Testing of list-colouring decision."""
                
    def setUp(self):
        """docstring for setUp"""
        # Graphs
        self.K22 = networkx.complete_bipartite_graph(2,2)
        self.K3 = networkx.complete_graph(3)
        # List assignments
        self.L1 = {0: [1, 2], 1: [2,3], 2: [1,3], 3: [1,2,3]}
        self.L2 = {0: ['a'], 1:['b'], 2:['c']}
        self.L3 = {0: ['a'], 1:['a'], 2:['a']}
        # Vertex colourings
        self.CT1 = {1: [2, 3], 2: [0, 1]}
        self.CT2 = {'a': [0], 'b': [1], 'c': [2]}
        self.CT3 = {'a': [0, 1, 2]}
        self.CF1 = {1: [0, 3], 2: [1, 2]}
        self.CF2 = {'a': [0,1], 'b': [2]}

    def test_is_list_colouring(self):
        """Positive cases."""
        self.assertTrue(is_list_colouring(self.K22, self.L1, self.CT1))
        self.assertTrue(is_list_colouring(self.K3, self.L2, self.CT2))
        self.assertTrue(is_list_colouring(self.K3, self.L3, self.CT3))

    def test_is_list_colouring_f(self):
        """Negative cases."""
        self.assertFalse(is_list_colouring(self.K22, self.L1, self.CF1))      
        self.assertFalse(is_list_colouring(self.K3, self.L2, self.CF2))

class TestIsProperListColouring(unittest.TestCase):
    """Testing of proper list colouring test function."""

    def setUp(self):
        self.K22 = networkx.complete_bipartite_graph(2,2)
        self.L1 = {0: [1, 2], 1: [2,3], 2: [1,3], 3: [1,2,3]}
        self.CT1 = {1: [2, 3], 2: [0, 1]}
        self.CF1 = {1: [0, 2], 2: [1], 3:[3]}

    def test_is_proper_list_colouring(self):
        #self.assertTrue(is_proper_list_colouring(self.K22, self.L1, self.CT1))
        pass

    def test_is_proper_list_colouring_f(self):
        self.assertFalse(is_proper_list_colouring(self.K22, self.L1, self.CF1))

