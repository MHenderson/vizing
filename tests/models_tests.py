r"""
Testing of list-colouring models.

- Matthew Henderson (2010-12-23): initial version

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

from vizing.models import list_colouring
from vizing.test_functions import is_proper_list_colouring

class TestListColouring(unittest.TestCase):
    """Testing of list colouring."""

    def setUp(self):
        """Some graphs and lists used in testing."""
        self.K3 = networkx.complete_graph(3)
        self.L1 = dict([(node, range(3)) for node in self.K3.nodes()])        
        self.L2 = dict([(node, ['a','b','c','d']) for node in self.K3.nodes()])

    def test_list_colouring(self):
        """Positive cases."""   
#        C1 = list_colouring(self.K3, self.L1, model = 'CP')        
#        self.assertTrue(is_proper_list_colouring(self.K3, self.L1, C1))
        pass
