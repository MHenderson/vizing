.. Matthew Henderson, 2010.12.23

Tutorial
========

Proper list-colourings of simple graphs
---------------------------------------

Complete graph on 4 vertices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's start with a simple example. We take the complete graph :math:`K_{4}`
on 4 vertices. and assign each vertex the list of colours :math:`\{0,1,2,3\}`::

    >>> import networkx
    >>> G = networkx.complete_graph(4)

We're going to find a proper colouring of this graph when the colours at every
vertex are chosen from the list :math:`\{0,1,2,3\}`. So, we have to build the
appropriate map from vertices to lists::

    >>> L = dict([(node, range(4)) for node in G.nodes()])
    >>> L
    {0: [0, 1, 2, 3], 1: [0, 1, 2, 3], 2: [0, 1, 2, 3], 3: [0, 1, 2, 3]}

The next step is to use the list-colouring function to find a proper 
list-colouring::

    >>> from vizing.models import list_colouring
    >>> list_colouring(G, L)
    {0: [3], 1: [2], 2: [1], 3: [0]}

Lists may contain objects other than integers. Strings, for example ::

    >>> L = dict([(node,['a','b','c','d']) for node in G.nodes()])
    >>> L
    {0: ['a', 'b', 'c', 'd'], 1: ['a', 'b', 'c', 'd'], 2: ['a', 'b', 'c', 'd'], 3: ['a', 'b', 'c', 'd']}
    >>> list_colouring(G, L)
    {}
