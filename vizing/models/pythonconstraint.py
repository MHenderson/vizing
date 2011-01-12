r"""
Python components for modelling list colourings of graphs.

This module provides the ``python-constraint`` list-colouring model.

AUTHORS:

- Matthew Henderson (2011-01-12): initial version
"""

#********************************************************************************
#       Copyright (C) 2011 Matthew Henderson <matthew.james.henderson@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#********************************************************************************

import constraint

from vizing.utils import vtc_to_ctv

class _CP_model_:

    """ 
    Constraint model via python-constraint.

    REFERENCES: 

    [pyco] http://labix.org/python-constraint
    """

    def __init__(self, graph, list_assignment):
    
        """ 
        XXX doc XXX 
        """

        self.graph = graph
        self.list_assignment = list_assignment
        self.problem = constraint.Problem()
        for node in self.graph.nodes():
            self.problem.addVariable(node, self.list_assignment.get(node)) 
        for edge in self.graph.edges():
            self.problem.addConstraint(constraint.AllDifferentConstraint(), edge)

    def first_solution(self):

        """ 
        XXX doc XXX 
        """

        return vtc_to_ctv(self.problem.getSolution())

