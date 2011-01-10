# Matthew Henderson, 2010.12.30 (Chandler's Ford)

import unittest

from vizing.utils import inverse
from vizing.utils import grange
from vizing.utils import support
from vizing.utils import vtc_to_ctv

vtc1 = {0:[1], 1:[2], 2:[0]}
vtc2 = {0:[1], 1:[1], 2:[1]}

ctv1 = {0:[0],1:[0]}
ctv2 = {0:[0,1],1:[2]}

la1 = {0:[1,2,3], 1:[0,1,2]}
la2 = {0:[1], 1:[0,1], 2:[0,1,2]}

class TestRange(unittest.TestCase):
    """
    Testing of colouring ranges.
    """
    
    def setUp(self):
        pass

    def test_range(self):
        self.assertEqual(grange(vtc1), [0,1,2])
        self.assertEqual(grange(vtc2), [1])
                
class TestInverse(unittest.TestCase):
    """
    Testing of inverse of color under vertex-to-colour map.
    """
    def setUp(self):
        pass

    def test_inverse(self):
        self.assertEqual(inverse(vtc1, 0), [2]) 
        self.assertEqual(inverse(vtc1, 1), [0]) 
        self.assertEqual(inverse(vtc1, 2), [1]) 
        self.assertEqual(inverse(vtc2, 1), [0,1,2]) 
                        
class TestVtcToCtv(unittest.TestCase):
    """
    Testing of translation of colouring representation.
    """

    def setUp(self):
        pass

    def test_vtc_to_ctv(self):    
        self.assertEqual(vtc_to_ctv(vtc1), {0:[2], 1:[0], 2:[1]})
        self.assertEqual(vtc_to_ctv(vtc2), {1:[0, 1, 2]})

class TestSupport(unittest.TestCase):
    """
    Testing of colour support function.
    """

    def setUp(self):
        pass

    def test_support(self):
        self.assertEqual(support(la1, [0,1], 0), [1])
        self.assertEqual(support(la1, [0,1], 1), [0,1])
        self.assertEqual(support(la1, [0,1], 2), [0,1])
        self.assertEqual(support(la1, [0,1], 3), [0])
        self.assertEqual(support(la2, [0,1,2], 0), [1,2])
        self.assertEqual(support(la2, [0,1,2], 1), [0,1,2])
        self.assertEqual(support(la2, [0,1,2], 2), [2])

