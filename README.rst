Vizing -- List-Colouring of Graphs
----------------------------------

Last updated: Mon Apr  8 17:03:58 BST 2013

Vizing is a collection of Python code for working with list-colouring
problems. List vertex-colourings and list edge-colourings are both of
interest here. With Vizing you can easily build a variety of models of
a list colouring problem instances and use solvers to find realisations
of your models. 

To use:

    >>> from networkx import cycle_graph
    >>> from vizing.colouring import list_colouring
    >>> L = {0: [1, 2], 1: [1, 3], 2: [2, 3], 3: [1, 2, 3]}
    >>> G = cycle_graph(4)
    >>> print list_colouring(G, L)

